// Unit structure validator. One entry the parts pipeline and the M1/M2 gates share.
//
//   node tools/validators/unit-structure.mjs
//   node tools/validators/unit-structure.mjs --limit 20
//   node tools/validators/unit-structure.mjs path\to\file.glb --class tank --key Tank
//
// Writes status/unit-structure/report.json and report.md (worst first).
// Exit 0 when the run finishes. Verdicts are data, not a process failure.
// The gate hook lives in status/unit-structure-validator.md. This file does not edit gates.mjs.

import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { evaluateCatalog, listCatalog, reportMarkdown } from './lib/catalog.mjs';
import { evaluateBuffer, loadRules } from './lib/structure-eval.mjs';

export { evaluateBuffer, evaluateCatalog, listCatalog, loadRules, reportMarkdown };
export { syntheticGlb, parseGlb } from './lib/glb-parse.mjs';
export { classifyName, evaluateParsed, loadSupport } from './lib/structure-eval.mjs';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const OUT_DIR = path.join(ROOT, 'status/unit-structure');

function dropPriority() {
  if (process.platform !== 'win32') return;
  spawn('powershell.exe', [
    '-NoProfile',
    '-Command',
    `try { (Get-Process -Id ${process.pid}).PriorityClass = 'BelowNormal' } catch {}`,
  ], { windowsHide: true, stdio: 'ignore', detached: true }).unref();
}

function argValue(flag) {
  const index = process.argv.indexOf(flag);
  if (index === -1) return null;
  return process.argv[index + 1] ?? null;
}

async function main() {
  dropPriority();
  const positional = [];
  for (let i = 2; i < process.argv.length; i++) {
    const arg = process.argv[i];
    if (arg.startsWith('--')) { i += 1; continue; }
    positional.push(arg);
  }
  if (positional.length) {
    const structureClass = argValue('--class');
    const key = argValue('--key');
    for (const file of positional) {
      const buf = fs.readFileSync(file);
      const result = await evaluateBuffer(buf, {
        structureClass: structureClass || undefined,
        key: key || path.basename(file),
        file,
        scale: 1,
        scaleIsMetres: true,
        yawOffset: 0,
      });
      console.log(`${result.verdict} ${result.score} ${result.class} ${file}`);
      for (const reason of result.reasons) console.log(`  ${reason}`);
      for (const fix of result.fixes) console.log(`  fix: ${fix}`);
    }
    console.log('UNIT STRUCTURE VALIDATOR DONE');
    return;
  }
  const limitRaw = argValue('--limit');
  const limit = limitRaw ? Number(limitRaw) : 0;
  const report = await evaluateCatalog({
    limit: limit > 0 ? limit : 0,
    onProgress: (index, total, glb) => console.log(`  ${index}/${total} ${glb}`),
  });
  fs.mkdirSync(OUT_DIR, { recursive: true });
  fs.writeFileSync(path.join(OUT_DIR, 'report.json'), JSON.stringify(report, null, 2));
  fs.writeFileSync(path.join(OUT_DIR, 'report.md'), reportMarkdown(report));
  console.log(`STRUCTURED ${report.counts.STRUCTURED}  PARTIAL ${report.counts.PARTIAL}  STATIC ${report.counts.STATIC}  BROKEN ${report.counts.BROKEN}`);
  console.log(`wrote ${path.join(OUT_DIR, 'report.md')}`);
  console.log('UNIT STRUCTURE VALIDATOR DONE');
}

const invoked = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (invoked) {
  main().catch((err) => {
    console.error(err);
    process.exit(1);
  });
}

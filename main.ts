import * as fs from 'node:fs';
import * as path from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR || '/output';
fs.mkdirSync(outDir, { recursive: true });
fs.copyFileSync('entry.png', path.join(outDir, 'entry.png'));

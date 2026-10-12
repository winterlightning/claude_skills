// A side_layout.mjs work folder composed by combine-side.js: shared by side_layout.mjs and side_overlap.mjs.
import {readFileSync} from 'node:fs';
import {createRequire} from 'node:module';
import path from 'node:path';

const require = createRequire(import.meta.url);
export const Side = require('./templates/combine-side.js');
// The combination size: 64 (main 48, sub 32) by default, 72 (main 54, sub 36) with SIDE_SIZE=72. Every side tool reads
// it from here, and the 72 pairs keep their own work folder.
export const SIZE = Number(process.env.SIDE_SIZE) === 72 ? 72 : 64;
export const PARTS = SIZE === 72 ? {main: 54, sub: 36} : {main: 48, sub: 32};
export const WORK_NAME = SIZE === 72 ? 'side-layout-adjust-72' : 'side-layout-adjust';

export const readJSON = file => JSON.parse(readFileSync(file, 'utf8'));
export const drawingMap = drawings => new Map(Object.entries(drawings));

// The layout to compose: a role is left automatic (omitted) while its groups are still the automatic ones it was
// fetched with, so an untouched part is placed exactly as before.
export function layoutFor(dir, layout) {
  const base = readJSON(path.join(dir, 'base-layout.json'));
  const out = {};
  for (const role of ['main', 'sub']) {
    const same = JSON.stringify(layout[role]) === JSON.stringify(base[role]) && layout.position === base.position;
    if (same && !base.hand[role]) continue;
    out[role] = layout[role];
  }
  return Object.keys(out).length ? out : null;
}

export function compose(dir, layout) {
  const item = readJSON(path.join(dir, 'item.json'));
  const drawings = drawingMap(readJSON(path.join(dir, 'drawings.json')));
  return Side.pairRequest(item, drawings, {position: layout.position, layout: layoutFor(dir, layout), size: SIZE});
}

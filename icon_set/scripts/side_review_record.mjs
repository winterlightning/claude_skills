#!/usr/bin/env node
// Record the agent's review of one side pair (/side-layout-adjust) in its work folder as review.json, which the
// side-overlap review page (review.py) shows on the pair's card.
//
//   node icon_set/scripts/side_review_record.mjs <DIR> --verdict ok --note "Clean knockout."
//   node icon_set/scripts/side_review_record.mjs <DIR> --verdict fix --note "The pencil clips the hem." [--model claude-opus-5-5]
//   node icon_set/scripts/side_review_record.mjs <DIR> --verdict redraw --note "Needs a smaller main drawing."
//   ... --part-ok "The dash under the cursor is the corner it points at."   (accept a lost_part on purpose)
//
// ok      reviewed, the stored layout looks right; nothing changes
// fix     the stored layout is wrong and layout.json holds the proposed one (its before/after are measured here)
// redraw  the layout cannot fix it; a part needs redrawing (left alone)
// `side_layout.mjs push` later marks a fix as pushed.
import {existsSync, readFileSync, writeFileSync} from 'node:fs';
import path from 'node:path';
import {PARTS, compose, layoutFor, readJSON} from './side_compose.mjs';
import {analyze, summary} from './side_overlap.mjs';
import {contact} from './side_contact_check.mjs';
import {keyshapeCheck} from './side_keyshape_check.mjs';

function fail(message) { console.error('error: ' + message); process.exit(1); }

const args = process.argv.slice(2);
const dir = args.find(a => !a.startsWith('--'));
const opt = name => { const i = args.indexOf('--' + name); return i >= 0 ? args[i + 1] : undefined; };
if (!dir) fail('usage: side_review_record.mjs <DIR> --verdict ok|fix|redraw --note "..."');
const root = path.resolve(dir);
if (!existsSync(path.join(root, 'item.json'))) fail(`${root} is not a side_layout.mjs work folder (fetch the pair first).`);
const verdict = opt('verdict'), note = (opt('note') || '').trim();
if (!['ok', 'fix', 'redraw'].includes(verdict)) fail('--verdict is ok, fix or redraw.');
if (!note) fail('--note says what you saw: why it looks ok, or what is wrong.');

const measure = layout => {
  const a = analyze(compose(root, layout), layoutFor(root, layout)), s = summary(a), c = contact(a);
  return {flags: s.flags, penalty: s.penalty, reach: s.reach, erased_pct: s.erased_pct, main_to_sub: s.main_to_sub,
          new_pieces: s.fragments.new, stubs: s.fragments.stubs, parts_lost: s.fragments.removed,
          lost_parts: s.parts.lost, parts_cut: s.parts.cut,
          contact: c.verdict, contact_problems: c.problems};
};
const base = readJSON(path.join(root, 'base-layout.json'));
const layout = readJSON(path.join(root, 'layout.json'));
const item = readJSON(path.join(root, 'item.json'));
const box = groups => {
  const x0 = Math.min(...groups.map(g => g.x)), y0 = Math.min(...groups.map(g => g.y));
  return [x0, y0, Math.max(...groups.map(g => g.x + g.w)) - x0, Math.max(...groups.map(g => g.y + g.h)) - y0];
};
const changed = JSON.stringify({p: layout.position, m: layout.main, s: layout.sub}) !== JSON.stringify({p: base.position, m: base.main, s: base.sub});
if (verdict === 'fix' && !changed) fail('a fix needs the proposed layout in layout.json (run preview first).');
if (verdict !== 'fix' && changed) fail(`layout.json differs from the stored layout; for verdict ${verdict} reset it (preview with the stored boxes) or record a fix.`);

// Cut or clear, never a nick (side_contact_check.mjs): a pair is ok, or a fix is done, only when its layout passes.
const before = measure({position: base.position, main: base.main, sub: base.sub});
const after = verdict === 'fix' ? measure(layout) : null;
// --keep-stored "<why>": the stored layout reads well by eye, so it stays (ok) even though a script check flags it
// (a graze, a lost_part on a repeated part such as a database disk). Only for verdict ok; the keyshape check still applies.
const keepStored = (opt('keep-stored') || '').trim();
if (keepStored && verdict !== 'ok') fail('--keep-stored goes with --verdict ok.');
if (verdict === 'ok' && before.contact === 'fail' && !keepStored)
  fail(`the stored layout fails the contact check, so it is not ok:\n  ${before.contact_problems.join('\n  ')}\nIf it still reads well by eye and every fix would make it worse (a smaller sub), pass --keep-stored "<what you saw>".`);
// --gap-ok "<why>": the user approved a clear gap a little wider than 4.5 (up to 6) by eye, such as a small palm-up hand or a star resized so no point is cut
// with the sub floating just above its fingertips. Only for a fix whose only contact problem is that the parts float apart.
const gapOk = (opt('gap-ok') || '').trim();
if (gapOk && verdict !== 'fix') fail('--gap-ok goes with --verdict fix.');
const gapOnly = after && after.contact === 'fail' && after.reach !== null && after.reach > 4.5 && after.reach <= 6
  && (after.flags || []).every(f => f === 'detached');
if (gapOk && after?.contact === 'fail' && !gapOnly)
  fail(`--gap-ok only accepts parts floating 4.5 to 6 apart with nothing else wrong (reach ${after.reach}, flags ${(after.flags || []).join(',') || 'none'}).`);
if (verdict === 'fix' && after.contact === 'fail' && !(gapOk && gapOnly))
  fail(`the proposal fails the contact check; keep adjusting (cut or clear, never a nick):\n  ${after.contact_problems.join('\n  ')}`);

// The keyshape system (side_keyshape_check.mjs): main + sub together inside one canvas keyshape (rule 2026-10-12), and
// the main and the sub sit only on their own keyshape at a preset size
// (every 4) in their corner, as the layout editor's presets put them. A part moved or stretched off those boxes is
// never accepted: an off-system stored layout is not ok, and a proposal off the system is not a fix.
const ksLine = r => [...(r.canvas && !r.canvas.ok ? [r.canvas.problem] : []), ...Object.values(r.roles).filter(x => !x.ok).map(x => `${x.problem}; nearest allowed: ${x.nearest.join(' | ')}`)].join('\n  ');
const ksBefore = keyshapeCheck(root, {position: base.position, main: base.main, sub: base.sub});
const ksAfter = verdict === 'fix' ? keyshapeCheck(root, layout) : null;
// --off-system-ok "<why>": the user judged this stored layout by eye and keeps it although its boxes sit slightly off the
// presets (user rule 2026-10-11: the helper scripts are a reference, not the judge). Only with ok --keep-stored.
const offSystemOk = (opt('off-system-ok') || '').trim();
if (offSystemOk && !(verdict === 'ok' && keepStored)) fail('--off-system-ok goes with --verdict ok --keep-stored.');
if (verdict === 'ok' && !ksBefore.ok && !offSystemOk)
  fail(`the stored layout is off the keyshape system, so it is not ok; propose an on-system layout (side_keyshape_check.mjs --list main|sub):\n  ${ksLine(ksBefore)}`);
if (verdict === 'fix' && !ksAfter.ok)
  fail(`the proposal is off the keyshape system; use only boxes from side_keyshape_check.mjs <dir> --list main|sub:\n  ${ksLine(ksAfter)}`);
// Layout first, resize last: a fix may shrink the sub at most one preset step (4) and never below base - 4 (28 at 64,
// 32 at 72), and a one-step
// shrink needs --sub-smaller saying what was tried at full size (other positions, main sizes) and why it failed.
const presetSize = r => Number((r.roles.sub?.preset || '').match(/ at (\d+)$/)?.[1]) || null;
const subSmaller = (opt('sub-smaller') || '').trim();
if (verdict === 'fix') {
  const from = presetSize(ksBefore), to = presetSize(ksAfter);
  if (from && to && to < from) {
    const floor = PARTS.sub - 4;
    if (to < Math.min(floor, from) || from - to > 4)
      fail(`the proposal shrinks the sub from ${from} to ${to}: never more than one preset step and never below ${floor}. Try other positions and main sizes at the sub's full size first, or keep the stored layout (No layout fits).`);
    if (!subSmaller)
      fail(`the proposal shrinks the sub from ${from} to ${to}. Layout first, resize last: pass --sub-smaller "<which positions and main sizes you tried at sub ${from} and why each failed>", or keep the sub at ${from}.`);
  }
}
const ksSummary = r => ({...Object.fromEntries(Object.entries(r.roles).map(([k, x]) => [k, x.ok ? (x.preset || x.note) + (x.moved ? ' (moved)' : '') : 'off: ' + x.box])),
  ...(r.canvas ? {canvas: r.canvas.ok ? r.canvas.keyshape : 'off'} : {})});

// A drawn part of the main mostly erased (lost_part: a jar's lip, a bike's saddle, a phone's body) breaks the main's
// meaning even when the contact is clean. It is never ok and never a finished fix, unless the part is meant to go
// (a selection dash under the cursor) and --part-ok says why.
const partOk = (opt('part-ok') || '').trim();
const lostLine = m => `${m.lost_parts.join(', ')} (${m.parts_cut.filter(p => m.lost_parts.includes(p.name)).map(p => p.erased_pct + '%').join(', ')} erased)`;
if (verdict === 'ok' && before.lost_parts.length && !partOk && !keepStored)
  fail(`the sub erases most of the main's ${lostLine(before)}; the main loses a part it needs, so it is not ok. Fix the layout, or pass --part-ok "<why that part may go>".`);
if (verdict === 'fix' && after.lost_parts.length && !partOk)
  fail(`the proposal still erases most of the main's ${lostLine(after)}; keep adjusting (move the sub off that part, another position, or clear space), or pass --part-ok "<why that part may go>".`);

const old = existsSync(path.join(root, 'review.json')) ? readJSON(path.join(root, 'review.json')) : {};
const record = {
  reference_id: item.reference_id, concept: item.concept, verdict, note,
  reviewed_at: new Date().toISOString(), model: opt('model') || old.model || null,
  ...(partOk ? {part_ok: partOk} : {}),
  ...(subSmaller ? {sub_smaller: subSmaller} : {}),
  ...(keepStored ? {keep_stored: keepStored} : {}),
  ...(offSystemOk ? {off_system_ok: offSystemOk} : {}),
  ...(gapOk ? {gap_ok: gapOk} : {}),
  before: {position: base.position, main: box(base.main), sub: box(base.sub), ...before, keyshape: ksSummary(ksBefore)},
  ...(verdict === 'fix' ? {
    after: {position: layout.position, main: box(layout.main), sub: box(layout.sub), ...after, keyshape: ksSummary(ksAfter)},
    // Pictures beside this file: stored | proposed, and the proposal alone.
    images: {compare: 'compare.png', proposed: 'proposed@4x.png', proposed_64: 'proposed.png'},
    result: 'not pushed',
  } : {result: verdict === 'ok' ? 'kept' : 'needs redraw'}),
};
// Keep every earlier review of this pair (review-history.json, oldest first) before replacing review.json.
if (old.verdict) {
  const hist = path.join(root, 'review-history.json');
  const list = existsSync(hist) ? readJSON(hist) : [];
  if (!list.some(r => r.reviewed_at === old.reviewed_at)) writeFileSync(hist, JSON.stringify([...list, old], null, 2) + '\n');
}
writeFileSync(path.join(root, 'review.json'), JSON.stringify(record, null, 2) + '\n');
console.log(`${item.concept}: ${verdict}${record.after ? ` (penalty ${record.before.penalty} → ${record.after.penalty})` : ''}`);

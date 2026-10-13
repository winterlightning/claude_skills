// The list rules (lib/rules.js): what counts as a usable drawing, a sub's problems, a pair's state, search and grouping.
import {describe, expect, test} from 'vitest';
import {usable, subProblems, key, category, matches, groups} from '../src/lib/rules.js';

const item = (icon, extra = {}) => ({icon, family: 'solo', model_key: 'solo/' + icon, bounds: [2, 2, 38, 38], ...extra});
// A store with two pairs: one ready, one whose sub fails its checks.
function store() {
  const pairs = new Map([
    ['p1', {id: 'p1', mains: [item('eye')], subs: [item('plus', {family: 'sub', ink32: {ink_width: 24, ink_height: 24}})]}],
    ['p2', {id: 'p2', mains: [item('eye')], subs: [item('star', {family: 'sub', ink32: {ink_width: 36, ink_height: 30}})], custom: true}],
  ]);
  return {pairs, reviews: {'solo/bad': 'pending'}, statuses: {}, previews: {p1: {built: true}},
          catalog: {rows: [], references: {m1: {concept: 'Eye'}, s1: {concept: 'Plus'}, s2: {concept: 'Star'}}},
          componentStatus: {main: new Map([['m1', 'done']]), sub: new Map([['s1', 'done'], ['s2', 'done']])}};
}
const rows = [{id: 'p1', concept: 'Eye plus', main_id: 'm1', sub_id: 's1'}, {id: 'p2', concept: 'Eye star', main_id: 'm1', sub_id: 's2'}];

describe('rules', () => {
  test('a passing drawing counts unless marked needs fix; a failing one once approved', () => {
    const s = store();
    expect(usable(s, {key: 'solo/eye', status: 'pass'})).toBe(true);
    expect(usable(s, {key: 'solo/bad', status: 'pass'})).toBe(false);
    expect(usable({...s, reviews: {'solo/x': 'approve'}}, {key: 'solo/x', status: 'fail'})).toBe(true);
  });
  test('a sub over 32×32 or disapproved has problems', () => {
    expect(subProblems(store(), item('star', {ink32: {ink_width: 36, ink_height: 30}}))).toEqual(['Ink 36×30 exceeds 32×32']);
    expect(subProblems(store(), item('plus', {ink32: {ink_width: 24, ink_height: 24}}), () => true)).toEqual(['Disapproved — needs fix']);
  });
  test('state and filters: ready vs fix sub, built, from review', () => {
    const s = store();
    expect(key(s, rows[0], () => false)).toBe('ready');
    expect(key(s, rows[1], () => false)).toBe('fix');
    expect(category(s, rows[0], () => false, 'built')).toMatchObject({ready: true, built: true, made: false, uncombined: false});
    expect(category(s, rows[1], () => false, undefined)).toMatchObject({fix: true, unbuilt: true, made: true, uncombined: true});
  });
  test('search covers concepts, ids and icon names', () => {
    const s = store();
    expect(rows.filter(r => matches(s, r, 'star')).map(r => r.id)).toEqual(['p2']);
    expect(rows.filter(r => matches(s, r, 'EYE')).map(r => r.id)).toEqual(['p1', 'p2']);
    expect(rows.filter(r => matches(s, r, 's1')).map(r => r.id)).toEqual(['p1']);
  });
  test('grouping by main collects pairs sharing an icon, largest first', () => {
    const g = groups(store(), rows, 'main', () => false);
    expect(g.map(x => [x.title, x.rows.length])).toEqual([['eye', 2]]);
    expect(groups(store(), rows, 'sub', () => false).map(x => x.title)).toEqual(['plus', 'star']);
  });
});

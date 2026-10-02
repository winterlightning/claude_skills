// The layout editor's model (lib/editor.svelte.js): selection, keys, drags and the layout it saves.
import {beforeEach, describe, expect, test} from 'vitest';
import {LayoutEditor, boxOf} from '../src/lib/editor.svelte.js';

let editor;
// A main of two elements and a sub of one, on the 64 canvas.
beforeEach(() => {
  editor = new LayoutEditor();
  const unit = (paths, x, y, w, h) => ({paths, src: [x, y, x + w, y + h], x, y, w, h});
  editor.ctx = {pair: {id: 'p'}, canvas: 64, roles: {main: {units: [unit([0], 4, 4, 20, 20), unit([1], 24, 4, 16, 20)]}, sub: {units: [unit([0], 40, 40, 20, 20)]}},
                dirty: new Set(), sel: new Set(), level: 'whole', token: 0, stale: false, loaded: true, preset: {}};
});
const key = (k, extra = {}) => editor.key({key: k, shiftKey: false, altKey: false, ...extra});

describe('layout editor', () => {
  test('a click selects the whole icon, Shift-click adds the other, again removes it', () => {
    editor.press({role: 'main', unit: 1}, false);
    expect([...editor.ctx.sel]).toEqual(['main:0', 'main:1']);
    editor.press({role: 'sub', unit: 0}, true);
    expect(editor.ctx.sel.size).toBe(3);
    editor.press({role: 'sub', unit: 0}, true);
    expect([...editor.ctx.sel]).toEqual(['main:0', 'main:1']);
  });
  test('arrows move 1 (Shift 8), Alt+arrows resize by 1, + / − both, Esc clears', () => {
    editor.ctx.level = 'element';editor.press({role: 'sub', unit: 0}, false);
    key('ArrowRight');key('ArrowDown', {shiftKey: true});
    expect(boxOf(editor.ctx.roles.sub.units[0])).toEqual([41, 48, 61, 68]);
    key('ArrowLeft', {altKey: true});
    expect(editor.ctx.roles.sub.units[0].w).toBe(19);
    key('+');
    expect([editor.ctx.roles.sub.units[0].w, editor.ctx.roles.sub.units[0].h]).toEqual([20, 21]);
    expect(editor.ctx.stale).toBe(true);
    expect(editor.anyOutside()).toBe(true);
    key('Escape');
    expect(editor.ctx.sel.size).toBe(0);
  });
  test('a corner drag pins the opposite corner; edges land on grid lines; touching elements stay touching', () => {
    const d = editor.press({role: 'main', unit: 0}, false);
    const start = [40, 24], drag = editor.press({handle: 'se'}, false);
    editor.drag(drag, start, [40 + 7.6, 24 + 3.2], false);
    const [a, b] = editor.ctx.roles.main.units;
    expect([a.x, a.y]).toEqual([4, 4]);
    expect(a.x + a.w).toBe(b.x);
    expect(boxOf(b)[2]).toBe(Math.round(47.6 - 2));
    expect(d.list.length).toBe(2);
  });
  test('Shift keeps proportions while resizing', () => {
    editor.press({role: 'sub', unit: 0}, false);
    const drag = editor.press({handle: 'e'}, false);
    editor.drag(drag, [62, 50], [72, 50], true);
    const u = editor.ctx.roles.sub.units[0];
    expect(u.w).toBe(u.h);
  });
  test('the saved layout lists only the parts that were edited', () => {
    expect(editor.layout()).toBe(null);
    editor.press({role: 'sub', unit: 0}, false);key('ArrowUp');
    expect(editor.layout()).toEqual({sub: [{paths: [0], x: 40, y: 39, w: 20, h: 20}]});
  });
});

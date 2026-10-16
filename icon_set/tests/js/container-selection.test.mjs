// Run after `npm ci --prefix web`: exercises the actual container page against an in-memory API.
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createRequire} from 'node:module';
const require = createRequire(new URL('../../../web/package.json', import.meta.url));
const {JSDOM} = require('jsdom');
const templates = new URL('../../scripts/templates/', import.meta.url);
const html = readFileSync(new URL('container-pairs.html', templates), 'utf8');
const json = value => JSON.parse(JSON.stringify(value));
const svg = (size, body) => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${size} ${size}" fill="none" stroke="black" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">${body}</svg>`;
const main = svg(64, '<rect x="4" y="4" width="56" height="56" rx="4"/>');
const symbol = svg(32, '<path d="M 6 16 H 26 M 16 6 V 26"/>');
const wide = svg(32, '<rect x="4" y="10" width="24" height="12" rx="2"/>');
const box = {x: 20, y: 18, w: 24, h: 28};
const pair = (id, container = 'container/box', icon = 'symbol/plus') => ({reference_id: id, concept: 'Combination ' + id, state: 'unbuilt', icon: null, parts: [
  {role: 'container', icon: container}, {role: 'symbol', icon, layout: null}
]});

async function settle(predicate) {
  for (let i = 0; i < 100; i++) {
    if (predicate()) return;
    await new Promise(resolve => setImmediate(resolve));
  }
  assert.fail('Page did not settle');
}

async function page(t) {
  const dom = new JSDOM(html, {url: 'http://localhost/gallery/container-pairs.html', runScripts: 'outside-only'});
  t.after(() => dom.window.close());
  const w = dom.window, rows = [pair('source'), pair('adjusted', undefined, 'symbol/wide'), pair('later'), pair('missing', undefined, 'symbol/missing'), pair('other', 'container/other')];
  const defaultPlacement = {center: [30, 34], size: null};
  rows[1].parts[1].layout = [{x: 10, y: 12, w: 16, h: 18, scope: 'pair', container: defaultPlacement}];
  const art = {'container/box': main, 'container/other': main, 'symbol/plus': symbol, 'symbol/wide': wide};
  const calls = [], posts = [], fixture = {sourceFailure: false, targetFailure: null, warnings: null};
  w.HTMLDialogElement.prototype.showModal = function () { this.open = true; };
  w.HTMLDialogElement.prototype.close = function () { this.open = false; };
  w.confirm = () => true;
  w.scrollTo = () => {};
  w.fetch = async (path, options = {}) => {
    const url = new URL(path, w.location.href), body = options.body && JSON.parse(options.body);
    calls.push(url.pathname + url.search);
    let data;
    if (url.pathname === '/api/combinations') {
      const offset = Number(url.searchParams.get('offset') || 0), all = url.searchParams.get('limit') === '500';
      // Force related results onto multiple pages, independent of the currently visible grid.
      const limit = all ? 2 : 1, items = rows.slice(offset, offset + limit);
      data = {items, total: rows.length, counts: {container: {unbuilt: rows.length}}, next_offset: offset + limit < rows.length ? offset + limit : null};
    } else if (url.pathname === '/api/combinations/drawings') {
      data = Object.fromEntries(url.searchParams.get('keys').split(',').filter(key => art[key]).map(key => [key, {svg: art[key], svg_sha256: 'hash-' + key, review: 'approve'}]));
    } else if (url.pathname === '/api/combinations/candidates') data = [];
    else if (url.pathname === '/api/icon-artwork/overrides') data = {records: []};
    else if (url.pathname.endsWith('container-text-v2.json')) data = {icons: []};
    else if (url.pathname.endsWith('container-centers.json')) data = {containers: {}, pairs: {}};
    else if (url.pathname === '/api/combinations/build') {
      posts.push(body);
      data = {results: body.builds.map(request => {
        if (fixture.sourceFailure && request.reference_id === 'source' || fixture.targetFailure === request.reference_id) return {ok: false, error: 'Rejected'};
        const row = rows.find(row => row.reference_id === request.reference_id);
        row.parts = row.parts.map(part => ({...part, ...request.parts[part.role]}));
        return {ok: true, key: 'container_combination64/' + row.reference_id, build_failed: fixture.warnings === row.reference_id, errors: fixture.warnings === row.reference_id ? ['Needs review'] : []};
      })};
    } else throw Error('Unexpected request: ' + path);
    return {ok: true, json: async () => json(data)};
  };
  for (const file of ['combine.js', 'container-placement.js', 'text-combine.js', 'container-text-symbol.js']) w.eval(readFileSync(new URL(file, templates), 'utf8'));
  w.eval(html.match(/<script>\s*([\s\S]*?)<\/script>/)[1] + '\nwindow.page = {editor, related, openEditor, drawStage, loadRelated, getItems: () => items};');
  await settle(() => w.page.getItems().length);
  w.page.openEditor(w.page.getItems()[0]);
  await settle(() => !w.page.related.loading);
  const $ = id => w.document.getElementById(id);
  const select = id => {
    const checkbox = w.document.querySelector(`[data-pair="${id}"]`);
    checkbox.checked = true; checkbox.dispatchEvent(new w.Event('change', {bubbles: true}));
  };
  return {w, $, select, rows, calls, posts, fixture, art};
}

test('editor lists all exact-container pairs across pages and resets selection with the container', async t => {
  const {w, $, calls} = await page(t);
  assert.equal($('relatedCount').textContent, '3');
  assert.equal(w.document.querySelectorAll('#relatedList svg').length, 2);
  assert.equal(w.document.querySelector('[data-pair="missing"]').disabled, true);
  assert.match($('relatedList').textContent, /Adjusted/);
  assert.ok(calls.some(call => call.includes('offset=4')));
  assert.equal(w.page.related.selected.size, 0);
  $('relatedAll').click();
  assert.deepEqual([...w.page.related.selected], ['adjusted', 'later']);
  $('relatedNone').click();
  assert.equal(w.page.related.selected.size, 0);
  $('relatedAll').click();
  w.page.editor.icons.container = 'container/other'; w.page.drawStage();
  await settle(() => !w.page.related.loading);
  assert.equal(w.page.related.selected.size, 0);
  assert.equal($('relatedCount').textContent, '1');
  assert.ok(w.document.querySelector('[data-pair="other"]'));
});

test('save selected copies the exact box, preserves other symbols/defaults, and persists on reopen', async t => {
  const {w, $, select, rows, posts} = await page(t);
  const unselected = json(rows[2]), oldContainer = json(rows[1].parts[0]);
  select('adjusted');
  w.page.editor.box = {...box}; w.page.drawStage();
  $('scope').value = 'container'; // This action is deliberately independent of the legacy scope control.
  await $('relatedApply').onclick();
  assert.deepEqual(posts.map(post => post.builds.map(request => request.reference_id)), [['source'], ['adjusted']]);
  assert.deepEqual(rows[2], unselected);
  assert.equal(rows[1].parts[0].icon, oldContainer.icon);
  assert.equal(rows[1].parts[1].icon, 'symbol/wide');
  assert.deepEqual(rows[1].parts[1].layout[0].container, {center: [30, 34], size: null});
  assert.equal(rows[1].parts[1].layout[0].scope, 'pair');
  assert.deepEqual(json(w.ContainerPlacement.savedBox(rows[1].parts[1])), box);
  assert.match($('relatedStatus').textContent, /Applied to 1 of 1/);
  assert.match($('relatedList').textContent, /Applied/);
  w.page.openEditor(json(rows[1]));
  await settle(() => !w.page.related.loading);
  assert.deepEqual(json(w.page.editor.box), box);
  assert.equal(w.page.related.selected.size, 0);
});

test('source failures stop writes; target findings and failures remain visible and retryable', async t => {
  const {w, $, select, posts, fixture} = await page(t);
  select('adjusted'); select('later');
  fixture.sourceFailure = true;
  await $('relatedApply').onclick();
  assert.equal(posts.length, 1);
  assert.match($('edMsg').textContent, /Rejected/);
  assert.equal(w.page.editor.busy, false);
  assert.equal(w.page.related.selected.size, 2);
  fixture.sourceFailure = false; fixture.targetFailure = 'later'; fixture.warnings = 'adjusted';
  await $('relatedApply').onclick();
  assert.match($('relatedList').textContent, /Saved · validation findings: Needs review/);
  assert.match($('relatedList').textContent, /Rejected/);
  assert.deepEqual([...w.page.related.selected], ['later']);
  assert.match($('relatedStatus').textContent, /Applied to 1 of 2/);
});

test('refresh before applying skips changed containers and drawings removed since opening', async t => {
  const {w, $, select, rows, posts, art} = await page(t);
  select('adjusted'); select('later');
  rows[1].parts[0].icon = 'container/other';
  delete art['symbol/plus'];
  await $('relatedApply').onclick();
  assert.equal(posts.length, 1, 'only the source was submitted');
  assert.match($('relatedList').textContent, /no longer uses this container/);
  assert.match($('relatedList').textContent, /Both parts need a drawing/);
  assert.equal(w.page.editor.busy, false);
});

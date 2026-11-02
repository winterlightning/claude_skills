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

async function page(t, size = 64, recovered = false, cutout = null) {
  const dom = new JSDOM(html, {url: `http://localhost/gallery/container-pairs.html?size=${size}`, runScripts: 'outside-only'});
  t.after(() => dom.window.close());
  const w = dom.window, rows = [pair('source'), pair('adjusted', undefined, 'symbol/wide'), pair('later'), pair('missing', undefined, 'symbol/missing'), pair('other', 'container/other')];
  const defaultPlacement = {center: [30, 34], size: null};
  rows[1].parts[1].layout = [{x: 10, y: 12, w: 16, h: 18, scope: 'pair', container: defaultPlacement}];
  const art = {'container/box': main, 'container/other': main, 'symbol/plus': symbol, 'symbol/wide': wide};
  if (cutout) {
    const data = JSON.parse(readFileSync(new URL('./container-cutout-fixture.json', import.meta.url)));
    rows[0].parts[0].icon = 'container/universal-prohibited-symbol';
    rows[0].parts[1].icon = cutout;
    rows[0].parts[1].layout = [{x:18,y:18,w:28,h:28,scope:'pair'}];
    art[rows[0].parts[0].icon] = data.main;
    art[cutout] = data.symbols[cutout];
  }
  const nativeKey = key => key?.replace('container/', 'container-72/').replace('symbol/', 'symbol-36/');
  if (size === 72) {
    for (const row of rows) for (const p of row.parts) { p.icon = nativeKey(p.icon); p.current_sha = 'hash-' + p.icon; }
    for (const [key, svg] of Object.entries({...art})) { art[nativeKey(key)] = svg.replaceAll('0 0 64 64', '0 0 72 72').replaceAll('0 0 32 32', '0 0 36 36'); delete art[key]; }
  }
  const nativeDefaults = {canvas: 72, containers: {'container-72/box': {sha256: 'hash-container-72/box', room: {center: [36, 31.5], clear_square_side: 32, symbol_guide_size: 32, status: 'provisional'}}}, pairs: {}};
  if (recovered) {
    const p = rows[0].parts[1]; p.icon = null;
    nativeDefaults.pairs.source = {container:'container-72/box', symbol:'text/local-source', container_sha256:'hash-container-72/box', symbol_sha256:'local-hash', native_text:true, center:[36,31.5], size:24, text_svg:art['symbol-36/plus']};
  }
  const uploads = [], hashes = {};
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
      data = Object.fromEntries(url.searchParams.get('keys').split(',').filter(key => art[key]).map(key => [key, {svg: art[key], svg_sha256: hashes[key] || 'hash-' + key, review: 'approve'}]));
    } else if (url.pathname === '/api/icons/upload') {
      uploads.push(body);
      const key = fixture.existingUploadKey || 'symbol-36/registered';
      art[key] = body.svg; hashes[key] = 'uploaded-revision-' + uploads.length;
      data = {record: {key, svg_sha256: hashes[key]}};
    } else if (url.pathname === '/api/combinations/candidates') data = [];
    else if (url.pathname === '/api/icon-artwork/overrides') data = {records: []};
    else if (url.pathname.endsWith('container-text-v2.json')) data = {icons: []};
    else if (url.pathname.endsWith('container-layouts72.json')) data = nativeDefaults;
    else if (url.pathname.endsWith('container-centers.json')) data = {containers: {}, pairs: {}};
    else if (url.pathname === '/api/combinations/build') {
      posts.push(body);
      data = {results: body.builds.map(request => {
        if (fixture.sourceFailure && request.reference_id === 'source' || fixture.targetFailure === request.reference_id) return {ok: false, error: 'Rejected'};
        if (Object.values(request.parts).some(p => p.svg_sha256 !== (hashes[p.icon] || 'hash-' + p.icon))) return {ok: false, error: 'The part was redrawn since it was loaded.'};
        const row = rows.find(row => row.reference_id === request.reference_id);
        row.parts = row.parts.map(part => ({...part, ...request.parts[part.role]}));
        return {ok: true, key: 'container_combination64/' + row.reference_id, build_failed: fixture.warnings === row.reference_id, errors: fixture.warnings === row.reference_id ? ['Needs review'] : []};
      })};
    } else throw Error('Unexpected request: ' + path);
    return {ok: true, json: async () => json(data)};
  };
  for (const file of ['combine.js', 'combine-side.js', 'container-placement.js', 'text-combine.js', 'container-text-symbol.js']) w.eval(readFileSync(new URL(file, templates), 'utf8'));
  w.eval(html.match(/<script>\s*([\s\S]*?)<\/script>/)[1] + '\nwindow.page = {editor, related, openEditor, drawStage, loadRelated, getItems: () => items};');
  await settle(() => w.page.getItems().length);
  w.page.openEditor(w.page.getItems()[0]);
  await settle(() => !w.page.related.loading);
  const $ = id => w.document.getElementById(id);
  const select = id => {
    const checkbox = w.document.querySelector(`[data-pair="${id}"]`);
    checkbox.checked = true; checkbox.dispatchEvent(new w.Event('change', {bubbles: true}));
  };
  return {w, $, select, rows, calls, posts, fixture, art, nativeDefaults, uploads};
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


test('native72 editor restores room, draws a 72px grid and saves selected layouts only at size72', async t => {
  const {w, $, select, rows, posts, calls} = await page(t, 72);
  assert.equal($('stage').getAttribute('viewBox'), '0 0 72 72');
  assert.match($('roomInfo').textContent, /36, 31.5.*32.*provisional/);
  assert.equal(w.page.editor.last.svg.includes('viewBox="0 0 72 72"'), true);
  const original = json(rows[2]);
  select('adjusted');
  const fractional = {x: 22.25, y: 18.5, w: 24.5, h: 27};
  w.page.editor.box = fractional; w.page.drawStage();
  await $('relatedApply').onclick();
  assert.ok(posts.length === 2 && posts.every(p => p.size === 72));
  assert.ok(calls.filter(c => c.startsWith('/api/combinations?') || c.startsWith('/api/combinations/candidates?')).every(c => c.includes('size=72')));
  assert.equal(rows[1].parts[1].icon, 'symbol-36/wide');
  assert.deepEqual(json(w.ContainerPlacement.savedBox(rows[1].parts[1])), fractional);
  assert.deepEqual(rows[2], original);
  w.page.openEditor(rows[1]); await settle(() => !w.page.related.loading);
  assert.deepEqual(json(w.page.editor.box), fractional);
});

test('recovered native text is read-only until save and is registered without a local approval', async t => {
 const {w,$,uploads,posts,rows}=await page(t,72,true);
 assert.equal(uploads.length,0); assert.ok(w.page.editor.last);
 await $('edSave').onclick();
 assert.equal(uploads.length,1); assert.equal(uploads[0].approve,false); assert.equal(uploads[0].bypass_validation,true);
 assert.equal(uploads[0].family,'symbol-36');
 assert.equal(posts[0].builds[0].parts.symbol.icon,'symbol-36/registered');
 assert.equal(rows[0].parts[1].layout[0].native_text,true);
 assert.equal(w.page.editor.icons.symbol,'symbol-36/registered');
});

for (const size of [64, 72]) test(`edited ${size}px symbol reloads a new revision uploaded to the same icon key`, async t => {
  const {w, $, fixture, posts, uploads, rows} = await page(t, size);
  const key = w.page.editor.icons.symbol;
  fixture.existingUploadKey = key;
  const edited = svg(size === 72 ? 36 : 32, '<path d="M 8 16 H 24 M 16 8 V 24"/>');
  w.page.editor.symbolSvg = edited;
  w.page.editor.box = {...box};
  w.page.drawStage();
  await $('edSave').onclick();
  assert.equal(uploads.length, 1);
  assert.equal(posts[0].builds[0].parts.symbol.svg_sha256, 'uploaded-revision-1');
  assert.equal(rows[0].parts[1].icon, key);
  assert.equal(w.page.editor.last.symbol.svg, uploads[0].svg);
  assert.match(w.page.editor.last.symbol.svg, /M 8 16 H 24 M 16 8 V 24/);
  assert.match($('edMsg').textContent, /^Saved/);
  assert.equal(w.page.editor.symbolSvg, null);
});

for (const symbolKey of ['symbol/boot-sub32', 'symbol/geometric-three-toed-paw-sub32-symbol']) {
  test('64px editor saves and reopens the slash cutout: ' + symbolKey, async t => {
    const {w, $, rows, posts, uploads} = await page(t, 64, false, symbolKey);
    const container = result => w.Combine.serialize(w.Combine.parse(result.svg).children.find(n => n.attrs?.id === 'container'));
    const initialMain = container(w.page.editor.last);
    $('bx').value = '20'; $('bx').onchange();
    $('bw').value = '24'; $('bw').onchange();
    const preview = w.page.editor.last.svg;
    assert.notEqual(container(w.page.editor.last), initialMain, 'gap follows the edited symbol');
    assert.equal(w.ContainerPlacement.placementOf(rows[0]).overlay, true);
    await $('edSave').onclick();
    assert.equal(posts.length, 1);
    const request = posts[0].builds[0];
    assert.equal(request.svg, preview, 'save sends exactly the previewed cutout');
    assert.equal(request.parts.symbol.layout[0].overlay, true);
    assert.equal(request.parts.container.icon, 'container/universal-prohibited-symbol');
    assert.equal(request.parts.symbol.icon, symbolKey);
    assert.deepEqual(Object.keys(request.parts).sort(), ['container', 'symbol']);
    assert.equal(uploads.length, 0, 'whole-layout changes reuse both component identities');
    assert.equal(w.page.editor.last.svg, preview, 'after-save renderer retains the gap');
    $('edCancel').click();
    w.page.openEditor(json(rows[0]));
    await settle(() => !w.page.related.loading);
    assert.equal(w.page.editor.last.svg, preview, 'close/reopen retains the gap');
    $('scope').value = 'container';
    await $('edSave').onclick();
    assert.equal(posts[1].builds[0].svg, preview, 'same-container wide save retains the cutout');
    assert.equal(posts[1].builds[0].parts.symbol.layout[0].overlay, true);
  });
}

for (const size of [64, 72]) test(`container navigation keeps the ${size}px canvas`, async t => {
  const {$} = await page(t, size);
  const list = new URL($('allCombinations').href);
  assert.equal(list.searchParams.get('size'), String(size));
  assert.equal(list.searchParams.get('kind'), 'container');
  const side = new URL($('sideLayouts').href);
  assert.equal(side.searchParams.get('view'), 'side');
  assert.equal(side.searchParams.get('grid'), String(size));
  assert.equal(side.searchParams.has('size'), false, 'Progression size means page length, not canvas');
  assert.equal($('edCanvas').textContent, `${size}×${size} container layout`);
});

test('container-wide save after replacing an overlay container matches preview', async t => {
  const {w, $, rows, posts, art} = await page(t, 64, false, 'symbol/boot-sub32');
  await $('edSave').onclick();
  assert.equal(rows[0].parts[1].layout[0].overlay, true, 'start with persisted overlay metadata');
  const replacement = 'container/review-replacement';
  art[replacement] = svg(64, '<path d="M4 32H60"/>');
  await w.eval("loadDrawings(['container/review-replacement'])");
  w.page.editor.icons.container = replacement;
  w.page.drawStage();
  await settle(() => !w.page.related.loading);
  const preview = w.page.editor.last.svg;
  assert.equal(w.ContainerPlacement.placementOf(rows[0], {container:replacement}).overlay, undefined);
  $('scope').value = 'container';
  await $('edSave').onclick();
  assert.equal(posts.length, 2, $('edMsg').textContent);
  const saved = posts[1].builds[0];
  assert.equal(saved.svg, preview, 'replacement container must not acquire old overlay mode on save');
  assert.equal(saved.parts.container.icon, replacement);
  assert.notEqual(saved.parts.symbol.layout[0].overlay, true);
  assert.equal(w.page.editor.last.svg, preview, 'after-save rendering matches the intact preview');
  $('edCancel').click();
  w.page.openEditor(json(rows[0]));
  await settle(() => !w.page.related.loading);
  assert.equal(w.page.editor.last.svg, preview, 'reopen keeps the replacement intact');
});

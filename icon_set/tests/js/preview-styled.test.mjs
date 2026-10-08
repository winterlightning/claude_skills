// preview-editor.js round / sharp views: a placement shows its styled record only while that record is approved
// and not a failed build, and a revoked approval falls back to the normal icon on the next switch (PR #4 review).
//   NODE_PATH=web/node_modules node --test icon_set/tests/js/*.test.mjs   (needs jsdom; skipped without it)
import test from 'node:test';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import {readFileSync} from 'node:fs';

const require = createRequire(import.meta.url);
let JSDOM = null;
try { ({JSDOM} = require('jsdom')); } catch { /* skipped below */ }
const source = name => readFileSync(new URL('../../scripts/templates/' + name, import.meta.url), 'utf8');

const solo = id => ({icon_id: id, name: id, family: 'solo', preview_url: `../api/icon-artwork/svg?icon=solo%2F${id}`});
const card = (id, state, failed = false) => ({key: 'solo/' + id, icon_id: id, name: id, family: 'solo', build_failed: failed,
  preview_url: `../api/icon-artwork/svg?icon=solo%2F${id}`, review: {state, status: state}});

test('round view shows approved styled records only and drops revoked ones', {skip: !JSDOM && 'jsdom not installed'}, async () => {
  const dom = new JSDOM('<body></body>', {runScripts: 'outside-only', url: 'http://localhost/gallery/preview.html'});
  const w = dom.window;
  let styled = {'cup--round': card('cup--round', 'approve'), 'mug--round': card('mug--round', 'ready'),
                'pen--round': card('pen--round', 'approve', true)};
  w.fetch = async url => {
    const keys = decodeURIComponent(String(url).split('keys=')[1] || '').split(',').map(k => k.slice(5));
    return {ok: true, json: async () => ({items: keys.map(k => styled[k]).filter(Boolean)})};
  };
  w.eval(source('preview-library.js'));
  w.eval(source('preview-editor.js'));
  const editor = w.PreviewIconEditor({icons: [solo('cup'), solo('mug'), solo('pen')], example: 't'});
  // the placements as a scene writes them
  w.document.body.innerHTML = editor.icon('cup', '', 'a') + editor.icon('mug', '', 'b') + editor.icon('pen', '', 'c');
  const shown = () => [...w.document.querySelectorAll('.icon-swap')].map(el => el.dataset.icon);

  await editor.setMode('round');
  assert.deepEqual(shown(), ['cup--round', 'mug', 'pen'], 'approved round record only; Ready and failed builds stay normal');

  styled = {...styled, 'cup--round': card('cup--round', 'ready')};   // approval revoked
  await editor.setMode('solo');
  await editor.setMode('round');
  assert.deepEqual(shown(), ['cup', 'mug', 'pen'], 'a revoked approval falls back to the normal icon');

  w.fetch = async () => { throw Error('offline'); };
  styled = {...styled, 'cup--round': card('cup--round', 'approve')};
  await editor.setMode('round');
  assert.deepEqual(shown(), ['cup', 'mug', 'pen'], 'a failed request shows the normal icons, not a stale card');
});

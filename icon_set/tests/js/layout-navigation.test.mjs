import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createRequire} from 'node:module';
import {runInNewContext} from 'node:vm';
const require = createRequire(new URL('../../../web/package.json', import.meta.url));
const {JSDOM} = require('jsdom');
const templates = new URL('../../scripts/templates/', import.meta.url);
const html = name => readFileSync(new URL(name, templates), 'utf8');
const script = name => html(name).match(/<script>([\s\S]*?)<\/script>/)[1];
for (const size of [64, 72]) for (const kind of ['container', 'side']) {
  test(`Icon review resolves an uploaded ${kind} key to its ${size}px editor`, async t => {
    const dom = new JSDOM(html('combinations.html'));t.after(() => dom.window.close());
    const key = `${kind === 'side' ? 'combination' : 'container-combination'}-${size}/uploaded-name`;
    const ref = 'reference-with-a-different-id';
    let resolve;const redirected = new Promise(r => {resolve = r;});
    runInNewContext(script('combinations.html'), {
      document: dom.window.document, URLSearchParams, setTimeout, clearTimeout,
      history: {replaceState() {}},
      location: {search: '?' + new URLSearchParams({icon: key, size, edit: 1}), replace: resolve},
      fetch: async path => {
        const query = new URL(path, 'http://localhost').searchParams;
        assert.equal(query.get('icon'), key);assert.equal(query.get('size'), String(size));
        return {ok: true, json: async () => ({items: [{reference_id: ref, kind}], total: 1})};
      }
    });
    const destination = new URL(await redirected, 'http://localhost/gallery/');
    assert.equal(destination.pathname, `/gallery/${kind}-pairs.html`);
    assert.equal(destination.searchParams.get('size'), String(size));
    assert.equal(destination.searchParams.get('edit'), ref);
    if (kind === 'side') {
      let next;
      runInNewContext(script('side-pairs.html'), {URLSearchParams, location: {search: destination.search, replace: url => {next = url;}}});
      const side = new URL(next, 'http://localhost/gallery/');
      assert.equal(side.pathname, '/gallery/primitives.html');
      assert.equal(side.searchParams.get('grid'), size === 72 ? '72' : null);
      assert.equal(side.searchParams.get('edit'), ref);
      assert.equal(side.searchParams.has('size'), false);
    }
  });
}

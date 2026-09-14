// Verify the public collection fails closed and exposes only SVG downloads.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
class Element {
  constructor(tag) { this.tag = tag; this.children = []; }
  append(...children) { this.children.push(...children); }
  replaceChildren(...children) { this.children = children; }
  setAttribute(name, value) { this[name] = value; }
}
const script = fs.readFileSync(path.join(__dirname, '../scripts/templates/approved-icons.js'), 'utf8');
async function render(reviews, failed = false) {
  const grid = new Element('div'), status = new Element('p');
  const icons = ['approved','pending','rejected','ready','missing','old'].map(key => ({key, name:key, icon_id:key, preview_url:key+'.svg'}));
  await vm.runInNewContext(script, {
    document: {getElementById: id => id === 'approvedGrid' ? grid : status, createElement: tag => new Element(tag), createDocumentFragment: () => new Element('fragment')},
    fetch: async url => ({ok: !failed, json: async () => url === 'icons.json' ? {icons} : reviews})
  });
  return {grid, status};
}
(async()=>{
  const {grid} = await render({approved:'approve', pending:'pending', rejected:'rejected', ready:'ready', old:'re-generated'});
  const cards = grid.children[0].children;
  assert.equal(cards.length, 1);
  assert.equal(cards[0].children[1].textContent, 'approved');
  const download = cards[0].children[2];
  assert.equal(download.tag, 'a');
  assert.equal(download.href, 'approved.svg');
  assert.equal(download.download, 'approved.svg');
  assert.equal(cards[0].children.length, 3);
  assert.match((await render({})).status.textContent, /No approved icons/);
  const failure = await render({}, true);
  assert.equal(failure.grid.children.length, 0);
  assert.match(failure.status.textContent, /Could not load/);
  console.log('Approved-only filtering, download links, empty state, and fail-closed loading passed.');
})();

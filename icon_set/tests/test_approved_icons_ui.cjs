// Verify the public collection fails closed and exposes only SVG downloads.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
class Element {
  constructor(tag) { this.tag = tag; this.children = []; }
  append(...children) { this.children.push(...children); }
  replaceChildren(...children) { this.children = children; }
  scrollIntoView() {}
  setAttribute(name, value) { this[name] = value; }
}
const script = fs.readFileSync(path.join(__dirname, '../scripts/templates/approved-icons.js'), 'utf8');
async function render(reviews, failed = false, catalog = null, search = '') {
  const elements=new Map();
  const get=id=>{if(!elements.has(id))elements.set(id,new Element('div'));return elements.get(id);};
  const icons = catalog || ['approved','pending','rejected','ready','missing','old'].map(key => ({key, name:key, icon_id:key, preview_url:key+'.svg'}));
  const location={href:'http://localhost/gallery/icons.html'+search,search};
  const update=(a,b,url)=>{location.href=String(url);location.search=new URL(url).search;};
  const events={};
  await vm.runInNewContext(script, {
    document: {getElementById:get, createElement: tag => new Element(tag), createElementNS:(ns,tag)=>new Element(tag), createDocumentFragment: () => new Element('fragment')},
    window:{location,history:{replaceState:update,pushState:update},addEventListener:(name,fn)=>events[name]=fn},URL,URLSearchParams,
    fetch: async url => ({ok: !failed, json: async () => url === 'icons.json' ? {icons} : reviews})
  });
  return {grid:get('approvedGrid'), status:get('approvedStatus'),get,location,events};
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
  assert.equal(download.children[0].tag, 'svg');
  assert.equal(download['aria-label'], 'Download approved SVG');
  assert.equal(cards[0].children.length, 3);
  assert.match((await render({})).status.textContent, /No approved icons/);
  const failure = await render({}, true);
  assert.equal(failure.grid.children.length, 0);
  assert.match(failure.status.textContent, /Could not load/);
  const many=Array.from({length:101},(_,i)=>({key:String(i),name:'Icon '+i,icon_id:String(i),preview_url:i+'.svg'}));
  const collection=await render(Object.fromEntries(many.map(i=>[i.key,'approve'])),false,many);
  assert.equal(collection.grid.children[0].children.length,48);
  assert.equal(collection.get('approvedPrevious').disabled,true);
  collection.get('approvedNext').onclick();
  assert.equal(collection.grid.children[0].children[0].children[1].textContent,'Icon 48');
  assert.match(collection.location.search,/page=2/);
  collection.get('approvedNext').onclick();
  assert.equal(collection.grid.children[0].children.length,5);
  assert.equal(collection.get('approvedNext').disabled,true);
  collection.get('approvedPageSize').value='24';collection.get('approvedPageSize').onchange();
  assert.equal(collection.grid.children[0].children.length,24);
  assert.equal(collection.get('approvedPage').value,'1');
  collection.location.search='?page=999&page_size=48';collection.events.popstate();
  assert.equal(collection.grid.children[0].children.length,5);
  assert.equal(collection.get('approvedPage').value,'3');
  assert.equal(failure.get('approvedPagination').hidden,true);
  console.log('Pagination, page-size changes, URL clamping and icon buttons passed.');
  console.log('Approved-only filtering, download links, empty state, and fail-closed loading passed.');
})();

// Run with: node icon_set/tests/test_gallery_ui.cjs
// Exercise the actual page scripts without a browser or a paid generation run.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
class Element {
  constructor() { this.value = ''; this.children = []; this.dataset = {}; this.options = []; }
  append(...items) { this.children.push(...items); this.options = this.children; }
  replaceChildren(...items) { this.children = items; this.options = this.children; }
  setAttribute() {}
  addEventListener() {}
  querySelector() { return new Element(); }
  querySelectorAll() {
    return this.children.flatMap(child => typeof child === 'object'
      ? [...(child.className === 'card' ? [child] : []), ...child.querySelectorAll()]
      : []);
  }
}
function page(name) {
  const elements = new Map(), storage = new Map(), navigations = [];
  const document = {
    body: new Element(),
    getElementById(id) { if (!elements.has(id)) elements.set(id, new Element()); return elements.get(id); },
    createElement() { return new Element(); }, createTextNode(s) { return s; },
    createDocumentFragment() { return new Element(); }
  };
  const localStorage = { getItem: k => storage.get(k), setItem: (k,v) => storage.set(k,v), removeItem: k => storage.delete(k) };
  const location = { search: '', href: 'http://localhost/gallery/generate.html', assign: url => navigations.push(url) };
  const context = vm.createContext({document, localStorage, sessionStorage: localStorage, location,
    window: {addEventListener() {}}, history: {replaceState() {}, pushState() {}}, URL, URLSearchParams, console});
  let script = fs.readFileSync(path.join(__dirname, '../scripts/templates', name+'.html'), 'utf8').split('<script>')[1].split('</script>')[0];
  script = name === 'gallery' ? script.slice(0, script.lastIndexOf('(async()=>')) : script.replace('refresh();setInterval(()=>{if(!document.hidden)refresh();},4000);', '');
  vm.runInContext(script, context);
  return {context, document, navigations, run: code => vm.runInContext(code, context)};
}
async function main() {
  const gallery = page('gallery');
  gallery.run(`icons=[
    {key:'solo/test',family:'solo',icon_id:'test',name:'Test',preview_url:'v1.svg'},
    ...[2,3,12].map(n=>({key:'solo/test-v'+n,family:'solo',icon_id:'test-v'+n,variant_root:'test',variant_of:'test',name:'Test v'+n,preview_url:'v'+n+'.svg'})),
    {key:'sub/other',family:'sub',icon_id:'other',name:'Other',preview_url:'other.svg'}
  ];reviewsLoaded=true;setIconView('versions');render();`);
  assert.equal(gallery.run('versionGroups(filteredIcons()).length'), 2);
  assert.equal(gallery.run('versionGroups(filteredIcons())[0].map(iconVersion).join(",")'), 'v1,v2,v3,v12');
  assert.equal(gallery.document.getElementById('grid').querySelectorAll().length, 5);
  gallery.run("$('search').value='test-v3';render();");
  assert.equal(gallery.run('filteredIcons().length'), 4, 'Searching one variant includes all siblings');
  gallery.run("reviews['solo/test-v2']='rejected';render();");
  assert.equal(gallery.run('filteredIcons().length'), 3);
  const cards = gallery.document.getElementById('grid').querySelectorAll();
  assert.equal(cards.length, 3);
  assert.ok(cards.every(card => card.dataset.key !== 'solo/test-v2'));
  assert.equal(cards[0].children.at(-1).children.at(-1).textContent, 'Reject');
  gallery.run("$('search').value='';reviewFilter='rejected';render();");
  assert.equal(gallery.run('filteredIcons()[0].icon_id'), 'test-v2', 'Rejected tab retains access');
  gallery.run("reviewFilter='';reviews['solo/test']='re-generated';reviewFilter='re-generated';render();");
  assert.equal(gallery.run('filteredIcons().length'), 3, 'Status match brings active siblings into comparison');
  gallery.run("reviewFilter='';pageSize=1;page=1;render();");
  assert.equal(gallery.document.getElementById('grid').querySelectorAll().length, 3, 'Pagination keeps versions together');
  gallery.run("page=2;render();");
  assert.equal(gallery.document.getElementById('grid').querySelectorAll().length, 1);
  gallery.run("setIconView('generated');pageSize=48;render();");
  assert.equal(gallery.run('filteredIcons().length'), 4, 'Rejected icons stay hidden in ordinary view');

  const generate = page('generate');
  generate.context.fetch = async () => ({ok:true,json:async()=>({icons:[{key:'solo/test-v3'}]})});
  generate.run("row={id:'job',name:'Test',status:'accepting',candidate:{key:'solo/test-v3',icon_id:'test-v3',family:'solo',variant_of:'test'}};rememberGridJob(row.id);");
  await generate.run('finishAddToGrid([row])');
  assert.equal(generate.navigations.length, 0, 'Do not navigate while build is running');
  generate.context.fetch = async () => ({ok:true,json:async()=>({icons:[]})});
  await assert.rejects(generate.run("row.status='accepted';finishAddToGrid([row])"), /Waiting for the built icon/);
  assert.equal(generate.navigations.length, 0, 'Do not navigate before publication');
  generate.context.fetch = async () => ({ok:true,json:async()=>({icons:[{key:'solo/test-v3'}]})});
  await generate.run('finishAddToGrid([row])');
  assert.equal(generate.navigations.length, 1);
  const url = new URL(generate.navigations[0], 'http://localhost/gallery/');
  assert.equal(url.searchParams.get('q'), 'test-v3');
  assert.equal(url.searchParams.get('view'), 'versions');
  assert.equal(url.searchParams.has('version'), false);
  generate.run("rememberGridJob(row.id);row.status='candidate';row.error='Build failed';");
  await generate.run('finishAddToGrid([row])');
  assert.equal(generate.document.getElementById('notice').textContent, 'Build failed');
  assert.equal(generate.run('pendingGridJob'), '');
  assert.equal(generate.navigations.length, 1, 'Failed build stays on Generate');
  console.log('Gallery version groups, rejection, pagination, and build-to-grid navigation passed.');
}
main().catch(error => { console.error(error); process.exitCode = 1; });

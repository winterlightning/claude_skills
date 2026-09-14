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
  closest() { return new Element(); }
  focus() {}
  scrollIntoView() {}
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
    window: {addEventListener() {}}, history: {replaceState() {}, pushState() {}}, URL, URLSearchParams, console,
    fetch: async () => ({ok: false, json: async () => null})});
  let script = fs.readFileSync(path.join(__dirname, '../scripts/templates', name+'.html'), 'utf8').split('<script>')[1].split('</script>')[0];
  script = name === 'gallery' ? script.slice(0, script.lastIndexOf('(async()=>')) : script.replace('refresh();setInterval(()=>{if(!document.hidden)refresh();},4000);', '');
  vm.runInContext(fs.readFileSync(path.join(__dirname, '../scripts/templates/reference-picker.js'), 'utf8'), context);
  vm.runInContext('var ReferencePicker=window.ReferencePicker,referenceThumbs=window.referenceThumbs;', context);
  vm.runInContext(script, context);
  return {context, document, navigations, run: code => vm.runInContext(code, context)};
}
async function main() {
  const authors = page('gallery');
  authors.run(`icons=[
    {key:'solo/base',family:'solo',icon_id:'base',name:'Base',author:'json_to_solo'},
    {key:'solo/base-v2',family:'solo',icon_id:'base-v2',name:'Revision',author:'gpt-6',variant_of:'base',variant_root:'base'},
    {key:'solo/unknown',family:'solo',icon_id:'unknown',name:'Unknown'}
  ];section='json';setIconView('versions');`);
  assert.equal(authors.run('filteredIcons().map(i=>i.icon_id).join(",")'), 'base', 'Version expansion stays within the author tab');
  authors.run("section='ai';");
  assert.equal(authors.run('filteredIcons().map(i=>i.icon_id).join(",")'), 'base-v2', 'Unknown authors are not classified as AI');
  authors.run("icons[0].author='gpt-6';section='json';");
  assert.equal(authors.run('filteredIcons().length'), 0, 'Updating model author removes the icon from the converter backlog');
  authors.run("failedIcons=[{key:'solo/failed',family:'solo',icon_id:'failed',name:'Failed',author:'json_to_solo',build_failed:true}];reviews['solo/failed']='rejected';");
  assert.equal(authors.run('filteredIcons().length'), 1, 'Author tabs include failed and rejected icons by default');
  authors.run("reviewFilter='approve';");
  assert.equal(authors.run('filteredIcons().length'), 0, 'Converter tab applies its selected Approved filter');
  authors.run("reviewFilter='rejected';");
  assert.equal(authors.run('filteredIcons().length'), 1, 'Converter tab can filter rejected failed icons');
  authors.run("reviewFilter='';");
  assert.equal(authors.run('selectable(failedIcons[0])'), false, 'Failed builds cannot be bulk approved');
  authors.run("section='icons';setIconView('generated');");
  assert.equal(authors.run('filteredIcons().some(i=>i.build_failed)'), false, 'Failed icons stay out of the exported library');
  authors.run("loadReviews=()=>{};section='icons';reviewFilter='approve';showSection('json');");
  assert.equal(authors.run('reviewFilter'), '', 'Entering converter tab does not inherit Approved from Icons');
  assert.equal(authors.document.getElementById('reviewTabs').hidden, false);
  authors.run("reviewFilter='rejected';showSection('icons');");
  assert.equal(authors.run('reviewFilter'), 'approve', 'Icons keeps its own review filter');
  authors.run("showSection('json');");
  assert.equal(authors.run('reviewFilter'), 'rejected', 'Converter tab remembers its own review filter');
  const selection = page('gallery');
  selection.run(`icons=Array.from({length:53},(_,n)=>({key:'solo/icon-'+n,family:'solo',icon_id:'icon-'+n,name:'Icon '+n}));reviewsLoaded=true;setIconView('generated');pageSize=48;render();$('selectAll').checked=true;$('selectAll').onchange();`);
  assert.equal(selection.run('selectedKeys.size'), 48, 'Select all is limited to the visible page');
  selection.run('changePage(2);');
  assert.equal(selection.run('selectedKeys.size'), 0, 'Changing pages clears selection');
  selection.run("$('selectAll').checked=true;$('selectAll').onchange();");
  assert.equal(selection.run('selectedKeys.size'), 5, 'Last page selects only its remaining icons');
  selection.run("selectedKeys.add('solo/icon-0');updateSelection();");
  assert.equal(selection.run("selectedKeys.has('solo/icon-0')"), false, 'Off-page icons cannot remain selected');
  selection.run("$('pageSize').value='24';$('pageSize').onchange();");
  assert.equal(selection.run('selectedKeys.size'), 0, 'Changing page size clears selection');
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
  assert.equal(gallery.run('currentPageIcons().length'), 3, 'Version groups select exactly the versions rendered on the page');
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

  // Reference images: feedback keeps them, Regenerate carries them into the fix, and both forms send ids.
  const refs = [{id:'a'.repeat(64),kind:'png',name:'shape.png'}];
  const posts = [];
  gallery.context.fetch = async (url, options={}) => { if (options.method === 'POST') posts.push([url, JSON.parse(options.body)]); return {ok:true,status:201,headers:{get:()=> 'application/json'},json:async()=>({status:'pending'}),text:async()=>''}; };
  gallery.run("selected=icons[0];feedbackPicker.set(" + JSON.stringify(refs) + ");$('feedback').value='Softer';");
  await gallery.run("$('feedbackForm').onsubmit({preventDefault(){}})");
  assert.deepEqual(posts.at(-1)[1].reference_images, [refs[0].id]);
  assert.deepEqual(JSON.parse(gallery.run('JSON.stringify(feedbackPicker.ids())')), [], 'Saved feedback clears the picker');
  gallery.run("inspect=()=>{};addRegenerate(" + JSON.stringify({feedback:'Softer',svg_sha256:'x',reference_images:refs}) + ",Object.assign(icons[0],{python_source:{path:'p.py'}}),$('fixActions'));$('fixActions').children.at(-1).onclick();");
  assert.deepEqual(JSON.parse(gallery.run('JSON.stringify(fixPicker.ids())')), [refs[0].id], 'Regenerate carries feedback references');
  await gallery.run("$('fixForm').onsubmit({preventDefault(){}})");
  assert.equal(posts.at(-1)[0], '../api/generation');
  assert.deepEqual(posts.at(-1)[1].reference_images, [refs[0].id]);
  generate.context.fetch = async (url, options={}) => { if (options.method === 'POST') posts.push([url, JSON.parse(options.body)]); return {ok:true,status:202,headers:{get:()=> 'application/json'},json:async()=>(options.method === 'POST' ? {} : [])}; };
  generate.run("referencePicker.set(" + JSON.stringify(refs) + ");");
  await generate.run("$('generateForm').onsubmit({preventDefault(){}})");
  assert.deepEqual(posts.at(-1)[1].reference_images, [refs[0].id]);
  assert.deepEqual(JSON.parse(generate.run('JSON.stringify(referencePicker.ids())')), []);
  console.log('Gallery version groups, rejection, pagination, build-to-grid navigation, and reference images passed.');
}
main().catch(error => { console.error(error); process.exitCode = 1; });

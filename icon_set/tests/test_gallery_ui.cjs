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
  const elements = new Map(), storage = new Map(), navigations = [], listeners = new Map();
  const document = {
    body: new Element(),
    getElementById(id) { if (!elements.has(id)) elements.set(id, new Element()); return elements.get(id); },
    createElement() { return new Element(); }, createTextNode(s) { return s; },
    createDocumentFragment() { return new Element(); }
  };
  const localStorage = { getItem: k => storage.get(k), setItem: (k,v) => storage.set(k,v), removeItem: k => storage.delete(k) };
  const location = { search: '', href: 'http://localhost/gallery/generate.html', assign: url => navigations.push(url) };
  const context = vm.createContext({document, localStorage, sessionStorage: localStorage, location,
    window: {addEventListener(type, handler) { listeners.set(type, handler); }}, history: {replaceState() {}, pushState() {}}, URL, URLSearchParams, console,
    fetch: async () => ({ok: false, json: async () => null})});
  let script = fs.readFileSync(path.join(__dirname, '../scripts/templates', name+'.html'), 'utf8').split('<script>')[1].split('</script>')[0];
  script = name === 'gallery' ? script.slice(0, script.lastIndexOf('(async()=>')) : script.replace('refresh();setInterval(()=>{if(!document.hidden)refresh();},4000);', '');
  vm.runInContext(fs.readFileSync(path.join(__dirname, '../scripts/templates/reference-picker.js'), 'utf8'), context);
  vm.runInContext('var ReferencePicker=window.ReferencePicker,referenceThumbs=window.referenceThumbs;', context);
  vm.runInContext(script, context);
  return {context, document, navigations, dispatch: (type, detail) => listeners.get(type)({detail}), run: code => vm.runInContext(code, context)};
}
async function main() {
  const artwork = page('gallery');
  artwork.run("icons=[{key:'solo/example',family:'solo',icon_id:'example',name:'Example',preview_url:'original.svg'}];reviewsLoaded=true;render();");
  const gridImage = () => {
    const visit = node => node.src ? [node.src] : (node.children || []).flatMap(visit);
    return visit(artwork.document.getElementById('grid'))[0];
  };
  assert.equal(gridImage(), 'original.svg');
  // Review refresh may be slow or stalled; the saved pick must appear immediately.
  artwork.context.fetch = () => new Promise(() => {});
  for (const [mode, url] of [['use_edited','edited.svg'],['use_upload','uploaded.svg'],['use_org','original.svg']]) {
    artwork.dispatch('icon-artwork-saved', {key:'solo/example', artwork_source:mode, preview_url:url});
    assert.equal(gridImage(), url, 'Grid immediately displays the saved '+mode+' selection');
    artwork.run('render();');
    assert.equal(gridImage(), url, 'Rerender retains the picked artwork');
  }

  const types = page('gallery');
  types.run("selected={key:'solo/example'};revision=1;");
  types.context.fetch=async()=>({ok:true,json:async()=>({icon_type:'portrait',updated_by:'jakes'})});
  await types.run('loadIconType(selected,revision)');
  assert.equal(types.run("$('iconType').value"),'__custom__');
  assert.equal(types.run("$('customIconType').value"),'portrait');
  assert.equal(types.run("$('customIconTypeField').hidden"),false);
  const typePosts=[];
  types.context.fetch=async(_url,options)=>{
    const body=JSON.parse(options.body);typePosts.push(body);
    return {ok:true,json:async()=>({...body,updated_by:'jakes'})};
  };
  for(const value of ['human','avatar','']){
    types.run(`$('iconType').value=${JSON.stringify(value)};$('iconType').onchange();`);
    await types.run("$('iconTypeForm').onsubmit({preventDefault(){}})");
    assert.equal(typePosts.at(-1).icon_type,value);
    assert.equal(types.run('selected.icon_type'),value);
    assert.equal(types.run("$('customIconTypeField').hidden"),true);
  }
  types.run("$('iconType').value='__custom__';$('iconType').onchange();$('customIconType').value='  person outline  ';");
  await types.run("$('iconTypeForm').onsubmit({preventDefault(){}})");
  assert.equal(typePosts.at(-1).icon_type,'person outline');
  types.context.fetch=async()=>({ok:false,json:async()=>({error:'Save failed'})});
  types.run("$('customIconType').value='keep my draft';");
  await types.run("$('iconTypeForm').onsubmit({preventDefault(){}})");
  assert.equal(types.run("$('customIconType').value"),'keep my draft');
  assert.equal(types.run("$('iconTypeMessage').textContent"),'Save failed');
  let finishTypeLoad;
  types.context.fetch=()=>new Promise(resolve=>{finishTypeLoad=resolve;});
  const typeLoad=types.run('loadIconType(selected,revision)');
  types.run("revision=2;showIconType('avatar');");
  finishTypeLoad({ok:true,json:async()=>({icon_type:'human'})});
  await typeLoad;
  assert.equal(types.run("$('iconType').value"),'avatar','Stale loads cannot overwrite another icon');

  const pendingReason = page('gallery');
  pendingReason.run(`selected={key:'solo/example',icon_id:'example',family:'solo',svg_sha256:'current'};
    icons=[selected];reviewsLoaded=true;reviews={'solo/example':'ready'};
    render=()=>syncInspector();loadReviewActor=()=>{};loadIconFeedback=()=>{};
    resetPendingReason();syncInspector();`);
  let reasonPosts=[];
  pendingReason.context.fetch=async(url,options)=>{
    reasonPosts.push({url,...JSON.parse(options.body)});
    return {ok:true,json:async()=>({status:'pending',updated_by:'jakes'})};
  };
  pendingReason.run("$('reviewState').value='pending';$('reviewState').onchange();");
  assert.equal(reasonPosts.length,0,'Choosing Pending waits for its reason');
  assert.equal(pendingReason.run("reviews[selected.key]"),'ready');
  assert.equal(pendingReason.run("$('pendingReasonField').hidden"),false);
  await pendingReason.run("$('feedbackForm').onsubmit({preventDefault(){}})");
  assert.equal(reasonPosts.length,0,'Other requires written feedback');
  pendingReason.run("$('pendingReason').value='bad-draw';$('pendingReason').onchange();");
  assert.equal(pendingReason.run("$('feedback').required"),false);
  await pendingReason.run("$('feedbackForm').onsubmit({preventDefault(){}})");
  assert.equal(reasonPosts.length,1,'Reason and status use a single existing feedback request');
  assert.equal(reasonPosts[0].url,'../api/feedback');
  assert.equal(reasonPosts[0].feedback,'Bad stroke drawn');
  assert.equal(reasonPosts[0].svg_sha256,'current');
  assert.equal(pendingReason.run('reviews[selected.key]'),'pending');
  assert.equal(pendingReason.run('disapprovedBy[selected.key]'),'jakes');
  assert.equal(pendingReason.run('feedbackBy[selected.key].join()'),'jakes');
  pendingReason.run("$('pendingReason').value='meaning';$('feedback').value='The shape looks like a leaf.';");
  pendingReason.context.fetch=async()=>({ok:false,json:async()=>({error:'Could not save'})});
  await pendingReason.run("$('feedbackForm').onsubmit({preventDefault(){}})");
  assert.equal(pendingReason.run("$('pendingReason').value"),'meaning','Failed save keeps reason');
  assert.equal(pendingReason.run("$('feedback').value"),'The shape looks like a leaf.','Failed save keeps details');
  pendingReason.context.fetch=async(url,options)=>{
    reasonPosts.push({url,...JSON.parse(options.body)});
    return {ok:true,json:async()=>({status:'pending'})};
  };
  await pendingReason.run("$('feedbackForm').onsubmit({preventDefault(){}})");
  assert.equal(reasonPosts.at(-1).feedback,'Does not convey the intended meaning\n\nThe shape looks like a leaf.');
  pendingReason.run("$('pendingReason').value='other';$('feedback').value='Round the base.';");
  await pendingReason.run("$('feedbackForm').onsubmit({preventDefault(){}})");
  assert.equal(reasonPosts.at(-1).feedback,'Round the base.');
  pendingReason.run("$('pendingReason').value='bad-draw';resetPendingReason();");
  assert.equal(pendingReason.run("$('pendingReason').value"),'other','Opening another icon clears the prior reason');

  const sorting = page('gallery');
  sorting.run(`icons=[
    {key:'solo/a',icon_id:'a',name:'A',family:'solo',created_at:'2026-09-14T12:00:00Z'},
    {key:'solo/b',icon_id:'b',name:'B',family:'solo',created_at:'2026-09-15T13:00:00+07:00'},
    {key:'solo/c',icon_id:'c',name:'C',family:'solo'},
    {key:'sub/d',icon_id:'d',name:'D',family:'sub',created_at:'2026-09-16T00:00:00Z'}
  ];$('family').value='solo';$('iconSort').value='newest';pageSize=1;`);
  assert.equal(sorting.run('filteredIcons().map(i=>i.icon_id).join()'),'b,a,c','Newest first within filters, unknown dates last');
  assert.equal(sorting.run('currentPageIcons()[0].icon_id'),'b','Sort applies before pagination');
  sorting.run("$('iconSort').value='oldest';");
  assert.equal(sorting.run('filteredIcons().map(i=>i.icon_id).join()'),'a,b,c');

  sorting.context.window.location = {href:'http://localhost/gallery/index.html?sort=oldest',search:'?sort=oldest'};
  let savedURL;
  sorting.context.window.history = {replaceState(_state,_title,url){savedURL=url;},pushState(_state,_title,url){savedURL=url;}};
  sorting.run('urlReady=true;restoreURL();');
  assert.equal(sorting.run("$('iconSort').value"),'oldest','Shared URL restores creation sort');
  sorting.run("$('iconSort').value='newest';writeURL();");
  assert.equal(savedURL.searchParams.get('sort'),'newest','Chosen order is saved in the URL');
  sorting.run("urlReady=false;$('family').value='solo';");
  sorting.run("page=3;selectedKeys.add('solo/c');$('iconSort').onchange();");
  assert.equal(sorting.run('page'),1,'Changing order resets pagination');
  assert.equal(sorting.run('selectedKeys.size'),0,'Changing order clears bulk selection');
  sorting.run("$('iconSort').value='name';");
  assert.equal(sorting.run('filteredIcons().map(i=>i.icon_id).join()'),'a,b,c');
  sorting.run("icons[0].modified_at='2026-09-16T00:00:00Z';icons[1].modified_at='2026-09-15T00:00:00Z';$('iconSort').value='modified-newest';pageSize=1;");
  assert.equal(sorting.run('currentPageIcons()[0].icon_id'),'a','Modification sorting differs from creation sorting');
  sorting.run("$('iconSort').value='modified-oldest';");
  assert.equal(sorting.run('filteredIcons().map(i=>i.icon_id).join()'),'b,a,c','Unknown modification dates remain last');
  sorting.context.window.location.search='?sort=modified-newest';
  sorting.run('urlReady=true;restoreURL();');
  assert.equal(sorting.run("$('iconSort').value"),'modified-newest','Shared URL restores modification sort');

  const facets = page('gallery');
  facets.run(`icons=[
    {key:'solo/a',icon_id:'a',name:'A',family:'solo',svg_sha256:'a1',keyshape:'CIRCLE',primitives:[{element_id:'a'},{element_id:'b'},{element_id:'c'}],contours:[{members:['a','b','c']}],original_sources:[{}]},
    {key:'solo/b',icon_id:'b',name:'B',family:'solo',svg_sha256:'b1',keyshape:'SQUARE',primitives:[{element_id:'a'},{element_id:'b'}],variant_of:'a'},
    {key:'solo/c',icon_id:'c',name:'C',family:'solo',svg_sha256:'c2'}
  ];reviewFacets={'solo/a':{svg_sha256:'a1',axes:['vertical','horizontal']},'solo/b':{svg_sha256:'b1',axes:[]},'solo/c':{svg_sha256:'c1',axes:['vertical']}};reviewsLoaded=true;`);
  assert.equal(facets.run('strokeCount(icons[0])'),1,'A contour is one drawn stroke');
  facets.run("$('iconSort').value='strokes-desc';");
  assert.equal(facets.run('filteredIcons().map(i=>i.icon_id).join()'),'b,a,c','Unknown counts sort last');
  facets.run("$('iconSort').value='segments-desc';");
  assert.equal(facets.run('filteredIcons().map(i=>i.icon_id).join()'),'a,b,c','Segments differ from continuous strokes');
  for(const [symmetry,expected] of [['both','a'],['vertical','a'],['symmetric','a'],['asymmetric','b'],['unknown','c']]){
    facets.run(`$('symmetryFilter').value='${symmetry}';`);
    assert.equal(facets.run('filteredIcons().map(i=>i.icon_id).join()'),expected,'Symmetry '+symmetry+' ignores stale measurements');
  }
  facets.run("$('symmetryFilter').value='';$('strokeFilter').value='1-3';$('keyshapeFilter').value='CIRCLE';");
  assert.equal(facets.run('filteredIcons().map(i=>i.icon_id).join()'),'a','Geometry filters combine');
  facets.run("$('keyshapeFilter').value='';$('versionFilter').value='variant';");
  assert.equal(facets.run('filteredIcons().map(i=>i.icon_id).join()'),'b');
  facets.run("$('clearFilters').onclick();$('referenceFilter').value='without';");
  assert.equal(facets.run('filteredIcons().map(i=>i.icon_id).join()'),'b,c');
  facets.run("$('referenceFilter').value='';reviews={'solo/a':'pending','solo/b':'pending','solo/c':'pending'};render=()=>{};");
  facets.context.fetch=async()=>({ok:true,json:async()=>[
    {id:10,icon:'solo/a',svg_sha256:'a1',reason:'meaning'},
    {id:8,icon:'solo/a',svg_sha256:'a1',reason:'bad-stroke'},
    {id:11,icon:'solo/c',svg_sha256:'c1',reason:'meaning'},
    {id:9,icon:'solo/b',svg_sha256:'b1',reason:'bad-draw'}
  ]});
  await facets.run('loadPendingFeedback()');
  for(const [reason,expected] of [['meaning','a'],['bad-stroke','b'],['missing','c']]){
    facets.run(`$('reasonFilter').value='${reason}';$('reasonFilter').onchange();`);
    assert.equal(facets.run('reviewFilter'),'pending');
    assert.equal(facets.run('filteredIcons().map(i=>i.icon_id).join()'),expected,'Latest current revision reason '+reason);
  }
  facets.context.window.location={href:'http://localhost/gallery/index.html',search:'?family=solo&symmetry=both&strokes=1-3&sort=strokes-desc'};
  let facetURL;
  facets.context.window.history={replaceState(_s,_t,url){facetURL=url;},pushState(_s,_t,url){facetURL=url;}};
  facets.run(`for(const [id,values] of [['family',['','solo']],['symmetryFilter',['','both']],['strokeFilter',['','1-3']]])$(id).options=values.map(value=>({value}));urlReady=true;loadReviews=()=>{};restoreURL();`);
  assert.equal(facets.run("$('symmetryFilter').value"),'both');
  assert.equal(facets.run("$('iconSort').value"),'strokes-desc');
  assert.equal(facetURL.searchParams.get('strokes'),'1-3','Facets survive URL restoration');
  facets.run("page=4;selectedKeys.add('solo/a');$('clearFilters').onclick();");
  assert.equal(facets.run('page'),1);
  assert.equal(facets.run('selectedKeys.size'),0);
  assert.equal(facetURL.searchParams.has('symmetry'),false,'Clear removes URL filters');

  const removal = page('gallery');
  removal.run(`feedbackRows=[{id:1,icon:'solo/a',feedback:'Round it'},{id:2,icon:'solo/a',feedback:'Keep'}];
    renderFeedback=()=>{};loadFeedback=async()=>{};loadPendingFeedback=async()=>{};
    feedbackRemover(feedbackRows[0],$('removeActions'));`);
  let removePosts=0;
  removal.context.window.confirm=()=>false;
  removal.context.fetch=async()=>{removePosts++;throw Error('Unexpected request');};
  await removal.run("$('removeActions').children[0].onclick()");
  assert.equal(removePosts,0,'Cancelling removal never sends a request');
  removal.context.window.confirm=()=>true;
  removal.context.fetch=async(url,options)=>{
    removePosts++;
    assert.equal(url,'../api/feedback/delete');
    assert.deepEqual(JSON.parse(options.body),{id:1,previous_feedback:'Round it',previous_edited_at:null});
    return {ok:false,json:async()=>({error:'Feedback changed. Refresh before removing it.'})};
  };
  await removal.run("$('removeActions').children[0].onclick()");
  assert.equal(removal.run('feedbackRows.length'),2,'Failure keeps feedback visible');
  assert.equal(removal.run("$('removeActions').children[0].disabled"),false,'Failure allows retry');
  assert.match(removal.run("$('removeActions').children[1].textContent"),/Feedback changed/);
  removal.context.fetch=async()=>({ok:true,json:async()=>({deleted:true,id:1})});
  await removal.run("$('removeActions').children[0].onclick()");
  assert.equal(removal.run('feedbackRows.map(row=>row.id).join()'),'2','Only the selected feedback disappears');
  assert.equal(removal.run("$('feedbackNotice').textContent"),'Feedback removed.');

  const categories = page('gallery');
  categories.run(`icons=[{key:'solo/a',family:'solo',icon_id:'a',name:'A',category:'animals'}, {key:'solo/b',family:'solo',icon_id:'b',name:'B',category:'tools'}, {key:'sub/c',family:'sub',icon_id:'c',name:'C',category:'tools'}, {key:'solo/d',family:'solo',icon_id:'d',name:'D',category:'tools'}];reviews={'solo/d':'rejected'};$('family').value='solo';$('category').value='animals';`);
  assert.equal(categories.run("categoryCounts().get('animals')"),1);
  assert.equal(categories.run("categoryCounts().get('tools')"),1,'Counts ignore the selected category but respect family and status');
  categories.run("reviewFilter='rejected';");
  assert.equal(categories.run("categoryCounts().get('tools')"),1);
  assert.equal(categories.run("categoryCounts().has('animals')"),false);
  const actions = page('gallery');
  actions.run("icons=[{key:'solo/example',family:'solo',icon_id:'example',name:'Example'}];reviewsLoaded=true;");
  for(const [state, expected] of [['ready',['✓ Approve','Disapprove','Reject']],['pending',['✓ Approve','Reject']],['rejected',['Ready','Discard']]]) {
    actions.run(`reviews['solo/example']='${state}';reviewFilter='${state}';pendingFeedbackLoaded=true;render();`);
    const card=actions.document.getElementById('grid').querySelectorAll('.card[data-key]')[0];
    const footer=card.children.find(child=>child.className==='card-footer');
    assert.deepEqual(footer.children.slice(1).map(button=>button.textContent),expected, state+' card exposes exactly its allowed actions');
  }
  const pending = page('gallery');
  pending.run(`icons=[
    {key:'solo/with',family:'solo',icon_id:'with',name:'With feedback'},
    {key:'solo/without',family:'solo',icon_id:'without',name:'Without feedback'},
    {key:'solo/ready',family:'solo',icon_id:'ready',name:'Ready'}
  ];reviews={'solo/with':'pending','solo/without':'pending','solo/ready':'ready'};
  reviewFilter='pending';render=()=>{};`);
  pending.context.fetch = async () => ({ok:true,json:async()=>[{icon:'solo/with',svg_sha256:'old-revision'}]});
  await pending.run('loadPendingFeedback()');
  pending.run("$('pendingFeedback').value='with';");
  assert.equal(pending.run('filteredIcons().map(i=>i.key).join()'), 'solo/with', 'Saved feedback from earlier revisions still counts');
  pending.run("$('pendingFeedback').value='without';");
  assert.equal(pending.run('filteredIcons().map(i=>i.key).join()'), 'solo/without');
  pending.run("reviewFilter='ready';");
  assert.equal(pending.run('filteredIcons().map(i=>i.key).join()'), 'solo/ready', 'Pending-only filter does not affect other statuses');
  pending.context.fetch = async () => ({ok:false});
  await pending.run('loadPendingFeedback()');
  pending.run("reviewFilter='pending';");
  assert.equal(pending.run('filteredIcons().length'), 0, 'Unavailable feedback must not classify icons as having no feedback');
  const restored = page('gallery');
  restored.run("icons=[{key:'solo/rejected',name:'Rejected',svg_sha256:'current'}];reviews={'solo/rejected':'rejected'};selectedKeys.add('solo/rejected');render=()=>{};");
  const requests=[];
  restored.context.fetch=async(url,options)=>{requests.push({url,body:JSON.parse(options.body)});return {ok:true,json:async()=>({status:'pending'})};};
  await restored.run('restoreIcon(icons[0])');
  assert.equal(requests[0].url, '../api/reject-combination/restore');
  assert.equal(requests[0].body.svg_sha256, 'current');
  assert.equal(restored.run("reviews['solo/rejected']"), 'pending');
  assert.equal(restored.run('selectedKeys.size'), 0);
  restored.run("reviews['solo/rejected']='rejected';");
  restored.context.fetch=async()=>({ok:false,json:async()=>({error:'Restore failed'})});
  await restored.run('restoreIcon(icons[0])');
  assert.equal(restored.run("reviews['solo/rejected']"), 'rejected', 'Failed restores retain rejected status');
  assert.equal(restored.run('saving.size'), 0, 'Restore failure allows retry');
  const authors = page('gallery');
  authors.run(`icons=[{key:'solo/a',family:'solo',icon_id:'a',name:'A',author:'json_to_solo'},{key:'solo/b',family:'solo',icon_id:'b',name:'B',author:'gpt-6'},{key:'solo/c',family:'solo',icon_id:'c',name:'C'}];loadReviews=()=>{};showSection('ai');`);
  assert.equal(authors.run('section'),'icons','Legacy author links open the unfiltered Icons page');
  assert.equal(authors.run('filteredIcons().length'),3,'All authors and missing author metadata remain visible');
  authors.run("reviewsLoaded=true;reviews={'solo/a':'approve','solo/b':'approve'};showSection('final');");
  assert.equal(authors.run('filteredIcons().length'),2,'Approved collection does not filter authors');
  assert.equal(authors.run('section'),'icons','Old Final links open Icons');
  assert.equal(authors.run('reviewFilter'),'approve','Old Final links select Approved');
  const approvers = page('gallery');
  approvers.run(`icons=[
    {key:'solo/a',family:'solo',icon_id:'a',name:'A',category:'animals'},
    {key:'solo/a-v2',family:'solo',icon_id:'a-v2',variant_of:'a',name:'A revised',category:'animals'},
    {key:'solo/b',family:'solo',icon_id:'b',name:'B',category:'tools'},
    {key:'solo/c',family:'solo',icon_id:'c',name:'C',category:'tools'}
  ];reviewsLoaded=true;reviews={'solo/a':'approve','solo/b':'approve','solo/c':'pending'};
  approvedBy={'solo/a':'phuong','solo/b':'hina','solo/c':'phuong'};
  page=4;selectedKeys.add('solo/b');$('approvedBy').value='phuong';$('approvedBy').onchange();`);
  assert.equal(approvers.run('filteredIcons().map(i=>i.key).join()'), 'solo/a');
  assert.equal(approvers.run('page'), 1);
  assert.equal(approvers.run('selectedKeys.size'), 0);
  assert.equal(approvers.run('categoryCounts().has("tools")'), false);
  approvers.run("setIconView('versions');");
  assert.equal(approvers.run('filteredIcons().map(i=>i.key).join()'), 'solo/a', 'Versions must not introduce unapproved siblings');
  approvers.run("$('approvedBy').value='hina';");
  assert.equal(approvers.run('filteredIcons().map(i=>i.key).join()'), 'solo/b');
  approvers.run("$('approvedBy').value='jakes';");
  assert.equal(approvers.run('filteredIcons().length'), 0);
  approvers.run("$('approvedBy').value='';");
  assert.equal(approvers.run('filteredIcons().length'), 3, 'Anyone restores normal version grouping');
  const rejectors = page('gallery');
  rejectors.run(`icons=[
    {key:'solo/a',family:'solo',icon_id:'a',name:'A',category:'animals'},
    {key:'solo/b',family:'solo',icon_id:'b',name:'B',category:'tools'},
    {key:'solo/c',family:'solo',icon_id:'c',name:'C',category:'tools'}
  ];reviewFilter='rejected';`);
  rejectors.context.fetch=async()=>({ok:true,json:async()=>({
    statuses:{'solo/a':'rejected','solo/b':'rejected','solo/c':'approve'},
    approved_by:{'solo/c':'ray'},rejected_by:{'solo/a':'phuong','solo/b':'ray'}
  })});
  await rejectors.run('loadReviews()');
  rejectors.run("page=4;selectedKeys.add('solo/a');$('approvedBy').value='ray';$('approvedBy').onchange();");
  assert.equal(rejectors.run('reviewFilter'),'rejected','Changing reviewer must stay on Rejected');
  assert.equal(rejectors.run("$('reviewerLabel').textContent"),'Rejected by');
  assert.equal(rejectors.run('filteredIcons().map(i=>i.key).join()'),'solo/b','Ray matches rejection attribution, not approval');
  assert.equal(rejectors.run('page'),1);
  assert.equal(rejectors.run('selectedKeys.size'),0);
  assert.equal(rejectors.run('categoryCounts().has("animals")'),false);
  rejectors.run("setIconView('versions');$('approvedBy').value='phuong';$('approvedBy').onchange();");
  assert.equal(rejectors.run('filteredIcons().map(i=>i.key).join()'),'solo/a');
  rejectors.run("$('approvedBy').value='';$('approvedBy').onchange();");
  assert.equal(rejectors.run('reviewFilter'),'rejected');
  assert.equal(rejectors.run('filteredIcons().length'),2,'Anyone shows all rejected icons');
  rejectors.context.window.location={href:'http://localhost/gallery/index.html?status=rejected&approved_by=ray',search:'?status=rejected&approved_by=ray'};
  rejectors.context.window.history={replaceState(){},pushState(){}};
  rejectors.run("$('approvedBy').options=[{value:''},{value:'ray'}];urlReady=true;restoreURL();");
  assert.equal(rejectors.run('reviewFilter'),'rejected','Shared links retain Rejected');
  assert.equal(rejectors.run('filteredIcons().map(i=>i.key).join()'),'solo/b');
  rejectors.run("urlReady=false;reviewFilter='approve';render();");
  assert.equal(rejectors.run("$('reviewerLabel').textContent"),'Approved by');
  assert.equal(rejectors.run('filteredIcons().map(i=>i.key).join()'),'solo/c');
  assert.match(fs.readFileSync(path.join(__dirname,'../scripts/templates/gallery.html'),'utf8'),/<option value="ray">Ray<\/option>/);
  const disapprovers = page('gallery');
  disapprovers.run(`icons=[
    {key:'solo/a',family:'solo',icon_id:'a',name:'A',category:'animals'},
    {key:'solo/a-v2',family:'solo',icon_id:'a-v2',variant_of:'a',name:'A revised',category:'animals'},
    {key:'solo/b',family:'solo',icon_id:'b',name:'B',category:'tools'}
  ];reviewFilter='pending';pendingFeedbackLoaded=true;`);
  disapprovers.context.fetch=async()=>({ok:true,json:async()=>({
    statuses:{'solo/a':'pending','solo/a-v2':'ready','solo/b':'pending'},approved_by:{},
    disapproved_by:{'solo/a':'ray','solo/b':'hina'},feedback_by:{'solo/a':['ray','hina'],'solo/b':['hina']}
  })});
  await disapprovers.run('loadReviews()');
  disapprovers.run("page=4;selectedKeys.add('solo/b');$('approvedBy').value='ray';$('approvedBy').onchange();");
  assert.equal(disapprovers.run('reviewFilter'),'pending','Reviewer selection stays on Disapproved');
  assert.equal(disapprovers.run("$('reviewerLabel').textContent"),'Disapproved by');
  assert.equal(disapprovers.run('filteredIcons().map(i=>i.key).join()'),'solo/a');
  assert.equal(disapprovers.run('selectedKeys.size'),0);
  assert.equal(disapprovers.run('page'),1);
  disapprovers.run("$('approvedBy').value='hina';$('approvedBy').onchange();$('iconFeedbackBy').value='ray';$('iconFeedbackBy').onchange();");
  assert.equal(disapprovers.run('filteredIcons().length'),0,'Disapproval and feedback authors are independent filters');
  disapprovers.run("$('approvedBy').value='';$('approvedBy').onchange();setIconView('versions');");
  assert.equal(disapprovers.run('filteredIcons().map(i=>i.key).join()'),'solo/a','Feedback filter does not include siblings without feedback');
  disapprovers.run("reviews['solo/a']='approve';reviewFilter='approve';render();");
  assert.equal(disapprovers.run('filteredIcons().map(i=>i.key).join()'),'solo/a','Feedback authors still match approved icons');
  disapprovers.run("$('iconFeedbackBy').value='';$('iconFeedbackBy').onchange();");
  assert.equal(disapprovers.run('filteredIcons().length'),2,'Anyone restores normal version grouping');
  let attributionURL;
  disapprovers.context.window.location={href:'http://localhost/gallery/index.html?status=pending&approved_by=ray&icon_feedback_by=hina&feedback_by=ray',search:'?status=pending&approved_by=ray&icon_feedback_by=hina&feedback_by=ray'};
  disapprovers.context.window.history={replaceState(_s,_t,url){attributionURL=url;},pushState(_s,_t,url){attributionURL=url;}};
  disapprovers.run("for(const id of ['approvedBy','iconFeedbackBy','feedbackAuthor'])$(id).options=[{value:''},{value:'ray'},{value:'hina'}];urlReady=true;restoreURL();");
  assert.equal(disapprovers.run('reviewFilter'),'pending');
  assert.equal(disapprovers.run("$('iconFeedbackBy').value"),'hina');
  assert.equal(disapprovers.run("$('feedbackAuthor').value"),'ray');
  assert.equal(attributionURL.searchParams.get('icon_feedback_by'),'hina');
  assert.equal(attributionURL.searchParams.get('feedback_by'),'ray');
  disapprovers.run(`urlReady=false;section='feedback';feedbackLoaded=true;feedbackRows=[
    {id:1,icon:'solo/a',author:'ray',feedback:'Round it'},
    {id:2,icon:'solo/b',author:'hina',edited_by:'ray',feedback:'Keep it'},
    {id:3,icon:'solo/b',feedback:'Legacy anonymous feedback'}
  ];feedbackPage=4;$('feedbackAuthor').oninput();`);
  assert.equal(disapprovers.run('feedbackPage'),1);
  assert.equal(disapprovers.run("$('feedbackCount').textContent"),'1 feedback requests','Feedback matches its author, not its editor');
  disapprovers.run("$('feedbackAuthor').value='';$('feedbackAuthor').oninput();");
  assert.equal(disapprovers.run("$('feedbackCount').textContent"),'3 feedback requests','Anyone includes anonymous feedback');
  const stableTabs = page('gallery');
  stableTabs.run("icons=[{key:'solo/a',family:'solo',icon_id:'a',name:'A'}];reviewsLoaded=true;pendingFeedbackLoaded=true;render();");
  const reviewButtons = [...stableTabs.document.getElementById('reviewTabs').children];
  for (const status of ['pending','approve','rejected','ready']) {
    stableTabs.run(`reviewFilter='${status}';render();`);
    assert.ok(reviewButtons.every((button,index)=>button===stableTabs.document.getElementById('reviewTabs').children[index]),'Review buttons retain their identity and keyboard focus');
    assert.equal(stableTabs.document.getElementById('pendingFeedback').disabled,status!=='pending');
  }
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
  assert.equal(gallery.run('versionGroups(filteredIcons()).find(group=>versionGroupKey(group[0])==="solo/test").map(iconVersion).join(",")'), 'v1,v2,v3,v12');
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
  gallery.run("reviewFilter='';reviews['solo/test']='re-generated';reviewFilter='ready';render();");
  assert.equal(gallery.run('filteredIcons().length'), 4, 'Legacy regenerated statuses now appear under Ready');
  gallery.run("reviewFilter='';pageSize=1;page=2;render();");
  assert.equal(gallery.run('currentPageIcons().length'), 3, 'Version groups select exactly the versions rendered on the page');
  assert.equal(gallery.document.getElementById('grid').querySelectorAll().length, 3, 'Pagination keeps versions together');
  gallery.run("page=1;render();");
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

  // Queue navigation combines status, type and search before pagination.
  const queue = page('generate');
  queue.run(`jobRows=Array.from({length:23},(_,n)=>({id:'run-'+n,name:'Document '+n,prompt:'Folded paper',mode:n%2?'fix':'generate',status:n<13?'candidate':n<18?'running':'accepted',candidate:{key:'solo/doc-'+n,icon_id:'doc-'+n,family:'solo'}}));renderPage();`);
  assert.equal(queue.document.getElementById('jobs').children.length,10);
  const queueButtons = [...queue.document.getElementById('jobFilters').children];
  queue.run('renderPage();');
  assert.ok(queueButtons.every((button,index)=>button===queue.document.getElementById('jobFilters').children[index]),'Queue filtering and polling preserve focused buttons');
  queue.run("jobFilter='candidate';$('jobsMode').value='fix';changePage(1);");
  assert.equal(queue.run('filteredJobs().length'),6);
  queue.run("$('jobsSearch').value='document 11';$('jobsSearch').oninput();");
  assert.equal(queue.run('filteredJobs()[0].id'),'run-11');
  queue.run("$('jobsSearch').value='no match';$('jobsSearch').oninput();");
  assert.equal(queue.document.getElementById('jobs').children[0].className,'queue-empty');
  queue.run("$('jobsSearch').value='';$('jobsMode').value='';jobFilter='candidate';changePage(2);");
  assert.equal(queue.document.getElementById('jobs').children.length,3);
  queue.run("jobFilter='accepted';changePage(8);");
  assert.equal(queue.run('page'),1,'Filters clamp the page to the matching results');
  queue.run(`location.search='?status=running&q=paper&mode=fix&page_size=25';readPages();`);
  assert.equal(queue.run('jobFilter'),'running');
  assert.equal(queue.run('pageSize'),25);
  assert.equal(queue.run('filteredJobs().length'),3);
  assert.equal(queue.run("matchesJobStatus({status:'accepting'},'running')"),true);
  // Retrying a failed new icon restores the brief without starting another paid run.
  queue.run(`render([{id:'failed',name:'Paper',prompt:'Fold the corner',family:'solo',model:'test-model',mode:'generate',status:'failed'}]);`);
  const retry=queue.document.getElementById('jobs').children[0].children.find(el=>el.className==='job-actions').children.find(el=>el.textContent==='Edit brief & retry');
  retry.onclick();
  assert.equal(queue.document.getElementById('name').value,'Paper');
  assert.equal(queue.document.getElementById('prompt').value,'Fold the corner');
  assert.equal(queue.document.getElementById('family').value,'solo');
  // Direct result links escape existing filters and land on the right page.
  queue.context.location.hash='#job-run-17';
  queue.context.fetch=async()=>({ok:true,headers:{get:()=> 'application/json'},json:async()=>JSON.parse(queue.run('JSON.stringify(jobRows)'))});
  queue.run("locateHash=true;pageSize=10;jobFilter='candidate';");
  await queue.run('refresh()');
  assert.equal(queue.run('jobFilter'),'all');
  assert.equal(queue.run('page'),2);

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

// Run with: node icon_set/tests/test_primitives_briefs_ui.cjs
const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
const source=fs.readFileSync(__dirname+'/../scripts/templates/primitives.html','utf8').split('<script>')[1].split('</script>')[0];
const context=vm.createContext({document:{getElementById(){}},URL,URLSearchParams});
vm.runInContext(source.slice(0,source.indexOf("for(const [k,l] of Object.entries(REASONS))")),context);
const run=s=>vm.runInContext(s,context);
run(`catalog={root_label:'pictographic-primitives',rows:[
  {uuid:'ready',category:'food',batch:'1',state:'none',path:'food/a.svg'},
  {uuid:'missing',category:'food',batch:'1',state:'none',path:'food/b.svg'},
  {uuid:'generated',category:'food',batch:'1',state:'generated'},
  {uuid:'skipped',category:'food',batch:'1',state:'none'},
  {uuid:'elsewhere',category:'food',batch:'2',state:'none',path:'food/c.svg'},
  {uuid:'other',category:'other',state:'none'}]};
  statuses={skipped:{reason:'container'},generated:{reason:'container'}};
  referenceBriefs=Object.fromEntries(['ready','generated','skipped','elsewhere','other'].map(uuid=>[uuid,{family:'solo',brief:'Saved brief'}]));
  briefsAvailable=statusesAvailable=true;state.category='food';state.batch='1';`);
assert.equal(run('JSON.stringify(briefCounts(categoryRows("food")))'),JSON.stringify({brief_ready:2,brief_missing:1}));
assert.equal(run('JSON.stringify(readyBriefHandoff().briefs.map(r=>r.uuid))'),'["ready"]','Export excludes generated, skipped, other categories, and other batches');
assert.equal(run('readyBriefHandoff().briefs[0].reference_path'),'pictographic-primitives/food/a.svg');
run("state.brief='ready'");assert.equal(run('JSON.stringify(detailRows().map(r=>r.uuid))'),'["ready"]');
run("state.brief='missing'");assert.equal(run('JSON.stringify(detailRows().map(r=>r.uuid))'),'["missing"]');
assert.equal(run('JSON.stringify(missingBriefHandoff().primitives.map(r=>r.uuid))'),'["missing"]','Missing-brief task excludes saved briefs, generated, skipped, other categories and batches');
assert.equal(run('missingBriefHandoff().primitives[0].reference_path'),'pictographic-primitives/food/b.svg');
assert.equal(run('matchesCategoryBrief({todo:3,brief_ready:2,brief_missing:1},"missing")'),true,'Partially processed categories still need briefs');
assert.equal(run('matchesCategoryBrief({todo:3,brief_ready:2,brief_missing:1},"none")'),false);
assert.equal(run('matchesCategoryBrief({todo:3,brief_ready:0,brief_missing:3},"none")'),true);
assert.equal(run('matchesCategoryBrief({todo:0,brief_ready:0,brief_missing:0},"none")'),false,'Finished categories do not need briefs');
run('statusesAvailable=false');
assert.equal(run('missingBriefHandoff().primitives.length'),0);
assert.equal(run('matchesCategoryBrief({todo:3,brief_ready:0,brief_missing:3},"missing")'),false);
assert.equal(run('readyBriefHandoff().briefs.length'),0,'Unknown skip status must not export possibly skipped originals');
run('statusesAvailable=true;briefsAvailable=false');assert.equal(run('readyBriefHandoff().briefs.length'),0);
run('briefsAvailable=true;referenceBriefs.ready.brief="  "');assert.equal(run('readyBriefHandoff().briefs.length'),0,'Blank briefs are not ready');
assert.equal(run('briefProgress({todo:0})'),'No TODO icons');
assert.equal(run('briefProgress({todo:2,brief_ready:2,brief_missing:0})'),'All TODO briefs processed');
assert.equal(run('briefProgress({todo:2,brief_ready:1,brief_missing:1})'),'Partially processed');
console.log('TODO brief counts, filters, export scope, and unavailable-data checks passed.');

run("state.view='todo';state.category='';state.batch='';state.brief='';state.q='';statusesAvailable=true;briefsAvailable=true;");
assert.equal(run('JSON.stringify(detailRows().map(r=>r.uuid))'),'["ready","missing","elsewhere","other"]','All-TODO grid spans categories but excludes generated and skipped');
run("state.category='other'");assert.equal(run('JSON.stringify(detailRows().map(r=>r.uuid))'),'["other"]');
run("state.category='';state.brief='ready'");assert.equal(run('JSON.stringify(detailRows().map(r=>r.uuid))'),'["elsewhere","other"]');
run('statusesAvailable=false');assert.equal(run('detailRows().length'),0,'Do not show possibly skipped icons when statuses are unavailable');
run('statusesAvailable=true;const manyRows=Array.from({length:123},(_,uuid)=>({uuid}));page=1;');
assert.equal(run('pageRows(manyRows).length'),50);
run('page=2');assert.equal(run('pageRows(manyRows).length'),50);assert.equal(run('pageRows(manyRows)[0].uuid'),50);
run('page=3');assert.equal(run('pageRows(manyRows).length'),23);assert.equal(run('pageRows(manyRows)[0].uuid'),100);
context.location={href:'http://localhost/gallery/primitives.html',search:'?view=todo&brief=missing&page=2'};
context.history={replaceState(_a,_b,url){context.savedURL=String(url);}};
run('readURL();writeURL()');assert.equal(run('state.view'),'todo');assert.equal(run('page'),2);assert.ok(context.savedURL.includes('brief=missing'));assert.ok(context.savedURL.includes('page=2'));
for(const [target,pages,expected] of [['first',8,1],['middle',8,4],['middle',9,5],['last',8,8],['last',1,1]]){
  context.location.search='?view=todo&brief=missing&page='+target;
  run(`readURL();resolvePage(${pages});writeURL()`);
  assert.equal(run('page'),expected,`${target} resolves after filtering to ${pages} pages`);
  assert.ok(context.savedURL.includes('page='+target),'Named page remains bookmarkable');
}
context.location.search='?view=todo&brief=missing&page=last';
run('readURL();resolvePage(8);resolvePage(6)');assert.equal(run('page'),6,'Last follows a shrinking filtered result set');
context.location.search='?view=todo&brief=missing&page=999';
run('readURL();resolvePage(8)');assert.equal(run('page'),8,'Numeric pages still clamp');
context.location.search='?view=todo&brief=missing&page=invalid';
run('readURL();resolvePage(8)');assert.equal(run('page'),1,'Invalid pages still fall back to first');
context.location.search='?category=food';run('readURL()');assert.equal(run('state.view'),'category','Existing category links retain their behavior');
context.location.search='';run('readURL()');assert.equal(run('state.view'),'todo','Default view is all TODO icons');
console.log('All-TODO grid scope, 50-item pagination, and URL state checks passed.');

(async()=>{
  context.document.hidden=false;
  context.document.querySelector=()=>null;
  run("state.view='todo';state.category='';state.batch='';state.brief='missing';state.q='';state.reason='';statusesAvailable=briefsAvailable=true;referenceBriefs={};statuses={skipped:{reason:'container'}};selected.clear();show=()=>{};");
  assert.ok(!JSON.parse(run('JSON.stringify(detailRows().map(r=>r.uuid))')).includes('skipped'),'SKIP with no brief is excluded');
  let nextStatuses={skipped:{reason:'container'},missing:{reason:'container'}};
  context.fetch=async url=>({ok:true,json:async()=>url.endsWith('/status')?nextStatuses:{}});
  await run('refreshGalleryState()');
  assert.ok(!JSON.parse(run('JSON.stringify(detailRows().map(r=>r.uuid))')).includes('missing'),'External SKIP disappears after automatic refresh');
  run("briefDrafts.set('ready',{brief:'Human draft'});");nextStatuses={...nextStatuses,ready:{reason:'container'}};
  await run('refreshGalleryState()');
  assert.equal(run('statuses.ready'),undefined,'Refresh preserves active edits');
  assert.equal(run("briefDrafts.get('ready').brief"),'Human draft');
  run('briefDrafts.clear();');
  await run('refreshGalleryState()');assert.equal(run('statuses.ready.reason'),'container');
  context.fetch=async()=>{throw Error('offline');};await run('refreshGalleryState()');
  assert.equal(run('detailRows().length'),0,'Unavailable live statuses never show stale TODO candidates');
  context.fetch=async url=>({ok:true,json:async()=>url.endsWith('/status')?nextStatuses:{}});
  await run('refreshGalleryState()');assert.equal(run('statusesAvailable'),true,'Refresh recovers after failure');
  context.fetch=async url=>({ok:true,json:async()=>{run('galleryRevision++');return {};}});
  await run('refreshGalleryState()');assert.equal(run('statuses.ready.reason'),'container','An older refresh cannot replace state after a local write');
  console.log('Live TODO-only missing-brief refresh, edit preservation, failure, recovery and save-race checks passed.');
})().catch(error=>{console.error(error);process.exitCode=1;});

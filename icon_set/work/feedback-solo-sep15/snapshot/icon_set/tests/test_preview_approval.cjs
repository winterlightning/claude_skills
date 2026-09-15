// Run: node icon_set/tests/test_preview_approval.cjs
const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
const source=fs.readFileSync(require('node:path').join(__dirname,'../scripts/templates/preview-library.js'),'utf8');
async function main(){
  const context=vm.createContext({window:{},fetch:async()=>{throw Error('offline');}});
  vm.runInContext(source,context);
  const catalog={icons:[{family:'solo',icon_id:'yes'},{family:'solo',icon_id:'pending'},{family:'solo',icon_id:'rejected'},{family:'solo',icon_id:'missing'},{family:'container',icon_id:'yes'}]};
  const statuses={'solo/yes':'approve','solo/pending':'pending','solo/rejected':'rejected','sub/yes':'approve'};
  assert.deepEqual(Array.from(context.window.approvedPreviewIcons(catalog,statuses),i=>i.family+'/'+i.icon_id),['solo/yes']);
  const saved=context.window.approvedPreviewReplacements({hero:'yes',nav:'pending',footer:'missing'},context.window.approvedPreviewIcons(catalog,statuses));
  assert.equal(JSON.stringify(saved),JSON.stringify({hero:'yes'}),'Saved edits cannot bypass approval');
  assert.equal(JSON.stringify(context.window.approvedPreviewReplacements(['yes'],catalog.icons)),'{}');
  assert.equal(context.window.approvedPreviewIcons(catalog,{}).length,0,'Missing statuses never imply approval');
  assert.throws(()=>context.window.approvedPreviewIcons(catalog,null));
  await assert.rejects(context.window.loadApprovedPreviewIcons(),'Unavailable API must fail closed');
  context.fetch=async url=>({ok:!url.includes('reviews'),json:async()=>catalog});
  await assert.rejects(context.window.loadApprovedPreviewIcons());
  const requests=[];
  context.fetch=async(url,options)=>{requests.push({url,options});return{ok:true,json:async()=>url.includes('reviews')?statuses:catalog};};
  assert.equal((await context.window.loadApprovedPreviewIcons()).length,1);
  assert.ok(requests.every(r=>r.options.cache==='no-store'));
  statuses['solo/yes']='pending';
  assert.equal((await context.window.loadApprovedPreviewIcons()).length,0,'Revoked approval is excluded on the next check');
  console.log('Preview approval filtering, identity, live refresh, and unavailable-status checks passed.');
}
main().catch(e=>{console.error(e);process.exitCode=1;});

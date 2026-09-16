const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
function setup(){
  const context=vm.createContext({window:{},Map,Promise,encodeURIComponent});
  vm.runInContext(fs.readFileSync(__dirname+'/../scripts/templates/icon-feedback.js','utf8'),context);
  let icon={key:'solo/a',svg_sha256:'v1'};
  const drafts=new Map(),elements=Object.fromEntries(['button','status','result','text','feedback'].map(k=>[k,{value:''}]));
  let resolvePoll,posts=0,revealed=0;
  const responses=[],delay=async()=>{};
  const request=async(url,options)=>{
    if(options?.method==='POST'){posts++;return {ok:true,json:async()=>({id:'job'})};}
    const response=responses.shift();
    if(response instanceof Error)throw response;
    if(response)return {ok:true,json:async()=>response};
    return new Promise(resolve=>{resolvePoll=result=>resolve({ok:true,json:async()=>result});});
  };
  const api=context.window.IconFeedbackReviewer({getIcon:()=>icon,getDraft:k=>icon?.key===k?elements.feedback.value:drafts.get(k)||'',setDraft:(k,v)=>drafts.set(k,v),elements,reveal:()=>revealed++,request,delay});
  return {api,elements,drafts,responses,setIcon:i=>{icon=i;},finish:r=>resolvePoll(r),posts:()=>posts,revealed:()=>revealed};
}
const result=(extra={})=>({status:'completed',icon:'solo/a',svg_sha256:'v1',verdict:'repair',feedback:'Repair: balance the curves.',...extra});
const tick=()=>new Promise(resolve=>setImmediate(resolve));
(async()=>{
  const a=setup();a.elements.feedback.value='Keep the handle.';
  const running=a.api.ask();await tick();await a.api.ask();assert.equal(a.posts(),1);
  a.elements.feedback.value='Keep the handle. And the base.';
  a.finish(result());await running;
  assert.equal(a.elements.feedback.value,'Keep the handle. And the base.\n\nRepair: balance the curves.');
  assert.equal(a.revealed(),1);assert.equal(a.elements.button.disabled,false);
  const b=setup(),pending=b.api.ask();await tick();
  b.setIcon({key:'solo/b',svg_sha256:'v2'});b.elements.feedback.value='B draft';b.api.open();
  b.finish(result());await pending;assert.equal(b.elements.feedback.value,'B draft');
  assert.equal(b.drafts.get('solo/a'),'Repair: balance the curves.');
  const c=setup(),old=c.api.ask();await tick();c.setIcon({key:'solo/a',svg_sha256:'v2'});c.elements.feedback.value='New artwork draft';
  c.finish(result());await old;assert.equal(c.elements.feedback.value,'New artwork draft');assert.equal(c.drafts.size,0);
  const d=setup();d.responses.push(new Error('Connection lost'));await d.api.ask();
  assert.match(d.elements.status.textContent,/Connection lost/);d.responses.push(result({verdict:'keep',feedback:'Keep. No changes needed.'}));
  await d.api.ask();assert.equal(d.posts(),1);assert.match(d.elements.feedback.value,/No changes needed/);
  assert.match(d.elements.status.textContent,/no decision has been saved/);
  const e=setup();e.elements.feedback.value='x'.repeat(9000);e.responses.push(result({feedback:'y'.repeat(3000)}));
  await e.api.ask();assert.equal(e.elements.feedback.value.length,9000);assert.equal(e.elements.text.value.length,3000);assert.equal(e.elements.result.hidden,false);
  const f=setup();f.responses.push({status:'stale',error:'Artwork changed'});await f.api.ask();assert.equal(f.elements.feedback.value,'');assert.match(f.elements.status.textContent,/Artwork changed/);
  console.log('AI feedback drafts, keep verdicts, retry, stale results and concurrent edits passed.');
})().catch(error=>{console.error(error);process.exitCode=1;});

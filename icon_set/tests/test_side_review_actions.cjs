const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const elements=[];
class Element{
 constructor(tag){this.tag=tag;this.children=[];this.dataset={};this.className='';this.attributes={};this.isConnected=true;elements.push(this);}
 get classList(){return {contains:c=>this.className.split(' ').includes(c),add(){},toggle(){}}}
 append(...xs){for(const x of xs){this.children.push(x);if(x instanceof Element)x.parentElement=this;}}
 prepend(...xs){this.append(...xs)}
 replaceChildren(...xs){this.children=[];this.append(...xs)}
 setAttribute(k,v){this.attributes[k]=v}
 toggleAttribute(k,v){if(v)this.attributes[k]='';else delete this.attributes[k]}
 querySelectorAll(q){return this.children.filter(x=>x instanceof Element&&(q==='button'?x.tag==='button':x.classList.contains(q.slice(1))))}
 querySelector(q){if(this.tag==='dialog'){this.parts??={};return this.parts[q]??=new Element(q==='form'?'form':'div');}return this.querySelectorAll(q)[0]||null}
 after(){} remove(){} showModal(){} close(){}
}
const calls=[],responses=[],document={createElement:t=>new Element(t),head:new Element('head'),body:new Element('body'),
 addEventListener(){},dispatchEvent(){},querySelectorAll:q=>elements.filter(e=>e.classList.contains(q.slice(1))),getElementById(){return null},querySelector(){return null}};
const c=vm.createContext({document,window:{},location:{protocol:'http:'},localStorage:{getItem(){},setItem(){}},CustomEvent:class{},queueMicrotask:fn=>fn(),
 fetch:async(url,opts)=>{calls.push([url,opts?.body&&JSON.parse(opts.body)]);const next=responses.shift()||{status:'pending'};return {ok:!next.error,status:next.error?500:200,json:async()=>next}}});
vm.runInContext(fs.readFileSync('icon_set/scripts/templates/side-repair-flags.js','utf8'),c);
(async()=>{
 const api=c.window.SideRepairFlags,item={icon:'example',family:'solo',sha256:'latest'},pair={id:'pair',concept:'Example'};
 api.setReviews({'solo/example':'ready'});
 const a=api.button('main',item,pair),b=api.button('main',item,pair);
 const [approve,disapprove]=a.querySelectorAll('button');
 assert.equal(approve.textContent,'Approve');assert.equal(disapprove.textContent,'Disapprove');
 responses.push({status:'approve'});await approve.onclick();
 assert.deepEqual(calls.at(-1),['/api/reviews',{icon:'solo/example',svg_sha256:'latest',status:'approve'}]);
 assert.equal(a.dataset.status,'approve');assert.equal(b.dataset.status,'approve');assert.equal(approve.disabled,true);assert.equal(disapprove.disabled,false);
 responses.push({status:'pending'});await disapprove.onclick();
 assert.equal(calls.at(-1)[0],'/api/feedback');assert.equal(a.dataset.status,'pending');assert.equal(approve.disabled,false);assert.equal(disapprove.disabled,true);
 responses.push({error:'Cannot save'});await approve.onclick();
 assert.equal(a.dataset.status,'pending');assert.equal(approve.disabled,false);
 responses.push({status:'approve'});await approve.onclick();assert.equal(a.dataset.status,'approve');
 api.setReviews({'solo/example':'claimed'});assert.equal(approve.disabled,true);assert.equal(disapprove.disabled,true);
 api.setReviews({'solo/example':'rejected'});assert.equal(approve.disabled,true);assert.equal(disapprove.disabled,true);
 console.log('Direct approve/disapprove, revision targeting, shared status, failure recovery and protected states passed.');
})().catch(e=>{console.error(e);process.exitCode=1});

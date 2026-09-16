const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const elements=new Map(),events=[];
const $=id=>{if(!elements.has(id))elements.set(id,{value:'',files:[]});return elements.get(id);};
const response=(data,ok=true)=>({ok,json:async()=>data});
const original={key:'solo/example',icon_id:'example',preview_url:'../solo48/example.svg',svg_sha256:'source'};
const loaded={choice:null,svg_sha256:'source',edit_revision:2,preview_url:'../api/icon-artwork/svg?icon=solo/example'};
let unsaved=false;
const context=vm.createContext({console,window:{dispatchEvent:e=>events.push(e),StrokeEditor:{hasUnsavedChanges:()=>unsaved}},
 document:{getElementById:$,addEventListener:(_e,fn)=>fn()},CustomEvent:class{constructor(type,opts){this.type=type;this.detail=opts.detail;}},fetch:async()=>response(loaded)});
vm.runInContext(fs.readFileSync(__dirname+'/../scripts/templates/icon-artwork.js','utf8'),context);
const tick=()=>new Promise(r=>setImmediate(r));
(async()=>{
 const ui=context.window.IconArtwork;
 ui.open(original);await tick();assert.equal($('artworkMode').value,'use_org');
 $('artworkMode').value='use_upload';await $('artworkApply').onclick();assert.match($('artworkStatus').textContent,/Choose an SVG/);
 $('artworkFile').files=[{name:'bad.png',size:1}];$('artworkFile').onchange();assert.match($('artworkStatus').textContent,/SVG file/);
 const svg='<svg viewBox="0 0 48 48"><path d="M0 0L20 20"/></svg>';
 $('artworkFile').files=[{name:'manual.svg',size:svg.length,text:async()=>svg}];$('artworkFile').onchange();
 assert.equal($('artworkMode').value,'use_upload');
 let body;
 context.fetch=async(url,options)=>{body=JSON.parse(options.body);return response({...loaded,choice:{source_mode:'use_upload',revision:1,uploaded:{name:'manual.svg'}},record:{...original,artwork_source:'use_upload'}});};
 await $('artworkApply').onclick();assert.equal(body.svg,svg);assert.equal(body.revision,0);assert.equal(body.source_mode,'use_upload');
 assert.equal(events.length,1);assert.equal(events[0].detail.artwork_source,'use_upload');
 assert.match($('artworkCurrent').textContent,/Uploaded/);
 $('artworkMode').value='use_edited';unsaved=true;
 await $('artworkApply').onclick();assert.match($('artworkStatus').textContent,/Save your gallery edits/);
 unsaved=false;ui.editSaved(original.key,4);
 context.fetch=async(url,options)=>{body=JSON.parse(options.body);return response({error:'Someone changed this artwork.'},false);};
 await $('artworkApply').onclick();assert.equal(body.edit_revision,4);assert.equal(body.svg,undefined);assert.match($('artworkStatus').textContent,/Someone changed/);
 // A late save cannot update a different icon's inspector.
 let resolve;context.fetch=()=>new Promise(r=>resolve=r);
 const saving=$('artworkApply').onclick();
 const savedResolve=resolve;context.fetch=async()=>response(loaded);
 ui.open({...original,key:'solo/other',icon_id:'other'});await tick();
 savedResolve(response({...loaded,choice:{source_mode:'use_edited'},record:original}));await saving;
 assert.equal(events.length,1);assert.equal($('artworkMode').value,'use_org');
 console.log('Artwork upload, source choice, saved-edit binding, failure recovery, and stale-response UI checks passed.');
})().catch(e=>{console.error(e);process.exitCode=1;});

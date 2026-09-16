// Run with node icon_set/tests/test_stroke_editor_ui.cjs.
const assert=require('node:assert/strict'), fs=require('node:fs'), vm=require('node:vm');
class Element {
  constructor(){this.value='';this.children=[];this.attrs={};this.dataset={};}
  setAttribute(k,v){this.attrs[k]=v;}
  append(...values){this.children.push(...values);}
  replaceChildren(...values){this.children=values;}
  focus(){}
  getAttribute(k){return this.attrs[k];}
  getBBox(){
    // Resize interactions below use straight-sided fixtures; the browser supplies real SVG bounds.
    const points=[...(this.attrs.d || '').matchAll(/[ML](-?[\d.]+) (-?[\d.]+)/g)].map(m=>[+m[1],+m[2]]);
    const xs=points.map(p=>p[0]),ys=points.map(p=>p[1]);
    return {x:Math.min(...xs),y:Math.min(...ys),width:Math.max(...xs)-Math.min(...xs),height:Math.max(...ys)-Math.min(...ys)};
  }
  createSVGPoint(){return {x:0,y:0,matrixTransform(){return this;}};}
  getScreenCTM(){return {inverse(){return {};}};}
  setPointerCapture(){}
}
const elements=new Map(), storage=new Map();
const $=id=>{if(!elements.has(id))elements.set(id,new Element());return elements.get(id);};
const context=vm.createContext({console,window:{addEventListener(){},confirm:()=>true},
  document:{getElementById:$,createElement:()=>new Element(),createElementNS:()=>new Element(),addEventListener:(_event,fn)=>fn()},
  localStorage:{getItem:k=>storage.get(k),setItem:(k,v)=>storage.set(k,v),removeItem:k=>storage.delete(k)},
  fetch:async()=>response({svg_sha256:'sha',edit:null,previous_versions:[]})});
function response(body,ok=true){return {ok,headers:{get:()=> 'application/json'},json:async()=>body};}
const run=code=>vm.runInContext(code,context);
run(fs.readFileSync(__dirname+'/../scripts/templates/stroke-editor.js','utf8'));
const icon={key:'sub/test',icon_id:'test',svg_sha256:'sha',canvas_size:32,primitives:[
 {kind:'line',element_id:'a',start:[2,2],end:[8,2]},
 {kind:'arc',element_id:'b',start:[8,2],end:[12,6],radius_x:4,radius_y:4,large_arc:false,sweep:true},
 {kind:'bezier',element_id:'c',start:[2,10],end:[12,10],segments:[[[4,8],[10,8],[12,10]]]}],
 contours:[{contour_id:'outline',members:['a','b'],closed:false}]};
const resizeIcon={...icon,primitives:[
 {kind:'line',element_id:'a',start:[2,2],end:[12,2]},
 {kind:'line',element_id:'b',start:[12,2],end:[12,6]},
 {kind:'line',element_id:'c',start:[12,6],end:[2,6]},
 {kind:'line',element_id:'d',start:[2,6],end:[2,2]},
 {kind:'line',element_id:'extra',start:[16,16],end:[18,18]}],
 contours:[{contour_id:'outline',members:['a','b','c','d'],closed:true}]};
context.icon=icon;
const tick=()=>new Promise(resolve=>setImmediate(resolve));
(async()=>{
  const editor=context.window.StrokeEditor;
  const groups=editor.groups(icon);
  assert.equal(groups.length,2);
  assert.equal(editor.pathData(icon,groups[0]),'M2 2L8 2A4 4 0 0 1 12 6');
  const edited=editor.translatedGraph(icon,groups,{'contour:outline':[2,3],'primitive:c':[.5,-1]});
  assert.deepEqual(JSON.parse(JSON.stringify(edited.primitives[2].segments)),[[[4.5,7],[10.5,7],[12.5,9]]]);
  assert.deepEqual(icon.primitives[0].start,[2,2]);
  editor.open(resizeIcon);assert.equal($('reviewTab').attrs['aria-selected'],'true');assert.equal($('inspectorWorkspace').dataset.tab,'review');$('editingTab').onclick();await tick();
  assert.equal($('strokeX').disabled,false);
  $('strokeCanvas').onkeydown({key:'ArrowRight',preventDefault(){}});
  assert.equal($('strokeX').value,1);
  $('strokeUndo').onclick();assert.equal($('strokeX').value,0);
  $('strokeRedo').onclick();assert.equal($('strokeX').value,1);
  $('reviewTab').onclick();$('editingTab').onclick();assert.equal($('strokeX').value,1);
  // Typed odd dimensions snap to even bounds without locking the other axis.
  $('strokeScaleX').valueAsNumber=19;
  $('strokeScaleX').onchange();assert.equal($('strokeScaleX').value,20);assert.equal($('strokeScaleY').value,8);
  $('strokeUndo').onclick();assert.equal($('strokeScaleX').value,14);assert.equal($('strokeX').value,1);
  $('strokeRedo').onclick();assert.equal($('strokeScaleX').value,20);
  $('strokeReset').onclick();assert.equal($('strokeScaleX').value,14);assert.equal($('strokeX').value,0);
  $('strokeUndo').onclick();assert.equal($('strokeScaleX').value,20);
  const resizedOffset=$('strokeX').value;
  $('strokeScope').value='icon';$('strokeScope').onchange();
  $('strokeScaleX').valueAsNumber=27;$('strokeScaleX').onchange();
  assert.equal($('strokeScaleX').value,28);assert.equal($('strokeScaleY').value%2,0);
  $('strokeUndo').onclick();$('strokeScope').value='stroke';$('strokeScope').onchange();
  // Dragging uses the same snap even with movement snapping turned off.
  const canvas=$('strokeCanvas'), handle=canvas.children.find(e=>e.attrs['data-resize']);
  $('strokeSnap').checked=false;
  canvas.onpointerdown({target:handle,button:0,pointerId:1,clientX:20,clientY:12,preventDefault(){}});
  canvas.onpointermove({pointerId:1,clientX:22.3,clientY:13.1});
  canvas.onpointerup({pointerId:1});
  assert.equal($('strokeScaleX').value%2,0);assert.equal($('strokeScaleY').value%2,0);
  $('strokeUndo').onclick();assert.equal($('strokeScaleX').value,20);
  // Degenerate lines keep their stroke thickness; fractional centers snap onto the grid.
  const snapped=editor.snappedResize({width:10,height:6,cx:7.4,cy:9.7},1.27,1.38,4);
  assert.equal(10*snapped.rx+4,16);assert.equal(6*snapped.ry+4,12);
  assert.equal(snapped.cx,7);assert.equal(snapped.cy,10);
  assert.equal(editor.snappedResize({width:0,height:10,cx:1,cy:2},2,1.3,4).rx,1);
  context.fetch=async()=>response({error:'Conflict'},false);
  await $('strokeSave').onclick();assert.match($('strokeStatus').textContent,/Conflict/);assert.equal($('strokeX').value,resizedOffset);
  assert.equal(storage.size,1);
  let post;
  context.fetch=async(_url,options)=>{post=JSON.parse(options.body);return response({revision:1,updated_by:'jakes',offsets:post.offsets,scales:post.scales});};
  await $('strokeSave').onclick();assert.equal(post.revision,0);assert.equal(storage.size,0);assert.equal($('strokeSave').disabled,true);
  // A late save cannot replace the next icon's state.
  $('strokeCanvas').onkeydown({key:'ArrowRight',preventDefault(){}});
  let resolve;
  context.fetch=()=>new Promise(r=>resolve=r);
  const pending=$('strokeSave').onclick();editor.open({...icon,key:'sub/other'});
  resolve(response({revision:2,offsets:{'contour:outline':[2,0]}}));await pending;
  assert.equal($('strokeX').value,0);assert.equal($('strokeSave').disabled,true);
  // A rebuilt catalog cannot silently apply a saved edit onto old geometry.
  context.fetch=async()=>response({svg_sha256:'new-sha',edit:null});
  $('editingTab').onclick();await tick();assert.match($('strokeStatus').textContent,/icon changed/);assert.equal($('strokeSave').disabled,true);
  // Keyshape experiments are undoable, persisted, and checked against the current draft.
  context.fetch=async()=>response({svg_sha256:'sha',edit:null,previous_versions:[]});
  editor.open({...resizeIcon,keyshape:'VRECT_L'});$('editingTab').onclick();await tick();
  $('strokeKeyshape').value='VRECT_M';$('strokeKeyshape').onchange();
  assert.equal($('strokeSave').disabled,false);
  $('strokeUndo').onclick();assert.equal($('strokeKeyshape').value,'VRECT_L');
  $('strokeRedo').onclick();assert.equal($('strokeKeyshape').value,'VRECT_M');
  let checked;
  const report={status:'fail',keyshape:'VRECT_M',errors:['Does not fit VRECT_M'],checks_run:['canvas/keyshape bounds']};
  context.fetch=async(_url,options)=>{checked=JSON.parse(options.body);return response(report);};
  await $('strokeValidate').onclick();
  assert.equal(checked.keyshape,'VRECT_M');assert.equal($('strokeValidation').dataset.status,'fail');
  context.fetch=async(_url,options)=>{const body=JSON.parse(options.body);assert.equal(body.validate,true);return response({...body,revision:1,validation:report,updated_by:'jakes'});};
  await $('strokeSave').onclick();assert.equal($('strokeSave').disabled,true);
  // A human decision is saved separately from failed automatic findings.
  $('strokeForcePass').checked=true;$('strokeForcePass').onchange();
  assert.equal($('strokeSave').disabled,true,'A reason is required');
  $('strokeOverrideReason').value='Visually reviewed: intentional circle.';$('strokeOverrideReason').oninput();
  assert.equal($('strokeSave').disabled,false);
  context.fetch=async(_url,options)=>{const body=JSON.parse(options.body);assert.equal(body.validation_override.reason,'Visually reviewed: intentional circle.');return response({...body,revision:2,validation:report,validation_override:{...body.validation_override,reviewed_by:'jakes',reviewed_at:new Date().toISOString()},effective_validation_status:'pass',updated_by:'jakes'});};
  await $('strokeSave').onclick();
  assert.equal($('strokeValidation').dataset.status,'pass');
  assert.match($('strokeValidation').children[0].textContent,/Passed by human override/);
  assert.match($('strokeValidation').children[1].textContent,/Automatic checks: Needs fixes/);
  assert.equal($('strokeSave').disabled,true);
  $('strokeCanvas').onkeydown({key:'ArrowRight',preventDefault(){}});
  assert.equal($('strokeForcePass').checked,false);
  assert.equal($('strokeValidation').dataset.status,'not-run');
  context.fetch=()=>new Promise(r=>resolve=r);
  const checking=$('strokeValidate').onclick();editor.open({...resizeIcon,key:'sub/another'});
  resolve(response(report));await checking;
  assert.equal($('strokeValidation').dataset.status,'not-run');
  // Auto resize measures all strokes, independently fits both axes, centers, and validates.
  context.window.IconGuides={resolve:item=>({bounds:item.keyshape==='VRECT_M'?[6,0,26,32]:[4,0,28,32]}),envelope:()=>null,label:item=>item.keyshape,choices:()=>[{name:'VRECT_L',label:'L'},{name:'VRECT_M',label:'M'}]};
  context.fetch=async()=>response({svg_sha256:'sha',edit:null,previous_versions:[]});
  editor.open({...resizeIcon,key:'sub/auto',keyshape:'VRECT_L'});$('editingTab').onclick();await tick();
  $('strokeKeyshape').value='VRECT_M';$('strokeKeyshape').onchange();
  let fitted;
  context.fetch=async(url,options)=>{assert.equal(url,'../api/stroke-edits/validate');fitted=JSON.parse(options.body);return response({...report,errors:['Needs grid repair']});};
  await $('strokeAutoResize').onclick();
  assert.equal($('strokeScope').value,'icon');assert.equal($('strokeScaleX').value,20);assert.equal($('strokeScaleY').value,32);
  assert.equal(fitted.keyshape,'VRECT_M');assert.deepEqual(fitted.scales['contour:outline'],[1,1.75]);assert.deepEqual(fitted.scales['primitive:extra'],[1,1.75]);
  assert.deepEqual(fitted.offsets['contour:outline'],[6,10.5]);
  assert.equal($('strokeValidation').dataset.status,'fail');
  $('strokeUndo').onclick();assert.equal($('strokeScaleX').value,20);assert.equal($('strokeScaleY').value,20);assert.equal($('strokeKeyshape').value,'VRECT_M');
  $('strokeRedo').onclick();assert.equal($('strokeScaleY').value,32);
  // Existing per-stroke transforms remain part of the whole-icon fit; repeated fits do not drift.
  await $('strokeAutoResize').onclick();assert.equal($('strokeScaleX').value,20);assert.equal($('strokeScaleY').value,32);
  // A flat drawing cannot acquire width by scaling; leave its draft unchanged.
  context.fetch=async()=>response({svg_sha256:'sha',edit:null,previous_versions:[]});
  editor.open({...resizeIcon,key:'sub/flat',keyshape:'VRECT_M',primitives:[{kind:'line',element_id:'flat',start:[16,2],end:[16,30]}],contours:[]});$('editingTab').onclick();await tick();
  await $('strokeAutoResize').onclick();assert.match($('strokeStatus').textContent,/flat dimension/);assert.equal($('strokeUndo').disabled,true);
  console.log('Stroke geometry, even-grid typed and dragged resizing, whole-icon resizing, undo/redo, persistence, and stale-response checks passed.');
})().catch(error=>{console.error(error);process.exitCode=1;});

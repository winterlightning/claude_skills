/* Pending stroke translations and resizing. Authored geometry remains the versioned baseline. */
(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const clone = value => JSON.parse(JSON.stringify(value));
  const fields = ['icon_id','name','family','profile','canvas_size','keyshape','keyshape_bounds','style','primitives','contours','anchors','relationships','human_figures','composition_class','children','semantic_role','semantic_kind','category','free_keyshape'];
  const graph = icon => Object.fromEntries(fields.filter(key => key in icon).map(key => [key, clone(icon[key])]));
  function groups(icon) {
    const byId = new Map((icon.primitives || []).map(p => [p.element_id,p]));
    if (!byId.size || [...byId.values()].some(p => !['line','arc','bezier'].includes(p.kind))) throw Error('This icon has no editable stroke geometry.');
    const used = new Set(), result = [];
    for (const contour of icon.contours || []) {
      if (!contour.members.length || contour.members.some(id => !byId.has(id) || used.has(id))) throw Error('This icon has unsupported overlapping contours.');
      contour.members.forEach(id => used.add(id));
      result.push({id:'contour:'+contour.contour_id, label:contour.contour_id, members:contour.members, closed:contour.closed});
    }
    for (const p of byId.values()) if (!used.has(p.element_id)) result.push({id:'primitive:'+p.element_id,label:p.element_id,members:[p.element_id],closed:false});
    return result;
  }
  function pathData(icon, group) {
    const byId = new Map(icon.primitives.map(p => [p.element_id,p]));
    let result = '', cursor = null;
    for (const id of group.members) {
      const p = byId.get(id);
      if (!cursor || cursor[0] !== p.start[0] || cursor[1] !== p.start[1]) result += 'M'+p.start.join(' ');
      if (p.kind === 'line') result += 'L'+p.end.join(' ');
      if (p.kind === 'arc') result += `A${p.radius_x} ${p.radius_y} 0 ${+p.large_arc} ${+p.sweep} ${p.end.join(' ')}`;
      if (p.kind === 'bezier') result += p.segments.map(segment => 'C'+segment.flat().join(' ')).join('');
      cursor = p.end;
    }
    return result + (group.closed ? 'Z' : '');
  }
  function translatedGraph(icon, strokes, offsets, scales={}) {
    const result = graph(icon), moves = new Map();
    for (const g of strokes) for (const id of g.members) moves.set(id,offsets[g.id] || [0,0]);
    for (const p of result.primitives) {
      const [dx,dy] = moves.get(p.element_id), group=strokes.find(g=>g.members.includes(p.element_id)), [sx,sy]=scales[group.id] || [1,1], center=icon.canvas_size/2, move = point => [round(center+(point[0]-center)*sx+dx),round(center+(point[1]-center)*sy+dy)];
      p.start = move(p.start); p.end = move(p.end);
      if (p.kind === 'bezier') p.segments = p.segments.map(segment => segment.map(move));
      if (p.kind === 'arc') {p.radius_x=round(p.radius_x*sx);p.radius_y=round(p.radius_y*sy);}
    }
    return result;
  }
  function round(n) { return Math.round(n*1e6)/1e6; }
  // SVG getBBox uses float precision; don't display 31.999998 for a snapped 32.
  function measured(n) { return Math.abs(n-Math.round(n))<1e-5 ? Math.round(n) : round(n); }
  // Snap the visible selection size, not its scale percentage. The stroke stays fixed.
  function snappedResize(bounds, rx, ry, strokeWidth) {
    const ratio = (extent, value) => extent > 1e-6
      ? (Math.max(strokeWidth+2, Math.round((extent*value+strokeWidth)/2)*2)-strokeWidth)/extent
      : 1;
    return {rx:ratio(bounds.width,rx),ry:ratio(bounds.height,ry),cx:Math.round(bounds.cx),cy:Math.round(bounds.cy)};
  }
  let icon = null, strokes = [], offsets = {}, scales = {}, savedOffsets = {}, savedScales = {}, saved = null, baseRevision = 0;
  let selected = '', undo = [], redo = [], drag = null, request = 0, ready = false, busy = false, loaded = false;
  let selectionBounds=null, iconBounds=null;
  let keyshape='',savedKeyshape='',validation=null,checking=false,override=null;
  const state=()=>({offsets:clone(offsets),scales:clone(scales),keyshape});
  const experiment=()=>{
    const result={...icon,keyshape};
    const spec=window.IconGuides?.resolve(result);
    if(spec?.bounds)result.keyshape_bounds=[...spec.bounds];
    if(keyshape!=='FREE')delete result.free_keyshape;
    return result;
  };
  const targets=()=> $('strokeScope').value==='icon'?strokes:strokes.filter(g=>g.id===selected);
  const activeId=()=>targets()[0]?.id;
  const geometryDirty = () => JSON.stringify(offsets) !== JSON.stringify(savedOffsets) || JSON.stringify(scales)!==JSON.stringify(savedScales) || keyshape!==savedKeyshape;
  const overrideRequest=()=>override ? {reason:override.reason} : null;
  const overrideDirty=()=>JSON.stringify(overrideRequest())!==JSON.stringify(saved?.validation_override ? {reason:saved.validation_override.reason} : null);
  const dirty=()=>geometryDirty() || overrideDirty();
  const overrideValid=()=>!override || !!override.reason.trim();
  const validationNeedsSave=()=>!!validation && JSON.stringify(validation)!==JSON.stringify(saved?.validation);
  const draftKey = () => 'pictographic-stroke-edit:'+icon.key+':'+icon.svg_sha256;
  function remember() {
    try {
      if (dirty()) localStorage.setItem(draftKey(), JSON.stringify({revision:baseRevision,offsets,scales,keyshape,validation_override:overrideRequest()}));
      else localStorage.removeItem(draftKey());
    } catch { $('strokeStatus').textContent = 'Browser backup is unavailable. Save edits or download JSON before leaving.'; }
  }
  function controls() {
    const blocked = !ready || busy;
    for (const id of ['strokeSelect','strokeX','strokeY','strokeScaleX','strokeScaleY','strokeScope','strokeReset']) $(id).disabled = blocked || !selected;
    $('strokeSave').disabled = blocked || !overrideValid() || (!dirty() && !validationNeedsSave());
    $('strokeDownload').disabled = !ready || busy || !overrideValid();
    $('strokeForcePass').disabled=blocked;
    $('strokeForcePass').checked=!!override;
    $('strokeOverrideReason').disabled=blocked;
    $('strokeOverrideFields').hidden=!override;
    $('strokeOverrideReason').value=override?.reason || '';
    $('strokeUndo').disabled = blocked || !undo.length;
    $('strokeRedo').disabled = blocked || !redo.length;
    $('strokeResetAll').disabled = blocked || !Object.keys(offsets).length && !Object.keys(scales).length && keyshape===(icon?.keyshape || '');
    $('strokeReload').disabled = busy;
    $('strokeKeyshape').disabled=blocked;
    $('strokeKeyshape').value=keyshape;
    $('strokeAutoResize').disabled=blocked || !iconBounds || !window.IconGuides?.resolve(experiment())?.bounds;
    $('strokeValidate').disabled=blocked;
    $('strokeValidate').textContent=checking?'Checking…':'Run validation';
    $('strokeCanvas').setAttribute('aria-disabled',String(blocked));
    const [dx,dy] = offsets[activeId()] || [0,0];
    const width=icon?.style?.stroke_width || 4;
    for(const [id,extent] of [['strokeScaleX','width'],['strokeScaleY','height']]){
      $(id).value=selectionBounds ? measured(selectionBounds[extent]+width) : '';
      $(id).min=width+2;
      $(id).disabled=blocked || !selectionBounds || selectionBounds[extent]<1e-6;
    }
    $('strokeReset').textContent=$('strokeScope').value==='icon'?'Reset icon':'Reset stroke';
    $('strokeX').value = dx; $('strokeY').value = dy;
    $('strokeSelect').value = selected;
    $('strokeSelect').disabled=blocked || !selected || $('strokeScope').value==='icon';
    $('strokeSave').textContent = busy && !checking ? 'Saving…' : 'Save edits';
  }
  function node(tag, attrs) {
    const el = document.createElementNS('http://www.w3.org/2000/svg',tag);
    for (const [key,value] of Object.entries(attrs)) el.setAttribute(key,value);
    return el;
  }
  function unionBounds(bounds) {
    if(!bounds.length)return null;
    const x=measured(Math.min(...bounds.map(b=>b.x))),y=measured(Math.min(...bounds.map(b=>b.y)));
    const right=measured(Math.max(...bounds.map(b=>b.x+b.width))),bottom=measured(Math.max(...bounds.map(b=>b.y+b.height)));
    return {x,y,width:right-x,height:bottom-y,cx:(x+right)/2,cy:(y+bottom)/2};
  }
  function draw() {
    const canvas = $('strokeCanvas'); canvas.replaceChildren();
    if (!icon || !strokes.length) return;
    const size = icon.canvas_size, width = icon.style?.stroke_width || 4;
    canvas.setAttribute('viewBox',`-4 -4 ${size+8} ${size+8}`);
    canvas.append(node('rect',{x:0,y:0,width:size,height:size,fill:'#fff',stroke:'#bdcbbb','stroke-width':.15}));
    const grid = node('g',{'pointer-events':'none',stroke:'#dfe7da','stroke-width':.1});
    for (let i=0;i<=size;i++) grid.append(node('path',{d:`M${i} 0V${size}M0 ${i}H${size}`}));
    canvas.append(grid);
    const guide=window.IconGuides?.envelope(experiment());if(guide)canvas.append(guide);
    $('editingKeyshape').textContent=window.IconGuides?'Keyshape: '+window.IconGuides.label(experiment())+' · dashed orange':'';
    if ($('strokeOriginal').checked) {
      const ghost = node('g',{fill:'none',stroke:'#b5c2ae','stroke-width':width,'stroke-linecap':'round','stroke-linejoin':'round',opacity:.35,'pointer-events':'none'});
      for (const g of strokes) ghost.append(node('path',{d:pathData(icon,g)}));
      canvas.append(ghost);
    }
    const edited=translatedGraph(icon,strokes,offsets,scales), bounds=[], allBounds=[];
    const targetIds=new Set(targets().map(g=>g.id));
    for (const g of strokes) {
      const path = node('path',{d:pathData(edited,g),fill:'none',stroke:targetIds.has(g.id)?'#287650':'#24352c','stroke-width':width,'stroke-linecap':icon.style?.line_cap || 'round','stroke-linejoin':icon.style?.line_join || 'round','data-stroke':g.id,'pointer-events':'stroke'});
      const title = node('title',{}); title.textContent = g.label; path.append(title); canvas.append(path);
      if(path.getBBox){const b=path.getBBox();allBounds.push(b);if(targetIds.has(g.id))bounds.push(b);}
    }
    iconBounds=unionBounds(allBounds);selectionBounds=unionBounds(bounds);
    if(selectionBounds){
      const {x,y,width:w,height:h}=selectionBounds,right=x+w,bottom=y+h;
      const pad=width/2+.6;
      canvas.append(node('rect',{x:x-pad,y:y-pad,width:right-x+2*pad,height:bottom-y+2*pad,class:'stroke-selection'}));
      canvas.append(node('rect',{x:right+pad-.7,y:bottom+pad-.7,width:1.4,height:1.4,class:'resize-handle','data-resize':'true','aria-label':'Drag to resize selection'}));
    }
    controls();
  }
  function change(next, history = true) {
    if (history) { undo.push(state()); if (undo.length > 100) undo.shift(); redo=[]; }
    offsets = next.offsets; scales=next.scales; keyshape=next.keyshape ?? keyshape;override=null;validation=null;renderValidation('Edits changed. Run validation again.');draw(); $('strokeStatus').textContent = dirty() ? 'Unsaved edits · save to keep them on this server.' : 'Matches the saved version.'; remember();
  }
  function apply(next,history=true){if(JSON.stringify(next)!==JSON.stringify(state()))change(next,history);}
  function move(dx,dy,history=true,basis=state()) {
    if (!ready || busy || !selected || ![dx,dy].every(n => Number.isFinite(n) && Math.abs(n)<=1024)) return;
    const next=clone(basis), first=basis.offsets[activeId()] || [0,0], delta=[dx-first[0],dy-first[1]];
    for(const g of targets()){
      const prior=basis.offsets[g.id] || [0,0], value=[round(prior[0]+delta[0]),round(prior[1]+delta[1])];
      if(value.some(n=>Math.abs(n)>1024))return;
      if(value.every(n=>n===0))delete next.offsets[g.id];else next.offsets[g.id]=value;
    }
    apply(next,history);
  }
  async function autoResize() {
    if(!ready || busy || !iconBounds)return;
    const spec=window.IconGuides?.resolve(experiment());if(!spec?.bounds)return;
    const [left,top,right,bottom]=spec.bounds,width=icon.style?.stroke_width || 4;
    const w=right-left,h=bottom-top,b=iconBounds,c=icon.canvas_size/2;
    if(w%2 || h%2){$('strokeStatus').textContent='This custom keyshape has odd dimensions. Choose an even-sized keyshape for grid-snapped resizing.';return;}
    const ratio=(extent,target)=>extent>1e-6?(target-width)/extent:Math.abs(target-width)<1e-6?1:null;
    const rx=ratio(b.width,w),ry=ratio(b.height,h);
    if(rx===null || ry===null || rx<=0 || ry<=0){$('strokeStatus').textContent='This icon has a flat dimension that cannot fill the selected keyshape without adding geometry.';return;}
    const next=state(),cx=(left+right)/2,cy=(top+bottom)/2;
    for(const g of strokes){
      const priorScale=scales[g.id] || [1,1],priorOffset=offsets[g.id] || [0,0];
      const scale=[priorScale[0]*rx,priorScale[1]*ry];
      const offset=[measured(cx+rx*(c+priorOffset[0]-b.cx)-c),measured(cy+ry*(c+priorOffset[1]-b.cy)-c)];
      if(scale.some(n=>!Number.isFinite(n)||n<.05||n>20)||offset.some(n=>!Number.isFinite(n)||Math.abs(n)>1024)){$('strokeStatus').textContent='This keyshape exceeds the supported resize range.';return;}
      if(scale.every(n=>n===1))delete next.scales[g.id];else next.scales[g.id]=scale;
      if(offset.every(n=>n===0))delete next.offsets[g.id];else next.offsets[g.id]=offset;
    }
    $('strokeScope').value='icon';apply(next);draw();
    $('strokeStatus').textContent=`Resized to ${w} × ${h} keyshape bounds. Validation checks whether the geometry fits.`;
    await validate();
  }
  function resize(sx,sy,history=true,basis=state(),pivot=selectionBounds) {
    if(!ready || busy || !selected || !pivot || ![sx,sy].every(n=>Number.isFinite(n)&&n>0))return;
    const next=clone(basis), previous=basis.scales[activeId()] || [1,1], c=icon.canvas_size/2;
    const {rx,ry,cx,cy}=snappedResize(pivot,sx/previous[0],sy/previous[1],icon.style?.stroke_width || 4);
    for(const g of targets()){
      const oldScale=basis.scales[g.id] || [1,1], oldOffset=basis.offsets[g.id] || [0,0];
      const scale=[oldScale[0]*rx,oldScale[1]*ry],offset=[measured(cx+rx*(c+oldOffset[0]-pivot.cx)-c),measured(cy+ry*(c+oldOffset[1]-pivot.cy)-c)];
      if(scale.some(n=>n<.05||n>20)||offset.some(n=>Math.abs(n)>1024)){ $('strokeStatus').textContent='That size exceeds the supported resize range.';controls();return; }
      if(scale.every(n=>n===1))delete next.scales[g.id];else next.scales[g.id]=scale;
      if(offset.every(n=>n===0))delete next.offsets[g.id];else next.offsets[g.id]=offset;
    }
    apply(next,history);
  }
  function tab(name, focus=false) {
    for (const key of ['information','review','editing']) {
      $(key+'Panel').hidden=key!==name; $(key+'Tab').setAttribute('aria-selected',String(key===name)); $(key+'Tab').tabIndex=key===name?0:-1;
    }
    $('inspectorWorkspace').dataset.tab=name;
    if (focus) $(name+'Tab').focus();
    if (name==='editing') {if(!loaded)load();else if(ready)draw();}
  }
  async function load(discard=false) {
    if (!icon) return;
    if (discard && dirty() && !window.confirm('Discard your unsaved stroke movements and load the server copy?')) return;
    const token = ++request;
    loaded=true; ready=false; busy=false; controls();
    $('strokeStatus').textContent='Loading saved edits…';
    try {
      strokes=groups(icon); selected=strokes[0]?.id || '';
      $('strokeSelect').replaceChildren(...strokes.map(g => {const option=document.createElement('option');option.value=g.id;option.textContent=g.label;return option;}));
      const response = await fetch('../api/stroke-edits?icon='+encodeURIComponent(icon.key));
      if (!(response.headers.get('content-type') || '').includes('application/json')) throw Error('Editing needs the updated gallery server. Restart deploy.py, then reload saved edits.');
      const data = await response.json();
      if (!response.ok) throw Error(data.error || 'Could not load saved edits.');
      if (token!==request) return;
      if (data.svg_sha256 !== icon.svg_sha256) throw Error('The icon changed on this server. Refresh the gallery before editing.');
      saved=data.edit; override=clone(saved?.validation_override || null); baseRevision=saved?.revision || 0;
      offsets=clone(saved?.offsets || {}); scales=clone(saved?.scales || {});savedOffsets=clone(offsets);savedScales=clone(scales);keyshape=saved?.keyshape || icon.keyshape || '';savedKeyshape=keyshape; undo=[]; redo=[];
      let draft=null;
      try { if (discard) localStorage.removeItem(draftKey()); else draft=JSON.parse(localStorage.getItem(draftKey()) || 'null'); } catch {}
      if (draft && Number.isInteger(draft.revision) && draft.offsets && Object.entries(draft.offsets).every(([id,offset]) => strokes.some(g=>g.id===id) && Array.isArray(offset) && offset.length===2 && offset.every(n=>typeof n==='number' && Number.isFinite(n) && Math.abs(n)<=1024))) {
        if(validScales(draft.scales || {})){offsets=draft.offsets;scales=draft.scales || {};keyshape=draft.keyshape || keyshape;baseRevision=draft.revision;override=typeof draft.validation_override?.reason==='string'?{reason:draft.validation_override.reason}:null;}
      }
      validation=!geometryDirty() && saved?.validation?.status!=='not-run'?saved?.validation:null;renderValidation();
      ready=true; draw();
      $('strokeStatus').textContent=draft && dirty() ? (baseRevision!==(saved?.revision || 0) ? 'Recovered draft conflicts with newer server edits. Download JSON, then reload saved edits.' : 'Recovered unsaved edits from this browser.') : saved ? `Saved by ${saved.updated_by} · ${new Date(saved.updated_at).toLocaleString()}` : data.previous_versions?.length ? 'Edits exist for an older icon version. This version starts from its current geometry.' : 'Select a stroke to start editing.';
    } catch(error) { if (token===request) { ready=false; $('strokeCanvas').replaceChildren(); $('strokeStatus').textContent=error.message; controls(); } }
  }
  function renderValidation(message='Not checked yet. Run validation on the current edits.') {
    const box=$('strokeValidation');box.replaceChildren();box.dataset.status=override && !dirty()?'pass':validation?.status || 'not-run';
    const title=document.createElement('p');
    const labels={pass:'Passed',fail:'Needs fixes',review:'Needs review',error:'Could not complete validation'};
    title.textContent=validation ? (labels[validation.status] || validation.status)+' · '+validation.keyshape : message;
    if(override){
      const note=document.createElement('p');
      note.textContent=!dirty()?`Passed by human override · ${override.reviewed_by} · ${new Date(override.reviewed_at).toLocaleString()}. ${override.reason}`:'Force pass selected · enter a reason and save edits to apply it.';
      box.append(note);
      title.textContent='Automatic checks: '+title.textContent;
    }
    box.append(title);
    if(!validation)return;
    const checks=document.createElement('p');checks.className='validation-checks';
    checks.textContent='Checked '+(validation.checked_at?new Date(validation.checked_at).toLocaleString():'now')+': '+(validation.checks_run || []).join(', ');
    box.append(checks);
    for(const [name,status] of Object.entries(validation.checks || {})){
      const line=document.createElement('p');line.className='validation-checks';line.textContent=name.replaceAll('_',' ')+': '+status;box.append(line);
    }
    for(const circle of validation.circles || []){
      const line=document.createElement('p');line.className='validation-circle';
      const dimensions=`${circle.element_id}: ${measured(circle.path_diameter)} × ${measured(circle.path_diameter)} circle path (${measured(circle.visible_diameter)} × ${measured(circle.visible_diameter)} including stroke). `;
      const approved=(circle.approved_visible_diameters || []).map(d=>`${d} × ${d}`).join(' or ');
      line.textContent=dimensions+(circle.exception_applied?'Circle hole exception applied. Other checks still apply.':circle.size_eligible?'Circle size qualifies; the hole must also be complete and unobstructed.':`This size does not qualify for the circle exception. Approved circle sizes in the width/height fields: ${approved}.`);
      box.append(line);
    }
    for(const [kind,items] of [['Issue',validation.errors],['Review',validation.warnings]]){
      if(!items?.length)continue;
      const list=document.createElement('ul');
      for(const message of items){const row=document.createElement('li');row.textContent=kind+': '+message;list.append(row);}
      box.append(list);
    }
  }
  async function validate() {
    if(!ready || busy)return;
    const token=request, snapshot=JSON.stringify(state());
    busy=true;checking=true;validation=null;renderValidation('Checking current geometry and keyshape…');controls();
    try{
      const response=await fetch('../api/stroke-edits/validate',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({icon:icon.key,svg_sha256:icon.svg_sha256,offsets:clone(offsets),scales:clone(scales),keyshape})});
      if(!(response.headers.get('content-type') || '').includes('application/json'))throw Error('Validation needs the updated gallery server. Restart it and try again.');
      const result=await response.json();if(!response.ok)throw Error(result.error || 'Validation could not run.');
      if(token!==request || snapshot!==JSON.stringify(state()))return;
      validation=result;renderValidation();
    }catch(error){if(token===request)renderValidation(error.message);}
    finally{if(token===request){busy=false;checking=false;controls();}}
  }
  async function save() {
    if (!ready || busy || !overrideValid() || (!dirty() && !validationNeedsSave())) return;
    const token=request, body={icon:icon.key,svg_sha256:icon.svg_sha256,revision:baseRevision,offsets:clone(offsets),scales:clone(scales),keyshape:keyshape || undefined,validate:!!validation,validation_override:overrideRequest()};
    busy=true;controls();$('strokeStatus').textContent='Saving edits to this server…';
    try {
      const response=await fetch('../api/stroke-edits',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
      const data=await response.json();
      if (!response.ok) throw Error(data.error || 'Could not save edits.');
      if (token!==request) return;
      saved=data; override=clone(data.validation_override || null); baseRevision=data.revision; savedOffsets=clone(data.offsets);offsets=clone(data.offsets);scales=clone(data.scales || {});savedScales=clone(scales);keyshape=data.keyshape || keyshape;savedKeyshape=keyshape;validation=data.validation?.status!=='not-run'?data.validation:null;renderValidation();remember();
      $('strokeStatus').textContent=`Saved on this server by ${data.updated_by}. Ready for Python to read.`;
    } catch(error) { if (token===request) $('strokeStatus').textContent=error.message+' Your draft is still here.'; }
    finally { if (token===request) {busy=false;controls();} }
  }
  function download() {
    if (!ready) return;
    const document = !dirty() && saved ? {...saved,validation:validation || saved.validation} : {schema:'pictographic.stroke-edit.v2',icon:icon.key,source_svg_sha256:icon.svg_sha256,python_source:icon.python_source,revision:baseRevision,status:'draft',updated_at:new Date().toISOString(),updated_by:null,offsets:clone(offsets),scales:clone(scales),keyshape,scale_origin:[icon.canvas_size/2,icon.canvas_size/2],stroke_groups:strokes.map(({id,members})=>({id,members})),original_graph:graph(icon),edited_graph:translatedGraph(experiment(),strokes,offsets,scales),validation:validation || {status:'not-run',note:'Reconcile anchors and relationships and run Python validation before publishing.'}};
    if(dirty()){document.validation_override_request=overrideRequest();document.validation_override=null;document.effective_validation_status='not-run';}
    const url=URL.createObjectURL(new Blob([JSON.stringify(document,null,2)+'\n'],{type:'application/json'}));
    const link=document.createElement('a');link.href=url;link.download=icon.icon_id+'-stroke-edits.json';link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
  }
  function validScales(values){return values && !Array.isArray(values) && typeof values==='object' && Object.entries(values).every(([id,pair])=>strokes.some(g=>g.id===id) && Array.isArray(pair)&&pair.length===2&&pair.every(n=>typeof n==='number'&&Number.isFinite(n)&&n>=.05&&n<=20));}
  function open(next) {
    if (icon && ready) remember();
    request++;icon=next;keyshape=icon.keyshape || '';savedKeyshape=keyshape;override=null;validation=null;checking=false;renderValidation();strokes=[];offsets={};scales={};savedOffsets={};savedScales={};saved=null;selected='';selectionBounds=null;iconBounds=null;ready=false;loaded=false;busy=false;drag=null;undo=[];redo=[];
    $('strokeKeyshape').replaceChildren(...(window.IconGuides?.choices(icon) || [{name:keyshape,label:keyshape}]).map(item=>{const option=document.createElement('option');option.value=item.name;option.textContent=item.label;return option;}));
    $('strokeCanvas').replaceChildren();$('strokeSelect').replaceChildren();$('strokeStatus').textContent='';$('strokeScope').value='stroke';controls();tab('review');
  }
  function point(event) {
    const canvas=$('strokeCanvas'), p=canvas.createSVGPoint();p.x=event.clientX;p.y=event.clientY;return p.matrixTransform(canvas.getScreenCTM().inverse());
  }
  function init() {
    const names=['information','review','editing'];
    for (const name of names) {
      $(name+'Tab').onclick=()=>tab(name);
      $(name+'Tab').onkeydown=event=>{let index=names.indexOf(name);if(event.key==='ArrowRight')index=(index+1)%3;else if(event.key==='ArrowLeft')index=(index+2)%3;else if(event.key==='Home')index=0;else if(event.key==='End')index=2;else return;event.preventDefault();tab(names[index],true);};
    }
    $('strokeSelect').onchange=()=>{selected=$('strokeSelect').value;draw();};
    for (const id of ['strokeX','strokeY']) $(id).onchange=()=>{const x=$('strokeX').valueAsNumber,y=$('strokeY').valueAsNumber;if (![x,y].every(n=>Number.isFinite(n)&&Math.abs(n)<=1024)) { $('strokeStatus').textContent='Enter offsets between -1024 and 1024.';controls();return;}move(x,y);};
    $('strokeOriginal').onchange=draw;
    $('strokeScope').onchange=draw;
    $('strokeKeyshape').onchange=()=>{if(!ready || busy)return;apply({...state(),keyshape:$('strokeKeyshape').value});};
    $('strokeForcePass').onchange=()=>{if(!ready || busy)return;override=$('strokeForcePass').checked?{reason:''}:null;renderValidation();controls();remember();};
    $('strokeOverrideReason').oninput=()=>{if(!ready || busy || !override)return;override={reason:$('strokeOverrideReason').value};renderValidation();controls();remember();};
    $('strokeValidate').onclick=validate;
    $('strokeAutoResize').onclick=autoResize;
    for(const id of ['strokeScaleX','strokeScaleY'])$(id).onchange=()=>{
      if(!selectionBounds)return;
      const width=icon.style?.stroke_width || 4, extent=id==='strokeScaleX'?'width':'height', value=$(id).valueAsNumber;
      if(!Number.isFinite(value)||value<=width){$('strokeStatus').textContent='Enter a size larger than the stroke width ('+width+' units).';controls();return;}
      const ratio=(value-width)/selectionBounds[extent], previous=scales[activeId()] || [1,1];
      const rx=id==='strokeScaleX'?ratio:1, ry=id==='strokeScaleY'?ratio:1;
      resize(previous[0]*rx,previous[1]*ry);
    };
    $('strokeReset').onclick=()=>{const next=state();for(const g of targets()){delete next.offsets[g.id];delete next.scales[g.id];}apply(next);};
    $('strokeResetAll').onclick=()=>apply({offsets:{},scales:{},keyshape:icon.keyshape || ''});
    $('strokeUndo').onclick=()=>{if(!undo.length)return;redo.push(state());change(undo.pop(),false);};
    $('strokeRedo').onclick=()=>{if(!redo.length)return;undo.push(state());change(redo.pop(),false);};
    $('strokeSave').onclick=save;$('strokeDownload').onclick=download;$('strokeReload').onclick=()=>load(true);
    const canvas=$('strokeCanvas');
    canvas.onpointerdown=event=>{
      const id=event.target.getAttribute('data-stroke'), sizing=event.target.getAttribute('data-resize');
      if((!id && !sizing) || !ready || busy || event.button!==0)return;
      event.preventDefault();if(id && $('strokeScope').value!=='icon')selected=id;draw();
      drag={pointer:event.pointerId,start:point(event),offset:clone(offsets[activeId()] || [0,0]),scale:clone(scales[activeId()] || [1,1]),before:state(),mode:sizing?'resize':'move',bounds:selectionBounds};
      canvas.setPointerCapture(event.pointerId);canvas.focus();
    };
    canvas.onpointermove=event=>{
      if(!drag){const id=event.target.getAttribute('data-stroke'),g=strokes.find(g=>g.id===id);$('strokeHover').textContent=g?'Hover: '+g.label+(g.id===selected?' · selected':' · click to select'):'Hover over a stroke to identify it.';return;}
      if(event.pointerId!==drag.pointer)return;
      const p=point(event), step=$('strokeSnap').checked?1:.1;
      if(drag.mode==='resize'){
        const b=drag.bounds;if(!b)return;
        let rx=(p.x-b.cx)/(drag.start.x-b.cx),ry=(p.y-b.cy)/(drag.start.y-b.cy);
        resize(drag.scale[0]*rx,drag.scale[1]*ry,false,drag.before,b);
      }else move(Math.round((drag.offset[0]+p.x-drag.start.x)/step)*step,Math.round((drag.offset[1]+p.y-drag.start.y)/step)*step,false,drag.before);
    };
    canvas.onpointerleave=()=>{if(!drag)$('strokeHover').textContent='Hover over a stroke to identify it.';};
    const finish=event=>{if(!drag || event.pointerId!==drag.pointer)return;const before=drag.before;drag=null;if(JSON.stringify(before)!==JSON.stringify(state())){undo.push(before);redo=[];}controls();};
    canvas.onpointerup=finish;canvas.onlostpointercapture=finish;
    canvas.onpointercancel=event=>{if(!drag || event.pointerId!==drag.pointer)return;const before=drag.before;drag=null;change(before,false);};
    canvas.onkeydown=event=>{
      if(!ready || busy || !selected)return;
      const moves={ArrowLeft:[-1,0],ArrowRight:[1,0],ArrowUp:[0,-1],ArrowDown:[0,1]}, delta=moves[event.key];
      if(!delta)return;event.preventDefault();const offset=offsets[activeId()] || [0,0],step=event.shiftKey?.1:1;move(offset[0]+delta[0]*step,offset[1]+delta[1]*step);
    };
    window.addEventListener('beforeunload',event=>{if(ready && dirty()){remember();event.preventDefault();event.returnValue='';}});
  }
  window.StrokeEditor={open,groups,pathData,translatedGraph,snappedResize};
  document.addEventListener('DOMContentLoaded',init);
})();

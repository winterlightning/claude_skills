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
  function withoutStrokes(drawing, allGroups, deleted) {
    const result=clone(drawing),removed=new Set(allGroups.filter(g=>deleted.includes(g.id)).flatMap(g=>g.members));
    for(const c of result.contours || [])if(c.members.some(id=>removed.has(id)))removed.add(c.contour_id);
    result.primitives=result.primitives.filter(p=>!removed.has(p.element_id));
    if(result.contours)result.contours=result.contours.filter(c=>!removed.has(c.contour_id));
    if(result.relationships)result.relationships=result.relationships.filter(r=>!r.members.some(id=>removed.has(id)));
    if(result.human_figures)result.human_figures=result.human_figures.filter(f=>!removed.has(f.head)&&!removed.has(f.torso));
    return result;
  }
  function snapGeometry(primitives, center) {
    // Use symmetric tie-breaking around the canvas center, including half units.
    const snap=value=>center+Math.sign(value-center)*Math.floor(Math.abs(value-center)+.5);
    const point=p=>p.map(snap), shift=(p,from,to)=>p.map((n,i)=>round(n+to[i]-from[i]));
    return primitives.map(source=>{
      const p=clone(source);p.start=point(source.start);p.end=point(source.end);
      if(p.kind==='bezier'){
        let from=source.start,to=p.start;
        p.segments=source.segments.map(([c1,c2,end])=>{
          const knot=point(end),segment=[shift(c1,from,to),shift(c2,end,knot),knot];
          from=end;to=knot;return segment;
        });
      }else if(p.kind==='arc'){
        p.radius_x=Math.max(1,Math.round(p.radius_x));p.radius_y=Math.max(1,Math.round(p.radius_y));
      }
      return p;
    });
  }
  function round(n) { return Math.round(n*1e6)/1e6; }
  function pathPoints(drawing, group) {
    const points=[];
    for(const p of drawing.primitives.filter(p=>group.members.includes(p.element_id))){
      const knots=[['start',p.start],['end',p.end],...(p.segments || []).map((s,i)=>['segment:'+i,s[2]])];
      for(const [address,position] of knots){
        const ref=p.element_id+':'+address;
        let knot=points.find(n=>n.position.every((v,i)=>v===position[i]));
        if(!knot){knot={id:ref,position:[...position],refs:[]};points.push(knot);}
        knot.refs.push(ref);
      }
    }
    return points;
  }
  function movePathPoint(drawing, group, pointId, destination) {
    const knot=pathPoints(drawing,group).find(n=>n.refs.includes(pointId));
    if(!knot)return null;
    const result=clone(drawing.primitives),same=p=>p.every((v,i)=>v===knot.position[i]);
    const shift=p=>p.map((v,i)=>round(v+destination[i]-knot.position[i]));
    for(const p of result.filter(p=>group.members.includes(p.element_id))){
      // Move both sides of a shared junction, carrying adjacent curve handles with it.
      if(p.kind==='bezier'){
        let start=p.start;
        for(const segment of p.segments){
          const end=segment[2];
          if(same(start))segment[0]=shift(segment[0]);
          if(same(end)){segment[1]=shift(segment[1]);segment[2]=[...destination];}
          start=end;
        }
      }
      if(same(p.start))p.start=[...destination];
      if(same(p.end))p.end=[...destination];
    }
    return result;
  }
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
  let selectedPoint=null,deletedStrokes=[],savedDeletedStrokes=[];
  let keyshape='',savedKeyshape='',validation=null,checking=false,override=null,geometry=null,savedGeometry=null;
  let viewport=null,panMode=false,spacePan=false;
  const viewZoom=()=>viewport && icon ? (icon.canvas_size+8)/viewport.size : 1;
  function updateView() {
    if(!icon)return;
    viewport ||= {x:-4,y:-4,size:icon.canvas_size+8};
    const canvas=$('strokeCanvas'),zoom=viewZoom();
    canvas.setAttribute('viewBox',`${viewport.x} ${viewport.y} ${viewport.size} ${viewport.size}`);
    canvas.dataset.panMode=String(panMode || spacePan);
    canvas.dataset.panning=String(drag?.mode==='pan');
    $('strokeZoomLevel').textContent=Math.round(zoom*100)+'%';
    $('strokePan').setAttribute('aria-pressed',String(panMode));
    const blocked=!ready || busy || !!drag;
    $('strokePan').disabled=blocked;
    $('strokeZoomFit').disabled=blocked;
    $('strokeZoomIn').disabled=blocked || zoom>=16;
    $('strokeZoomOut').disabled=blocked || zoom<=.25;
  }
  function zoomView(factor,anchor) {
    if(!ready || busy || drag)return;
    updateView();
    anchor ||= {x:viewport.x+viewport.size/2,y:viewport.y+viewport.size/2};
    const size=(icon.canvas_size+8)/Math.max(.25,Math.min(16,viewZoom()*factor)),ratio=size/viewport.size;
    viewport={x:anchor.x+(viewport.x-anchor.x)*ratio,y:anchor.y+(viewport.y-anchor.y)*ratio,size};
    updateView();
  }
  const state=()=>({offsets:clone(offsets),scales:clone(scales),keyshape,geometry:clone(geometry),deleted_strokes:clone(deletedStrokes)});
  const workingIcon=()=>({...icon,primitives:geometry || icon.primitives});
  const experiment=()=>{
    const result={...workingIcon(),keyshape};
    const spec=window.IconGuides?.resolve(result);
    if(spec?.bounds)result.keyshape_bounds=[...spec.bounds];
    if(keyshape!=='FREE')delete result.free_keyshape;
    return result;
  };
  const visibleStrokes=()=>strokes.filter(g=>!deletedStrokes.includes(g.id));
  const targets=()=> $('strokeScope').value==='icon'?visibleStrokes():visibleStrokes().filter(g=>g.id===selected);
  const displayGraph=()=>withoutStrokes(translatedGraph(experiment(),strokes,offsets,scales),strokes,deletedStrokes);
  const activeId=()=>targets()[0]?.id;
  const geometryDirty = () => JSON.stringify(offsets) !== JSON.stringify(savedOffsets) || JSON.stringify(scales)!==JSON.stringify(savedScales) || keyshape!==savedKeyshape || JSON.stringify(geometry)!==JSON.stringify(savedGeometry) || JSON.stringify(deletedStrokes)!==JSON.stringify(savedDeletedStrokes);
  const overrideRequest=()=>override ? {reason:override.reason} : null;
  const overrideDirty=()=>JSON.stringify(overrideRequest())!==JSON.stringify(saved?.validation_override ? {reason:saved.validation_override.reason} : null);
  const dirty=()=>geometryDirty() || overrideDirty();
  const validationBlocksSave=()=>validation?.status==='fail' && !override;
  const validationNeedsSave=()=>!!validation && JSON.stringify(validation)!==JSON.stringify(saved?.validation);
  const draftKey = () => 'pictographic-stroke-edit:'+icon.key+':'+icon.svg_sha256;
  function remember() {
    try {
      if (dirty()) localStorage.setItem(draftKey(), JSON.stringify({revision:baseRevision,offsets,scales,keyshape,geometry,deleted_strokes:deletedStrokes,validation_override:overrideRequest()}));
      else localStorage.removeItem(draftKey());
    } catch { $('strokeStatus').textContent = 'Browser backup is unavailable. Save edits or download JSON before leaving.'; }
  }
  function controls() {
    const blocked = !ready || busy;
    updateView();
    for (const id of ['strokeSelect','strokeX','strokeY','strokeScaleX','strokeScaleY','strokeScope','strokeReset']) $(id).disabled = blocked || !selected;
    $('strokeSave').disabled = blocked || validationBlocksSave() || (!dirty() && !validationNeedsSave());
    $('strokeDownloadSVG').disabled=!ready || busy;
    $('strokeDownload').disabled = !ready || busy;
    $('strokeForcePass').disabled=blocked;
    $('strokeForcePass').checked=!!override;
    $('strokeOverrideReason').disabled=blocked;
    $('strokeOverrideFields').hidden=!override;
    $('strokeOverrideReason').value=override?.reason || '';
    $('strokeUndo').disabled = blocked || !undo.length;
    $('strokeRedo').disabled = blocked || !redo.length;
    $('strokeResetAll').disabled = blocked || !Object.keys(offsets).length && !Object.keys(scales).length && keyshape===(icon?.keyshape || '') && !geometry && !deletedStrokes.length;
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
    $('strokeDelete').disabled=blocked || !selected || $('strokeScope').value==='icon' || visibleStrokes().length<=1;
    $('strokeDelete').title=visibleStrokes().length<=1?'Keep at least one stroke in the icon.':$('strokeScope').value==='icon'?'Choose Selected stroke to delete a stroke.':'Delete the selected stroke. Undo restores it.';
    $('strokeSelect').value = selected;
    $('strokeSelect').disabled=blocked || !selected || $('strokeScope').value==='icon';
    const currentPoint=selectedPoint && pathPoints(translatedGraph(workingIcon(),strokes,offsets,scales),strokes.find(g=>g.id===selectedPoint.group)).find(n=>n.refs.includes(selectedPoint.id));
    $('strokePointFields').hidden=!currentPoint;
    for(const [i,id] of ['strokePointX','strokePointY'].entries()){$(id).disabled=blocked || !currentPoint;$(id).value=currentPoint?.position[i] ?? '';}
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
    const visible=visibleStrokes();
    if(!visible.some(g=>g.id===selected))selected=visible[0]?.id || '';
    if(selectedPoint && deletedStrokes.includes(selectedPoint.group))selectedPoint=null;
    $('strokeSelect').replaceChildren(...visible.map(g=>{const option=document.createElement('option');option.value=g.id;option.textContent=g.label;return option;}));
    const size = icon.canvas_size, width = icon.style?.stroke_width || 4;
    updateView();
    canvas.append(node('rect',{x:0,y:0,width:size,height:size,fill:'#fff',stroke:'#bdcbbb','stroke-width':.15}));
    const grid = node('g',{'pointer-events':'none',stroke:'#dfe7da','stroke-width':.1});
    for (let i=0;i<=size;i++) grid.append(node('path',{d:`M${i} 0V${size}M0 ${i}H${size}`}));
    canvas.append(grid);
    if($('strokePoints').checked)canvas.append(node('path',{d:`M${size/2} 0V${size}M0 ${size/2}H${size}`,class:'editor-center-axes'}));
    const guide=window.IconGuides?.envelope(experiment());if(guide)canvas.append(guide);
    $('editingKeyshape').textContent=window.IconGuides?'Keyshape: '+window.IconGuides.label(experiment())+' · dashed orange':'';
    if ($('strokeOriginal').checked) {
      const ghost = node('g',{fill:'none',stroke:'#b5c2ae','stroke-width':width,'stroke-linecap':'round','stroke-linejoin':'round',opacity:.35,'pointer-events':'none'});
      for (const g of visible) ghost.append(node('path',{d:pathData(icon,g)}));
      canvas.append(ghost);
    }
    const edited=translatedGraph(workingIcon(),strokes,offsets,scales), bounds=[], allBounds=[];
    const targetIds=new Set(targets().map(g=>g.id));
    for (const g of visible) {
      const path = node('path',{d:pathData(edited,g),fill:'none',stroke:targetIds.has(g.id)?'#287650':'#24352c','stroke-width':width,'stroke-linecap':icon.style?.line_cap || 'round','stroke-linejoin':icon.style?.line_join || 'round','data-stroke':g.id,'pointer-events':'stroke'});
      const title = node('title',{}); title.textContent = g.label; path.append(title); canvas.append(path);
      let b;try{b=window.StrokeFit.bounds(edited.primitives.filter(p=>g.members.includes(p.element_id)));}catch{b=path.getBBox();}allBounds.push(b);if(targetIds.has(g.id))bounds.push(b);
    }
    iconBounds=unionBounds(allBounds);selectionBounds=unionBounds(bounds);
    if(selectionBounds){
      const {x,y,width:w,height:h}=selectionBounds,right=x+w,bottom=y+h;
      const pad=width/2+.6;
      canvas.append(node('rect',{x:x-pad,y:y-pad,width:right-x+2*pad,height:bottom-y+2*pad,class:'stroke-selection'}));
      canvas.append(node('rect',{x:right+pad-.7,y:bottom+pad-.7,width:1.4,height:1.4,class:'resize-handle','data-resize':'true','aria-label':'Drag to resize selection'}));
    }
    if($('strokePoints').checked){
      for(const g of visible){
        canvas.append(node('path',{d:pathData(edited,g),class:'editor-centerline','data-stroke':g.id}));
        if(!targetIds.has(g.id))continue;
        for(const knot of pathPoints(edited,g)){
          const active=selectedPoint?.group===g.id && knot.refs.includes(selectedPoint.id);
          const dot=node('circle',{cx:knot.position[0],cy:knot.position[1],r:.55,class:'editor-path-point'+(active?' is-selected':''),'data-point':knot.id,'data-stroke':g.id});
          const title=node('title',{});title.textContent=`Path point (${knot.position.join(', ')}) · drag to reshape`;dot.append(title);canvas.append(dot);
        }
      }
      if(selectionBounds){
        const {cx,cy}=selectionBounds;
        const center=node('path',{d:`M${cx} ${cy-.8}L${cx+.8} ${cy}L${cx} ${cy+.8}L${cx-.8} ${cy}Z`,class:'editor-center-point','data-center':'true'});
        const title=node('title',{});title.textContent='Selection center · drag to move selection';center.append(title);canvas.append(center);
      }
    }
    controls();
  }
  function movePoint(destination,history=true,basis=state()) {
    if(!ready || busy || !selectedPoint || !destination.every(n=>Number.isFinite(n)&&Math.abs(n)<=4096))return;
    const drawing=translatedGraph({...icon,primitives:basis.geometry || icon.primitives},strokes,basis.offsets,basis.scales);
    const primitives=movePathPoint(drawing,strokes.find(g=>g.id===selectedPoint.group),selectedPoint.id,destination);
    if(primitives)apply(JSON.stringify(primitives)===JSON.stringify(drawing.primitives)?clone(basis):{...clone(basis),geometry:primitives,offsets:{},scales:{}},history);
  }
  function change(next, history = true) {
    if (history) { undo.push(state()); if (undo.length > 100) undo.shift(); redo=[]; }
    deletedStrokes=clone(next.deleted_strokes || []);offsets = next.offsets; scales=next.scales;geometry=clone(next.geometry ?? null); keyshape=next.keyshape ?? keyshape;override=null;validation=null;renderValidation('Edits changed. Run validation again.');draw(); $('strokeStatus').textContent = dirty() ? 'Unsaved edits · save to keep them on this server.' : 'Matches the saved version.'; remember();
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
    const w=right-left,h=bottom-top;
    if(w%2 || h%2){$('strokeStatus').textContent='This custom keyshape has odd dimensions. Choose an even-sized keyshape for grid-snapped resizing.';return;}
    try {
      const drawing=translatedGraph(workingIcon(),strokes,offsets,scales),ids=new Set(visibleStrokes().flatMap(g=>g.members));
      const fitted=window.StrokeFit.fit(drawing.primitives.filter(p=>ids.has(p.element_id)),spec.bounds,width,icon.primitives);
      const byId=new Map(fitted.map(p=>[p.element_id,p])),next=state();
      next.geometry=drawing.primitives.map(p=>byId.get(p.element_id) || p);
      next.offsets={};next.scales={};selectedPoint=null;
      $('strokeScope').value='icon';apply(next);draw();
      $('strokeStatus').textContent=`Fitted to ${w} × ${h}. Curve extrema and grid-snapped points were measured before validation.`;
    } catch(error) {$('strokeStatus').textContent=error.message;return;}
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
      selectedPoint=null;strokes=groups(icon); selected=strokes[0]?.id || '';
      $('strokeSelect').replaceChildren(...strokes.map(g => {const option=document.createElement('option');option.value=g.id;option.textContent=g.label;return option;}));
      const response = await fetch('../api/stroke-edits?icon='+encodeURIComponent(icon.key));
      if (!(response.headers.get('content-type') || '').includes('application/json')) throw Error('Editing needs the updated gallery server. Restart deploy.py, then reload saved edits.');
      const data = await response.json();
      if (!response.ok) throw Error(data.error || 'Could not load saved edits.');
      if (token!==request) return;
      if (data.svg_sha256 !== icon.svg_sha256) throw Error('The icon changed on this server. Refresh the gallery before editing.');
      saved=data.edit;deletedStrokes=clone(saved?.deleted_strokes || []);savedDeletedStrokes=clone(deletedStrokes);geometry=clone(saved?.geometry || null);savedGeometry=clone(geometry); override=clone(saved?.validation_override || null); baseRevision=saved?.revision || 0;
      offsets=clone(saved?.offsets || {}); scales=clone(saved?.scales || {});savedOffsets=clone(offsets);savedScales=clone(scales);keyshape=saved?.keyshape || icon.keyshape || '';savedKeyshape=keyshape; undo=[]; redo=[];
      let draft=null;
      try { if (discard) localStorage.removeItem(draftKey()); else draft=JSON.parse(localStorage.getItem(draftKey()) || 'null'); } catch {}
      if (draft && Number.isInteger(draft.revision) && draft.offsets && Object.entries(draft.offsets).every(([id,offset]) => strokes.some(g=>g.id===id) && Array.isArray(offset) && offset.length===2 && offset.every(n=>typeof n==='number' && Number.isFinite(n) && Math.abs(n)<=1024))) {
        if(validScales(draft.scales || {}) && validGeometry(draft.geometry ?? null) && validDeleted(draft.deleted_strokes || [])){deletedStrokes=clone(draft.deleted_strokes || []);geometry=clone(draft.geometry ?? null);offsets=draft.offsets;scales=draft.scales || {};keyshape=draft.keyshape || keyshape;baseRevision=draft.revision;override=typeof draft.validation_override?.reason==='string'?{reason:draft.validation_override.reason}:null;}
      }
      validation=!geometryDirty() && saved?.validation?.status!=='not-run'?saved?.validation:null;renderValidation();
      ready=true; draw();
      $('strokeStatus').textContent=draft && dirty() ? (baseRevision!==(saved?.revision || 0) ? 'Recovered draft conflicts with newer server edits. Download JSON, then reload saved edits.' : 'Recovered unsaved edits from this browser.') : saved ? `Saved by ${saved.updated_by} · ${new Date(saved.updated_at).toLocaleString()}` : data.previous_versions?.length ? 'Edits exist for an older icon version. This version starts from its current geometry.' : 'Select a stroke to start editing.';
    } catch(error) { if (token===request) { ready=false; $('strokeCanvas').replaceChildren(); $('strokeStatus').textContent=error.message; controls(); } }
  }
  function renderValidation(message='Not checked yet. Run validation on the current edits.') {
    const applied=override && !dirty()?saved?.validation_override:null;
    const box=$('strokeValidation');box.replaceChildren();box.dataset.status=applied?'pass':validation?.status || 'not-run';
    const title=document.createElement('p');
    const labels={pass:'Passed',fail:'Needs fixes',review:'Needs review',error:'Could not complete validation'};
    title.textContent=validation ? (labels[validation.status] || validation.status)+' · '+validation.keyshape : message;
    if(override){
      const note=document.createElement('p');
      note.textContent=applied?`Passed by human override · ${applied.reviewed_by} · ${new Date(applied.reviewed_at).toLocaleString()}${applied.reason ? '. '+applied.reason : ''}`:'Force pass selected · save edits to apply it. A note is optional.';
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
      const response=await fetch('../api/stroke-edits/validate',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({icon:icon.key,svg_sha256:icon.svg_sha256,offsets:clone(offsets),scales:clone(scales),keyshape,geometry:clone(geometry),deleted_strokes:clone(deletedStrokes)})});
      if(!(response.headers.get('content-type') || '').includes('application/json'))throw Error('Validation needs the updated gallery server. Restart it and try again.');
      const result=await response.json();if(!response.ok)throw Error(result.error || 'Validation could not run.');
      if(token!==request || snapshot!==JSON.stringify(state()))return;
      validation=result;renderValidation();
    }catch(error){if(token===request)renderValidation(error.message);}
    finally{if(token===request){busy=false;checking=false;controls();}}
  }
  async function save() {
    if (!ready || busy || validationBlocksSave() || (!dirty() && !validationNeedsSave())) return;
    const token=request, body={icon:icon.key,svg_sha256:icon.svg_sha256,revision:baseRevision,offsets:clone(offsets),scales:clone(scales),keyshape:keyshape || undefined,geometry:clone(geometry),deleted_strokes:clone(deletedStrokes),validate:!!validation,validation_override:overrideRequest()};
    busy=true;controls();$('strokeStatus').textContent='Saving edits to this server…';
    try {
      const response=await fetch('../api/stroke-edits',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
      const data=await response.json();
      if (!response.ok) throw Error(data.error || 'Could not save edits.');
      if (token!==request) return;
      saved=data;deletedStrokes=clone(data.deleted_strokes || []);savedDeletedStrokes=clone(deletedStrokes);geometry=clone(data.geometry || null);savedGeometry=clone(geometry); override=clone(data.validation_override || null); baseRevision=data.revision; savedOffsets=clone(data.offsets);offsets=clone(data.offsets);scales=clone(data.scales || {});savedScales=clone(scales);keyshape=data.keyshape || keyshape;savedKeyshape=keyshape;validation=data.validation?.status!=='not-run'?data.validation:null;renderValidation();remember();
      window.IconArtwork?.editSaved(icon.key,data.revision);
      $('strokeStatus').textContent=`Saved on this server by ${data.updated_by}. Ready for Python to read.`;
    } catch(error) { if (token===request) $('strokeStatus').textContent=error.message+' Your draft is still here.'; }
    finally { if (token===request) {busy=false;controls();} }
  }
  function download() {
    if (!ready) return;
    const handoff = !dirty() && saved ? {...saved,validation:validation || saved.validation} : {schema:'pictographic.stroke-edit.v2',icon:icon.key,source_svg_sha256:icon.svg_sha256,python_source:icon.python_source,revision:baseRevision,status:'draft',updated_at:new Date().toISOString(),updated_by:null,offsets:clone(offsets),scales:clone(scales),keyshape,geometry:clone(geometry),deleted_strokes:clone(deletedStrokes),scale_origin:[icon.canvas_size/2,icon.canvas_size/2],stroke_groups:strokes.map(({id,members})=>({id,members})),original_graph:graph(icon),edited_graph:displayGraph(),validation:validation || {status:'not-run',note:'Reconcile anchors and relationships and run Python validation before publishing.'}};
    if(dirty()){handoff.validation_override_request=overrideRequest();handoff.validation_override=null;handoff.effective_validation_status='not-run';}
    const url=URL.createObjectURL(new Blob([JSON.stringify(handoff,null,2)+'\n'],{type:'application/json'}));
    const link=document.createElement('a');link.href=url;link.download=icon.icon_id+'-stroke-edits.json';link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
  }
  function downloadSVG(){
    if(!ready || busy)return;
    const edited=displayGraph(),size=icon.canvas_size;
    const escape=value=>String(value).replaceAll('&','&amp;').replaceAll('"','&quot;').replaceAll('<','&lt;');
    const paths=visibleStrokes().map(g=>`  <path id="${escape(g.label)}" d="${escape(pathData(edited,g))}"/>`).join('\n');
    const svg=`<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 ${size} ${size}" fill="none" stroke="currentColor" stroke-width="${icon.style?.stroke_width || 4}" stroke-linecap="round" stroke-linejoin="round">\n${paths}\n</svg>\n`;
    const url=URL.createObjectURL(new Blob([svg],{type:'image/svg+xml'}));
    const link=document.createElement('a');link.href=url;link.download=icon.icon_id+'-edited.svg';link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
  }
  function validGeometry(value){return value===null || Array.isArray(value) && value.length===icon.primitives.length && value.every((p,i)=>p && p.element_id===icon.primitives[i].element_id && p.kind===icon.primitives[i].kind && [p.start,p.end,...(p.segments || []).flat()].every(point=>Array.isArray(point) && point.length===2 && point.every(n=>typeof n==='number' && Number.isFinite(n) && Math.abs(n)<=4096)));}
  function validDeleted(value){return Array.isArray(value) && value.length<strokes.length && new Set(value).size===value.length && value.every(id=>strokes.some(g=>g.id===id));}
  function deleteStroke(){
    if(!ready || busy || !selected || $('strokeScope').value==='icon' || visibleStrokes().length<=1)return;
    const next=state(),name=strokes.find(g=>g.id===selected).label;
    next.deleted_strokes=strokes.filter(g=>g.id===selected || deletedStrokes.includes(g.id)).map(g=>g.id);
    selectedPoint=null;apply(next);$('strokeStatus').textContent=`Deleted ${name}. Undo restores it; save edits to keep this change.`;
  }
  function validScales(values){return values && !Array.isArray(values) && typeof values==='object' && Object.entries(values).every(([id,pair])=>strokes.some(g=>g.id===id) && Array.isArray(pair)&&pair.length===2&&pair.every(n=>typeof n==='number'&&Number.isFinite(n)&&n>=.05&&n<=20));}
  function open(next) {
    selectedPoint=null;
    viewport=null;panMode=false;spacePan=false;
    next={...next,...(next.generated_graph || {}),svg_sha256:next.generated_svg_sha256 || next.svg_sha256};
    if (icon && ready) remember();
    request++;icon=next;deletedStrokes=[];savedDeletedStrokes=[];geometry=null;savedGeometry=null;keyshape=icon.keyshape || '';savedKeyshape=keyshape;override=null;validation=null;checking=false;renderValidation();strokes=[];offsets={};scales={};savedOffsets={};savedScales={};saved=null;selected='';selectionBounds=null;iconBounds=null;ready=false;loaded=false;busy=false;drag=null;undo=[];redo=[];
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
    $('strokeSelect').onchange=()=>{selectedPoint=null;selected=$('strokeSelect').value;draw();};
    $('strokePoints').onchange=()=>{selectedPoint=null;draw();};
    for(const id of ['strokePointX','strokePointY'])$(id).onchange=()=>{
      const step=$('strokeSnap').checked?1:.1;
      movePoint(['strokePointX','strokePointY'].map(key=>round(Math.round($(key).valueAsNumber/step)*step)));controls();
    };
    for (const id of ['strokeX','strokeY']) $(id).onchange=()=>{const x=$('strokeX').valueAsNumber,y=$('strokeY').valueAsNumber;if (![x,y].every(n=>Number.isFinite(n)&&Math.abs(n)<=1024)) { $('strokeStatus').textContent='Enter offsets between -1024 and 1024.';controls();return;}move(x,y);};
    $('strokeOriginal').onchange=draw;
    $('strokeScope').onchange=()=>{selectedPoint=null;draw();};
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
    $('strokeReset').onclick=()=>{const next=state();for(const g of targets()){delete next.offsets[g.id];delete next.scales[g.id];if(next.geometry)for(const id of g.members){const i=icon.primitives.findIndex(p=>p.element_id===id);next.geometry[i]=clone(icon.primitives[i]);}}if(JSON.stringify(next.geometry)===JSON.stringify(icon.primitives))next.geometry=null;apply(next);};
    $('strokeDelete').onclick=deleteStroke;
    $('strokeResetAll').onclick=()=>apply({offsets:{},scales:{},geometry:null,deleted_strokes:[],keyshape:icon.keyshape || ''});
    $('strokeUndo').onclick=()=>{if(!undo.length)return;redo.push(state());change(undo.pop(),false);};
    $('strokeRedo').onclick=()=>{if(!redo.length)return;undo.push(state());change(redo.pop(),false);};
    $('strokeDownloadSVG').onclick=downloadSVG;$('strokeSave').onclick=save;$('strokeDownload').onclick=download;$('strokeReload').onclick=()=>load(true);
    const canvas=$('strokeCanvas');
    $('strokePan').onclick=()=>{if(!ready || busy || drag)return;panMode=!panMode;updateView();canvas.focus({preventScroll:true});};
    $('strokeZoomIn').onclick=()=>zoomView(1.25);
    $('strokeZoomOut').onclick=()=>zoomView(1/1.25);
    $('strokeZoomFit').onclick=()=>{if(!ready || busy || drag)return;viewport=null;updateView();};
    canvas.addEventListener('wheel',event=>{
      if(!ready)return;
      event.preventDefault();
      const delta=event.deltaY*(event.deltaMode===1?16:event.deltaMode===2?canvas.clientHeight:1);
      zoomView(Math.exp(-Math.max(-200,Math.min(200,delta))*.002),point(event));
    },{passive:false});
    canvas.onpointerdown=event=>{
      const id=event.target.getAttribute('data-stroke'), sizing=event.target.getAttribute('data-resize'),pointId=event.target.getAttribute('data-point'),center=event.target.getAttribute('data-center');
      if(!ready || busy || drag || ![0,1].includes(event.button))return;
      if(panMode || spacePan || event.button===1 || (!id && !sizing && !center)){
        event.preventDefault();
        drag={pointer:event.pointerId,mode:'pan',start:point(event),view:{...viewport},matrix:canvas.getScreenCTM().inverse()};
        canvas.setPointerCapture(event.pointerId);canvas.focus({preventScroll:true});updateView();return;
      }
      event.preventDefault();selectedPoint=pointId?{group:id,id:pointId}:null;if(id && $('strokeScope').value!=='icon')selected=id;draw();
      const knot=selectedPoint && pathPoints(translatedGraph(workingIcon(),strokes,offsets,scales),strokes.find(g=>g.id===id)).find(n=>n.refs.includes(pointId));
      drag={pointer:event.pointerId,start:point(event),position:knot?.position,offset:clone(offsets[activeId()] || [0,0]),scale:clone(scales[activeId()] || [1,1]),before:state(),mode:pointId?'point':sizing?'resize':'move',bounds:selectionBounds};
      canvas.setPointerCapture(event.pointerId);canvas.focus({preventScroll:true});
    };
    canvas.onpointermove=event=>{
      if(!drag){const id=event.target.getAttribute('data-stroke'),g=strokes.find(g=>g.id===id);$('strokeHover').textContent=event.target.getAttribute('data-point')?'Path point · drag to reshape':event.target.getAttribute('data-center')?'Selection center · drag to move selection':g?'Hover: '+g.label+(g.id===selected?' · selected':' · click to select'):'Hover over a stroke or point to identify it.';return;}
      if(event.pointerId!==drag.pointer)return;
      if(drag.mode==='pan'){
        const cursor=canvas.createSVGPoint();cursor.x=event.clientX;cursor.y=event.clientY;
        const p=cursor.matrixTransform(drag.matrix);
        viewport={...drag.view,x:drag.view.x+drag.start.x-p.x,y:drag.view.y+drag.start.y-p.y};
        updateView();return;
      }
      const p=point(event), step=$('strokeSnap').checked?1:.1;
      if(drag.mode==='point')movePoint(drag.position.map((n,i)=>round(Math.round((n+(i?p.y-drag.start.y:p.x-drag.start.x))/step)*step)),false,drag.before);
      else if(drag.mode==='resize'){
        const b=drag.bounds;if(!b)return;
        let rx=(p.x-b.cx)/(drag.start.x-b.cx),ry=(p.y-b.cy)/(drag.start.y-b.cy);
        resize(drag.scale[0]*rx,drag.scale[1]*ry,false,drag.before,b);
      }else move(Math.round((drag.offset[0]+p.x-drag.start.x)/step)*step,Math.round((drag.offset[1]+p.y-drag.start.y)/step)*step,false,drag.before);
    };
    canvas.onpointerleave=()=>{if(!drag)$('strokeHover').textContent='Hover over a stroke to identify it.';};
    const finish=event=>{if(!drag || event.pointerId!==drag.pointer)return;const before=drag.before;drag=null;if(before && JSON.stringify(before)!==JSON.stringify(state())){undo.push(before);redo=[];}controls();};
    canvas.onpointerup=finish;canvas.onlostpointercapture=finish;
    canvas.onpointercancel=event=>{if(!drag || event.pointerId!==drag.pointer)return;const before=drag.before,view=drag.view;drag=null;if(view){viewport=view;updateView();}else change(before,false);};
    canvas.onkeydown=event=>{
      if(!ready || busy || !selected)return;
      if(event.code==='Space'){event.preventDefault();spacePan=true;updateView();return;}
      if(event.key==='Escape' && panMode){event.preventDefault();event.stopPropagation();panMode=false;updateView();return;}
      if(event.key==='Escape' && selectedPoint){event.preventDefault();event.stopPropagation();selectedPoint=null;draw();return;}
      const moves={ArrowLeft:[-1,0],ArrowRight:[1,0],ArrowUp:[0,-1],ArrowDown:[0,1]}, delta=moves[event.key];
      if(!delta)return;event.preventDefault();const offset=offsets[activeId()] || [0,0],step=event.shiftKey?.1:1;
      if(selectedPoint){const knot=pathPoints(translatedGraph(workingIcon(),strokes,offsets,scales),strokes.find(g=>g.id===selectedPoint.group)).find(n=>n.refs.includes(selectedPoint.id));if(knot)movePoint(knot.position.map((n,i)=>round(n+delta[i]*step)));}
      else move(offset[0]+delta[0]*step,offset[1]+delta[1]*step);
    };
    window.addEventListener('keyup',event=>{if(event.code==='Space'){spacePan=false;updateView();}});
    canvas.addEventListener('blur',()=>{spacePan=false;updateView();});
    window.addEventListener('beforeunload',event=>{if(ready && dirty()){remember();event.preventDefault();event.returnValue='';}});
  }
  window.StrokeEditor={open,refresh:()=>{if(ready)draw();},groups,pathData,translatedGraph,snappedResize,snapGeometry,pathPoints,movePathPoint,withoutStrokes,hasUnsavedChanges:()=>ready && dirty()};
  document.addEventListener('DOMContentLoaded',init);
})();

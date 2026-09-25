/* Side pair layout editor: move and resize the main, the sub, or any chosen set of their elements,
   always snapped to the 64 grid. Boxes are centerline units (the painted box is ±2, stroke 4).
   Width and height are independent; Shift keeps the proportions while resizing.
   A unit is what moves as one piece: a connected element by default, or a single path once split. */
(()=>{
  const ns='http://www.w3.org/2000/svg',STROKE=4,HANDLE=1.6,EDGE=1e-9;
  // Main size presets every 4 units from 32 to 56: the main's SOLO48 keyshape grows or shrinks
  // by the same amount on both axes (48 is the automatic size).
  const MAIN_PRESETS=Array.from({length:7},(_v,i)=>32+4*i),PADDING=2;
  const ANCHORS={br:[1,1],bl:[0,1],tr:[1,0],tl:[0,0],ri:[1,.5],le:[0,.5],bo:[.5,1],to:[.5,0]};
  const style=document.createElement('style');style.textContent=`
  .side-layout{width:min(1080px,96vw);max-height:96vh;border:1px solid #a7b8be;border-radius:14px;padding:22px;color:#20302d;background:#fff}.side-layout::backdrop{background:#101b24a8}
  .side-layout header{display:flex;justify-content:space-between;align-items:center;gap:16px}.side-layout h2{font:600 19px system-ui;margin:0}
  .side-layout button{font:13px system-ui;padding:7px 12px;border:1px solid #9bafb5;border-radius:6px;background:#f5f8f8;cursor:pointer}.side-layout button:disabled{opacity:.5;cursor:default}
  .side-layout [aria-pressed=true]{background:#e4f2e6;border-color:#2f7d4a}
  .side-layout-presets{display:grid;gap:8px;margin-bottom:0}.side-layout-sizes,.side-layout-shapes{display:flex;flex-wrap:wrap;gap:6px;align-items:center}.side-layout-sizes>span,.side-layout-shapes>span{min-width:112px}
  .side-layout-sizes button{min-width:40px;padding:7px 8px;font-variant-numeric:tabular-nums}.side-layout-presets small{color:#5b6b67;font-variant-numeric:tabular-nums}
  .side-layout .side-layout-shape{display:grid;grid-template-columns:22px auto;grid-template-rows:auto auto;column-gap:6px;align-items:center;text-align:left;padding:5px 9px}.side-layout-shape svg{grid-row:1/3}.side-layout-shape span{font-size:12px;font-weight:600}.side-layout-shape small{font-size:11px}
  .side-layout-canvas .guide{stroke:#7c3aed;stroke-width:.3;stroke-dasharray:1.2 .8;pointer-events:none}
  .side-layout-bar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:14px 0 10px;font:13px system-ui}.side-layout-bar .spacer{flex:1}.side-layout-bar label{display:flex;gap:5px;align-items:center}
  .side-layout-stages{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,3fr) minmax(180px,2fr);gap:16px;align-items:start}
  .side-layout-stages figure{margin:0}.side-layout-stages figcaption{font:12px system-ui;color:#5b6b67;margin-top:6px}
  .side-layout-canvas,.side-layout-result{display:block;width:100%;height:auto;background:#fbfdfb;box-shadow:inset 0 0 0 1px #99adb4;touch-action:none;user-select:none;outline:none}
  .side-layout-canvas .art{cursor:pointer}.side-layout-canvas .art.picked{color:#2f7d4a}
  .side-layout-canvas[data-centerline] .art{opacity:.35}.side-layout-canvas .trace{pointer-events:none}
  .side-layout-canvas .sel{fill:none;stroke-width:.3;stroke-dasharray:1 .6;pointer-events:none;stroke:#2f7d4a}.side-layout-canvas .unit{fill:none;stroke-width:.2;pointer-events:none;stroke:#2f7d4a;opacity:.6}.side-layout-canvas .out{stroke:#dc2626!important;stroke-dasharray:none;stroke-width:.45;opacity:1}
  .side-layout-canvas .move{fill:transparent;cursor:move}.side-layout-canvas .handle{fill:#fff;stroke-width:.25;stroke:#20302d}
  .side-layout-canvas .handle.nw,.side-layout-canvas .handle.se{cursor:nwse-resize}.side-layout-canvas .handle.ne,.side-layout-canvas .handle.sw{cursor:nesw-resize}.side-layout-canvas .handle.n,.side-layout-canvas .handle.s{cursor:ns-resize}.side-layout-canvas .handle.e,.side-layout-canvas .handle.w{cursor:ew-resize}
  .side-layout-preview{display:grid;place-items:center;aspect-ratio:1;background:#fbfdfb;box-shadow:inset 0 0 0 1px #99adb4;font:13px system-ui;color:#5b6b67;text-align:center}
  .side-layout-list{font:13px system-ui;display:grid;gap:10px;max-height:60vh;overflow:auto}.side-layout-list h3{font:600 12px system-ui;text-transform:uppercase;letter-spacing:.03em;color:#5b6b67;margin:0 0 4px}
  .side-layout-list label{display:flex;gap:6px;align-items:flex-start;padding:3px 0;cursor:pointer;overflow-wrap:anywhere}.side-layout-list small{color:#5b6b67}
  .side-layout-list .row-actions{display:flex;flex-wrap:wrap;gap:6px;margin-top:4px}.side-layout-list .row-actions button{padding:4px 8px;font-size:12px}
  .side-layout-readout{font:13px/1.5 system-ui;font-variant-numeric:tabular-nums;margin:10px 0 0}.side-layout-readout.bad{color:#b91c1c}
  .side-layout-hint{font:12px/1.5 system-ui;color:#5b6b67;margin:6px 0 0}.side-layout-error{font:13px system-ui;color:#b91c1c;margin:6px 0 0}
  .side-layout-open{margin-top:4px;font:600 12px system-ui;padding:6px 12px;border:1px solid #2f7d4a;border-radius:6px;background:#f1f6f1;color:#25653a;cursor:pointer}.side-layout-open:hover{background:#e4f2e6}
  .side-layout-save{background:#2f7d4a!important;border-color:#2f7d4a!important;color:#fff}
  @media(max-width:900px){.side-layout-stages{grid-template-columns:1fr 1fr}.side-layout-list{grid-column:1/-1}}@media(max-width:600px){.side-layout-stages{grid-template-columns:1fr}}`;document.head.append(style);

  const el=(name,attrs={})=>{const e=document.createElementNS(ns,name);for(const [k,v] of Object.entries(attrs))e.setAttribute(k,v);return e;};
  const html=(tag,cls,text)=>{const e=document.createElement(tag);if(cls)e.className=cls;if(text!=null)e.textContent=text;return e;};
  const fmt=n=>String(Math.round(n*100)/100);
  let dialog,ctx,centerline=true;
  try{centerline=localStorage.getItem('side-layout-centerline')!=='off';}catch{}

  // A unit maps its source box onto (x, y, w, h). A flat axis (a straight rule) has no scale of its own.
  const scales=u=>{
    const sw=u.src[2]-u.src[0],sh=u.src[3]-u.src[1];
    let sx=sw>EDGE?u.w/sw:null,sy=sh>EDGE?u.h/sh:null;
    return [sx??sy??1,sy??sx??1];
  };
  const boxOf=u=>[u.x,u.y,u.x+u.w,u.y+u.h];
  const unionOf=list=>list.map(boxOf).reduce((a,b)=>[Math.min(a[0],b[0]),Math.min(a[1],b[1]),Math.max(a[2],b[2]),Math.max(a[3],b[3])]);
  const keyOf=(role,i)=>role+':'+i;
  const selected=()=>[...ctx.sel].map(k=>{const [role,i]=k.split(':');return ctx.roles[role]?.units[Number(i)];}).filter(Boolean);
  const selectedRoles=()=>new Set([...ctx.sel].map(k=>k.split(':')[0]));
  const outside=b=>b[0]-2<-1e-6||b[1]-2<-1e-6||b[2]+2>ctx.canvas+1e-6||b[3]+2>ctx.canvas+1e-6;
  const anyOutside=()=>Object.values(ctx.roles).some(r=>r.units.some(u=>outside(boxOf(u))));

  function build(){
    dialog=html('dialog','side-layout');
    dialog.innerHTML=`<header><h2></h2><button type="button" data-close>Close</button></header>
      <div class="side-layout-bar side-layout-presets" role="group" aria-label="Main size"></div>
      <div class="side-layout-bar"><span>Click selects</span><button type="button" data-level="whole">Whole icon</button><button type="button" data-level="element">Element</button>
      <label><input type="checkbox" data-centerline> Centerline</label><span class="spacer"></span>
      <button type="button" data-reset>Reset to automatic</button><button type="button" data-cancel>Discard changes</button><button type="button" class="side-layout-save" data-save>Save layout</button></div>
      <div class="side-layout-stages"><figure><svg class="side-layout-canvas" tabindex="0" role="application" aria-label="Layout editor, 64 by 64 grid"></svg>
      <figcaption>Editing view: main and sub drawn whole, centerline in red.</figcaption></figure>
      <figure><div class="side-layout-preview"></div><figcaption>Combined result (the sub erases the main where they meet).</figcaption></figure>
      <div class="side-layout-list" aria-label="Elements"></div></div>
      <p class="side-layout-readout" role="status"></p>
      <p class="side-layout-hint">Main size 32–56 (every 4) and a keyshape snap the main onto that keyshape at that size (purple dashes) — 48 on its own keyshape is automatic; Free lets you drag it to any size. Shift- or ⌘-click (or tick the list) to choose several elements. Drag to move; drag a corner or edge to resize — width and height change independently, hold Shift to keep proportions. Arrow keys move 1 unit (Shift: 8); Alt+arrows change width / height by 1; + and − change both. Everything snaps to the grid; the stroke stays 4.</p>
      <p class="side-layout-error" role="alert"></p>`;
    document.body.append(dialog);
    const q=s=>dialog.querySelector(s);
    q('[data-close]').onclick=()=>dialog.close();
    q('[data-cancel]').onclick=()=>load(ctx.pair,ctx.main,ctx.sub,ctx.onSaved,ctx.saved);
    q('[data-save]').onclick=save;q('[data-reset]').onclick=reset;
    const toggle=q('[data-centerline]');toggle.checked=centerline;
    toggle.onchange=()=>{centerline=toggle.checked;try{localStorage.setItem('side-layout-centerline',centerline?'on':'off');}catch{}draw();if(ctx.result)preview(ctx.result);};
    for(const b of dialog.querySelectorAll('[data-level]'))b.onclick=()=>{ctx.level=b.dataset.level;draw();};
    const svg=q('.side-layout-canvas');
    svg.addEventListener('pointerdown',down);svg.addEventListener('keydown',key);
    new ResizeObserver(()=>{if(ctx&&dialog.open)draw();}).observe(svg);
  }

  async function combine(body){
    const r=await fetch('/api/combinations/side/preview',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    const data=await r.json().catch(()=>({error:'Unexpected response.'}));if(!r.ok||data.error)throw Error(data.error||'Could not combine.');return data;
  }
  // `saved` is the layout the pair's published result was rendered with, if any.
  function open(pair,main,sub,onSaved,saved=null){
    if(!dialog)build();
    dialog.querySelector('h2').textContent='Adjust layout · '+pair.concept;
    if(!dialog.open)dialog.showModal();
    load(pair,main,sub,onSaved,saved);
  }
  async function load(pair,main,sub,onSaved,saved){
    ctx={pair,main,sub,onSaved,saved,canvas:64,roles:{},dirty:new Set(),sel:new Set(),level:ctx?.level||'whole',busy:false,token:0,result:null};
    dialog.querySelector('.side-layout-canvas').replaceChildren();dialog.querySelector('.side-layout-list').replaceChildren();
    error('');readout('Loading elements…');preview(null,'Loading…');
    let data;
    try{data=await combine({id:pair.id,main:main.icon,sub:sub.icon,elements:true,...(saved?{layout:saved}:{})});}
    catch(e){
      if(!saved){readout('');error(e.message);return;}
      try{data=await combine({id:pair.id,main:main.icon,sub:sub.icon,elements:true});error('The saved layout no longer fits these drawings: '+e.message);}catch(e2){readout('');error(e2.message);return;}
    }
    if(ctx.pair!==pair)return;
    if(!data.elements){readout('');error(data.elements_error||'This pair cannot be adjusted.');preview(data);return;}
    ctx.canvas=data.canvas||64;ctx.keyshapes=data.keyshapes||{};ctx.shapes=null;ctx.size=null;ctx.shape=null;
    for(const [role,c] of Object.entries(data.elements)){
      ctx.roles[role]={markup:c.markup,names:c.names,sources:c.sources,units:c.groups.map(g=>{const b=g.box;return {paths:g.paths,src:g.source,x:b[0],y:b[1],w:b[2]-b[0],h:b[3]-b[1]};})};
      if(saved?.[role])ctx.dirty.add(role);
    }
    preview(data);draw();
  }

  // The first edit of a role snaps every one of its units onto the grid (edges, so touching units stay touching).
  function touch(roles){
    for(const role of roles){
      if(ctx.dirty.has(role))continue;ctx.dirty.add(role);
      for(const u of ctx.roles[role].units){const x1=Math.round(u.x+u.w),y1=Math.round(u.y+u.h);u.x=Math.round(u.x);u.y=Math.round(u.y);u.w=x1-u.x;u.h=y1-u.y;}
    }
  }
  function layout(){
    const out={};
    for(const role of ctx.dirty)out[role]=ctx.roles[role].units.map(u=>({paths:u.paths,x:u.x,y:u.y,w:u.w,h:u.h}));
    return Object.keys(out).length?out:null;
  }
  // Split the chosen units into one unit per path, each keeping exactly where it is drawn now.
  function split(){
    touch(selectedRoles());
    const next=new Set();
    for(const [role,r] of Object.entries(ctx.roles)){
      const units=[];
      r.units.forEach((u,i)=>{
        if(!ctx.sel.has(keyOf(role,i))||u.paths.length<2){if(ctx.sel.has(keyOf(role,i)))next.add(keyOf(role,units.length));units.push(u);return;}
        const [sx,sy]=scales(u);
        for(const p of u.paths){
          const s=r.sources[p],x0=Math.round(u.x+(s[0]-u.src[0])*sx),y0=Math.round(u.y+(s[1]-u.src[1])*sy);
          const x1=Math.round(u.x+(s[2]-u.src[0])*sx),y1=Math.round(u.y+(s[3]-u.src[1])*sy);
          next.add(keyOf(role,units.length));units.push({paths:[p],src:s,x:x0,y:y0,w:x1-x0,h:y1-y0});
        }
      });
      r.units=units;
    }
    ctx.sel=next;ctx.level='element';refresh();
  }

  function pxPerUnit(svg){const m=svg.getScreenCTM();return m&&m.a>0?m.a:6;}
  // The main's keyshape: its drawing's centerline box on the 48 canvas, when that is a SOLO48 keyshape.
  function mainSource(){
    const r=ctx.roles.main;if(!r)return null;
    const boxes=r.sources.filter(Boolean);
    return boxes.length?boxes.reduce((a,b)=>[Math.min(a[0],b[0]),Math.min(a[1],b[1]),Math.max(a[2],b[2]),Math.max(a[3],b[3])]):null;
  }
  // The six distinct SOLO48 keyshapes of the contract (several names share one set of bounds),
  // in picker order: square, circle, tall, wide, tall small, wide small.
  function shapes(){
    if(ctx.shapes)return ctx.shapes;
    const unique=new Map();
    for(const [name,b] of Object.entries(ctx.keyshapes)){const k=b.join(',');if(!unique.has(k))unique.set(k,{names:[],bounds:b});unique.get(k).names.push(name);}
    const list=[...unique.values()].map(s=>({...s,w:s.bounds[2]-s.bounds[0],h:s.bounds[3]-s.bounds[1],circle:s.names.includes('CIRCLE')}));
    const pick=(filter,sort)=>list.filter(filter).sort(sort);
    const tall=pick(s=>s.h>s.w,(a,b)=>b.w-a.w),wide=pick(s=>s.w>s.h,(a,b)=>b.h-a.h);
    const named=[['square','Square',list.find(s=>s.w===s.h&&!s.circle)],['circle','Circle',list.find(s=>s.circle)],
      ['tall','Tall',tall[0]],['wide','Wide',wide[0]],['tall-small','Tall small',tall[1]],['wide-small','Wide small',wide[1]]];
    return ctx.shapes=named.filter(([, ,s])=>s).map(([id,label,s])=>({id,label,...s}));
  }
  function ownShape(){
    const src=mainSource();if(!src||Math.abs((ctx.main.canvas||48)-48)>1e-6)return null;
    return shapes().find(s=>s.bounds.every((v,i)=>Math.abs(v-src[i])<.05))?.id||null;
  }
  // Centerline box of the main at a preset: a keyshape grows or shrinks by (size − 48) on both axes
  // (square 40 → 44 at 52) and sits in the corner opposite the sub, as the automatic placement puts it.
  // 'own' (a drawing on no keyshape) scales the drawing evenly instead.
  function presetBox(size,shapeId){
    const [ax,ay]=ANCHORS[ctx.pair.position]||[1,1],c=ctx.canvas,shape=shapes().find(s=>s.id===shapeId);
    let w,h;
    if(shape){w=shape.w+size-48;h=shape.h+size-48;}
    else{const src=mainSource();if(!src)return null;const k=size/(ctx.main.canvas||48);w=Math.round((src[2]-src[0])*k);h=Math.round((src[3]-src[1])*k);}
    if(w<4||h<4||w+4>c-2*PADDING||h+4>c-2*PADDING)return null;
    const x=Math.round(PADDING+(c-2*PADDING-w-4)*(1-ax))+2,y=Math.round(PADDING+(c-2*PADDING-h-4)*(1-ay))+2;
    return [x,y,x+w,y+h];
  }
  const sameBox=(a,b)=>a&&b&&a.every((v,i)=>Math.abs(v-b[i])<1e-6);
  // The preset (size + keyshape) the main is on right now, if any.
  function currentPreset(){
    const r=ctx.roles.main;if(!r)return null;const box=unionOf(r.units);
    // Boxes can coincide (circle at 44 = square at 48): what was chosen last wins, then the main's own keyshape.
    if(ctx.size&&ctx.shape&&sameBox(box,presetBox(ctx.size,ctx.shape)))return {size:ctx.size,shape:ctx.shape};
    const ids=[...(ownShape()?[ownShape()]:['own']),...shapes().map(s=>s.id)];
    for(const id of ids)for(const size of MAIN_PRESETS)if(sameBox(box,presetBox(size,id)))return {size,shape:id};
    return null;
  }
  // Map every main unit from the main's current box onto the preset box (edges rounded to the grid).
  function applyPreset(size,shapeId){
    const r=ctx.roles.main,target=presetBox(size,shapeId);if(!r||!target)return;
    touch(['main']);ctx.size=size;ctx.shape=shapeId;
    const from=unionOf(r.units),fw=from[2]-from[0],fh=from[3]-from[1];
    const mapX=v=>Math.round(fw>EDGE?target[0]+(v-from[0])*(target[2]-target[0])/fw:target[0]);
    const mapY=v=>Math.round(fh>EDGE?target[1]+(v-from[1])*(target[3]-target[1])/fh:target[1]);
    for(const u of r.units){const x0=mapX(u.x),y0=mapY(u.y),x1=mapX(u.x+u.w),y1=mapY(u.y+u.h);u.x=x0;u.y=y0;u.w=u.w>0?Math.max(1,x1-x0):0;u.h=u.h>0?Math.max(1,y1-y0):0;}
    ctx.sel=new Set(r.units.map((_u,i)=>keyOf('main',i)));refresh();
    dialog.querySelector('.side-layout-canvas').focus();
  }
  // A small drawing of a keyshape at its proportions.
  function shapeIcon(w,h,circle){
    const k=18/Math.max(w,h),sw=w*k,sh=h*k,svg=el('svg',{viewBox:'0 0 22 22',width:22,height:22,'aria-hidden':'true'});
    svg.append(circle?el('circle',{cx:11,cy:11,r:sw/2,fill:'none',stroke:'currentColor','stroke-width':1.6})
      :el('rect',{x:11-sw/2,y:11-sh/2,width:sw,height:sh,rx:2,fill:'none',stroke:'currentColor','stroke-width':1.6}));
    return svg;
  }
  function drawPresets(){
    const bar=dialog.querySelector('.side-layout-presets');bar.replaceChildren();
    const r=ctx.roles.main;if(!r)return;
    const own=ownShape(),now=currentPreset();
    if(now){ctx.size=now.size;ctx.shape=now.shape;}
    ctx.size??=48;ctx.shape??=own||'own';
    const canvas=dialog.querySelector('.side-layout-canvas'),current=unionOf(r.units),painted=b=>`${b[2]-b[0]+4}×${b[3]-b[1]+4}`;
    const sizes=html('div','side-layout-sizes');sizes.append(html('span','','Main size'));
    for(const size of MAIN_PRESETS){
      if(!presetBox(size,ctx.shape))continue;
      const b=html('button','',String(size));b.type='button';b.setAttribute('aria-pressed',String(!!now&&now.size===size));
      b.onclick=()=>applyPreset(size,ctx.shape);sizes.append(b);
    }
    const free=html('button','','Free');free.type='button';free.setAttribute('aria-pressed',String(!now));
    free.title='Resize the main freely: drag its handles';
    // Keyboard nudges (arrows, Alt+arrows, + / −) go to the canvas straight after choosing.
    free.onclick=()=>{ctx.level='whole';ctx.sel=new Set(r.units.map((_u,i)=>keyOf('main',i)));draw();canvas.focus();};
    sizes.append(free,html('small','',`painted ${painted(current)}`));
    // Keyshapes at the chosen size, each with its painted size.
    const tiles=html('div','side-layout-shapes');tiles.append(html('span','',`Keyshape at ${ctx.size}`));
    const options=[...(own?[]:[{id:'own',label:'Own shape'}]),...shapes()];
    for(const s of options){
      const box=presetBox(ctx.size,s.id);if(!box)continue;
      const w=box[2]-box[0]+4,h=box[3]-box[1]+4,b=html('button','side-layout-shape');b.type='button';
      b.setAttribute('aria-pressed',String(!!now&&now.shape===s.id));
      b.title=`${s.label}${s.names?' ('+s.names.join(', ')+')':''}: painted ${w}×${h} at size ${ctx.size}`;
      b.append(shapeIcon(w,h,s.circle),html('span','',s.label),html('small','',`${w}×${h}${s.id===own?' · own':''}`));
      b.onclick=()=>applyPreset(ctx.size,s.id);tiles.append(b);
    }
    bar.append(sizes,tiles);
  }
  // Dashed outline of the chosen keyshape at the chosen size (painted), behind the artwork.
  function keyshapeGuide(){
    const box=ctx.roles.main&&presetBox(ctx.size??48,ctx.shape??'own');if(!box)return null;
    const shape=shapes().find(s=>s.id===ctx.shape),p=[box[0]-2,box[1]-2,box[2]+2,box[3]+2],attrs={class:'guide',fill:'none'};
    return shape?.circle?el('circle',{...attrs,cx:(p[0]+p[2])/2,cy:(p[1]+p[3])/2,r:(p[2]-p[0])/2})
      :el('rect',{...attrs,x:p[0],y:p[1],width:p[2]-p[0],height:p[3]-p[1],rx:1});
  }

  function draw(){
    drawPresets();
    const svg=dialog.querySelector('.side-layout-canvas'),c=ctx.canvas;svg.setAttribute('viewBox',`-1 -1 ${c+2} ${c+2}`);svg.replaceChildren();
    if(centerline)svg.setAttribute('data-centerline','');else svg.removeAttribute('data-centerline');
    for(const b of dialog.querySelectorAll('[data-level]'))b.setAttribute('aria-pressed',String(b.dataset.level===ctx.level));
    const grid=el('g',{'pointer-events':'none'});
    for(let i=0;i<=c;i++){const a={stroke:i%8===0?'#9eb3bd':'#dae4e9','stroke-width':i%8===0?.13:.055};grid.append(el('line',{x1:i,y1:0,x2:i,y2:c,...a}),el('line',{x1:0,y1:i,x2:c,y2:i,...a}));}
    svg.append(grid);
    const guide=keyshapeGuide();if(guide)svg.append(guide);
    // Strokes do not stretch with the unit: drawn in screen pixels, 4 canvas units wide.
    const px=pxPerUnit(svg),traces=el('g',{class:'trace',fill:'none',stroke:'#ef4444'});
    for(const role of ['main','sub']){
      const r=ctx.roles[role];if(!r)continue;
      const layer=el('g',{fill:'none',stroke:'currentColor','stroke-linecap':'round','stroke-linejoin':'round'});
      r.units.forEach((u,i)=>{
        const [sx,sy]=scales(u),transform=`matrix(${sx} 0 0 ${sy} ${u.x-u.src[0]*sx} ${u.y-u.src[1]*sy})`;
        const art=el('g',{class:'art'+(ctx.sel.has(keyOf(role,i))?' picked':''),'data-role':role,'data-unit':i,transform});
        const parsed=new DOMParser().parseFromString(`<svg xmlns="${ns}">${u.paths.map(p=>r.markup[p]).join('')}</svg>`,'image/svg+xml').documentElement;
        for(const child of [...parsed.children]){const n=document.importNode(child,true);n.setAttribute('vector-effect','non-scaling-stroke');n.setAttribute('stroke-width',STROKE*px);art.append(n);}
        layer.append(art);
        if(centerline){const t=art.cloneNode(true);t.removeAttribute('class');for(const n of t.children){n.setAttribute('stroke','#ef4444');n.setAttribute('stroke-width',1.3);n.setAttribute('fill','none');}traces.append(t);}
      });
      svg.append(layer);
    }
    svg.append(traces);
    const list=selected();
    if(list.length){
      for(const u of list){const b=boxOf(u);if(list.length>1||outside(b))svg.append(el('rect',{class:'unit'+(outside(b)?' out':''),x:b[0]-2,y:b[1]-2,width:b[2]-b[0]+4,height:b[3]-b[1]+4}));}
      const b=unionOf(list),p=[b[0]-2,b[1]-2,b[2]+2,b[3]+2],mx=(p[0]+p[2])/2,my=(p[1]+p[3])/2;
      svg.append(el('rect',{class:'move',x:p[0],y:p[1],width:p[2]-p[0],height:p[3]-p[1],'data-move':''}));
      svg.append(el('rect',{class:'sel'+(outside(b)?' out':''),x:p[0],y:p[1],width:p[2]-p[0],height:p[3]-p[1]}));
      for(const [name,x,y] of [['nw',p[0],p[1]],['n',mx,p[1]],['ne',p[2],p[1]],['e',p[2],my],['se',p[2],p[3]],['s',mx,p[3]],['sw',p[0],p[3]],['w',p[0],my]])
        svg.append(el('rect',{class:'handle '+name,'data-handle':name,x:x-HANDLE/2,y:y-HANDLE/2,width:HANDLE,height:HANDLE}));
    }
    drawList();status();
  }
  // Checklist of units: choose exactly which elements a move or resize applies to.
  function drawList(){
    const box=dialog.querySelector('.side-layout-list');box.replaceChildren();
    for(const role of ['main','sub']){
      const r=ctx.roles[role];if(!r)continue;
      const section=html('section');section.append(html('h3','',role==='main'?'Main elements':'Sub elements'));
      r.units.forEach((u,i)=>{
        const label=html('label'),check=html('input');check.type='checkbox';check.checked=ctx.sel.has(keyOf(role,i));
        check.onchange=()=>{if(check.checked)ctx.sel.add(keyOf(role,i));else ctx.sel.delete(keyOf(role,i));draw();};
        // Unnamed geometry (native text glyphs) is numbered instead of listed as "path + path".
        const named=u.paths.some(p=>!['path','circle','ellipse','rect','line','polyline','polygon'].includes(r.names[p]));
        const text=html('span','',named?u.paths.map(p=>r.names[p]).join(' + '):`${role==='sub'&&ctx.pair.native_text?'Glyph':'Element'} ${i+1}`);
        text.append(html('small','',` · ${fmt(u.w+4)}×${fmt(u.h+4)}`));
        label.append(check,text);section.append(label);
      });
      const actions=html('div','row-actions'),all=html('button','','Select all');all.type='button';
      all.onclick=()=>{r.units.forEach((_u,i)=>ctx.sel.add(keyOf(role,i)));draw();};actions.append(all);section.append(actions);
      box.append(section);
    }
    const actions=html('div','row-actions'),splitButton=html('button','','Split into paths'),none=html('button','','Clear selection');
    splitButton.type=none.type='button';splitButton.title='Resize the paths of a connected element one by one';
    splitButton.disabled=!selected().some(u=>u.paths.length>1);splitButton.onclick=split;
    none.disabled=!ctx.sel.size;none.onclick=()=>{ctx.sel.clear();draw();};
    actions.append(splitButton,none);box.append(actions);
  }
  function status(){
    const bad=anyOutside();
    dialog.querySelector('[data-save]').disabled=ctx.busy||bad||!ctx.dirty.size;
    dialog.querySelector('[data-reset]').disabled=ctx.busy||!ctx.saved;
    const list=selected();
    if(!list.length){readout(bad?'Part of the artwork is outside the canvas.':'Select the main, the sub or some elements to adjust them.',bad);return;}
    const b=unionOf(list),what=list.length===1?'1 element':`${list.length} elements`;
    readout(`${what}: painted ${fmt(b[2]-b[0]+4)}×${fmt(b[3]-b[1]+4)} at (${fmt(b[0]-2)}, ${fmt(b[1]-2)})`+(bad?' · outside the canvas':''),bad);
  }
  const readout=(text,bad)=>{const r=dialog.querySelector('.side-layout-readout');r.textContent=text;r.classList.toggle('bad',!!bad);};
  const error=text=>{dialog.querySelector('.side-layout-error').textContent=text;};
  // The combined result, with its centerline traced on top when that view is on.
  function preview(result,text){
    const box=dialog.querySelector('.side-layout-preview');box.replaceChildren();
    if(!result){box.append(html('span','',text||''));return;}
    ctx.result=result;
    const svg=new DOMParser().parseFromString(result.svg,'image/svg+xml').documentElement;
    svg.setAttribute('class','side-layout-result');svg.removeAttribute('width');svg.removeAttribute('height');svg.setAttribute('role','img');svg.setAttribute('aria-label','Combined result');
    if(centerline){
      for(const id of ['main-icon-clipped','state-icon']){
        const g=svg.querySelector(`[id="${id}"]`);if(!g)continue;
        const t=g.cloneNode(true);t.setAttribute('opacity','1');
        for(const n of [t,...t.querySelectorAll('*')]){n.removeAttribute('id');n.setAttribute('stroke','#ef4444');n.setAttribute('fill','none');n.setAttribute('stroke-width','1.2');n.setAttribute('vector-effect','non-scaling-stroke');}
        g.setAttribute('opacity','.35');svg.append(t);
      }
    }
    box.append(document.importNode(svg,true));
  }
  // Re-combine shortly after an edit so the erased result stays in step with the editor.
  let timer;
  function refresh(){
    clearTimeout(timer);draw();
    if(anyOutside()){preview(null,'Move the artwork back inside the canvas to preview.');ctx.result=null;return;}
    timer=setTimeout(async()=>{
      const token=++ctx.token,body={id:ctx.pair.id,main:ctx.main.icon,sub:ctx.sub.icon},l=layout();if(l)body.layout=l;
      try{const data=await combine(body);if(token===ctx.token){preview(data);error('');}}
      catch(e){if(token===ctx.token)error(e.message);}
    },350);
  }

  // Scale the chosen units about a pinned point: fx / fy per axis (null leaves that axis alone).
  // Unit edges are rounded, so units that touched before still touch after.
  function scale(list,before,fx,fy,pinX,pinY){
    list.forEach((u,i)=>{
      const b=before[i],sw=b.src[2]-b.src[0],sh=b.src[3]-b.src[1];
      if(fx!=null){
        const x0=Math.round(pinX+(b.x-pinX)*fx),x1=Math.round(pinX+(b.x+b.w-pinX)*fx);
        u.x=sw>EDGE?Math.min(x0,x1-1):Math.round(pinX+(b.x-pinX)*fx);u.w=sw>EDGE?Math.max(1,x1-u.x):0;
      }
      if(fy!=null){
        const y0=Math.round(pinY+(b.y-pinY)*fy),y1=Math.round(pinY+(b.y+b.h-pinY)*fy);
        u.y=sh>EDGE?Math.min(y0,y1-1):Math.round(pinY+(b.y-pinY)*fy);u.h=sh>EDGE?Math.max(1,y1-u.y):0;
      }
    });
  }
  const point=(svg,e)=>{const p=new DOMPoint(e.clientX,e.clientY).matrixTransform(svg.getScreenCTM().inverse());return [p.x,p.y];};
  // Pointer: pick, move the selection, or resize it from a corner or an edge with the opposite side pinned.
  function down(e){
    const svg=e.currentTarget,additive=e.shiftKey||e.metaKey||e.ctrlKey;let target=e.target,art=target.closest('.art');
    // Artwork under the selection frame (the arrow inside a selected monitor) can still be picked.
    if(target.hasAttribute('data-move')){
      const under=document.elementsFromPoint(e.clientX,e.clientY).map(n=>n.closest?.('.art')).find(Boolean);
      if(under&&(additive||!ctx.sel.has(keyOf(under.dataset.role,under.dataset.unit)))&&(ctx.level==='element'||!selectedRoles().has(under.dataset.role)||additive)){target=under;art=under;}
    }
    if(!target.hasAttribute('data-handle')&&!target.hasAttribute('data-move')){
      if(!art){if(!additive)ctx.sel.clear();draw();return;}
      const role=art.dataset.role,keys=ctx.level==='element'?[keyOf(role,art.dataset.unit)]:ctx.roles[role].units.map((_u,i)=>keyOf(role,i));
      if(additive){const on=keys.every(k=>ctx.sel.has(k));for(const k of keys)on?ctx.sel.delete(k):ctx.sel.add(k);draw();return;}
      if(!keys.every(k=>ctx.sel.has(k))||keys.length!==ctx.sel.size)ctx.sel=new Set(keys);
    }
    if(!ctx.sel.size)return;
    svg.focus();touch(selectedRoles());
    const list=selected(),start=point(svg,e),before=list.map(u=>({...u})),box=unionOf(list),corner=target.dataset.handle;
    draw();svg.setPointerCapture(e.pointerId);e.preventDefault();
    let moved=false;
    const move=ev=>{
      const [px,py]=point(svg,ev);moved=true;
      if(!corner){
        const dx=Math.round(px-start[0]),dy=Math.round(py-start[1]);
        list.forEach((u,i)=>{u.x=before[i].x+dx;u.y=before[i].y+dy;});
      }else{
        const w=box[2]-box[0],h=box[3]-box[1],pinX=corner.includes('w')?box[2]:box[0],pinY=corner.includes('n')?box[3]:box[1];
        // The dragged edge lands on a grid line (the painted edge is the centerline edge ±2).
        const edgeX=corner.includes('w')?Math.round(px+2):Math.round(px-2),edgeY=corner.includes('n')?Math.round(py+2):Math.round(py-2);
        let fx=/[ew]/.test(corner)&&w>EDGE?Math.max(1,Math.abs(edgeX-pinX))/w:null,fy=/[ns]/.test(corner)&&h>EDGE?Math.max(1,Math.abs(edgeY-pinY))/h:null;
        if(ev.shiftKey){const f=Math.max(fx??0,fy??0)||1;fx=w>EDGE?f:null;fy=h>EDGE?f:null;}
        scale(list,before,fx,fy,pinX,pinY);
      }
      draw();
    };
    const up=()=>{svg.removeEventListener('pointermove',move);svg.removeEventListener('pointerup',up);svg.removeEventListener('pointercancel',up);if(moved)refresh();};
    svg.addEventListener('pointermove',move);svg.addEventListener('pointerup',up);svg.addEventListener('pointercancel',up);
  }
  function key(e){
    if(!ctx.sel.size)return;
    const list=selected(),steps={ArrowLeft:[-1,0],ArrowRight:[1,0],ArrowUp:[0,-1],ArrowDown:[0,1]},box=unionOf(list),w=box[2]-box[0],h=box[3]-box[1];
    const resize=(dw,dh)=>{
      touch(selectedRoles());const before=list.map(u=>({...u}));
      scale(list,before,dw&&w>EDGE&&w+dw>=1?(w+dw)/w:null,dh&&h>EDGE&&h+dh>=1?(h+dh)/h:null,box[0],box[1]);refresh();
    };
    if(steps[e.key]&&e.altKey){e.preventDefault();resize(steps[e.key][0],steps[e.key][1]);}
    else if(steps[e.key]){
      e.preventDefault();touch(selectedRoles());const n=e.shiftKey?8:1;
      for(const u of list){u.x+=steps[e.key][0]*n;u.y+=steps[e.key][1]*n;}refresh();
    }else if(['+','='].includes(e.key)){e.preventDefault();resize(1,1);}
    else if(['-','_'].includes(e.key)){e.preventDefault();resize(-1,-1);}
    else if(e.key==='Escape'){ctx.sel.clear();draw();e.preventDefault();e.stopPropagation();}
  }

  async function post(body){
    ctx.busy=true;status();error('');
    try{
      const r=await fetch('/api/combinations/side/layout',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
      const data=await r.json().catch(()=>({error:'Unexpected response.'}));if(!r.ok||data.error)throw Error(data.error||'Could not save the layout.');
      ctx.onSaved?.(data);return data;
    }finally{ctx.busy=false;status();}
  }
  async function save(){
    const l=layout();if(!l)return;
    try{const data=await post({pair_id:ctx.pair.id,main:ctx.main.icon,sub:ctx.sub.icon,layout:l});ctx.saved=data.layout.layout;preview(data.result);readout('Layout saved.');}
    catch(e){error(e.message);}
  }
  async function reset(){
    try{await post({pair_id:ctx.pair.id,layout:null});load(ctx.pair,ctx.main,ctx.sub,ctx.onSaved,null);}
    catch(e){error(e.message);}
  }

  function button(pair,main,sub,onSaved,saved){
    // Both workspaces: production edits and keeps its own layouts (saving needs a login there).
    const b=html('button','side-layout-open','Edit layout');b.type='button';
    b.title='Move and resize the main, the sub or chosen elements, snapped to the grid';
    b.onclick=()=>open(pair,main,sub,onSaved,saved);return b;
  }
  window.SideLayoutEditor={open,button};
})();

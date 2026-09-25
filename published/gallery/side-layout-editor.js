/* Side pair layout editor: move and resize the main, the sub, or one connected element of either,
   always snapped to the 64 grid. Positions are centerline units; the painted box is ±2 (stroke 4).
   A group's size is its longest axis; the other axis keeps its proportions. */
(()=>{
  const ns='http://www.w3.org/2000/svg',STROKE=4,HANDLE=1.8;
  const style=document.createElement('style');style.textContent=`
  .side-layout{width:min(980px,96vw);max-height:96vh;border:1px solid #a7b8be;border-radius:14px;padding:22px;color:#20302d;background:#fff}.side-layout::backdrop{background:#101b24a8}
  .side-layout header{display:flex;justify-content:space-between;align-items:center;gap:16px}.side-layout h2{font:600 19px system-ui;margin:0}
  .side-layout button{font:13px system-ui;padding:8px 13px;border:1px solid #9bafb5;border-radius:6px;background:#f5f8f8;cursor:pointer}.side-layout button:disabled{opacity:.5;cursor:default}
  .side-layout [aria-pressed=true]{background:#e4f2e6;border-color:#2f7d4a}
  .side-layout-bar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:14px 0 10px}.side-layout-bar .spacer{flex:1}
  .side-layout-stages{display:grid;grid-template-columns:minmax(0,3fr) minmax(0,2fr);gap:18px;align-items:start}
  .side-layout-stages figure{margin:0}.side-layout-stages figcaption{font:12px system-ui;color:#5b6b67;margin-top:6px}
  .side-layout-canvas{display:block;width:100%;height:auto;background:#fbfdfb;box-shadow:inset 0 0 0 1px #99adb4;touch-action:none;user-select:none;outline:none}
  .side-layout-canvas .art{cursor:pointer}.side-layout-canvas .art:hover{color:#2f7d4a}
  .side-layout-canvas .sel{fill:none;stroke-width:.35;stroke-dasharray:1 .6;pointer-events:none}.side-layout-canvas .sel.main{stroke:#bd4b30}.side-layout-canvas .sel.sub{stroke:#146dc5}.side-layout-canvas .sel.out{stroke:#dc2626;stroke-dasharray:none;stroke-width:.5}
  .side-layout-canvas .move{fill:transparent;cursor:move}.side-layout-canvas .handle{fill:#fff;stroke-width:.3;stroke:#20302d}
  .side-layout-canvas .handle.nw,.side-layout-canvas .handle.se{cursor:nwse-resize}.side-layout-canvas .handle.ne,.side-layout-canvas .handle.sw{cursor:nesw-resize}
  .side-layout-preview{display:grid;place-items:center;aspect-ratio:1;background:#fbfdfb;box-shadow:inset 0 0 0 1px #99adb4;font:13px system-ui;color:#5b6b67;text-align:center;padding:8px}
  .side-layout-preview img{width:100%;height:100%;display:block}
  .side-layout-readout{font:13px/1.5 system-ui;font-variant-numeric:tabular-nums;margin:10px 0 0}.side-layout-readout.bad{color:#b91c1c}
  .side-layout-hint{font:12px/1.5 system-ui;color:#5b6b67;margin:6px 0 0}.side-layout-error{font:13px system-ui;color:#b91c1c;margin:6px 0 0}
  .side-layout-save{background:#2f7d4a!important;border-color:#2f7d4a!important;color:#fff}
  @media(max-width:700px){.side-layout-stages{grid-template-columns:1fr}}`;document.head.append(style);

  const el=(name,attrs={})=>{const e=document.createElementNS(ns,name);for(const [k,v] of Object.entries(attrs))e.setAttribute(k,v);return e;};
  const html=(tag,cls,text)=>{const e=document.createElement(tag);if(cls)e.className=cls;if(text!=null)e.textContent=text;return e;};
  const fmt=n=>String(Math.round(n*100)/100);
  let dialog,ctx;

  // A group's placement: top-left (x, y) and longest axis `size`, from its own source box.
  const extent=g=>Math.max(g.src[2]-g.src[0],g.src[3]-g.src[1]);
  const scaleOf=g=>extent(g)>1e-9?g.size/extent(g):1;
  const boxOf=g=>{const k=scaleOf(g);return [g.x,g.y,g.x+(g.src[2]-g.src[0])*k,g.y+(g.src[3]-g.src[1])*k];};
  const unionOf=list=>list.map(boxOf).reduce((a,b)=>[Math.min(a[0],b[0]),Math.min(a[1],b[1]),Math.max(a[2],b[2]),Math.max(a[3],b[3])]);
  const selected=()=>ctx.sel?(ctx.sel.group==null?ctx.roles[ctx.sel.role].groups:[ctx.roles[ctx.sel.role].groups[ctx.sel.group]]):[];
  const outside=b=>b[0]-2<-1e-6||b[1]-2<-1e-6||b[2]+2>ctx.canvas+1e-6||b[3]+2>ctx.canvas+1e-6;

  function build(){
    dialog=html('dialog','side-layout');
    dialog.innerHTML=`<header><h2></h2><button type="button" data-close>Close</button></header>
      <div class="side-layout-bar"><span>Select</span><button type="button" data-level="whole">Whole icon</button><button type="button" data-level="element">Connected element</button><span class="spacer"></span>
      <button type="button" data-reset>Reset to automatic</button><button type="button" data-cancel>Discard changes</button><button type="button" class="side-layout-save" data-save>Save layout</button></div>
      <div class="side-layout-stages"><figure><svg class="side-layout-canvas" tabindex="0" role="application" aria-label="Layout editor, 64 by 64 grid"></svg>
      <figcaption>Editing view: main and sub drawn whole. Orange: main · blue: sub.</figcaption></figure>
      <figure><div class="side-layout-preview"></div><figcaption>Combined result (the sub erases the main where they meet).</figcaption></figure></div>
      <p class="side-layout-readout" role="status"></p>
      <p class="side-layout-hint">Click the main or sub to select it. Drag to move, drag a corner to resize. Arrow keys move 1 unit (Shift: 8), + and − resize by 1 unit. Everything snaps to the grid; the stroke stays 4.</p>
      <p class="side-layout-error" role="alert"></p>`;
    document.body.append(dialog);
    const q=s=>dialog.querySelector(s);
    q('[data-close]').onclick=()=>dialog.close();
    q('[data-cancel]').onclick=()=>load(ctx.pair,ctx.main,ctx.sub,ctx.onSaved,ctx.saved);
    q('[data-save]').onclick=save;q('[data-reset]').onclick=reset;
    for(const b of dialog.querySelectorAll('[data-level]'))b.onclick=()=>{ctx.level=b.dataset.level;if(ctx.sel)ctx.sel={role:ctx.sel.role,group:null};draw();};
    const svg=q('.side-layout-canvas');
    svg.addEventListener('pointerdown',down);svg.addEventListener('keydown',key);
  }

  async function combine(body){
    const r=await fetch('/api/combination-experiment',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
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
    ctx={pair,main,sub,onSaved,saved,canvas:64,roles:{},dirty:new Set(),sel:null,level:ctx?.level||'whole',busy:false,token:0};
    dialog.querySelector('.side-layout-canvas').replaceChildren();error('');readout('Loading connected elements…');preview(null,'Loading…');
    let data;
    try{data=await combine({id:pair.id,main:main.icon,sub:sub.icon,elements:true,...(saved?{layout:saved}:{})});}
    catch(e){
      if(!saved){readout('');error(e.message);return;}
      try{data=await combine({id:pair.id,main:main.icon,sub:sub.icon,elements:true});error('The saved layout no longer fits these drawings: '+e.message);}catch(e2){readout('');error(e2.message);return;}
    }
    if(ctx.pair!==pair)return;
    if(!data.elements){readout('');error(data.elements_error||'This pair cannot be adjusted.');preview(data);return;}
    ctx.canvas=data.canvas||64;
    for(const [role,c] of Object.entries(data.elements)){
      ctx.roles[role]={markup:c.markup,groups:c.groups.map(g=>{const b=g.box;return {paths:g.paths,src:g.source,x:b[0],y:b[1],size:Math.max(b[2]-b[0],b[3]-b[1])};})};
      if(saved?.[role])ctx.dirty.add(role);
    }
    preview(data);draw();
  }

  // The first edit of a role snaps every one of its groups onto the grid.
  function touch(role){
    if(ctx.dirty.has(role))return;ctx.dirty.add(role);
    for(const g of ctx.roles[role].groups){g.x=Math.round(g.x);g.y=Math.round(g.y);g.size=Math.round(g.size);}
  }
  function layout(){
    const out={};
    for(const role of ctx.dirty)out[role]=ctx.roles[role].groups.map(g=>({paths:g.paths,x:g.x,y:g.y,size:g.size}));
    return Object.keys(out).length?out:null;
  }

  function draw(){
    const svg=dialog.querySelector('.side-layout-canvas'),c=ctx.canvas;svg.setAttribute('viewBox',`-1 -1 ${c+2} ${c+2}`);svg.replaceChildren();
    for(const b of dialog.querySelectorAll('[data-level]'))b.setAttribute('aria-pressed',String(b.dataset.level===ctx.level));
    const grid=el('g',{'pointer-events':'none'});
    for(let i=0;i<=c;i++){const a={stroke:i%8===0?'#9eb3bd':'#dae4e9','stroke-width':i%8===0?.13:.055};grid.append(el('line',{x1:i,y1:0,x2:i,y2:c,...a}),el('line',{x1:0,y1:i,x2:c,y2:i,...a}));}
    svg.append(grid);
    for(const role of ['main','sub']){
      const r=ctx.roles[role];if(!r)continue;
      const layer=el('g',{fill:'none',stroke:'currentColor','stroke-linecap':'round','stroke-linejoin':'round'});
      r.groups.forEach((g,i)=>{
        const k=scaleOf(g),art=el('g',{class:'art','data-role':role,'data-group':i,'stroke-width':STROKE/k,
          transform:`translate(${g.x-g.src[0]*k} ${g.y-g.src[1]*k}) scale(${k})`});
        const parsed=new DOMParser().parseFromString(`<svg xmlns="${ns}">${g.paths.map(p=>r.markup[p]).join('')}</svg>`,'image/svg+xml').documentElement;
        for(const child of [...parsed.children])art.append(document.importNode(child,true));
        layer.append(art);
      });
      svg.append(layer);
    }
    const list=selected();
    if(list.length){
      const b=unionOf(list),bad=list.some(g=>outside(boxOf(g))),p=[b[0]-2,b[1]-2,b[2]+2,b[3]+2];
      svg.append(el('rect',{class:'move',x:p[0],y:p[1],width:p[2]-p[0],height:p[3]-p[1],'data-move':''}));
      svg.append(el('rect',{class:'sel '+ctx.sel.role+(bad?' out':''),x:p[0],y:p[1],width:p[2]-p[0],height:p[3]-p[1]}));
      for(const [name,x,y] of [['nw',p[0],p[1]],['ne',p[2],p[1]],['sw',p[0],p[3]],['se',p[2],p[3]]])
        svg.append(el('rect',{class:'handle '+name,'data-handle':name,x:x-HANDLE/2,y:y-HANDLE/2,width:HANDLE,height:HANDLE}));
    }
    status();
  }
  function status(){
    const bad=Object.values(ctx.roles).some(r=>r.groups.some(g=>outside(boxOf(g))));
    dialog.querySelector('[data-save]').disabled=ctx.busy||bad||!ctx.dirty.size;
    dialog.querySelector('[data-reset]').disabled=ctx.busy||!ctx.saved;
    const list=selected();
    if(!list.length){readout(bad?'Part of the artwork is outside the canvas.':'Select the main or the sub to adjust it.',bad);return;}
    const b=unionOf(list),name=ctx.sel.role==='main'?'Main':'Sub',what=ctx.sel.group==null?name:`${name} · element ${ctx.sel.group+1} of ${ctx.roles[ctx.sel.role].groups.length}`;
    readout(`${what}: painted ${fmt(b[2]-b[0]+4)}×${fmt(b[3]-b[1]+4)} at (${fmt(b[0]-2)}, ${fmt(b[1]-2)})`+(bad?' · outside the canvas':''),bad);
  }
  const readout=(text,bad)=>{const r=dialog.querySelector('.side-layout-readout');r.textContent=text;r.classList.toggle('bad',!!bad);};
  const error=text=>{dialog.querySelector('.side-layout-error').textContent=text;};
  function preview(result,text){
    const box=dialog.querySelector('.side-layout-preview');box.replaceChildren();
    if(!result){box.append(html('span','',text||''));return;}
    const img=html('img');img.alt='Combined result';img.src='data:image/svg+xml;charset=utf-8,'+encodeURIComponent(result.svg);box.append(img);
  }
  // Re-combine shortly after an edit so the erased result stays in step with the editor.
  let timer;
  function refresh(){
    clearTimeout(timer);draw();
    if(Object.values(ctx.roles).some(r=>r.groups.some(g=>outside(boxOf(g))))){preview(null,'Move the artwork back inside the canvas to preview.');return;}
    timer=setTimeout(async()=>{
      const token=++ctx.token,body={id:ctx.pair.id,main:ctx.main.icon,sub:ctx.sub.icon},l=layout();if(l)body.layout=l;
      try{const data=await combine(body);if(token===ctx.token){preview(data);error('');}}
      catch(e){if(token===ctx.token)error(e.message);}
    },350);
  }

  // Pointer: move the selection, or resize it from a corner with the opposite corner pinned.
  const point=(svg,e)=>{const p=new DOMPoint(e.clientX,e.clientY).matrixTransform(svg.getScreenCTM().inverse());return [p.x,p.y];};
  function down(e){
    const svg=e.currentTarget;let target=e.target,art=target.closest('.art');
    // Artwork under the selection frame (the arrow inside a selected monitor) can still be picked.
    if(target.hasAttribute('data-move')){
      const under=document.elementsFromPoint(e.clientX,e.clientY).map(n=>n.closest?.('.art')).find(Boolean);
      const inside=under&&under.dataset.role===ctx.sel.role&&(ctx.sel.group==null||Number(under.dataset.group)===ctx.sel.group);
      if(under&&!inside){target=under;art=under;}
    }
    if(!target.hasAttribute('data-handle')&&!target.hasAttribute('data-move')){
      if(!art){ctx.sel=null;draw();return;}
      const role=art.dataset.role;ctx.sel={role,group:ctx.level==='element'?Number(art.dataset.group):null};
    }
    if(!ctx.sel)return;
    svg.focus();touch(ctx.sel.role);
    const list=selected(),start=point(svg,e),before=list.map(g=>({...g})),box=unionOf(list),corner=target.dataset.handle;
    draw();svg.setPointerCapture(e.pointerId);e.preventDefault();
    let moved=false;
    const move=ev=>{
      const [px,py]=point(svg,ev);moved=true;
      if(!corner){
        const dx=Math.round(px-start[0]),dy=Math.round(py-start[1]);
        list.forEach((g,i)=>{g.x=before[i].x+dx;g.y=before[i].y+dy;});
      }else{
        const pinX=corner.includes('w')?box[2]:box[0],pinY=corner.includes('n')?box[3]:box[1];
        const w=box[2]-box[0],h=box[3]-box[1],longest=Math.max(w,h);if(longest<1e-9)return;
        const votes=[];if(w>1e-9)votes.push(Math.abs(px-pinX)/w);if(h>1e-9)votes.push(Math.abs(py-pinY)/h);
        const f=Math.max(1,Math.round(longest*Math.max(...votes)))/longest;
        scale(list,before,f,pinX,pinY);
      }
      draw();
    };
    const up=()=>{svg.removeEventListener('pointermove',move);svg.removeEventListener('pointerup',up);svg.removeEventListener('pointercancel',up);if(moved)refresh();};
    svg.addEventListener('pointermove',move);svg.addEventListener('pointerup',up);svg.addEventListener('pointercancel',up);
  }
  // Scale every group about the pinned point, then snap each one's position and size.
  function scale(list,before,f,pinX,pinY){
    list.forEach((g,i)=>{
      const b=before[i];
      if(list.length===1){
        const w=(b.src[2]-b.src[0])*scaleOf(b),h=(b.src[3]-b.src[1])*scaleOf(b);
        g.size=Math.max(1,Math.round(b.size*f));const k=g.size/b.size;
        // Keep the pinned edges where they were.
        g.x=Math.round(pinX>b.x+1e-9?pinX-w*k:b.x);g.y=Math.round(pinY>b.y+1e-9?pinY-h*k:b.y);
      }else{
        g.size=Math.max(1,Math.round(b.size*f));
        g.x=Math.round(pinX+(b.x-pinX)*f);g.y=Math.round(pinY+(b.y-pinY)*f);
      }
    });
  }
  function key(e){
    if(!ctx.sel)return;
    const list=selected(),steps={ArrowLeft:[-1,0],ArrowRight:[1,0],ArrowUp:[0,-1],ArrowDown:[0,1]};
    if(steps[e.key]){
      e.preventDefault();touch(ctx.sel.role);const n=e.shiftKey?8:1;
      for(const g of list){g.x+=steps[e.key][0]*n;g.y+=steps[e.key][1]*n;}refresh();
    }else if(['+','=','-','_'].includes(e.key)){
      e.preventDefault();touch(ctx.sel.role);
      const box=unionOf(list),longest=Math.max(box[2]-box[0],box[3]-box[1]),grow=['+','='].includes(e.key)?1:-1;
      if(longest<1e-9||longest+grow<1)return;
      scale(list,list.map(g=>({...g})),(longest+grow)/longest,box[0],box[1]);refresh();
    }else if(e.key==='Escape'&&ctx.sel){ctx.sel=null;draw();e.preventDefault();}
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
    try{const data=await post({pair_id:ctx.pair.id,main:ctx.main.icon,sub:ctx.sub.icon,layout:l});ctx.saved=data.layout.layout;preview(data.result);readout('Layout saved. The combined icon is republished.');}
    catch(e){error(e.message);}
  }
  async function reset(){
    try{const data=await post({pair_id:ctx.pair.id,layout:null});load(ctx.pair,ctx.main,ctx.sub,ctx.onSaved,null);preview(data.result);}
    catch(e){error(e.message);}
  }

  function button(pair,main,sub,onSaved,saved){
    const b=html('button','side-layout-open','Adjust layout');b.type='button';b.setAttribute('data-development-only','');
    b.title='Move and resize the main, the sub or one connected element, snapped to the grid';
    b.onclick=()=>open(pair,main,sub,onSaved,saved);return b;
  }
  window.SideLayoutEditor={open,button};
})();

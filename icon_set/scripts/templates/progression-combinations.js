/* Combination views share the progression page's navigation and URL state. */
let combinationCatalog=null, combinationLoading=false, combinationError='';
let containerResults=null, containerResultError='', containerResultsLoading=false, combineRunning=false, combineProgress='';
const containerPreviews=new Map(), expandedContainers=new Set();
// Symbol centers: published defaults (container-centers.json) under edits saved on the cloud.
let containerCenters=null, containerCentersLoading=false, savedCenters={containers:{},pairs:{}}, savedCentersError='';
const centerViews=new Map(); // container icon id → refresh callbacks of the cards and headings showing it
async function loadContainerCenters(){
  containerCentersLoading=true;
  const empty={containers:{},pairs:{}};
  const [,,defaults,saved]=await Promise.all([loadArtworkOverrides(),loadReferenceUploads(),
    fetch('container-centers.json',{cache:'no-store'}).then(r=>r.ok?r.json():empty).catch(()=>empty),
    fetch('/api/container-centers',{cache:'no-store'}).then(r=>r.ok?r.json():Promise.reject(Error('Saved centers are unavailable.'))).catch(error=>{savedCentersError=error.message;return null;})]);
  containerCenters=defaults;if(saved)savedCenters=saved;containerCentersLoading=false;
  if(state.view==='container')renderCombinations();
}
// A saved symbol size is its painted ink box [width, height] (even, so its edges sit on the grid);
// null keeps the symbol's natural size in the standard 32 × 32 box.
const boxSize=v=>Array.isArray(v)&&v.length===2?v.map(Number):null;
const sizeText=v=>v?`ink ${v[0]} × ${v[1]}`:'natural size';
function effectiveCenter(main,sub){
  const pair=savedCenters.pairs[main]?.[sub], own=savedCenters.containers[main], d=containerCenters?.containers[main];
  if(pair)return {center:pair.center,size:boxSize(pair.size),label:'Saved · this pair',scope:'pair',by:pair.user};
  if(own)return {center:own.center,size:boxSize(own.size),label:'Saved · this container',scope:'container',by:own.user};
  const optical=containerCenters?.pairs[main]?.[sub];
  if(optical)return {center:optical,size:null,label:'Default · pair override',scope:'pair'};
  if(d)return {center:d.center,size:null,label:'Default · '+({preference:'placement preference',area:'reviewed content area',anchor:'container anchor'}[d.source]||d.source),scope:'container',stale:d.stale};
  return {center:[32,32],size:null,label:'Default · canvas center',scope:'container'};
}
// Combined previews open in the side view's inspect popup (SideCombinationPopup):
// the container and its symbol are inlined as the popup's main and sub groups.
async function svgSource(url){const r=await fetch(url,{cache:'no-cache'});if(!r.ok)throw Error('Artwork could not be loaded');const svg=new DOMParser().parseFromString(await r.text(),'image/svg+xml').documentElement;if(svg.tagName!=='svg')throw Error('Artwork is not an SVG');return svg;}
// Fits an SVG's viewBox into a size×size box the way <img> and <image> do (preserveAspectRatio meet,
// centered), so uploads with a non-square or off-canvas viewBox land where the thumbnails show them.
// Icon ink is always shown black, whatever color an uploaded SVG was drawn in (guides keep their colors;
// white knockout fills stay white). <image> drawings are blackened with a filter.
{const style=document.createElement('style');const ink='.ink-black:not([data-sub-centerline]):not([data-main-centerline])';
  style.textContent=`${ink}:not([stroke=none])[stroke],${ink} [stroke]:not([stroke=none]){stroke:#000}${ink}[fill]:not([fill=none]):not([fill=white]):not([fill="#fff"]):not([fill="#ffffff"]):not([fill="#FFF"]):not([fill="#FFFFFF"]),${ink} [fill]:not([fill=none]):not([fill=white]):not([fill="#fff"]):not([fill="#ffffff"]):not([fill="#FFF"]):not([fill="#FFFFFF"]){fill:#000}image.ink-black,img.ink-black{filter:brightness(0)}`;
  document.head.append(style);}
function svgFit(source,size){
  const vb=(source.getAttribute('viewBox')||'').trim().split(/[\s,]+/).map(Number);
  const [vx,vy,vw,vh]=vb.length===4&&vb.every(Number.isFinite)&&vb[2]>0&&vb[3]>0?vb:[0,0,+source.getAttribute('width')||size,+source.getAttribute('height')||size];
  const k=Math.min(size/vw,size/vh);return {k,tx:(size-vw*k)/2-vx*k,ty:(size-vh*k)/2-vy*k};
}
function placeGroup(source,id,size,x,y){
  const {k,tx,ty}=svgFit(source,size);
  const g=svgNode('g',{id,class:'ink-black',transform:`translate(${x+tx} ${y+ty}) scale(${k})`});
  for(const name of ['fill','stroke','stroke-width','stroke-linecap','stroke-linejoin'])if(source.getAttribute(name))g.setAttribute(name,source.getAttribute(name));
  for(const child of [...source.children])if(!['title','desc'].includes(child.tagName))g.append(document.importNode(child,true));
  return g;
}
// Stroke width set on the root or, for uploads, on the paths themselves.
function inkStroke(g){return +g.getAttribute('stroke-width')||+g.querySelector('[stroke-width]')?.getAttribute('stroke-width')||4;}
// Where a symbol is drawn around `center`, exactly as container_combination_render.py bakes it. With an ink size
// [W, H] its painted ink box is W × H; with none it keeps its natural size (its viewBox fitted to the standard
// 32 × 32 box), snapped the same way: ink edges on grid lines and even ink sizes. The drawing stretches, the
// stroke does not. A drawing with no extent on an axis (a straight line) stays a line there.
function symbolPlacement(group,fit,stroke,center,ink){
  const b=group.getBBox(),half=stroke/2;
  const axis=(start,extent,c,size,x0)=>{
    const natural=x0+start*fit.k;
    if(extent<=1e-6)return {x:Math.round(natural),w:0};
    if(!size)return {x:Math.round(natural),w:Math.max(2,2*Math.round(extent*fit.k/2))};
    return {x:c-size/2+half,w:size-stroke};
  };
  const X=axis(b.x,b.width,center[0],ink?.[0],center[0]-16+fit.tx),Y=axis(b.y,b.height,center[1],ink?.[1],center[1]-16+fit.ty);
  let kx=b.width>1e-6?X.w/b.width:null,ky=b.height>1e-6?Y.w/b.height:null;kx??=ky??fit.k;ky??=kx;
  return {transform:`translate(${X.x-b.x*kx} ${Y.x-b.y*ky}) scale(${kx} ${ky})`,box:{x:X.x-half,y:Y.x-half,w:X.w+stroke,h:Y.w+stroke},local:b};
}
// Non-scaling strokes are drawn in screen pixels, so they are redrawn whenever the canvas is resized.
function fixedStroke(group,canvas,units){
  const r=canvas.getBoundingClientRect(),vb=canvas.viewBox.baseVal,px=r.width&&vb?.width?r.width/vb.width:0;if(!px)return;
  for(const e of group.querySelectorAll('path,line,polyline,polygon,circle,ellipse,rect')){e.setAttribute('vector-effect','non-scaling-stroke');e.setAttribute('stroke-width',units*px);}
}
function paintedBox(g){const b=g.getBBox(),k=Number((g.getAttribute('transform')||'').match(/scale\(([-+.\deE]+)/)?.[1]||1),m=(g.getAttribute('transform')||'').match(/translate\(([-+.\deE]+) ([-+.\deE]+)/),tx=+(m?.[1]||0),ty=+(m?.[2]||0),r=inkStroke(g)*k/2;
  return {x:tx+b.x*k-r,y:ty+b.y*k-r,w:b.width*k+2*r,h:b.height*k+2*r};}
function measuredResult(svg,roles,filename){
  svg.setAttribute('style','position:absolute;left:-9999px;width:64px;height:64px');document.body.append(svg);
  const placements=roles.map(([role,id,icon])=>{const g=svg.querySelector('[id="'+id+'"]');return g?{role,icon,painted_box:paintedBox(g)}:null;}).filter(Boolean);
  svg.remove();svg.removeAttribute('style');return {svg:new XMLSerializer().serializeToString(svg),canvas:64,placements,filename};
}
async function openContainerCombination(label,mainUrl,subUrl,center,ids={},size=null){
  const [main,sub]=await Promise.all([svgSource(mainUrl),svgSource(subUrl)]);
  const svg=svgNode('svg',{xmlns:'http://www.w3.org/2000/svg',viewBox:'0 0 64 64',width:64,height:64});
  svg.append(placeGroup(main,'main-icon-clipped',64,0,0),placeGroup(sub,'state-icon',32,center[0]-16,center[1]-16));
  const result=measuredResult(svg,[['main','main-icon-clipped',ids.main],['sub','state-icon',ids.sub]],(label.replace(/[^\w.-]+/g,'_')||'combination')+'.svg');
  window.SideCombinationPopup.open(label,result);
  if(ids.main&&ids.sub)symbolCenterEditor(ids.main,ids.sub,center,size,svgFit(sub,32),result,ids.onSaved,{row:ids.row,subUrl});
}
// In the combined popup: select the symbol, drag it to move it, or drag a handle to resize it. Width and
// height are independent (Shift keeps the proportions); the side opposite the handle stays put. The ink box
// snaps to even sizes around a whole center, so its edges always sit on grid lines; the stroke keeps its width.
// Arrow keys move, Alt+arrows resize, + / − both sides. Changes show at once and are only stored when Save
// is pressed; the container never changes.
// "Click selects: Element" (like the side layout editor) picks one element of the symbol — a letter of a
// typeface text — with its own box: drag it to move, drag a handle to resize it (width and height apart,
// Shift keeps proportions). While elements are edited the symbol's placement is frozen, so the others never
// shift or rescale. Saving writes the edits into this pair's own symbol drawing (uploaded against the
// combination id) and combines it at exactly the size shown.
function symbolCenterEditor(main,sub,start,startSize,fit,result,onSaved,extra={}){
  const dialog=[...document.querySelectorAll('dialog.side-inspect[open]')].find(d=>d.querySelector('.side-stage'));if(!dialog)return;
  const canvas=dialog.querySelector('.side-stage svg'),group=canvas.querySelector('[id="state-icon"]');if(!group)return;
  if(!document.getElementById('symbol-center-style')){const style=document.createElement('style');style.id='symbol-center-style';style.textContent=`.symbol-center-controls{display:grid;gap:10px;margin:14px 0 4px;padding:14px;border:1px solid #c9d4cf;border-radius:10px;background:#f7faf8}.symbol-center-controls h3{margin:0;font:600 15px system-ui}.symbol-center-row{display:flex;gap:8px;align-items:center;flex-wrap:wrap;font:14px system-ui}.symbol-center-row input{width:64px;padding:6px;border:1px solid #9bafb5;border-radius:6px;font:inherit}.symbol-center-row select{padding:7px;border:1px solid #9bafb5;border-radius:6px;font:inherit}.symbol-center-row button.primary{background:#287650!important;border-color:#287650!important;color:#fff}.symbol-center-row button:disabled{opacity:.5;cursor:default}.symbol-center-status{margin:0!important;font-size:13px!important;color:#43564f}.symbol-center-status[data-dirty=true]{color:#8a4b12}.symbol-hit{fill:transparent;pointer-events:all;cursor:grab}.symbol-hit:hover,.side-canvas[data-selected=sub] .symbol-hit{fill:#146dc514;stroke:#146dc5;stroke-width:.35;stroke-dasharray:1 .6}.side-canvas[data-dragging=true] .symbol-hit{cursor:grabbing}.symbol-handle{display:none;fill:#fff;stroke:#146dc5;stroke-width:.3;pointer-events:all}.side-canvas[data-selected=sub] .symbol-handle{display:block}.symbol-handle.nw,.symbol-handle.se{cursor:nwse-resize}.symbol-handle.ne,.symbol-handle.sw{cursor:nesw-resize}.symbol-handle.n,.symbol-handle.s{cursor:ns-resize}.symbol-handle.e,.symbol-handle.w{cursor:ew-resize}.symbol-size-label{display:none;font:600 1.7px system-ui;fill:#146dc5;paint-order:stroke;stroke:#fff;stroke-width:.5;pointer-events:none}.side-canvas[data-selected=sub] .symbol-size-label,.side-canvas[data-dragging=true] .symbol-size-label{display:block}
.symbol-mode button[aria-pressed=true]{background:#e4f2e6;border-color:#2f7d4a}.symbol-element-hit{display:none;fill:transparent;pointer-events:all;cursor:grab}.side-canvas[data-symbol-mode=element] .symbol-element-hit{display:block}.side-canvas[data-symbol-mode=element] .symbol-element-hit:hover{stroke:#2f7d4a;stroke-width:.25;stroke-dasharray:.8 .6}.side-canvas[data-symbol-mode=element] .symbol-element-hit.picked{fill:#2f7d4a14;stroke:#2f7d4a;stroke-width:.35;stroke-dasharray:1 .6}.side-canvas[data-symbol-mode=element] .symbol-hit,.side-canvas[data-symbol-mode=element] .symbol-handle,.side-canvas[data-symbol-mode=element] .side-bound-sub,.side-canvas[data-symbol-mode=element] .symbol-size-label{display:none!important}.symbol-element-handle{display:none;fill:#fff;stroke:#2f7d4a;stroke-width:.3;pointer-events:all}.side-canvas[data-symbol-mode=element][data-element-picked=true] .symbol-element-handle{display:block}.symbol-element-handle.nw,.symbol-element-handle.se{cursor:nwse-resize}.symbol-element-handle.ne,.symbol-element-handle.sw{cursor:nesw-resize}.symbol-element-handle.n,.symbol-element-handle.s{cursor:ns-resize}.symbol-element-handle.e,.symbol-element-handle.w{cursor:ew-resize}
.side-inspect.with-symbol-editor{width:min(1180px,96vw);max-height:96vh;overflow:auto;margin-top:2vh;margin-bottom:auto}.symbol-center-controls p[role=status]{min-height:3.2em}.side-inspect.with-symbol-editor .side-dimensions{min-height:2.8em}.side-inspect.with-symbol-editor[open]{display:grid;grid-template-columns:minmax(0,auto) minmax(320px,1fr);column-gap:28px;align-content:start}.side-inspect.with-symbol-editor>*{grid-column:2;min-width:0}.side-inspect.with-symbol-editor>header{grid-column:1/-1}.side-inspect.with-symbol-editor>.side-stage{grid-column:1;grid-row:2/span 8;width:min(640px,calc(96vh - 110px),58vw);margin:16px 0 0}.side-inspect.with-symbol-editor .symbol-center-controls{margin-top:4px}
@media(max-width:800px){.side-inspect.with-symbol-editor[open]{display:block}.side-inspect.with-symbol-editor>.side-stage{width:100%;margin:16px auto}}`;document.head.append(style);}
  // The combined icon keeps every stroke at 4, whatever the source drew (container_combination_render.py).
  const saved=effectiveCenter(main,sub),stroke=4;
  const clampC=v=>Math.min(64,Math.max(0,Math.round(v))),even=v=>2*Math.round(v/2),clampS=v=>Math.min(64,Math.max(8,even(v)));
  // Opened as saved: a symbol placed element by element can have an odd size and a half-unit centre.
  let center=start.map(v=>Math.min(64,Math.max(0,Math.round(v*2)/2))),ink=startSize?startSize.map(v=>Math.min(64,Math.max(4,Math.round(v)))):null,base={center:[...center],ink:ink&&[...ink]};
  const trace=canvas.querySelector('[data-sub-centerline]'),bound=canvas.querySelector('.side-bound-sub');
  // Elements of the symbol: its drawn children (title / desc / defs skipped first), looking through single wrapping
  // groups (a typeface text: its letters). The same walk finds them in the popup, its centerline copy and the saved
  // drawing, so element i is the same element everywhere.
  const drawn=list=>list.filter(n=>!['title','desc','defs','style','metadata'].includes(n.tagName));
  const elementsOf=root=>{let list=drawn([...root.children]);while(list.length===1&&list[0].tagName==='g')list=drawn([...list[0].children]);return list;};
  const elementNodes=elementsOf(group);
  // The red centerline overlay is its own copy of the symbol: its elements move with the drawing's.
  const traceNodes=trace?elementsOf(trace):[];
  const elements=extra.row?elementNodes.map((n,i)=>({node:n,base:n.getAttribute('transform')||'',trace:traceNodes[i]||null,traceBase:traceNodes[i]?.getAttribute('transform')||'',box0:null,box:null})):[];
  // An element's box in the symbol's own units (its drawing, stroke excluded), measured before its first change.
  function measure(e){
    if(e.box0)return;const b=e.node.getBBox(),m=e.node.transform.baseVal.consolidate()?.matrix;
    const pts=[[b.x,b.y],[b.x+b.width,b.y+b.height]].map(([px,py])=>m?[m.a*px+m.c*py+m.e,m.b*px+m.d*py+m.f]:[px,py]);
    e.box0={x:Math.min(pts[0][0],pts[1][0]),y:Math.min(pts[0][1],pts[1][1]),w:Math.abs(pts[1][0]-pts[0][0]),h:Math.abs(pts[1][1]-pts[0][1])};e.box={...e.box0};
    // Wrapping groups between the symbol group and the element (a 32-box text is wrapped in a centring translate):
    // their scale and offset, so element boxes (in the element's parent units) map onto the canvas exactly.
    const w=group.getCTM().inverse().multiply(e.node.parentNode.getCTM());e.wrap={a:w.a,d:w.d,e:w.e,f:w.f};
  }
  const changedEl=e=>!!e.box&&['x','y','w','h'].some(k=>Math.abs(e.box[k]-e.box0[k])>1e-9);
  // The element drawn into its box: translate + scale written before its own transform (the combine flattens both).
  const elementTransform=e=>{if(!changedEl(e))return '';const b0=e.box0,b=e.box,sx=b0.w>1e-9?b.w/b0.w:1,sy=b0.h>1e-9?b.h/b0.h:1;
    return `translate(${+b.x.toFixed(4)} ${+b.y.toFixed(4)}) scale(${+sx.toFixed(6)} ${+sy.toFixed(6)}) translate(${+(-b0.x).toFixed(4)} ${+(-b0.y).toFixed(4)})`;};
  const placeElement=e=>{const pre=elementTransform(e);for(const [n,b] of [[e.node,e.base],[e.trace,e.traceBase]]){if(!n)continue;const t=(pre+' '+b).trim();if(t)n.setAttribute('transform',t);else n.removeAttribute('transform');}};
  let mode='whole',picked=-1,text=null;
  if(extra.row)window.ContainerTextSymbol?.pairText(extra.row).then(t=>{text=t;draw();});
  // A typeface text moves its letters only (its underline follows the text).
  const movable=e=>!text||e.node.tagName==='g';
  const elementHits=elements.map((e,i)=>{const r=svgNode('rect',{class:'symbol-element-hit','aria-hidden':'true'});canvas.append(r);return r;});
  const elementHandles=['nw','n','ne','e','se','s','sw','w'].map(name=>svgNode('rect',{class:'symbol-element-handle '+name,'data-corner':name,width:1.6,height:1.6}));
  const moved=()=>elements.filter(changedEl).length;
  // Element mode keeps the symbol exactly as shown (same size and place) and drops the group box: only the
  // elements that are moved or resized change, and they snap to the 64 grid. {transform, t: [tx, ty], k: [kx, ky]}.
  let frozen=null;
  const freeze=()=>{if(frozen)return;const m=(group.getAttribute('transform')||'').match(/translate\(([-+.\deE]+) ([-+.\deE]+)\) scale\(([-+.\deE]+) ([-+.\deE]+)\)/);
    frozen=m?{transform:m[0],t:[+m[1],+m[2]],k:[+m[3],+m[4]]}:{transform:'',t:[0,0],k:[1,1]};};
  const panel=node('section','symbol-center-controls');
  const x=node('input'),y=node('input'),wi=node('input'),he=node('input');
  for(const [input,name,min,step] of [[x,'x',0,1],[y,'y',0,1],[wi,'ink width',8,2],[he,'ink height',8,2]]){input.type='number';input.min=min;input.max=64;input.step=step;input.setAttribute('aria-label','Symbol '+name);}
  const nudge=node('span','symbol-center-row');
  for(const [label,dx,dy] of [['←',-1,0],['↑',0,-1],['↓',0,1],['→',1,0]]){const b=node('button','',label);b.type='button';b.title='Move 1 unit';b.onclick=()=>set([center[0]+dx,center[1]+dy],ink);nudge.append(b);}
  const smaller=node('button','','−'),larger=node('button','','+'),natural=node('button','','Natural size');for(const b of [smaller,larger,natural])b.type='button';
  smaller.title='Both sides smaller by 2';larger.title='Both sides larger by 2';natural.title='Back to the drawing’s own size in the standard 32 × 32 box';
  const inkNow=()=>ink||(()=>{const b=place().box;return [clampS(b.w),clampS(b.h)];})();
  smaller.onclick=()=>{const i=inkNow();set(center,[i[0]-2,i[1]-2]);};larger.onclick=()=>{const i=inkNow();set(center,[i[0]+2,i[1]+2]);};natural.onclick=()=>set(center,null);
  const scope=node('select');scope.setAttribute('aria-label','Apply to');scope.append(new Option('This container · all symbols','container'),new Option('This pair only','pair'));scope.value=saved.scope;
  const save=node('button','primary','Save'),revert=node('button','','Undo changes'),reset=node('button','','Reset to default');for(const b of [save,revert,reset])b.type='button';
  const status=node('p','symbol-center-status');status.setAttribute('role','status');
  const row1=node('div','symbol-center-row'),row2=node('div','symbol-center-row'),row3=node('div','symbol-center-row');
  row1.append('x',x,'y',y,nudge);row2.append('ink w',wi,'h',he,smaller,larger,natural);row3.append(scope,save,revert,reset);
  const modeRow=node('div','symbol-center-row symbol-mode'),wholeB=node('button','','Whole symbol'),elementB=node('button','','Element');
  wholeB.type=elementB.type='button';modeRow.append('Click selects',wholeB,elementB);modeRow.hidden=!elements.length;
  wholeB.onclick=()=>{mode='whole';picked=-1;draw();};elementB.onclick=()=>{mode='element';freeze();delete canvas.dataset.selected;draw();};
  panel.append(node('h3','','Symbol position and size'),modeRow,node('p','symbol-center-status','Element: the symbol stays as shown, with no group box. Click a letter or part of the symbol; drag it to move, drag a handle to resize it (hold Shift to keep proportions). Sizes are even and edges sit on grid lines. Arrow keys move 1 (Shift: 4), Alt+arrows resize by 2. The other elements stay where they are; saving gives this pair its own symbol drawing. Whole symbol: click the symbol to select it. Drag it to move; drag a side or corner handle to resize — width and height change independently (hold Shift to keep proportions). The ink box snaps to even sizes and whole grid units, so its edges sit on grid lines. Arrow keys move 1 (Shift: 4), Alt+arrows resize by 2, + / − both sides. Nothing is stored until you press Save.'),row1,row2,row3,status);
  dialog.querySelector('.side-dimensions').after(panel);
  const hit=svgNode('rect',{class:'symbol-hit','aria-hidden':'true'});canvas.append(hit);canvas.append(...elementHits,...elementHandles);
  const handles=['nw','n','ne','e','se','s','sw','w'].map(name=>{const h=svgNode('rect',{class:'symbol-handle '+name,'data-corner':name,width:1.6,height:1.6});canvas.append(h);return h;});
  // Live size on the selection frame: the painted ink box and where it starts.
  const label=svgNode('text',{class:'symbol-size-label'});canvas.append(label);
  canvas.tabIndex=0;
  const same=(a,b)=>a===b||(!!a&&!!b&&a[0]===b[0]&&a[1]===b[1]),dirty=()=>!same(center,base.center)||!same(ink,base.ink)||moved()>0;
  const place=()=>{
    if(!frozen)return symbolPlacement(group,fit,stroke,center,ink);
    const b=group.getBBox(),[kx,ky]=frozen.k,[tx,ty]=frozen.t;
    return {transform:frozen.transform,box:{x:tx+kx*b.x-stroke/2,y:ty+ky*b.y-stroke/2,w:kx*b.width+stroke,h:ky*b.height+stroke}};
  };
  function strokes(){fixedStroke(group,canvas,stroke);if(trace)fixedStroke(trace,canvas,.45);}
  function draw(){
    const p=place(),b=p.box;group.setAttribute('transform',p.transform);trace?.setAttribute('transform',p.transform);strokes();
    for(const r of [bound,hit])if(r){r.setAttribute('x',b.x);r.setAttribute('y',b.y);r.setAttribute('width',b.w);r.setAttribute('height',b.h);}
    const f=v=>String(+v.toFixed(2));label.textContent=`ink ${f(b.w)}×${f(b.h)} · at ${f(b.x)},${f(b.y)}${ink?'':' · natural'}`;
    label.setAttribute('x',Math.max(.5,Math.min(b.x,64-label.textContent.length*.95)));label.setAttribute('y',b.y>3.5?b.y-1.2:b.y+b.h+2.6);
    for(const h of handles){const c=h.dataset.corner,hx=c.includes('w')?b.x:c.includes('e')?b.x+b.w:b.x+b.w/2,hy=c.includes('n')?b.y:c.includes('s')?b.y+b.h:b.y+b.h/2;h.setAttribute('x',hx-.8);h.setAttribute('y',hy-.8);}
    const dims=dialog.querySelector('.side-dimensions');dims.textContent=dims.textContent.replace(/sub: .*$/,`sub: ${f(b.w)} × ${f(b.h)} at (${f(b.x)}, ${f(b.y)})`);
    for(const [input,value] of [[x,center[0]],[y,center[1]],[wi,ink?.[0]??''],[he,ink?.[1]??'']])if(document.activeElement!==input)input.value=value;
    wi.placeholder=f(b.w);he.placeholder=f(b.h);
    canvas.dataset.symbolMode=mode;wholeB.setAttribute('aria-pressed',String(mode==='whole'));elementB.setAttribute('aria-pressed',String(mode==='element'));
    if(mode==='element'){const inv=canvas.getScreenCTM()?.inverse();
      elements.forEach((e,i)=>{const r=e.node.getBoundingClientRect(),h=elementHits[i];if(!inv||!movable(e)||!r.width&&!r.height){h.setAttribute('width',0);h.setAttribute('height',0);return;}
        const a=new DOMPoint(r.left,r.top).matrixTransform(inv),z=new DOMPoint(r.right,r.bottom).matrixTransform(inv);
        h.setAttribute('x',a.x-2);h.setAttribute('y',a.y-2);h.setAttribute('width',z.x-a.x+4);h.setAttribute('height',z.y-a.y+4);h.classList.toggle('picked',i===picked);});
      const ph=elementHits[picked];canvas.dataset.elementPicked=String(picked>=0);
      if(ph){const bx=+ph.getAttribute('x'),by=+ph.getAttribute('y'),bw=+ph.getAttribute('width'),bh=+ph.getAttribute('height');
        for(const h of elementHandles){const c=h.dataset.corner,hx=c.includes('w')?bx:c.includes('e')?bx+bw:bx+bw/2,hy=c.includes('n')?by:c.includes('s')?by+bh:by+bh/2;h.setAttribute('x',hx-.8);h.setAttribute('y',hy-.8);}}}
    else canvas.dataset.elementPicked='false';
    const d=dirty(),now=effectiveCenter(main,sub),n=moved();status.dataset.dirty=String(d);
    status.textContent=(d?`Unsaved · center ${center[0]}, ${center[1]} · ${sizeText(ink)} (was ${base.center[0]}, ${base.center[1]} · ${sizeText(base.ink)})`:`Center ${center[0]}, ${center[1]} · ${sizeText(ink)} · ${now.label}`)
      +(n?` · ${n} element${n===1?'':'s'} edited`:'')+(mode==='element'&&picked>=0&&elements[picked].box&&frozen?(()=>{const [l,t,r,btm]=paintedOf(elements[picked].box,elements[picked]);return ` · element ${picked+1}: ink ${f(r-l)} × ${f(btm-t)} at ${f(l)}, ${f(t)}`;})():'');
    save.disabled=!d&&scope.value===now.scope;revert.disabled=!d;
  }
  function set(nextCenter,nextInk){frozen=null;center=nextCenter.map(clampC);ink=nextInk?nextInk.map(clampS):null;draw();}
  // Change element i's box (symbol units); the frozen placement keeps every other element where it is.
  // Snapping happens in canvas units (the 64 grid), whatever scale the symbol is drawn at.
  function setElement(i,box){const e=elements[i];freeze();measure(e);const r=v=>+v.toFixed(4);
    e.box={x:r(box.x),y:r(box.y),w:r(e.box0.w<=1e-9?0:Math.max(1/frozen.k[0],box.w)),h:r(e.box0.h<=1e-9?0:Math.max(1/frozen.k[1],box.h))};placeElement(e);draw();}
  const toLocal=p=>[(p.x-frozen.t[0])/frozen.k[0],(p.y-frozen.t[1])/frozen.k[1]];
  // The element's painted box on the canvas (stroke included) and back: [left, top, right, bottom].
  const half=stroke/2;
  const paintedOf=(b,el)=>{const w=el.wrap,[kx,ky]=frozen.k,[tx,ty]=frozen.t,X=v=>tx+kx*(w.a*v+w.e),Y=v=>ty+ky*(w.d*v+w.f);
    return [X(b.x)-half,Y(b.y)-half,X(b.x+b.w)+half,Y(b.y+b.h)+half];};
  // Even painted sizes, at least stroke + 2, so both edges sit on grid lines.
  const evenSize=v=>Math.max(stroke+2,2*Math.round(v/2));
  const boxOfPainted=([l,t,r,btm],el)=>{const w=el.wrap,[kx,ky]=frozen.k,[tx,ty]=frozen.t;return {x:((l+half-tx)/kx-w.e)/w.a,y:((t+half-ty)/ky-w.f)/w.d,w:(r-l-stroke)/kx/w.a,h:(btm-t-stroke)/ky/w.d};};

  x.oninput=y.oninput=()=>{if(x.value!==''&&y.value!=='')set([+x.value,+y.value],ink);};
  wi.oninput=he.oninput=()=>{const i=inkNow();set(center,[wi.value!==''?+wi.value:i[0],he.value!==''?+he.value:i[1]]);};
  for(const input of [x,y,wi,he])input.onblur=draw;scope.onchange=draw;
  new ResizeObserver(strokes).observe(canvas);
  const toCanvas=e=>{const p=canvas.createSVGPoint();p.x=e.clientX;p.y=e.clientY;return p.matrixTransform(canvas.getScreenCTM().inverse());};
  const select=()=>{canvas.dataset.selected='sub';canvas.dataset.active='sub';canvas.focus();};
  let drag=null;
  elementHits.forEach((h,i)=>{
    h.addEventListener('pointerdown',e=>{e.preventDefault();e.stopPropagation();freeze();measure(elements[i]);picked=i;
      // Measured in screen pixels from the press, so a scroll of the popup never counts as a move.
      drag={mode:'el-move',i,client:[e.clientX,e.clientY],box:{...elements[i].box}};canvas.focus({preventScroll:true});canvas.dataset.dragging='true';h.setPointerCapture(e.pointerId);draw();});
    h.addEventListener('pointermove',e=>{if(drag?.mode!=='el-move'||drag.i!==i)return;
      const px=canvas.getBoundingClientRect().width/64,[l,t,r,btm]=paintedOf(drag.box,elements[i]);
      const L=Math.round(l+(e.clientX-drag.client[0])/px),T=Math.round(t+(e.clientY-drag.client[1])/px);
      setElement(i,boxOfPainted([L,T,L+evenSize(r-l),T+evenSize(btm-t)],elements[i]));});
    for(const t of ['pointerup','pointercancel'])h.addEventListener(t,()=>{drag=null;delete canvas.dataset.dragging;});
  });
  for(const h of elementHandles){
    h.addEventListener('pointerdown',e=>{if(picked<0)return;e.preventDefault();e.stopPropagation();measure(elements[picked]);
      drag={mode:'el-resize',i:picked,corner:h.dataset.corner,box:{...elements[picked].box},client:[e.clientX,e.clientY]};h.setPointerCapture(e.pointerId);});
    h.addEventListener('pointermove',e=>{
      if(drag?.mode!=='el-resize')return;const c=drag.corner;
      // Relative to the press, in screen pixels: a click (under half a unit of movement) changes nothing, and a
      // scroll or zoom of the popup can never shrink the element.
      const px=canvas.getBoundingClientRect().width/64,mx=(e.clientX-drag.client[0])/px,my=(e.clientY-drag.client[1])/px;
      if(Math.abs(mx)<.5&&Math.abs(my)<.5&&!drag.started)return;drag.started=true;
      let [l,t,r,btm]=paintedOf(drag.box,elements[drag.i]);
      // The fixed edges go on grid lines; the dragged edge moves with the pointer, keeping the size even.
      l=Math.round(l);t=Math.round(t);r=l+evenSize(r-l);btm=t+evenSize(btm-t);const w0=r-l,h0=btm-t;
      if(c.includes('e'))r=l+evenSize(w0+mx);if(c.includes('w'))l=r-evenSize(w0-mx);
      if(c.includes('s'))btm=t+evenSize(h0+my);if(c.includes('n'))t=btm-evenSize(h0-my);
      if(e.shiftKey){
        const f=Math.max((r-l)/w0,(btm-t)/h0),w=evenSize(w0*f),hh=evenSize(h0*f);
        if(c.includes('w'))l=r-w;else r=l+w;if(c.includes('n'))t=btm-hh;else btm=t+hh;
      }
      setElement(drag.i,boxOfPainted([l,t,r,btm],elements[drag.i]));});
    for(const t of ['pointerup','pointercancel'])h.addEventListener(t,()=>{drag=null;});
  }
  hit.addEventListener('pointerdown',e=>{e.preventDefault();select();drag={mode:'move',p:toCanvas(e),c:[...center]};canvas.dataset.dragging='true';hit.setPointerCapture(e.pointerId);});
  for(const h of handles)h.addEventListener('pointerdown',e=>{
    e.preventDefault();e.stopPropagation();select();const b=place().box,c=h.dataset.corner,i=inkNow();
    // The ink edge opposite the handle is pinned to its grid line; only the dragged axis changes (both at a corner).
    const pinX=Math.round(c.includes('w')?b.x+b.w:b.x),pinY=Math.round(c.includes('n')?b.y+b.h:b.y);
    drag={mode:'resize',corner:c,pin:[pinX,pinY],ink:i,center:[...center]};h.setPointerCapture(e.pointerId);});
  function onMove(e){
    if(!drag)return;const p=toCanvas(e);
    if(drag.mode==='move'){set([drag.c[0]+p.x-drag.p.x,drag.c[1]+p.y-drag.p.y],ink);return;}
    const {corner,pin}=drag,alongX=/[ew]/.test(corner),alongY=/[ns]/.test(corner);
    let w=alongX?Math.abs(p.x-pin[0]):drag.ink[0],h=alongY?Math.abs(p.y-pin[1]):drag.ink[1];
    if(e.shiftKey){const f=Math.max(alongX?w/drag.ink[0]:0,alongY?h/drag.ink[1]:0)||1;w=drag.ink[0]*f;h=drag.ink[1]*f;}
    w=clampS(w);h=clampS(h);
    const cx=alongX||e.shiftKey?(corner.includes('w')?pin[0]-w/2:pin[0]+w/2):drag.center[0];
    const cy=alongY||e.shiftKey?(corner.includes('n')?pin[1]-h/2:pin[1]+h/2):drag.center[1];
    set([cx,cy],[w,h]);
  }
  const end=()=>{drag=null;delete canvas.dataset.dragging;};
  for(const t of [hit,...handles]){t.addEventListener('pointermove',onMove);t.addEventListener('pointerup',end);t.addEventListener('pointercancel',end);}
  canvas.addEventListener('pointerdown',e=>{if(e.target!==hit&&!handles.includes(e.target)&&!elementHits.includes(e.target)&&!elementHandles.includes(e.target)){delete canvas.dataset.selected;delete canvas.dataset.active;if(picked>=0){picked=-1;draw();}}});
  canvas.addEventListener('keydown',e=>{
    if(mode==='element'&&picked>=0){const d={ArrowLeft:[-1,0],ArrowRight:[1,0],ArrowUp:[0,-1],ArrowDown:[0,1]}[e.key];
      if(d){e.preventDefault();freeze();measure(elements[picked]);const [l,t,r,btm]=paintedOf(elements[picked].box,elements[picked]),k=e.shiftKey?4:1;
        // Canvas units: Alt+arrows change width / height by 2 (even sizes), arrows move by 1 (Shift: 4).
        const L=Math.round(l),T=Math.round(t),w=evenSize(r-l),hh=evenSize(btm-t);
        setElement(picked,boxOfPainted(e.altKey?[L,T,L+evenSize(w+2*d[0]),T+evenSize(hh+2*d[1])]:[L+d[0]*k,T+d[1]*k,L+d[0]*k+w,T+d[1]*k+hh],elements[picked]));}return;}
    if(canvas.dataset.selected!=='sub')return;const step=e.shiftKey?4:1,d={ArrowLeft:[-1,0],ArrowRight:[1,0],ArrowUp:[0,-1],ArrowDown:[0,1]}[e.key];
    if(d&&e.altKey){e.preventDefault();const i=inkNow();set(center,[i[0]+2*d[0],i[1]+2*d[1]]);}
    else if(d){e.preventDefault();set([center[0]+d[0]*step,center[1]+d[1]*step],ink);}
    else if(['+','='].includes(e.key)){e.preventDefault();larger.onclick();}else if(['-','_'].includes(e.key)){e.preventDefault();smaller.onclick();}
  });
  // Edited elements: write each element's box into this pair's own copy of the symbol drawing, upload it (approved,
  // against the combination id), and combine it at the painted size shown, so nothing is refitted.
  async function storeElements(){
    const row=extra.row,source=await svgSource(extra.subUrl);
    const nodes=elementsOf(source);
    if(nodes.length!==elements.length)throw Error(`The saved symbol has ${nodes.length} elements but the editor shows ${elements.length}; reload and try again.`);
    elements.forEach((e,i)=>{const pre=elementTransform(e);if(pre&&nodes[i])nodes[i].setAttribute('transform',(pre+' '+(nodes[i].getAttribute('transform')||'')).trim());});
    const desc=source.querySelector('desc');
    if(desc)try{const m=JSON.parse(desc.textContent);if(m.typeface){m.manual_elements=true;desc.textContent=JSON.stringify(m);}}catch{}
    const response=await fetch('/api/icons/upload',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({
      name:((text?'Text '+text.text.replace(/\n/g,' '):row.concept+' symbol')).slice(0,120),family:'symbol',...(text?{category:'text'}:{}),
      svg:new XMLSerializer().serializeToString(source),approve:true,reference:{id:row.id,role:'symbol'}})});
    const data=await response.json().catch(()=>({}));if(!response.ok)throw Error(data.error||'Could not save the edited elements.');
    // Exactly as drawn 1:1: the painted box's whole-unit size (odd allowed) and its centre (a half unit when odd).
    const record=data.record,b=place().box,L=Math.round(b.x),T=Math.round(b.y),W=Math.min(64,Math.max(4,Math.round(b.w))),H=Math.min(64,Math.max(4,Math.round(b.h)));
    await loadReferenceUploads();pairReviews[record.key]='approve';
    await saveCenter(main,record.icon_id,'pair',[L+W/2,T+H/2],[W,H]);
    await createCombined(row);refreshCards(r=>r.id===row.id);
    return record.icon_id;
  }
  async function store(value){
    for(const b of [save,revert,reset])b.disabled=true;status.textContent='Saving…';
    if(value&&moved()){
      try{const icon=await storeElements();status.textContent=`Saved ${icon} for this pair and recombined.`;setTimeout(()=>dialog.close(),600);}
      catch(error){status.textContent=error.message;save.disabled=revert.disabled=false;reset.disabled=false;}
      return;
    }
    try{const message=await saveCenter(main,sub,scope.value,value,ink);
      if(!value){const e=effectiveCenter(main,sub);center=e.center.map(clampC);ink=e.size;}
      base={center:[...center],ink:ink&&[...ink]};draw();status.textContent=message;
      if(onSaved){status.textContent=message+' Recombining…';await onSaved();status.textContent=message+' The combined icon is updated.';}}
    catch(error){status.textContent=error.message;draw();}finally{reset.disabled=false;}
  }
  save.onclick=()=>store([...center]);revert.onclick=()=>{elements.forEach(e=>{if(e.box0){e.box={...e.box0};placeElement(e);}});picked=-1;set(base.center,base.ink);};reset.onclick=()=>store(null);
  dialog.classList.add('with-symbol-editor');
  dialog.addEventListener('close',()=>{panel.remove();for(const h of [...elementHits,...elementHandles])h.remove();delete canvas.dataset.symbolMode;dialog.classList.remove('with-symbol-editor');},{once:true});
  draw();
}
async function openRenderedCombination(label,url){
  const svg=await svgSource(url);svg.setAttribute('viewBox',svg.getAttribute('viewBox')||'0 0 64 64');
  for(const id of ['main-icon-clipped','state-icon'])svg.querySelector('[id="'+id+'"]')?.classList.add('ink-black');
  window.SideCombinationPopup.open(label,measuredResult(svg,[['main','main-icon-clipped'],['sub','state-icon']],url.split('/').pop()||'combination.svg'));
}
function inspectable(el,label,launch){
  el.classList.add('side-inspectable');el.setAttribute('role','button');el.tabIndex=0;el.setAttribute('aria-label','Inspect '+label);el.style.cursor='zoom-in';
  const run=e=>{e.preventDefault();launch().catch(error=>{el.setAttribute('title',error.message);});};
  el.addEventListener('click',e=>{if(e.metaKey||e.ctrlKey||e.shiftKey||e.button)return;run(e);});
  el.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' ')run(e);});
}
// Saves (or, with no center, resets) a symbol center and box size for the container or one pair, then redraws every view of it.
async function saveCenter(main,sub,scope,center,size=null){
  const body={main,sub:scope==='pair'?sub:'',center,size:center&&size?size:null};
  const response=await fetch('/api/container-centers',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
  const data=await response.json().catch(()=>({}));if(!response.ok)throw Error(data.error||'Could not save the center.');
  if(body.sub){savedCenters.pairs[main]={...savedCenters.pairs[main]};if(center)savedCenters.pairs[main][sub]=data;else delete savedCenters.pairs[main][sub];}
  else if(center)savedCenters.containers[main]=data;else delete savedCenters.containers[main];
  for(const f of centerViews.get(main)||[])f();
  return center?(body.sub?'Saved for this pair.':'Saved for every symbol in this container.'):'Reset to the default.';
}
function watchCenter(main,refresh){if(!centerViews.has(main))centerViews.set(main,new Set());centerViews.get(main).add(refresh);}
function svgNode(tag,attrs){const n=document.createElementNS('http://www.w3.org/2000/svg',tag);for(const [k,v] of Object.entries(attrs))n.setAttribute(k,v);return n;}
function centerEditor(main,mainUrl,sub,subUrl,onSaved,row=null){
  const panel=node('div','center-editor'),svg=svgNode('svg',{viewBox:'0 0 64 64',class:'center-preview',role:'img','aria-label':'Symbol placed at the container center'});
  // The symbol is inlined (not an <image>) so a stretched box keeps its stroke width, as in the popup.
  const box=svgNode('rect',{width:32,height:32,class:'center-box'}),symbol=svgNode('g',{class:'ink-black'});let fit=null,stroke=4;
  const h=svgNode('line',{class:'center-cross'}),v=svgNode('line',{class:'center-cross'});
  const grid=svgNode('g',{class:'center-grid','aria-hidden':'true'});
  for(let i=4;i<64;i+=4){const cls=i%16?'minor':'major';grid.append(svgNode('line',{x1:i,x2:i,y1:0,y2:64,class:cls}),svgNode('line',{x1:0,x2:64,y1:i,y2:i,class:cls}));}
  grid.append(svgNode('rect',{width:64,height:64,class:'edge'}));
  svg.append(grid,svgNode('image',{href:mainUrl,width:64,height:64,class:'ink-black'}),box,symbol,h,v);
  const x=node('input'),y=node('input'),wi=node('input'),he=node('input');
  for(const [input,name,min,step] of [[x,'Center x',0,1],[y,'Center y',0,1],[wi,'Symbol ink width',8,2],[he,'Symbol ink height',8,2]]){input.type='number';input.min=min;input.max=64;input.step=step;input.setAttribute('aria-label',name);}
  wi.placeholder=he.placeholder='auto';
  const scope=node('select');scope.setAttribute('aria-label','Apply center to');scope.append(new Option('This container · all symbols','container'),new Option('This pair only','pair'));
  const save=node('button','','Save'),reset=node('button','','Reset'),source=node('p','muted'),status=node('p','muted');status.setAttribute('role','status');
  // Empty width and height keep the natural size; otherwise both are the painted ink size.
  const current=()=>wi.value===''&&he.value===''?null:[+wi.value||32,+he.value||32];
  function draw(){const cx=+x.value,cy=+y.value,ink=current(),[w,hh]=ink||[32,32];box.setAttribute('x',cx-w/2);box.setAttribute('y',cy-hh/2);box.setAttribute('width',w);box.setAttribute('height',hh);
    if(fit&&svg.isConnected){symbol.setAttribute('transform',symbolPlacement(symbol,fit,stroke,[cx,cy],ink).transform);fixedStroke(symbol,svg,stroke);}
    for(const [line,a] of [[h,{x1:cx-4,x2:cx+4,y1:cy,y2:cy}],[v,{x1:cx,x2:cx,y1:cy-4,y2:cy+4}]])for(const [k,val] of Object.entries(a))line.setAttribute(k,val);}
  svgSource(subUrl).then(source=>{const g=placeGroup(source,'',32,0,0);fit=svgFit(source,32);g.removeAttribute('id');g.removeAttribute('transform');
    symbol.replaceChildren(...g.childNodes);for(const a of ['fill','stroke','stroke-linecap','stroke-linejoin'])if(g.getAttribute(a))symbol.setAttribute(a,g.getAttribute(a));draw();}).catch(()=>{});
  new ResizeObserver(draw).observe(svg);
  function refresh(){const e=effectiveCenter(main,sub);[x.value,y.value]=e.center;[wi.value,he.value]=e.size||['',''];scope.value=e.scope;
    source.textContent=`Center ${e.center[0]}, ${e.center[1]}${e.size?' · '+sizeText(e.size):''} · ${e.label}${e.by?' by '+e.by:''}${e.stale?' · content area predates the current drawing':''}`;draw();}
  const nudge=node('div','center-nudge');
  for(const [label,dx,dy] of [['←',-1,0],['↑',0,-1],['↓',0,1],['→',1,0]]){const b=node('button','',label);b.type='button';b.title='Move 1 unit';
    b.onclick=()=>{x.value=Math.min(64,Math.max(0,+x.value+dx));y.value=Math.min(64,Math.max(0,+y.value+dy));draw();};nudge.append(b);}
  x.oninput=y.oninput=wi.oninput=he.oninput=draw;
  async function send(center){
    save.disabled=reset.disabled=true;status.textContent='Saving…';
    try{const message=await saveCenter(main,sub,scope.value,center,current());status.textContent=message;
      if(onSaved){status.textContent=message+' Recombining…';await onSaved();}}
    catch(error){status.textContent=error.message;}finally{save.disabled=reset.disabled=false;}
  }
  save.onclick=()=>{const cx=+x.value,cy=+y.value;if(![cx,cy].every(n=>n>=0&&n<=64&&Number.isInteger(n*2))){status.textContent='Use 0–64 in steps of 0.5.';return;}
    if(current()&&!current().every(n=>n>=8&&n<=64&&n%2===0)){status.textContent='Ink width and height must be even, 8–64 (leave both empty for the natural size).';return;}send([cx,cy]);};
  reset.onclick=()=>send(null);
  const coords=node('div','center-fields');coords.append('x',x,'y',y,nudge);
  const sizes=node('div','center-fields');sizes.append('ink w',wi,'h',he);
  const actions=node('div','center-fields');actions.append(scope,save,reset);
  inspectable(svg,main+' + '+sub,()=>openContainerCombination(main+' + '+sub,mainUrl,subUrl,[+x.value,+y.value],{main,sub,onSaved,row},current()));
  panel.append(svg,coords,sizes,actions,source,status);if(savedCentersError)panel.append(node('p','muted',savedCentersError+' Showing defaults.'));
  watchCenter(main,refresh);refresh();return panel;
}
// Versions picked in the artwork editor (browser or manual edit) replace the published drawing.
const artworkOverrides=new Map();
async function loadArtworkOverrides(){
  try{const response=await fetch('/api/icon-artwork/overrides',{cache:'no-store'});if(!response.ok)return;
    const {records=[]}=await response.json();artworkOverrides.clear();
    for(const r of records)if(/^(container|symbol|sub)\//.test(r.key)&&r.preview_url)artworkOverrides.set(r.key,r.preview_url);}catch{}
}
// Approved manual uploads standing in for a container or symbol that has no generated drawing (reference id → icon).
let referenceUploads={};
async function loadReferenceUploads(){try{const r=await fetch('/api/reference-uploads',{cache:'no-store'});if(r.ok)referenceUploads=await r.json();}catch{}}
function uploadedArt(ref){const u=referenceUploads[ref];return u?{key:u.icon_key,icon_id:u.icon_id,preview_url:u.preview_url,uploaded:true}:null;}
function uploadForm(ref,role,concept,replace=false){
  const form=node('div','reference-upload requires-login'),name=node('input'),file=node('input'),button=node('button','side-edit-component','Upload and approve'),message=node('p','side-editor-message');
  name.value=concept||'';name.setAttribute('aria-label',`${role} icon name`);file.type='file';file.accept='.svg,image/svg+xml';file.setAttribute('aria-label',`${role} SVG file`);
  button.type='button';message.setAttribute('role','status');
  button.onclick=async()=>{
    const chosen=file.files?.[0];if(!chosen){message.textContent='Choose an SVG file first.';return;}
    if(chosen.size>1024*1024){message.textContent='Choose an SVG up to 1 MB.';return;}
    button.disabled=true;message.textContent='Uploading…';
    try{const response=await fetch('/api/icons/upload',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({name:name.value.trim()||concept,family:role,svg:await chosen.text(),approve:true,reference:{id:ref,role}})});
      const data=await response.json().catch(()=>({}));if(!response.ok)throw Error(data.error||'Could not upload the icon.');
      referenceUploads[ref]={role,icon_key:data.record.key,icon_id:data.record.icon_id,preview_url:data.record.preview_url};
      refreshCards(row=>row.main_id===ref||row.sub_id===ref);
    }catch(error){message.textContent=error.message;button.disabled=false;}
  };
  if(replace){button.textContent='Replace and approve';const d=node('details','reference-upload-replace requires-login');d.append(node('summary','',`Replace uploaded ${role}`));form.classList.remove('requires-login');
    form.append(node('p','muted','The new upload is approved and used here; the previous upload stays in Icon review.'),name,file,button,message);d.append(form);return d;}
  form.append(node('p','muted',`No ${role} drawn yet. Upload any SVG (${role==='container'?'64×64':'32×32'} fits best); it is approved in Icon review at once.`),name,file,button,message);return form;
}
function currentArt(key,icon_id,url){return {key,icon_id,preview_url:artworkOverrides.get(key)||url};}
function containerMain(row,selection){
  if(selection?.main_key){const id=selection.main_key.split('/')[1];return currentArt(selection.main_key,id,'../container64/'+encodeURIComponent(id)+'.svg');}
  const g=combinationMain(row).generated[0];return g?currentArt(g.key||'container/'+g.icon_id,g.icon_id,g.preview_url):uploadedArt(row.main_id);
}
function containerSymbol(row,selection){
  // A pair's own symbol (its typeface text, or elements moved in the combined popup), uploaded against the combination id.
  {const own=uploadedArt(row.id);if(own)return own;}
  if(selection?.symbol_key){const id=selection.symbol_key.split('/')[1];return currentArt(selection.symbol_key,id,'../symbol32/'+encodeURIComponent(id)+'.svg');}
  const generated=row.sub_generated||combinationCatalog.references[row.sub_id].generated;
  const g=generated.find(g=>g.key?.startsWith('symbol/'))||generated.find(g=>g.key?.startsWith('sub/'));
  return g?currentArt(g.key,g.icon_id,g.preview_url):uploadedArt(row.sub_id);
}
// The side pairs' geometry editor (side-component-editor.js), opened on a container or symbol drawing.
function containerEditButton(art,role){
  if(!art||art.uploaded||!window.SideComponentEditor)return null;
  const wrap=node('div','requires-login'),button=node('button','side-edit-component',`Edit ${role} icon`),message=node('p','side-editor-message');
  button.type='button';message.setAttribute('role','status');
  button.onclick=async()=>{button.disabled=true;message.textContent='';
    try{await window.SideComponentEditor.open({key:art.key},`${role==='container'?'Container':'Symbol'} · ${art.icon_id}`);}
    catch(error){message.textContent=error.message;}finally{button.disabled=false;}};
  wrap.append(button,message);return wrap;
}
window.addEventListener('icon-artwork-saved',async()=>{if(state.view!=='container')return;partShas={};await Promise.all([loadArtworkOverrides(),loadReferenceUploads()]);refreshCards(()=>true);});
// Container combination 64 (routes/container_pairs.rs): each pair's saved combined icon, the review status of
// every icon, and each part's catalog revision and current drawing (to review a part, and to tell a combined
// icon made from an older drawing).
let pairIcons=null,pairReviews={},partShas={},pairStateLoading=false;
async function loadPairState(){
  pairStateLoading=true;
  const json=url=>fetch(url,{cache:'no-store'}).then(r=>r.ok?r.json():{}).catch(()=>({}));
  const [icons,reviews]=await Promise.all([json('/api/container-pairs/icons'),json('/api/reviews')]);
  pairIcons=icons;pairReviews=reviews;pairStateLoading=false;
  if(state.view==='container')refreshCards(()=>true);
}
// {row, drawing} of the given part keys, asked 100 at a time and cached until an edit or pick is saved.
async function loadPartShas(keys){
  const missing=[...new Set(keys.filter(k=>k&&!(k in partShas)))];
  for(let i=0;i<missing.length;i+=100){
    const chunk=missing.slice(i,i+100);
    const got=await fetch('/api/container-pairs/current?keys='+encodeURIComponent(chunk.join(',')),{cache:'no-store'}).then(r=>r.ok?r.json():{}).catch(()=>({}));
    for(const k of chunk)partShas[k]=got[k]||null;
  }
}
// The pair's container and symbol as the combined icon uses them, with the center and ink size it is made at.
function pairParts(row){
  if(row.kind!=='container')return null;
  const selection=containerResults?.selections?.[row.id]||containerPreviews.get(row.id);
  const main=containerMain(row,selection),symbol=containerSymbol(row,selection);
  if(!main||!symbol||!containerCenters)return null;
  const mainId=row.main_icon_id||main.icon_id,e=effectiveCenter(mainId,symbol.icon_id);
  // Half units: a symbol with an odd size (elements placed one by one) is centred between grid lines.
  return {main,symbol,mainId,center:e.center.map(v=>Math.round(v*2)/2),ink:e.size};
}
const REVIEW_STATES={approve:['Approved','ok'],ready:['To review','todo'],'re-generated':['To review','todo'],pending:['Disapproved','fix'],
  disapprove:['Disapproved','fix'],claimed:['Being fixed','fix'],rejected:['Rejected','rej']};
const reviewOf=key=>REVIEW_STATES[pairReviews[key]||'ready']||[pairReviews[key],'todo'];
// Where a pair's combined icon stands: not made, made from something that changed since, failing its check
// (a part not approved when it was made), or its review status.
function combinedState(row,parts){
  const saved=pairIcons?.[row.id];
  if(!parts)return {label:'Needs container and symbol',tone:'todo'};
  if(!pairIcons)return {label:'Loading…',tone:'todo'};
  if(!saved)return {label:'Not created',tone:'todo'};
  const r=saved.record||{},changes=[];
  if(r.main_key!==parts.main.key||r.symbol_key!==parts.symbol.key)changes.push('a different container or symbol is picked');
  if(JSON.stringify(r.center)!==JSON.stringify(parts.center)||JSON.stringify(r.ink??null)!==JSON.stringify(parts.ink??null))changes.push('the symbol position or size changed');
  for(const [role,key,label] of [['main',parts.main.key,'container'],['symbol',parts.symbol.key,'symbol']]){
    const now=partShas[key]?.drawing;if(now&&r.drawings?.[role]&&now!==r.drawings[role])changes.push(`the ${label} drawing changed`);
  }
  if(changes.length)return {label:'Outdated: recombine',tone:'fix',saved,why:'Since it was combined, '+changes.join(', ')+'.',outdated:true};
  const review=pairReviews[saved.key];
  // An approved combined icon shows Approved even when its check had failed (approving it is the reviewer's call).
  if(saved.build_failed&&!['pending','rejected','approve'].includes(review)){
    const ready=pairReviews[parts.main.key]==='approve'&&pairReviews[parts.symbol.key]==='approve';
    return ready?{label:'Parts approved: recombine',tone:'fix',saved,why:'Both parts are approved now. Recombine to clear the check.',outdated:true,checkOnly:true}
      :{label:'Failed check',tone:'fix',saved,why:(r.errors||[]).join(' · ')};
  }
  const [label,tone]=reviewOf(saved.key);return {label,tone,saved};
}
async function reviewIcon(key,status,sha,feedback){
  const body={icon:key,status,svg_sha256:sha};if(status==='pending'){body.reason='other';body.feedback=feedback;}
  const response=await fetch('/api/reviews',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
  const data=await response.json().catch(()=>({}));if(!response.ok)throw Error(data.error||'Could not save the review.');
  pairReviews[key]=status==='approve'?'approve':'pending';
}
// A review status chip with Approve and Disapprove (with a note) for one icon. `sha` resolves the revision the
// review names; `blocked` explains why Approve is not possible yet.
function reviewControls(key,sha,{blocked,after,chip=true}={}){
  const box=node('div','pair-review'),[label,tone]=reviewOf(key),row=node('div','pair-review-actions requires-login');
  const approve=node('button','side-edit-component','Approve'),disapprove=node('button','side-edit-component','Disapprove'),message=node('p','side-editor-message');
  for(const b of [approve,disapprove])b.type='button';message.setAttribute('role','status');
  approve.disabled=pairReviews[key]==='approve'||!!blocked;if(blocked)approve.title=blocked;
  const form=node('div','pair-review-note'),note=node('textarea'),send=node('button','side-edit-component','Send disapproval');form.hidden=true;
  note.rows=2;note.placeholder='What needs fixing?';note.setAttribute('aria-label','Disapproval note');send.type='button';form.append(note,send);
  const run=async(status,feedback)=>{
    for(const b of [approve,disapprove,send])b.disabled=true;message.textContent='Saving…';
    try{await reviewIcon(key,status,await sha(),feedback);message.textContent=status==='approve'?'Approved.':'Disapproved.';after?.();}
    catch(error){message.textContent=error.message;for(const b of [approve,disapprove,send])b.disabled=false;}
  };
  approve.onclick=()=>run('approve');disapprove.onclick=()=>{form.hidden=!form.hidden;if(!form.hidden)note.focus();};
  send.onclick=()=>{if(!note.value.trim()){message.textContent='Add a note first.';return;}run('pending',note.value.trim());};
  row.append(approve,disapprove);if(chip)box.append(node('span','review-chip '+tone,label));box.append(row,form,message);return box;
}
// (Re)makes the pair's combined icon from both parts' current drawings, at its current center and ink size.
async function createCombined(row){
  const parts=pairParts(row);if(!parts)throw Error('The pair needs a container and a symbol.');
  const body={pair_id:row.id,concept:row.concept,main_key:parts.main.key,symbol_key:parts.symbol.key,center:parts.center,ink:parts.ink,
              reference_url:combinationCatalog.references[row.id]?.reference_url||null};
  const response=await fetch('/api/container-pairs/icon',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
  const data=await response.json().catch(()=>({}));if(!response.ok)throw Error(data.error||'Could not combine this pair.');
  pairIcons??={};pairIcons[row.id]={key:data.key,svg_sha256:data.svg_sha256,build_failed:data.build_failed,preview_url:data.preview_url,record:data.record};
  delete pairReviews[data.key];  // a new drawing is a new revision: to review
  for(const [role,key] of [['main',parts.main.key],['symbol',parts.symbol.key]])partShas[key]={...partShas[key],drawing:data.record.drawings[role]};
  return data;
}
const rowsOfPart=key=>r=>{const p=pairParts(r);return !!p&&(p.main.key===key||p.symbol.key===key);};
// A saved symbol position / size remakes this pair's combined icon; the container's other pairs redraw and,
// when the save applied to the whole container, show Outdated until they are recombined.
async function afterCenterSaved(row){
  const mainId=pairParts(row)?.mainId;
  try{await createCombined(row);}
  finally{refreshCards(r=>pairParts(r)?.mainId===mainId);}
}
// Bulk: every pair whose container and symbol are approved and whose combined icon is missing or outdated.
let pairBulk={rows:null,running:false,stop:false,message:''};
async function countPairBulk(){
  const candidates=[];
  for(const r of combinationCatalog.rows)if(r.kind==='container'){
    const p=pairParts(r);if(p&&pairReviews[p.main.key]==='approve'&&pairReviews[p.symbol.key]==='approve')candidates.push([r,p]);
  }
  await loadPartShas(candidates.filter(([r])=>pairIcons?.[r.id]).flatMap(([,p])=>[p.main.key,p.symbol.key]));
  return candidates.filter(([r,p])=>{const c=combinedState(r,p);return !c.saved||c.outdated;}).map(([r])=>r);
}
function paintPairBulk(){
  const button=document.getElementById('pairBulk'),stop=document.getElementById('pairBulkStop'),status=document.getElementById('pairBulkStatus');if(!button)return;
  const n=pairBulk.rows?.length;
  button.textContent=pairBulk.running?'Combining…':n==null?'Count approved pairs to combine…':`Combine ${n.toLocaleString()} approved pair${n===1?'':'s'}`;
  button.disabled=pairBulk.running||!pairIcons||!containerCenters||n===0;stop.hidden=!pairBulk.running;status.textContent=pairBulk.message;
}
async function runPairBulk(){
  if(pairBulk.running)return;
  if(pairBulk.rows==null){pairBulk.message='Counting…';paintPairBulk();pairBulk.rows=await countPairBulk();
    pairBulk.message=pairBulk.rows.length?'Pairs whose container and symbol are both approved, with no combined icon or an outdated one.':'Every approved pair is combined and up to date.';paintPairBulk();return;}
  const queue=[...pairBulk.rows],total=queue.length,failed=[];let done=0;
  pairBulk={...pairBulk,running:true,stop:false};paintPairBulk();
  const worker=async()=>{for(let row=queue.shift();row&&!pairBulk.stop;row=queue.shift()){
    try{await createCombined(row);}catch(error){failed.push(row.concept+': '+error.message);}
    done++;pairBulk.message=`Combined ${done.toLocaleString()} of ${total.toLocaleString()}${failed.length?` · ${failed.length} failed`:''}`;paintPairBulk();}};
  await Promise.all([worker(),worker()]);
  pairBulk={rows:null,running:false,stop:false,message:(pairBulk.stop?'Stopped. ':'Done. ')+pairBulk.message+(failed.length?' — '+failed.slice(0,3).join(' · '):'')};
  paintPairBulk();refreshCards(()=>true);
}
{const style=document.createElement('style');style.textContent=`.review-chip{display:inline-block;padding:3px 10px;border-radius:999px;font:600 12px system-ui;white-space:nowrap}.review-chip.ok{background:#e3f4e8;color:#1f6b3a}.review-chip.todo{background:#eef2f6;color:#3f5163}.review-chip.fix{background:#fdf0e1;color:#8a4b12}.review-chip.rej{background:#fbe5e5;color:#9b1c1c}
.pair-review{display:grid;gap:6px;justify-items:center;margin:4px 0 10px}.pair-review-actions{display:flex;gap:6px;flex-wrap:wrap;justify-content:center}.pair-review-note{display:grid;gap:6px;width:100%}.pair-review-note textarea{width:100%;box-sizing:border-box;font:13px system-ui;padding:6px;border:1px solid #9bafb5;border-radius:6px}
.pair-combined-status{display:grid;justify-items:center;gap:4px;margin-bottom:8px}.pair-why{font-size:12px!important;margin:0!important;max-width:240px}.pair-combined-art{display:block;width:128px;height:128px;margin:6px auto;background:#fbfdfb;box-shadow:inset 0 0 0 1px #99adb4}.pair-combined-art img{width:128px;height:128px;display:block}`;document.head.append(style);}
// Redraws the matching combination cards where they are, keeping scroll position and open groups;
// falls back to a full render before the list exists.
let refreshCards=()=>renderCombinations();
async function loadContainerResults(){
  if(containerResultsLoading)return;
  containerResultsLoading=true;
  try{
    const response=await fetch('/api/combinations/container/results',{cache:'no-store'});
    const data=await response.json();if(!response.ok)throw Error(data.error||'Could not load combination results.');
    containerResults=data;containerPreviews.clear();for(const pair of data.pairs)containerPreviews.set(pair.pair_id,pair);
    containerResultError='';
  }catch(error){containerResultError=error.message;}
  finally{containerResultsLoading=false;}
  if(state.view==='container')renderCombinations();
}
async function combineAllPairs(){
  if(combineRunning)return;
  combineRunning=true;combineProgress='Preparing all container pairs…';renderCombinations();
  try{
    const response=await fetch('/api/combinations/container/results',{cache:'no-store'});
    const start=await response.json();if(!response.ok)throw Error(start.error||'Could not prepare pairs.');
    containerResults=start;containerPreviews.clear();let offset=0;
    do{
      const response=await fetch('/api/combinations/container/combine',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({limit:100,offset,snapshot:start.snapshot})});
      const batch=await response.json();if(!response.ok)throw Error(batch.error||'Could not combine pairs.');
      for(const pair of batch.pairs)containerPreviews.set(pair.pair_id,pair);
      const done=Math.min(batch.offset+batch.limit,batch.total);
      combineProgress=`Processed ${done.toLocaleString()} of ${batch.total.toLocaleString()} pairs`;
      offset=batch.next_offset;if(state.view==='container')renderCombinations();
    }while(offset!==null);
    combineProgress='All pairs processed. Missing components and fit problems are listed below.';
  }catch(error){combineProgress=error.message+' Completed batches are saved; you can retry.';}
  finally{combineRunning=false;await loadContainerResults();}
}
const combinationLabels={missing:'Components needed',partial:'One component generated',ready:'Both components generated',generated:'Generated'};
function combinationMain(row){
  const ref=combinationCatalog.references[row.main_id];
  if(row.kind!=='container')return ref;
  // A solo remake does not fulfill a container-main requirement. Keep this
  // fallback for older catalogs, while honoring an explicit empty build result.
  const generated=(row.main_generated??ref.generated).filter(g=>g.key?.startsWith('container/'));
  return {...ref,generated};
}
function containerGroups(rows){
  const groups=new Map();
  for(const row of rows){
    const main=combinationMain(row), generated=main.generated[0];
    const iconId=row.main_icon_id||generated?.icon_id;
    const key=iconId?'container/'+iconId:'reference/'+row.main_id;
    if(!groups.has(key))groups.set(key,{key,iconId,main,title:iconId?iconId.replace(/[-_]/g,' '):main.concept,rows:[]});
    groups.get(key).rows.push(row);
  }
  return [...groups.values()].sort((a,b)=>a.title.localeCompare(b.title)||a.key.localeCompare(b.key));
}
function combinationState(row){
  if(row.kind==='container'&&containerResults?.selections?.[row.id]){const selected=containerResults.selections[row.id];const n=Number(!!selected.main_key)+Number(!!selected.symbol_key);return n===2?'ready':n===1?'partial':'missing';}
  const refs=combinationCatalog.references;
  if((row.component_selection!=='explicit'&&refs[row.id].generated.length) || row.generated?.length)return 'generated';
  const count=Number(!!combinationMain(row).generated.length)+Number(!!(row.sub_generated??refs[row.sub_id].generated).length);
  return count===2?'ready':count===1?'partial':'missing';
}
async function renderCombinations(){
  const host=$('combinations');
  if(!combinationCatalog){
    host.replaceChildren(node('p','muted',combinationError||'Loading combinations…'));
    if(combinationError){const retry=node('button','','Retry');retry.onclick=()=>{combinationError='';renderCombinations();};host.append(retry);return;}
    if(combinationLoading)return;
    combinationLoading=true;
    try{const response=await fetch('combinations.json',{cache:'no-cache'});if(!response.ok)throw Error('Could not load the combination catalog.');combinationCatalog=await response.json();}
    catch(error){combinationError=error.message;}
    finally{combinationLoading=false;}
    if(['container','side'].includes(state.view))renderCombinations();return;
  }
  if(state.view==='container'&&!containerResults&&!containerResultError&&!containerResultsLoading)loadContainerResults();
  if(state.view==='container'&&!containerCenters&&!containerCentersLoading)loadContainerCenters();
  if(state.view==='container'&&!pairIcons&&!pairStateLoading)loadPairState();
  centerViews.clear();
  const all=combinationCatalog.rows.filter(r=>r.kind===state.view), counts={missing:0,partial:0,ready:0,generated:0};
  all.forEach(r=>counts[combinationState(r)]++);
  host.replaceChildren();
  host.append(node('h2','',state.view==='container'?'Container combination':'Side combination'),node('p','muted',state.view==='container'?'Combine each container with its latest standard 32×32 symbol. Expand a container to compare the original and combined preview.':'Work on each pair as Original → Main → Sub → Combined: one 48-unit main and one 32×32 sub. Group by main or sub to see where an icon is reused. Finished outputs live on Experiment › Side combination.'));
  const summary=node('div','combination-summary');
  // The side grid adds its own plain status counts (Ready, Fix sub, Waiting, Needs main, Needs sub).
  const summaryItems=state.view==='side'?[['Side pairs',all.length]]:[['Total',all.length],...Object.entries(counts).map(([k,v])=>[combinationLabels[k],v])];
  for(const [label,value] of summaryItems){
    const item=node('div');item.append(node('strong','',value.toLocaleString()),node('span','',label));summary.append(item);
  }
  if(state.view!=='container'){
    host.append(summary);
    if(state.view==='side'){
      const needed=node('p','muted');needed.append('Pair badges: Waiting = main and sub are drawn but not combined yet. Lists: ');const link=node('a','','Main icons →'),subs=node('a','','Sub icons →');link.href='side-mains.html';subs.href='side-subs.html';needed.append(link,' · ',subs);host.append(needed);
    }
  }
  if(state.view==='side'){renderSideGrid(host,all,summary);return;}
  else{
    const area=node('div','container-combine-controls');
    if(containerResults){
      const stats=node('div','combination-summary');
      for(const [label,value] of [['Container pairs',containerResults.total],['Container icons',containerResults.containers.total],['Containers needed',containerResults.containers.missing],['Symbol requirements · 32×32',containerResults.symbols.total],['Symbols needed',containerResults.symbols.missing]]){
        const item=node('div');item.append(node('strong','',value.toLocaleString()),node('span','',label));stats.append(item);
      }
      area.append(stats,node('p','muted',`${containerResults.containers.ready} containers and ${containerResults.symbols.ready} symbol requirements have eligible artwork. Symbols are counted once per source requirement; equivalent sources may share a drawing.`));
      const needed=node('p');const link=node('a','','Browse the symbols still needed →');link.href='symbols-needed.html';needed.append(link);area.append(needed);
    }
    const actions=node('div','toolbar'),button=node('button','','Combine all pairs');button.disabled=combineRunning;button.onclick=combineAllPairs;
    actions.append(button,node('span','muted','Latest published containers + standard 32×32 symbols. Applies to all pairs, including other pages.'));
    area.append(actions);
    const bulk=node('div','toolbar requires-login'),bulkButton=node('button',''),bulkStop=node('button','','Stop'),bulkStatus=node('span','muted');
    bulkButton.id='pairBulk';bulkStop.id='pairBulkStop';bulkStatus.id='pairBulkStatus';bulkButton.type=bulkStop.type='button';
    bulkButton.onclick=runPairBulk;bulkStop.onclick=()=>{pairBulk.stop=true;bulkStatus.textContent='Stopping after the current pairs…';};
    bulk.append(bulkButton,bulkStop,bulkStatus);area.append(bulk);queueMicrotask(paintPairBulk);
    const progress=node('p','muted',combineProgress||containerResultError||(containerResults?`${containerResults.processed.toLocaleString()} of ${containerResults.total.toLocaleString()} pairs processed. Saved previews appear when you expand a container.`:'Loading component counts…'));progress.setAttribute('role','status');area.append(progress);
    if(containerResults&&!combineRunning){const c=containerResults.counts;area.append(node('p','muted',`${c.pass||0} fit checks passed · ${c.fail||0} need fit changes · ${c.review||0} need review · ${c.missing||0} missing components · ${c.blocked||0} blocked`));}
    host.append(area);
  }
  const toolbar=node('div','toolbar'), search=node('input');search.type='search';search.placeholder='Search concept or component ID';search.setAttribute('aria-label','Search combinations');search.value=state.q;
  const filter=node('select');filter.setAttribute('aria-label','Combination progress');filter.append(new Option('All progress','todo'),...Object.entries(combinationLabels).map(([k,v])=>new Option(v,k)));
  if(state.view==='container')filter.append(new Option('Text symbols (typeface v2)','text'));filter.value=state.status;
  filter.onchange=()=>{state.status=filter.value;page=1;writeURL();renderCombinations();};
  let timer;search.oninput=()=>{clearTimeout(timer);timer=setTimeout(()=>{const cursor=search.selectionStart;state.q=search.value;page=1;writeURL();renderCombinations();const next=host.querySelector('input');next.focus();if(cursor!==null)next.setSelectionRange(cursor,cursor);},180);};
  toolbar.append(search,filter);host.append(toolbar);
  const q=state.q.trim().toLowerCase(),refs=combinationCatalog.references;
  // "Text symbols": pairs whose symbol source is marked Text / number on this page.
  const textOnly=state.view==='container'&&state.status==='text';
  const rows=all.filter(r=>(textOnly?statuses[r.sub_id]?.reason==='text_number':!combinationLabels[state.status]||combinationState(r)===state.status)&&(!q||[r.concept,r.id,r.main_id,r.sub_id,refs[r.main_id].concept,refs[r.sub_id].concept,r.main_icon_id,r.main_icon_id?.replace(/[-_]/g,' ')].join(' ').toLowerCase().includes(q)));
  const grouped=state.view==='container', groups=grouped?containerGroups(rows):[], pageSize=grouped?12:30;
  const pages=Math.max(1,Math.ceil((grouped?groups.length:rows.length)/pageSize));page=Math.min(page,pages);writeURL();
  function pager(){const bar=node('div','pager'),prev=node('button','','← Previous'),next=node('button','','Next →');prev.disabled=page<=1;next.disabled=page>=pages;prev.onclick=()=>{page--;renderCombinations();host.scrollIntoView();};next.onclick=()=>{page++;renderCombinations();host.scrollIntoView();};bar.append(prev,node('span','muted',`${rows.length.toLocaleString()} matches${grouped?' · '+groups.length+' main container'+(groups.length===1?'':'s'):''} · Page ${page} of ${pages}`),next);return bar;}
  host.append(pager());
  const list=node('div','combination-list');
  function imageLink(url,label){const link=node('a');link.href=url;link.target='_blank';link.rel='noopener';link.title=label;const img=node('img');img.src=url;img.alt=label;img.loading='lazy';img.onerror=()=>link.replaceWith(node('span','muted','Artwork unavailable'));link.append(img);return link;}
  // Generated icons are drawn inline on their own canvas grid so the padding
  // between the ink and the canvas edge can be read: a dashed box marks the
  // measured ink (stroke included) and the caption gives each side's padding.
  function canvasFor(key){const family=(key||'').split('/')[0];return {container:64,solo:48,combination_main:48,symbol:32,sub:32,symbol24:24}[family]||null;}
  function gridImageLink(url,label,canvas){
    const link=node('a','grid-tile-link');link.href=url;link.target='_blank';link.rel='noopener';link.title=label;
    const svg=svgNode('svg',{viewBox:`0 0 ${canvas} ${canvas}`,class:'grid-tile',role:'img','aria-label':label});
    const grid=svgNode('g',{class:'tile-grid','aria-hidden':'true'});
    for(let i=4;i<canvas;i+=4){const cls=i%16?'minor':'major';grid.append(svgNode('line',{x1:i,x2:i,y1:0,y2:canvas,class:cls}),svgNode('line',{x1:0,x2:canvas,y1:i,y2:i,class:cls}));}
    grid.append(svgNode('rect',{width:canvas,height:canvas,class:'edge'}));
    const art=svgNode('g',{class:'ink-black'}),pad=node('span','grid-tile-pad muted','');let fit={k:1,tx:0,ty:0};
    svg.append(grid,art);link.append(svg);
    fetch(url,{cache:'no-cache'}).then(r=>{if(!r.ok)throw Error();return r.text();}).then(text=>{
      const source=new DOMParser().parseFromString(text,'image/svg+xml').documentElement;
      fit=svgFit(source,canvas);if(fit.k!==1||fit.tx||fit.ty)art.setAttribute('transform',`translate(${fit.tx} ${fit.ty}) scale(${fit.k})`);
      for(const name of ['fill','stroke','stroke-width','stroke-linecap','stroke-linejoin'])if(source.getAttribute(name))art.setAttribute(name,source.getAttribute(name));
      for(const child of [...source.children])if(!['title','desc'].includes(child.tagName))art.append(document.importNode(child,true));
      const b=art.getBBox(),r=inkStroke(art)/2,round=v=>Math.round(v*2)/2,{k,tx,ty}=fit;
      const x0=round(tx+(b.x-r)*k),y0=round(ty+(b.y-r)*k),x1=round(tx+(b.x+b.width+r)*k),y1=round(ty+(b.y+b.height+r)*k);
      svg.append(svgNode('rect',{x:x0,y:y0,width:x1-x0,height:y1-y0,class:'ink-box'}));
      pad.textContent=`ink ${x1-x0}×${y1-y0} · pad ${x0}/${y0}/${canvas-x1}/${canvas-y1}`;pad.title=`${canvas}×${canvas} canvas · ink box ${x0},${y0} → ${x1},${y1} · padding left/top/right/bottom`;
    }).catch(()=>{link.replaceWith(node('span','muted','Artwork unavailable'));});
    const wrap=node('span','grid-tile-wrap');wrap.append(link,pad);return wrap;
  }
  function artwork(title,ref,generatedOnly=false,extra=[]){
    const panel=node('section','combination-artwork');panel.append(node('h4','',title));
    if(!generatedOnly){panel.append(ref.reference_url?imageLink(ref.reference_url,ref.concept+' — original'):node('div','combination-empty','Reference missing'));panel.append(node('p','component-name',ref.concept));}
    const generated=[...ref.generated,...extra];
    if(generated.length){const previews=node('div','combination-generated');for(const g of generated){const figure=node('figure');const canvas=canvasFor(g.key);figure.append(canvas?gridImageLink(g.preview_url,g.icon_id,canvas):imageLink(g.preview_url,g.icon_id),node('figcaption','',g.label||g.icon_id));previews.append(figure);}panel.append(node('p','combination-label','Generated'),previews);}
    else panel.append(node('div','combination-empty',generatedOnly?'Not combined yet':'Not generated yet'));
    return panel;
  }
  function combinationCard(row){
    const card=node('article','combination-card'),head=node('div','combination-heading');card.dataset.row=row.id;head.append(node('h3','',row.concept),node('span','chip',combinationLabels[combinationState(row)]));card.append(head);
    const grid=node('div','combination-artworks');
    const original=artwork('Reference combination',{...refs[row.id],concept:row.concept,generated:[]});original.lastChild.remove();
    const subRef={...refs[row.sub_id],generated:(row.sub_generated||refs[row.sub_id].generated).map(g=>{const reuse=(row.sub_exports||[]).find(e=>e.icon===g.icon_id);return reuse?{...g,preview_url:reuse.export_url,label:g.icon_id+' · 32px reuse export'}:g;})};
    const combined=artwork('Generated combination',row.component_selection==='explicit'?{...refs[row.id],generated:[]}:refs[row.id],true,row.generated||[]);
    if(row.kind!=='container'&&row.trial_preview){
      const trial=row.trial_preview, empty=combined.querySelector('.combination-empty');if(empty)empty.remove();
      combined.append(node('p','combination-label','Trial preview'),imageLink(trial.preview_url,row.concept+' — trial'),node('p','muted',trial.status==='clearance-estimate-pass'?'Solo artwork fitted inside container · review before approval':'Solo artwork fitted inside container · placement needs review'));
    }else if(row.trial_status==='stale')combined.append(node('p','muted','Trial needs rebuilding because a linked source or pairing changed.'));
    const latest=containerPreviews.get(row.id);
    const selection=containerResults?.selections?.[row.id]||latest;
    if(row.kind==='container'){
      combined.replaceChildren(node('h4','','Combined icon · 64'));
      const parts=pairParts(row),cs=combinedState(row,parts),standing=node('div','pair-combined-status');
      standing.append(Object.assign(node('span','review-chip '+cs.tone,cs.label),{title:cs.why||''}));if(cs.why)standing.append(node('p','muted pair-why',cs.why));
      combined.append(standing);
      if(cs.saved){
        const link=imageLink(cs.saved.preview_url,row.concept+' — combined icon');link.classList.add('pair-combined-art');link.querySelector('img')?.classList.add('ink-black');
        if(parts)inspectable(link,row.concept,()=>openContainerCombination(parts.mainId+' + '+parts.symbol.icon_id,parts.main.preview_url,parts.symbol.preview_url,parts.center,
          {main:parts.mainId,sub:parts.symbol.icon_id,row,onSaved:()=>afterCenterSaved(row)},parts.ink));
        combined.append(link);
      }
      if(parts){
        const actions=node('div','pair-review-actions requires-login'),make=node('button','side-edit-component',cs.saved?(cs.outdated?'Recombine (outdated)':'Recombine'):'Create combined icon'),makeMessage=node('p','side-editor-message');
        make.type='button';make.title='Combine the latest container and symbol at the saved position and size';makeMessage.setAttribute('role','status');
        make.onclick=async()=>{make.disabled=true;makeMessage.textContent='Combining…';try{await createCombined(row);refreshCards(r=>r.id===row.id);}catch(error){makeMessage.textContent=error.message;make.disabled=false;}};
        actions.append(make);combined.append(actions,makeMessage);
        if(cs.saved){
          // A Failed check (a part not approved) does not block approving the combined icon; only an outdated one
          // (made from parts that changed since) must be recombined first.
          const blocked=cs.outdated&&!cs.checkOnly?'Recombine first. '+cs.why:'';
          combined.append(reviewControls(cs.saved.key,async()=>cs.saved.svg_sha256,{blocked,chip:false,after:()=>refreshCards(r=>r.id===row.id)}));
        }
        // Part drawings are compared once they are known, then this card redraws with the result.
        if(cs.saved&&[parts.main.key,parts.symbol.key].some(k=>!(k in partShas)))loadPartShas([parts.main.key,parts.symbol.key]).then(()=>refreshCards(r=>r.id===row.id));
      }
      if(latest?.svg_url){
        const status=({pass:'Fit check passed',fail:'Needs fit changes',review:'Needs review'})[latest.status]||latest.status,zoom=imageLink(latest.svg_url,row.concept+' — combined');
        zoom.querySelector('img')?.classList.add('ink-black');
        inspectable(zoom,row.concept,()=>openRenderedCombination(row.concept,latest.svg_url));
        combined.append(zoom);
        combined.append(node('p','',status));
        combined.append(node('p','muted','64×64 · symbol at 32×32 · not yet approved'));
      }
      const mainArt=containerMain(row,selection);
      const symbolArt=containerSymbol(row,selection),mainId=row.main_icon_id||mainArt?.icon_id;
      if(mainArt&&symbolArt&&containerCenters)combined.append(node('p','combination-label','Symbol center'),centerEditor(mainId,mainArt.preview_url,symbolArt.icon_id,symbolArt.preview_url,()=>afterCenterSaved(row),row));
      else if(!latest?.svg_url)combined.append(node('p','combination-empty',!containerCenters?'Loading centers…':latest?.reason||(mainArt?'Symbol not generated yet':'Container not generated yet')));
    }
    const chosenMain=row.kind==='container'?containerMain(row,selection):null,chosenSymbol=row.kind==='container'?containerSymbol(row,selection):null;
    const selectedMain=row.kind==='container'?{...combinationMain(row),generated:chosenMain?[{icon_id:'Container · 64×64',key:chosenMain.key,label:chosenMain.icon_id+(chosenMain.uploaded?' · uploaded':''),preview_url:chosenMain.preview_url}]:[]}:combinationMain(row);
    const selectedSub=row.kind==='container'?{...subRef,generated:chosenSymbol?[{icon_id:'Symbol · 32×32',key:chosenSymbol.key,label:chosenSymbol.icon_id+(chosenSymbol.uploaded?' · uploaded':''),preview_url:chosenSymbol.preview_url}]:[]}:subRef;
    const mainPanel=artwork(row.kind==='container'?'Container · 64×64':'Main',selectedMain),subPanel=artwork(row.kind==='container'?'Symbol · 32×32':'Sub',selectedSub);
    if(row.kind==='container'){
      const a=containerEditButton(chosenMain,'container'),b=containerEditButton(chosenSymbol,'symbol');if(a)mainPanel.append(a);if(b)subPanel.append(b);
      for(const [panel,art] of [[mainPanel,chosenMain],[subPanel,chosenSymbol]])if(art?.key)panel.querySelector('h4').after(reviewControls(art.key,async()=>{
        await loadPartShas([art.key]);const sha=partShas[art.key]?.row;if(!sha)throw Error('This icon has no revision to review yet.');return sha;},
        {after:()=>refreshCards(rowsOfPart(art.key))}));
      if(chosenMain?.uploaded)mainPanel.append(uploadForm(row.main_id,'container',refs[row.main_id].concept,true));
      if(chosenSymbol?.uploaded)subPanel.append(uploadForm(row.sub_id,'symbol',refs[row.sub_id].concept,true));
      if(!chosenMain)mainPanel.querySelector('.combination-empty')?.after(uploadForm(row.main_id,'container',refs[row.main_id].concept));
      if(!chosenSymbol)subPanel.querySelector('.combination-empty')?.after(uploadForm(row.sub_id,'symbol',refs[row.sub_id].concept));
      if(window.ContainerTextSymbol?.isText(row.sub_id))subPanel.append(window.ContainerTextSymbol.panel(row));
    }
    grid.append(original,mainPanel,subPanel,combined);card.append(grid);
    for(const mapping of row.remappings||[])card.append(node('p','muted',`${mapping.role==='main'?'Main':'Sub'} remapped to an existing source: ${mapping.reason}.`));
    const details=node('details','combination-identities');details.append(node('summary','','Source IDs'));for(const [name,id] of [['Combination',row.id],['Main',row.main_id],['Sub',row.sub_id]])details.append(node('p','',name+': '+id));card.append(details);return card;
  }
  const rowById=new Map(all.map(r=>[r.id,r]));
  refreshCards=match=>{for(const card of host.querySelectorAll('.combination-card[data-row]')){const row=rowById.get(card.dataset.row);if(row&&match(row))card.replaceWith(combinationCard(row));}};
  if(grouped){
    host.append(node('p','muted','Grouped by main container. Expand a container to see its combinations.'));
    for(const group of groups.slice((page-1)*pageSize,page*pageSize)){
      const section=node('details','container-group'), heading=node('summary','container-group-heading');
      const generated=group.main.generated[0];
      if(generated){const img=node('img','ink-black');img.src=artworkOverrides.get(generated.key)||generated.preview_url;img.alt='';img.loading='lazy';heading.append(img);}
      const label=node('span','container-group-label'),where=node('span','muted');label.append(node('strong','',group.title),node('span','muted',generated?'Main · Container 64px':'Main · Container needed'),where);
      if(group.iconId&&containerCenters){const show=()=>{const e=effectiveCenter(group.iconId,'');where.textContent=`Symbol center ${e.center[0]}, ${e.center[1]} · ${e.label}`;};watchCenter(group.iconId,show);show();}
      heading.append(label,node('span','chip',`${group.rows.length.toLocaleString()} combination${group.rows.length===1?'':'s'}`));section.append(heading);
      const children=node('div','combination-list container-group-items');section.append(children);
      function fill(){if(section.open&&!children.childElementCount)for(const row of group.rows)children.append(combinationCard(row));}
      section.open=expandedContainers.has(group.key);fill();
      section.addEventListener('toggle',()=>{if(!section.isConnected)return;if(section.open)expandedContainers.add(group.key);else expandedContainers.delete(group.key);fill();});
      list.append(section);
    }
  }else for(const row of rows.slice((page-1)*pageSize,page*pageSize))list.append(combinationCard(row));
  if(!rows.length)list.append(node('p','muted','No combinations match these filters.'));
  host.append(list,pager());
}

// Live typeface v2 editing and container combining for container-text-report.html.
// Layout comes from text-combine.js (window.Typeface); edits stay in this browser and export as JSON.
(function(){
'use strict';
const $=id=>document.getElementById(id);
const DATA=JSON.parse($('reportData').textContent);
const V2=JSON.parse($('glyphV2').textContent), SIZES=JSON.parse($('glyphV2Sizes').textContent);
const STORE='container-text-edits.v1';
const DEFAULTS={size:'native',tracking:4,lineGap:4};
const pairs=new Map();  // combination id → {entry, combination}
for(const e of DATA.icons)for(const c of e.combinations)pairs.set(c.combination_id,{entry:e,combination:c});

let edits={};
try{edits=JSON.parse(localStorage.getItem(STORE)||'{}')||{};}catch{edits={};}
function persist(){try{localStorage.setItem(STORE,JSON.stringify(edits));}catch{}renderEditCount();}

// Container centers: saved (pair, then container) → defaults → 32,32, as on the Container pairs page.
let defaults={containers:{},pairs:{}}, saved={containers:{},pairs:{}};
function containerCenter(containerId){
  const own=saved.containers[containerId], d=defaults.containers[containerId];
  if(own)return {center:own.center.map(Number),label:'saved container center'};
  if(d)return {center:d.center.map(Number),label:'default container center ('+d.source+')'};
  return {center:[32,32],label:'canvas center'};
}

function settings(id){
  const {entry,combination}=pairs.get(id), e=edits[id]||{};
  return {text:e.text??entry.text, size:e.size??DEFAULTS.size, tracking:e.tracking??DEFAULTS.tracking,
          lineGap:e.lineGap??DEFAULTS.lineGap, underline:e.underline??!!entry.underline,
          center:e.center??containerCenter(combination.container_icon_id).center};
}

const glyphCache=new Map();
function glyphs(size){
  if(!glyphCache.has(size))glyphCache.set(size,size==='native'?V2.glyphs:SIZES.sizes[size]);
  return glyphCache.get(size);
}
const capHeight=size=>size==='native'?16:Number(size)-4;

function layoutText(s){
  const h=capHeight(s.size);
  return Typeface.layout(s.text.toUpperCase(),glyphs(s.size),{xHeight:h*36/52,capHeight:h,nativeSize:true,tracking:Number(s.tracking),
    lineGap:Number(s.lineGap),stroke:4,underline:s.underline,padding:0,trimInk:true,align:'center'});
}

const containerSVG=new Map();
function loadContainer(url){
  if(!containerSVG.has(url))containerSVG.set(url,fetch(url,{cache:'no-cache'}).then(r=>{if(!r.ok)throw Error('container '+r.status);return r.text();})
    .then(t=>{const svg=new DOMParser().parseFromString(t,'image/svg+xml').documentElement;svg.querySelector('title')?.remove();
      const attrs=['fill','stroke','stroke-width','stroke-linecap','stroke-linejoin'].filter(a=>svg.hasAttribute(a)).map(a=>`${a}="${svg.getAttribute(a)}"`).join(' ');
      return `<g ${attrs}>${svg.innerHTML}</g>`;}));
  return containerSVG.get(url);
}

// One 64×64 SVG: container artwork plus the text ink box centred on `center`.
async function combinedSVG(id,{grid=false}={}){
  const {combination}=pairs.get(id), s=settings(id), result=layoutText(s);
  const container=await loadContainer(combination.container_preview);
  const x=s.center[0]-result.width/2, y=s.center[1]-result.height/2;
  const text=Typeface.svg(result,s.text).replace(/^<svg[^>]*>/,'').replace(/<\/svg>$/,'').replace(/<title>.*?<\/title>/,'').replaceAll('#202820','currentColor');
  let guides='';
  if(grid){
    for(let i=0;i<=64;i+=2)guides+=`<path d="M${i} 0V64M0 ${i}H64" stroke="${i%8?'#dfe7e2':'#b9c9c0'}" stroke-width="${i%8?.08:.15}"/>`;
    guides+=`<rect x="${x}" y="${y}" width="${result.width}" height="${result.height}" fill="none" stroke="#d9534f" stroke-width=".2" stroke-dasharray=".8 .6"/>`
      +`<path d="M${s.center[0]-1.5} ${s.center[1]}h3M${s.center[0]} ${s.center[1]-1.5}v3" stroke="#d9534f" stroke-width=".25"/>`;
  }
  const svg=`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64" color="#111">${guides}${container}<g transform="translate(${+x.toFixed(4)} ${+y.toFixed(4)})">${text}</g></svg>`;
  return {svg,result,x,y,settings:s};
}

async function paint(el){
  const id=el.dataset.cid;if(!pairs.has(id))return;
  try{el.innerHTML=(await combinedSVG(id)).svg;}catch(error){el.textContent=error.message;el.classList.add('combo-error');}
  el.classList.toggle('edited',!!edits[id]);
}
function paintAll(){document.querySelectorAll('.combo[data-cid]').forEach(paint);}

// Editor dialog.
let current=null;
const dlg=$('editor');
function fillSizes(){
  const sel=$('edSize');sel.replaceChildren(new Option((SIZES.native_size||19)+' · native','native'));
  for(const h of Object.keys(SIZES.sizes).sort((a,b)=>a-b))sel.append(new Option(h+' · hinted',h));
}
function formSettings(){
  return {text:$('edText').value, size:$('edSize').value, tracking:Number($('edTracking').value), lineGap:Number($('edLineGap').value),
          underline:$('edUnderline').checked, center:[Number($('edX').value),Number($('edY').value)]};
}
function sameAsDefault(id,s){
  const {entry,combination}=pairs.get(id), c=containerCenter(combination.container_icon_id).center;
  return s.text===entry.text&&s.size===DEFAULTS.size&&s.tracking===DEFAULTS.tracking&&s.lineGap===DEFAULTS.lineGap&&s.underline===!!entry.underline&&s.center[0]===c[0]&&s.center[1]===c[1];
}
async function refreshEditor(){
  if(!current)return;
  const s=formSettings();
  if(!s.text.trim()){$('edStatus').textContent='Type some text.';return;}
  if(!s.center.every(n=>Number.isFinite(n))){$('edStatus').textContent='Center needs two numbers.';return;}
  if(sameAsDefault(current,s))delete edits[current];else edits[current]=s;persist();
  try{
    const big=await combinedSVG(current,{grid:true}), plain=await combinedSVG(current);
    $('edPreview').innerHTML=big.svg;$('edSmall').innerHTML=plain.svg;$('edTiny').innerHTML=plain.svg;
    const r=big.result, f=n=>+n.toFixed(2), right=big.x+r.width, bottom=big.y+r.height;
    const warn=[];if(big.x<2||big.y<2||right>62||bottom>62)warn.push('ink runs outside the 2-unit margin');
    if(!Number.isInteger(r.width)||!Number.isInteger(r.height))warn.push('ink size is not whole units'+(formSettings().size==='native'?' (native 19 glyphs)':'')+(/ /.test(formSettings().text)?' (space width is fractional)':''));
    $('edStatus').textContent=`Ink ${f(r.width)} × ${f(r.height)} at ${f(big.x)}, ${f(big.y)} → ${f(right)}, ${f(bottom)}`+(warn.length?' · ⚠ '+warn.join(' · '):'');
    $('edStatus').classList.toggle('warn',warn.length>0);
    $('edSource').textContent=edits[current]?'Edited in this browser.':'Defaults · '+containerCenter(pairs.get(current).combination.container_icon_id).label+'.';
  }catch(error){$('edStatus').textContent=error.message;$('edStatus').classList.add('warn');}
  document.querySelectorAll(`.combo[data-cid="${current}"]`).forEach(paint);
}
function openEditor(id){
  current=id;const {entry,combination}=pairs.get(id), s=settings(id);
  $('edTitle').textContent=`${combination.concept} · ${combination.container_icon_id}`;
  $('edMeta').textContent=`${entry.name} · ${entry.source_id} · combination ${id}`;
  $('edOriginal').src='combination-originals/'+id+'.svg';$('edReference').src=entry.reference_url;
  $('edText').value=s.text;$('edSize').value=s.size;$('edTracking').value=s.tracking;$('edLineGap').value=s.lineGap;
  $('edUnderline').checked=s.underline;[$('edX').value,$('edY').value]=s.center;
  dlg.showModal();refreshEditor();
}
function nudge(dx,dy){$('edX').value=Number($('edX').value)+dx;$('edY').value=Number($('edY').value)+dy;refreshEditor();}

function exportEdits(){
  const rows=Object.entries(edits).filter(([id])=>pairs.has(id)).map(([id,s])=>{const {entry,combination}=pairs.get(id);
    return {combination_id:id,concept:combination.concept,container_icon_id:combination.container_icon_id,container_id:combination.container_id,
            source_id:entry.source_id,...s};});
  return JSON.stringify({version:'v2',kind:'container-text-edits',exported_at:new Date().toISOString(),defaults:DEFAULTS,edits:rows},null,1);
}
function renderEditCount(){const n=Object.keys(edits).filter(id=>pairs.has(id)).length;$('editCount').textContent=n?`${n} edited pair${n>1?'s':''} in this browser`:'No edits yet';}

// Wiring.
fillSizes();renderEditCount();
for(const id of ['edText','edSize','edTracking','edLineGap','edUnderline','edX','edY'])$(id).addEventListener('input',refreshEditor);
$('edClose').onclick=()=>dlg.close();
dlg.addEventListener('close',()=>{current=null;});
for(const [id,dx,dy] of [['edLeft',-.5,0],['edRight',.5,0],['edUp',0,-.5],['edDown',0,.5]])$(id).onclick=()=>nudge(dx,dy);
$('edReset').onclick=()=>{if(!current)return;delete edits[current];persist();openEditor(current);};
$('edApplyContainer').onclick=()=>{
  if(!current)return;const s=formSettings(), cid=pairs.get(current).combination.container_icon_id;let n=0;
  for(const [id,p] of pairs)if(id!==current&&p.combination.container_icon_id===cid){const own=settings(id);edits[id]={...own,size:s.size,tracking:s.tracking,lineGap:s.lineGap,center:s.center};n++;}
  persist();paintAll();$('edSource').textContent=`Size, spacing and center copied to ${n} other pair(s) in ${cid}.`;
};
$('edDownload').onclick=async()=>{if(!current)return;const {svg}=await combinedSVG(current);const a=document.createElement('a');
  a.href=URL.createObjectURL(new Blob([svg],{type:'image/svg+xml'}));a.download=`${pairs.get(current).combination.concept.replace(/[^a-z0-9]+/gi,'-')}-${current.slice(0,8)}.svg`;a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000);};
$('copyEdits').onclick=async()=>{try{await navigator.clipboard.writeText(exportEdits());$('editCount').textContent='Copied edits JSON.';}catch{$('editCount').textContent='Clipboard unavailable; use Download.';}};
$('downloadEdits').onclick=()=>{const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([exportEdits()],{type:'application/json'}));a.download='container-text-edits.json';a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000);};
$('clearEdits').onclick=()=>{if(!Object.keys(edits).length)return;edits={};persist();paintAll();};
document.addEventListener('click',e=>{const el=e.target.closest('[data-edit]');if(el&&pairs.has(el.dataset.edit))openEditor(el.dataset.edit);});

// Published default centers; a pair's own box lives in the combination tables (container-pairs.html).
fetch('container-centers.json',{cache:'no-store'}).then(r=>r.ok?r.json():null).catch(()=>null).then(d=>{if(d)defaults=d;paintAll();});
})();

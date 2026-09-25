/* Side pairs as rows of Original → Main → Sub → Combined, optionally grouped by a shared
   main or sub. Subs are shown on the 32×32 system; a pair with several subs keeps one. */
let sidePairs=null, sidePreviews={}, sideStatuses={}, sideLoading=false, sideError='', sideStatus='';
const sidePreviewSub=new Map(), sideRendered=new Map(), sideRenderTargets=new Map(), sideQueue=[], sideFixItems=new WeakMap();
let sideActiveRenders=0;
const SIDE_POSITIONS={br:'Bottom-right',bl:'Bottom-left',tr:'Top-right',tl:'Top-left',ri:'Right',le:'Left',bo:'Bottom',to:'Top'};
// One plain status per pair. Waiting: main and sub are drawn but not in the combine data yet.
const SIDE_STATES={ready:'Ready',fix:'Fix sub',waiting:'Waiting',main:'Needs main',sub:'Needs sub',textsub:'Needs text sub'};
const SIDE_STATE_HINTS={ready:'Main and sub are drawn and can be combined.',fix:'The sub fails a check. Fix it before combining.',waiting:'Main and sub are drawn but not combined yet.',main:'No 48×48 solo main icon yet.',sub:'No 32×32 sub icon yet.',textsub:'The sub is text or a number and is not drawn yet. It is generated separately.'};
const SIDE_FILTERS={'':'All',...SIDE_STATES,text:'Text sub',multi:'2+ subs'};
const sideParams=new URLSearchParams(location.search);
// Main / sub status per source UUID from side-components.json, the same data as the Main icons and Sub icons pages.
let sideComponentStatus={main:new Map(),sub:new Map()},sideComponents=null;
let sideFilter=SIDE_FILTERS[sideParams.get('side')]?sideParams.get('side'):'', sidePageSize=[24,48,96].includes(Number(sideParams.get('size')))?Number(sideParams.get('size')):24;

async function loadSidePairs(){
  if(sideLoading)return;sideLoading=true;
  try{
    const [pairs,previews]=await Promise.all(['experiment-combination.json','experiment-combination-results.json'].map(async url=>{const r=await fetch(url,{cache:'no-store'});if(!r.ok)throw Error('Could not load side pair artwork.');return r.json();}));
    sidePairs=new Map(pairs.rows.map(r=>[r.id,r]));sidePreviews=previews.results||{};sideError='';
    const components=await fetch('side-components.json',{cache:'no-store'}).then(r=>{if(!r.ok)throw Error('Could not load side-components.json.');return r.json();});
    sideComponents=components;
    // Same rule as side-components.js: a passing drawing marked needs fix (review pending) or rejected does not count.
    const reviews=await fetch('/api/reviews',{cache:'no-store'}).then(r=>r.ok?r.json():{}).catch(()=>({}));
    const usable=d=>d.status==='pass'&&!['pending','rejected'].includes(reviews[d.key]);
    for(const item of [...components.mains,...components.subs])item.status=item.drawings.some(usable)?'done':item.drawings.length?'failing':'missing';
    for(const [role,list] of [['main',components.mains],['sub',components.subs]])for(const item of list)for(const id of item.source_ids)sideComponentStatus[role].set(id,item.status);
    // Native text is a separate layout family. Map its exact selected main and
    // sub by source UUID/key, then reuse the already generated native SVG.
    const native=await fetch('side-text-v2.json',{cache:'no-store'}).then(r=>r.ok?r.json():{pairs:[]}).catch(()=>({pairs:[]}));
    sideMapNativeText(native,components,usable);
    // Text / number marks are optional: without them the filter falls back to text-drawn subs.
    try{const r=await fetch('/api/primitives/status',{cache:'no-store'});if(r.ok)sideStatuses=await r.json();}catch{}
  }catch(error){sideError=error.message;}
  finally{sideLoading=false;}
  if(state.view==='side')renderCombinations();
}
function sideMapNativeText(report,components,usable){
  for(const result of report.pairs||[]){
    const row=combinationCatalog.rows.find(r=>r.id===result.id);
    if(!row)continue;
    if(sidePairs.get(row.id)?.subs.some(s=>s.sizing_mode==='typeface-native'))continue;
    const main=components.mains.flatMap(i=>i.drawings).find(d=>d.key===result.main_key&&usable(d));
    const source=components.subs.find(i=>[i.id,...i.source_ids].includes(result.sub_source_id));
    const sub=source?.drawings.find(d=>d.profile==='TEXT_NATIVE_V2'&&usable(d));
    if(!main||!sub)continue;
    const item=d=>({...d,icon:d.icon_id,model_key:d.key,model_validation:'pass'});
    const pair={...row,native_text:true,canvas_width:result.canvas_width||64,canvas_height:result.canvas_height||64,
      mains:[item(main)],subs:[{...item(sub),sizing_kind:'text',native_text:true,
        bounds:[2,2,sub.canvas_width-2,sub.canvas_height-2]}]};
    sidePairs.set(row.id,pair);
    sidePreviews[row.id]={url:result.preview_url,native_text:true,main:main.icon_id,sub:sub.icon_id};
  }
}
const sideSubKey=s=>s.model_key||s.family+'/'+s.icon;
const sideDataURL=svg=>'data:image/svg+xml;charset=utf-8,'+encodeURIComponent(svg);
const sideRound=n=>Math.round(n*10)/10;
// Ink box including the 4px stroke; subs report their normalized 32px ink directly.
function sideInk(item,sub){if(sub&&item.ink32)return [item.ink32.ink_width,item.ink32.ink_height];const b=item.bounds;return [b[2]-b[0]+4,b[3]-b[1]+4];}
function sideSubProblems(s){
  const problems=[],[w,h]=sideInk(s,true);
  if(s.model_validation&&s.model_validation!=='pass')problems.push('Model validation: '+s.model_validation);
  if(['needs_redraw','needs_review'].includes(s.sub32_status))problems.push(s.sub32_reason||'Needs a SUB32 redraw');
  if(!s.native_text&&(w>32.01||h>32.01))problems.push(`Ink ${sideRound(w)}×${sideRound(h)} exceeds 32×32`);
  if(window.SideRepairFlags?.flagged(s))problems.push('Flagged for repair');
  return problems;
}
const sideCurrentSub=pair=>pair.subs.find(s=>s.icon===sidePreviewSub.get(pair.id))||pair.subs[0];
// A sub is text when its source was marked text / number or its current drawing is sized as text.
function sideSubIsText(row,pair){
  const refs=combinationCatalog.references;
  if([row.sub_id,refs[row.sub_id]?.canonical_id].some(id=>id&&sideStatuses[id]?.reason==='text_number'))return true;
  return !!pair?.subs.length&&sideCurrentSub(pair).sizing_kind==='text';
}
// A main counts only as a passing 48×48 solo drawing; a sub only as a 32×32 sub drawing.
function sideKey(row){
  const pair=sidePairs.get(row.id),main=sideComponentStatus.main.get(row.main_id),sub=sideComponentStatus.sub.get(row.sub_id);
  const textSub=sub==='missing'&&sideSubIsText(row,pair);
  if(main!=='done')return sub==='missing'?(textSub?'both-text':'both'):'main';
  if(sub==='missing')return textSub?'textsub':'sub';
  if(sub==='failing')return 'fix';
  if(pair?.mains.length&&pair.subs.length)return sideSubProblems(sideCurrentSub(pair)).length?'fix':'ready';
  return 'waiting';
}
function sideCategory(row){
  const pair=sidePairs.get(row.id),key=sideKey(row);
  const both=key.startsWith('both');
  return {[both?'main':key]:true,...(both?{[key==='both'?'sub':'textsub']:true}:{}),multi:(pair?.subs.length||0)>1,text:sideSubIsText(row,pair)};
}

function sideCombined(pair,sub){
  const prebuilt=sidePreviews[pair.id],placed=role=>prebuilt?.result?.placements?.find(p=>p.role===role)?.icon;
  if(prebuilt?.native_text&&prebuilt.sub===sub.icon&&prebuilt.main===pair.mains[0].icon)return prebuilt;
  if(prebuilt&&placed('sub')===sub.icon&&placed('main')===pair.mains[0].icon)return prebuilt;
  return sideRendered.get(pair.id+'|'+sub.icon);
}
// The hand-set layout the pair's published result was rendered with, when it is for this main and sub.
function sideAdjusted(pair,sub){
  const result=sidePreviews[pair.id]?.result;
  return result?.layout&&result.placements?.every(p=>p.icon===(p.role==='main'?pair.mains[0].icon:sub.icon))?result.layout:null;
}
function sideFillCombined(media,pair,sub){
  const found=sideCombined(pair,sub);media.replaceChildren();
  if(found?.error){media.append(node('span','side-combined-empty',found.error));return;}
  if(!found){media.append(node('span','side-combined-empty','Rendering…'));sideRequestRender(pair,sub,media);return;}
  const img=node('img');img.src=found.url||sideDataURL(found.result.svg);img.alt=pair.concept+' — combined';img.width=img.height=128;
  if(found.native_text){const link=node('a');link.href=found.url;link.target='_blank';link.append(img);media.append(link);}
  else{media.append(img);window.SideCombinationPopup?.attach(img,pair.concept,found.result);}
}
// Renders missing previews on demand, two at a time, and fills the tile if it is still shown.
function sideRequestRender(pair,sub,media){
  const key=pair.id+'|'+sub.icon;
  if(!sideRenderTargets.has(key))sideQueue.push({key,pair,sub});
  sideRenderTargets.set(key,media);sideDrain();
}
function sideDrain(){
  while(sideActiveRenders<2&&sideQueue.length){
    const {key,pair,sub}=sideQueue.shift();sideActiveRenders++;
    fetch('/api/combination-experiment',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({id:pair.id,sub:sub.icon})})
      .then(async r=>{const data=await r.json();if(!r.ok||data.error)throw Error(data.error||'Preview could not be rendered.');sideRendered.set(key,{result:data});})
      .catch(error=>sideRendered.set(key,{error:location.protocol==='file:'?'Open through the local server to render.':error.message}))
      .finally(()=>{sideActiveRenders--;const media=sideRenderTargets.get(key);sideRenderTargets.delete(key);if(media?.isConnected)sideFillCombined(media,pair,sub);sideDrain();});
  }
}

function sidePart(label,item,size,isSub){
  const figure=node('figure','side-part'),art=node('div','side-part-art side-grid-'+size);
  if(item){
    const img=node('img');img.src=item.document?sideDataURL(item.document):item.preview_url;img.alt=label+' '+item.icon;img.loading='lazy';art.append(img);
    const caption=item.native_text?`${label} ${sideRound(item.canvas_width)}×${sideRound(item.canvas_height)} · native`:item.document?`${label} ${sideRound(sideInk(item,isSub)[0])}×${sideRound(sideInk(item,isSub)[1])} / ${size}`:`${label} · generated`;
    figure.append(art,node('figcaption','',caption));
    if(isSub&&item.document){sideFixItems.set(figure,item);sideMarkFix(figure);}
  }else{art.classList.add('side-part-missing');art.append(node('span','',label+' needed'));figure.append(art,node('figcaption','',label+' · '+size+'×'+size));}
  return figure;
}
function sideMarkFix(figure){
  const item=sideFixItems.get(figure);if(!item)return;
  const problems=sideSubProblems(item),art=figure.querySelector('.side-part-art');
  figure.classList.toggle('needs-fix',!!problems.length);art.querySelector('.side-fix-badge')?.remove();
  if(problems.length){const badge=node('span','side-fix-badge','Fix sub');badge.title=problems.join(' · ');art.append(badge);}
  figure.title=problems.join(' · ');
}
document.addEventListener('side-repair-flags-change',()=>{for(const figure of document.querySelectorAll('.side-part'))sideMarkFix(figure);});

function sidePicker(pair,current,rerender){
  const box=node('div','side-picker');box.append(node('p','side-picker-label',`${pair.subs.length} sub candidates · keep one`));
  const options=node('div','side-picker-options');
  for(const s of pair.subs){
    const button=node('button','side-option');button.type='button';button.setAttribute('aria-pressed',String(s===current));
    const problems=sideSubProblems(s),[w,h]=sideInk(s,true),img=node('img');img.src=sideDataURL(s.document);img.alt='';
    button.classList.toggle('needs-fix',!!problems.length);button.title=problems.join(' · ')||'Passing SUB32';
    button.append(img,node('span','side-option-name',s.icon),node('span','side-option-size',`${sideRound(w)}×${sideRound(h)} / 32${problems.length?' · fix':''}`));
    button.onclick=()=>{sidePreviewSub.set(pair.id,s.icon);rerender();};options.append(button);
  }
  const keep=node('button','side-keep','Keep this sub · remove others');keep.type='button';keep.setAttribute('data-development-only','');
  keep.onclick=()=>sideConfirmKeep(pair,current,keep);
  box.append(options,keep);return box;
}

let sideDialogElement=null;
function sideKeepDialog(){
  if(sideDialogElement)return sideDialogElement;
  const dialog=sideDialogElement=node('dialog','side-keep-dialog');
  dialog.innerHTML='<h2>Remove the other subs?</h2><p class="side-keep-summary"></p><ul></ul><p class="side-keep-warning">Removal is permanent. Each icon’s Python model, published SVG, reviews and feedback are deleted, and a copy is archived on the server. Every side pair that lists it loses it.</p><p class="side-keep-error" role="alert"></p><div class="side-keep-actions"><button type="button" class="side-keep-cancel">Cancel</button><button type="button" class="side-keep-confirm"></button></div>';
  document.body.append(dialog);
  dialog.querySelector('.side-keep-cancel').onclick=()=>dialog.close();
  return dialog;
}
async function sideKeepRequest(body){
  const response=await fetch('/api/combinations/side/keep-sub',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
  const data=await response.json();if(!response.ok)throw Error(data.error||'Could not remove the other subs.');return data;
}
async function sideConfirmKeep(pair,current,button){
  const sideDialog=sideKeepDialog();
  const body={pair_id:pair.id,keep:sideSubKey(current)};button.disabled=true;
  let plan;
  try{plan=await sideKeepRequest({...body,dry_run:true});}
  catch(error){sideStatus=error.message;renderCombinations();return;}
  finally{button.disabled=false;}
  sideDialog.querySelector('.side-keep-summary').textContent=`Keep ${current.icon} for “${pair.concept}”. This removes:`;
  sideDialog.querySelector('ul').replaceChildren(...plan.remove.map(r=>node('li','',`${r.icon} — used by ${r.pairs.toLocaleString()} side pair${r.pairs===1?'':'s'}`)));
  const confirm=sideDialog.querySelector('.side-keep-confirm'),error=sideDialog.querySelector('.side-keep-error');
  confirm.textContent=`Remove ${plan.remove.length} icon${plan.remove.length===1?'':'s'}`;confirm.disabled=false;error.textContent='';
  confirm.onclick=async()=>{
    confirm.disabled=true;confirm.textContent='Removing…';
    try{
      const result=await sideKeepRequest(body),removed=new Set(result.removed);
      for(const row of sidePairs.values())row.subs=row.subs.filter(s=>!removed.has(sideSubKey(s)));
      for(const id of result.affected_pairs)sidePreviewSub.delete(id);
      const failed=result.failed.map(f=>`${f.name||f.icon}: ${f.error}`).join(' · ');
      sideStatus=`Kept ${current.icon}. Removed ${result.removed.length} icon${result.removed.length===1?'':'s'} from ${result.affected_pairs.length} side pairs.`+(failed?' Not removed — '+failed:'');
      sideDialog.close();renderCombinations();
    }catch(e){error.textContent=e.message;confirm.disabled=false;confirm.textContent='Retry';}
  };
  sideDialog.showModal();
}

/* Each pair is one row: Original → Main → Sub → Combined, with one main and one sub. */
function sideParts(row){
  const refs=combinationCatalog.references,pair=sidePairs.get(row.id);
  const key=sideKey(row),hasMain=!['main','both','both-text'].includes(key),hasSub=!['sub','textsub','both','both-text'].includes(key);
  if(pair?.mains.length&&pair.subs.length&&hasMain&&hasSub)return {pair,key,main:pair.mains.find(m=>m.family==='solo'||m.family==='combination_main')||pair.mains[0],sub:sideCurrentSub(pair),ready:true};
  const main=combinationMain(row).generated.find(g=>/^(solo|combination_main)\//.test(g.key)),sub=(row.sub_generated??refs[row.sub_id].generated).find(g=>/^(sub|text)\//.test(g.key));
  return {pair,key,main:hasMain&&main&&{icon:main.icon_id,preview_url:main.preview_url,pending:true},sub:hasSub&&sub&&{icon:sub.icon_id,preview_url:sub.preview_url,pending:true},ready:false};
}
function sideState(row,parts){
  const key=parts.key.startsWith('both')?'main':parts.key,label=parts.key==='both'?'Needs main + sub':parts.key==='both-text'?'Needs main + text sub':SIDE_STATES[key];
  return [label,{ready:'ready',fix:'fix',waiting:'waiting',textsub:'info'}[key]||'needed',SIDE_STATE_HINTS[key]];
}
function sideStep(label,content,name){
  const step=node('div','side-step');step.append(node('p','side-step-label',label),content);
  if(name)step.append(node('p','side-step-name',name));return step;
}
function sideRow(row){
  const refs=combinationCatalog.references,ref=refs[row.id],parts=sideParts(row),{pair,main,sub}=parts;
  const card=node('article','side-row'),head=node('div','side-row-head'),[label,tone,hint]=sideState(row,parts);
  head.append(node('h3','',row.concept),node('span','side-meta',(SIDE_POSITIONS[pair?.position]||pair?.position||'Side')+' · '+(pair?.native_text?`${sideRound(pair.canvas_width)}×${sideRound(pair.canvas_height)}`:'64×64')),Object.assign(node('span','side-state '+tone,label),{title:hint}));
  if(sideSubIsText(row,pair))head.append(node('span','side-state info','Text sub'));
  if(pair?.mains.length>1)head.append(node('span','side-state info',`${pair.mains.length} mains · showing first`));
  if(parts.ready&&sideAdjusted(pair,sub))head.append(Object.assign(node('span','side-state info','Adjusted layout'),{title:'Main / sub positions and sizes were set by hand.'}));
  card.append(head);
  const original=node('div','side-original');
  if(ref?.reference_url){const img=node('img');img.src=ref.reference_url;img.alt=row.concept+' — original';img.loading='lazy';original.append(img);}
  else original.append(node('span','side-combined-empty','Reference missing'));
  const media=node('div','side-combined');
  if(parts.ready)sideFillCombined(media,pair,sub);else media.append(node('span','side-combined-empty','Not combined yet'));
  const steps=node('div','side-steps');
  const mainPart=sidePart('Main',main,48,false),subPart=sidePart('Sub',sub,32,true);
  if(main)sideInspectable(mainPart,'Main',main,48,row.concept);if(sub)sideInspectable(subPart,'Sub',sub,32,row.concept);
  steps.append(sideStep('Original',original),sideStep('Main · 48',mainPart,main?.icon),sideStep(sub?.native_text?'Sub · native':'Sub · 32',subPart,sub?.icon),sideStep(pair?.native_text?'Combined · native':'Combined · 64',media));
  card.append(steps);
  if(pair?.subs.length>1){
    const resolve=node('details','side-resolve');resolve.append(node('summary','',`${pair.subs.length} subs · keep one`),sidePicker(pair,sub,()=>card.replaceWith(sideRow(row))));
    resolve.open=sidePreviewSub.has(pair.id);card.append(resolve);
  }
  if(parts.ready){
    const actions=node('div','pair-card-actions'),found=sideCombined(pair,sub);
    if(found?.url){const a=node('a');a.href=found.url;a.download=pair.id+'.svg';window.SideRepairFlags?.download(a);actions.append(a);}
    if(window.SideRepairFlags&&!pair.native_text)actions.append(SideRepairFlags.button('main',main,pair),SideRepairFlags.button('sub',sub,pair));
    if(window.SideLayoutEditor&&!pair.native_text)actions.append(SideLayoutEditor.button(pair,main,sub,data=>{
      // The saved (or reset) layout is republished; show it here without a reload.
      sidePreviews[pair.id]={fingerprint:data.fingerprint,url:data.url,result:data.result};sideRendered.delete(pair.id+'|'+sub.icon);
      if(card.isConnected)card.replaceWith(sideRow(row));
    },sideAdjusted(pair,sub)));
    if(actions.childElementCount)card.append(actions);
  }
  return card;
}

/* Clicking a main or sub opens it large on its own grid with its stroke centerline. */
const SIDE_NS='http://www.w3.org/2000/svg';
let sideInspectDialog=null,sideInspectView='both';
function sideInspectable(figure,label,item,size,concept){
  const art=figure.querySelector('.side-part-art');art.classList.add('side-inspectable');art.tabIndex=0;art.setAttribute('role','button');art.setAttribute('aria-label',`Inspect ${label.toLowerCase()} ${item.icon}`);
  const openIt=()=>sideInspect(label,item,size,concept);
  art.onclick=openIt;art.onkeydown=e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();openIt();}};
}
function sideSvgEl(name,attrs){const e=document.createElementNS(SIDE_NS,name);for(const [k,v] of Object.entries(attrs))e.setAttribute(k,v);return e;}
async function sideDocument(item){
  if(item.document)return item.document;
  const r=await fetch(item.preview_url,{cache:'no-store'});if(!r.ok)throw Error('Artwork unavailable');return r.text();
}
// Artwork in soft gray, the same paths as a thin centerline on top, over a one-unit grid.
function sideInspectSVG(text){
  const source=new DOMParser().parseFromString(text,'image/svg+xml').documentElement;if(source.nodeName!=='svg')throw Error('Artwork is not an SVG');
  const box=(source.getAttribute('viewBox')||`0 0 ${source.getAttribute('width')||48} ${source.getAttribute('height')||48}`).split(/[\s,]+/).map(Number),[x,y,w,h]=box;
  const svg=sideSvgEl('svg',{viewBox:box.join(' '),class:'side-component-canvas',role:'img'});
  const grid=sideSvgEl('g',{'aria-hidden':'true'});
  for(let i=0;i<=w;i++)grid.append(sideSvgEl('line',{x1:x+i,y1:y,x2:x+i,y2:y+h,stroke:i%8===0?'#9eb3bd':'#dae4e9','stroke-width':i%8===0?.1:.045}));
  for(let i=0;i<=h;i++)grid.append(sideSvgEl('line',{x1:x,y1:y+i,x2:x+w,y2:y+i,stroke:i%8===0?'#9eb3bd':'#dae4e9','stroke-width':i%8===0?.1:.045}));
  const art=sideSvgEl('g',{class:'side-component-art'}),line=sideSvgEl('g',{class:'side-component-centerline','aria-hidden':'true'});
  for(const a of ['fill','stroke','stroke-width','stroke-linecap','stroke-linejoin'])if(source.hasAttribute(a))art.setAttribute(a,source.getAttribute(a));
  if(!art.hasAttribute('stroke'))art.setAttribute('stroke','currentColor');
  for(const child of [...source.children]){if(['title','desc','metadata'].includes(child.localName))continue;art.append(document.importNode(child,true));}
  const trace=art.cloneNode(true);
  for(const e of [trace,...trace.querySelectorAll('*')]){e.removeAttribute('id');if(e!==trace&&e.getAttribute('fill')&&e.getAttribute('fill')!=='none'&&!e.hasAttribute('stroke'))continue;e.setAttribute('stroke','#ef4444');e.setAttribute('stroke-width','.3');e.setAttribute('fill','none');}
  line.append(...trace.childNodes);svg.append(grid,art,line);
  return {svg,width:w,height:h};
}
function sideInspect(label,item,size,concept){
  if(!sideInspectDialog){
    const d=sideInspectDialog=node('dialog','side-inspect side-component-inspect');
    d.innerHTML='<header><h2></h2><button type="button" class="side-inspect-close">Close</button></header><div class="side-component-controls" role="group" aria-label="Display"><button type="button" data-view="both">Artwork + centerline</button><button type="button" data-view="art">Artwork</button><button type="button" data-view="line">Centerline only</button><a target="_blank" rel="noopener">Open SVG</a></div><div class="side-stage"></div><dl class="side-component-facts"></dl>';
    document.body.append(d);d.querySelector('.side-inspect-close').onclick=()=>d.close();
    d.onclick=e=>{if(e.target===d){const r=d.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)d.close();}};
    for(const b of d.querySelectorAll('[data-view]'))b.onclick=()=>{sideInspectView=b.dataset.view;sideInspectApply();};
  }
  const d=sideInspectDialog,stage=d.querySelector('.side-stage'),facts=d.querySelector('.side-component-facts'),link=d.querySelector('a');
  d.querySelector('h2').textContent=`${label} · ${item.icon}`;stage.replaceChildren(node('p','muted','Loading artwork…'));facts.replaceChildren();
  link.href=item.document?sideDataURL(item.document):item.preview_url;
  sideInspectApply();if(!d.open)d.showModal();
  sideDocument(item).then(text=>{
    const {svg,width,height}=sideInspectSVG(text);svg.setAttribute('aria-label',`${item.icon} on a ${width} by ${height} grid`);stage.replaceChildren(svg);
    const rows=[['Pair',concept],['Family',item.family||item.model_key?.split('/')[0]||'generated'],['Canvas',`${sideRound(width)}×${sideRound(height)}`]];
    if(item.bounds){const [w,h]=sideInk(item,label==='Sub');rows.push(['Ink',`${sideRound(w)}×${sideRound(h)} / ${size}`]);}
    if(item.sizing_kind)rows.push(['Sizing',item.sizing_kind]);
    if(item.model_validation)rows.push(['Validation',item.model_validation]);
    if(item.sub32_status)rows.push(['SUB32 status',item.sub32_status+(item.sub32_reason?' · '+item.sub32_reason:'')]);
    if(label==='Sub'&&item.document){const problems=sideSubProblems(item);rows.push(['Problems',problems.join(' · ')||'None']);}
    if(item.pending)rows.push(['Status','Waiting to combine']);
    if(item.python_source)rows.push(['Python model',item.python_source]);
    if(item.svg)rows.push(['SVG',item.svg]);
    for(const [k,v] of rows)facts.append(node('dt','',k),node('dd','',v));
  }).catch(error=>stage.replaceChildren(node('p','muted',error.message)));
}
function sideInspectApply(){
  const d=sideInspectDialog;d.dataset.view=sideInspectView;
  for(const b of d.querySelectorAll('[data-view]'))b.setAttribute('aria-pressed',String(b.dataset.view===sideInspectView));
}

/* Grouping collects pairs that reuse the same main or the same sub icon. */
const SIDE_GROUPS={'':'No grouping',main:'Group by main',sub:'Group by sub'};
let sideGroup=SIDE_GROUPS[sideParams.get('group')]?sideParams.get('group'):'';
const sideOpenGroups=new Set();
function sideGroups(rows){
  const refs=combinationCatalog.references,groups=new Map();
  for(const row of rows){
    const item=sideParts(row)[sideGroup],sourceId=sideGroup==='main'?row.main_id:row.sub_id;
    const key=item?sideGroup+'/'+item.icon:'needed/'+sourceId;
    if(!groups.has(key))groups.set(key,{key,item,title:item?item.icon:(refs[sourceId]?.concept||sourceId),rows:[]});
    groups.get(key).rows.push(row);
  }
  return [...groups.values()].sort((a,b)=>b.rows.length-a.rows.length||a.title.localeCompare(b.title));
}
function sideGroupSection(group){
  const section=node('details','container-group side-group'),heading=node('summary','container-group-heading'),item=group.item;
  if(item){const img=node('img');img.src=item.document?sideDataURL(item.document):item.preview_url;img.alt='';img.loading='lazy';heading.append(img);}
  const size=sideGroup==='main'?48:32,info=node('span','container-group-label');
  const detail=!item?`${sideGroup==='main'?'Main':'Sub'} needed`:item.pending?`Drawn ${sideGroup} · waiting`:item.document?`Shared ${sideGroup} · ${sideRound(sideInk(item,sideGroup==='sub')[0])}×${sideRound(sideInk(item,sideGroup==='sub')[1])} / ${size}`:`Shared ${sideGroup}`;
  info.append(node('strong','',group.title),node('span','muted',detail));
  heading.append(info,node('span','chip',`${group.rows.length.toLocaleString()} pair${group.rows.length===1?'':'s'}`));
  const children=node('div','side-list container-group-items');section.append(heading,children);
  const fill=()=>{if(section.open&&!children.childElementCount)children.append(...group.rows.map(sideRow));};
  section.open=sideOpenGroups.has(group.key);fill();
  section.addEventListener('toggle',()=>{if(!section.isConnected)return;if(section.open)sideOpenGroups.add(group.key);else sideOpenGroups.delete(group.key);fill();});
  return section;
}

/* Combine all reruns the side-pair refresh job on the server and reloads the rows. */
let sideCombine={status:'idle',message:''},sideCombinePolling=false,sideCombineChecked=false;
function sideCombineShow(){
  const button=document.getElementById('sideCombineAll'),status=document.getElementById('sideCombineStatus');
  if(button)button.disabled=sideCombine.status==='running';
  if(status)status.textContent=sideCombine.status==='running'?(sideCombine.message||'Combining…'):sideCombine.status==='error'?sideCombine.message+' You can retry.':'Main + chosen sub for every side pair. Results appear on Experiment › Side combination.';
}
async function sideCombineRequest(method){
  const init=method==='POST'?{method,headers:{'Content-Type':'application/json'},body:'{}'}:{method,cache:'no-store'};
  const response=await fetch('/api/combination-refresh',init),data=await response.json();
  if(!response.ok)throw Error(data.error||'Could not combine side pairs.');return data;
}
async function sideCombinePoll(){
  if(sideCombinePolling)return;sideCombinePolling=true;
  try{
    while(sideCombine.status==='running'){await new Promise(r=>setTimeout(r,2000));sideCombine=await sideCombineRequest('GET');sideCombineShow();}
    if(sideCombine.status==='complete'){
      sideStatus='Combined all side pairs. '+(sideCombine.message||'');sideCombine={status:'idle',message:''};
      sidePairs=null;sidePreviews={};sideRendered.clear();loadSidePairs();
    }
  }catch(error){sideCombine={status:'error',message:error.message};sideCombineShow();}
  finally{sideCombinePolling=false;}
}
async function sideCombineAll(){
  sideCombine={status:'running',message:'Starting…'};sideCombineShow();
  try{sideCombine=await sideCombineRequest('POST');sideCombineShow();sideCombinePoll();}
  catch(error){sideCombine={status:'error',message:error.message};sideCombineShow();}
}
// A refresh started earlier (or from another tab) keeps reporting progress here.
async function sideCombineCheck(){
  if(sideCombineChecked)return;sideCombineChecked=true;
  try{const data=await sideCombineRequest('GET');if(data.status==='running'){sideCombine=data;sideCombineShow();sideCombinePoll();}}catch{}
}

function writeSideURL(){
  const u=new URL(location.href);
  if(sideFilter)u.searchParams.set('side',sideFilter);else u.searchParams.delete('side');
  if(sidePageSize!==24)u.searchParams.set('size',sidePageSize);else u.searchParams.delete('size');
  if(sideGroup)u.searchParams.set('group',sideGroup);else u.searchParams.delete('group');
  history.replaceState(null,'',u);
}
// Side pairs are built from X main icons and Y sub icons; count the icons, the same way the Main icons and Sub icons pages do.
function sideIconSummary(pairCount){
  const isText=i=>[i.id,...i.source_ids].some(id=>sideStatuses[id]?.reason==='text_number');
  const mains=sideComponents.mains,subs=sideComponents.subs,textSubs=subs.filter(isText),iconSubs=subs.filter(i=>!isText(i));
  const count=(list,status)=>list.filter(i=>i.status===status).length;
  const wrap=node('section','side-icon-summary');
  wrap.append(node('p','side-icon-total',`${pairCount.toLocaleString()} side pairs, made from ${mains.length.toLocaleString()} main icons and ${subs.length.toLocaleString()} sub icons.`));
  const group=(title,total,page,cells)=>{
    const box=node('div','side-icon-group'),head=node('a','side-icon-head');head.href=page;head.append(node('strong','',title),node('span','',total.toLocaleString()+' icons →'));box.append(head);
    const row=node('div','side-icon-cells');
    for(const [label,value,status,tone] of cells){const a=node('a','side-icon-cell '+tone);a.href=page+'?status='+status;a.append(node('strong','',value.toLocaleString()),node('span','',label));row.append(a);}
    box.append(row);return box;
  };
  wrap.append(
    group('Main icons',mains.length,'side-mains.html',[['Generated',count(mains,'done'),'done','ok'],['Needs fix',count(mains,'failing'),'failing','fix'],['Not generated',count(mains,'missing'),'missing','todo']]),
    group('Sub icons',subs.length,'side-subs.html',[['Generated',count(iconSubs,'done'),'done','ok'],['Text',textSubs.length,'text','text'],['Needs fix',count(iconSubs,'failing'),'failing','fix'],['Not generated',count(iconSubs,'missing'),'missing','todo']]));
  return wrap;
}
function renderSideGrid(host,all,summary){
  if(!sidePairs){
    host.append(node('p','muted',sideError||'Loading side pairs…'));
    if(sideError){const retry=node('button','','Retry');retry.onclick=()=>{sideError='';loadSidePairs();renderCombinations();};host.append(retry);}
    else loadSidePairs();
    return;
  }
  const categories=new Map(all.map(r=>[r.id,sideCategory(r)])),count=key=>[...categories.values()].filter(c=>c[key]).length;
  summary.replaceWith(sideIconSummary(all.length));
  const combine=node('div','toolbar side-combine'),combineButton=node('button','','Combine all side pairs'),combineStatus=node('span','muted');
  combineButton.id='sideCombineAll';combineButton.type='button';combineButton.setAttribute('data-development-only','');combineButton.onclick=sideCombineAll;
  combineStatus.id='sideCombineStatus';combineStatus.setAttribute('role','status');combine.append(combineButton,combineStatus);host.append(combine);
  sideCombineShow();sideCombineCheck();
  const gallery=node('section');gallery.id='pairGallery';host.append(gallery);
  if(sideStatus){const status=node('p','side-status',sideStatus);status.setAttribute('role','status');gallery.append(status);}
  const toolbar=node('div','toolbar'),search=node('input'),filter=node('select'),group=node('select'),size=node('select');
  search.type='search';search.placeholder='Search concept, component ID or icon name';search.setAttribute('aria-label','Search side pairs');search.value=state.q;
  filter.setAttribute('aria-label','Side pair filter');filter.append(...Object.entries(SIDE_FILTERS).map(([k,v])=>new Option(v,k)));filter.value=sideFilter;
  group.setAttribute('aria-label','Group side pairs');group.append(...Object.entries(SIDE_GROUPS).map(([k,v])=>new Option(v,k)));group.value=sideGroup;
  size.setAttribute('aria-label','Items per page');size.append(...[24,48,96].map(n=>new Option(n+(sideGroup?' groups':' pairs')+' per page',n)));size.value=sidePageSize;
  filter.onchange=()=>{sideFilter=filter.value;page=1;renderCombinations();};
  group.onchange=()=>{sideGroup=group.value;page=1;renderCombinations();};
  size.onchange=()=>{sidePageSize=Number(size.value);page=1;renderCombinations();};
  let timer;search.oninput=()=>{clearTimeout(timer);timer=setTimeout(()=>{const cursor=search.selectionStart;state.q=search.value;page=1;renderCombinations();const next=host.querySelector('input[type=search]');next.focus();if(cursor!==null)next.setSelectionRange(cursor,cursor);},180);};
  toolbar.append(search,filter,group,size);gallery.append(toolbar);
  const q=state.q.trim().toLowerCase(),refs=combinationCatalog.references;
  const rows=all.filter(r=>{
    if(sideFilter&&!categories.get(r.id)[sideFilter])return false;if(!q)return true;
    const pair=sidePairs.get(r.id);
    return [r.concept,r.id,r.main_id,r.sub_id,refs[r.main_id]?.concept,refs[r.sub_id]?.concept,...(pair?[...pair.mains,...pair.subs].map(m=>m.icon):[])].join(' ').toLowerCase().includes(q);
  });
  const groups=sideGroup?sideGroups(rows):null,items=groups||rows;
  const pages=Math.max(1,Math.ceil(items.length/sidePageSize));page=Math.min(page,pages);writeURL();writeSideURL();
  function pager(){const bar=node('div','pager'),prev=node('button','','← Previous'),next=node('button','','Next →');prev.disabled=page<=1;next.disabled=page>=pages;prev.onclick=()=>{page--;renderCombinations();host.scrollIntoView();};next.onclick=()=>{page++;renderCombinations();host.scrollIntoView();};bar.append(prev,node('span','muted',`${rows.length.toLocaleString()} pairs${groups?' · '+groups.length.toLocaleString()+' '+(sideGroup==='main'?'main':'sub')+' icons':''} · Page ${page} of ${pages}`),next);return bar;}
  const list=node('div','side-list'),visible=items.slice((page-1)*sidePageSize,page*sidePageSize);
  list.append(...visible.map(groups?sideGroupSection:sideRow));
  if(!rows.length)list.append(node('p','muted','No side pairs match these filters.'));
  gallery.append(pager(),list,pager());
  window.SideRepairFlags?.setRows([...sidePairs.values()]);
}

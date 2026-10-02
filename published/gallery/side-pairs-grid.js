/* Side pairs as rows of Original → Main → Sub → Combined, optionally grouped by a shared
   main or sub. Subs are shown on the 32×32 system; a pair with several subs keeps one. */
let sidePairs=null, sidePreviews={}, sideStatuses={}, sideLoading=false, sideError='', sideStatus='';
const sidePreviewSub=new Map(), sideRendered=new Map(), sideRenderTargets=new Map(), sideQueue=[], sideFixItems=new WeakMap();
let sideActiveRenders=0;
const SIDE_POSITIONS={br:'Bottom-right',bl:'Bottom-left',tr:'Top-right',tl:'Top-left',ri:'Right',le:'Left',bo:'Bottom',to:'Top'};
// One plain status per pair. Waiting: main and sub are drawn but not in the combine data yet.
const SIDE_STATES={ready:'Ready',fix:'Fix sub',fixmain:'Fix main',waiting:'Waiting',main:'Needs main',sub:'Needs sub',textsub:'Needs text sub'};
const SIDE_STATE_HINTS={ready:'Main and sub are drawn and can be combined.',fix:'The sub fails a check. Fix it before combining.',fixmain:'A 48×48 main is drawn but fails validation or was marked needs fix, so it is not in Icon review. Fix it on the Main icons page (Needs fix).',waiting:'Main and sub are drawn but not combined yet.',main:'No 48×48 solo main icon yet.',sub:'No 32×32 sub icon yet.',textsub:'The sub is text or a number and is not drawn yet. It is generated separately.'};
const SIDE_FILTERS={'':'All',...SIDE_STATES,uncombined:'Not combined',text:'Text sub',multi:'2+ subs',made:'From review',changed:'Main / sub changed',
  built:'Built',stale:'Stale (built from older drawings)',unbuilt:'Not built'};
const sideParams=new URLSearchParams(location.search);
// Main / sub status per source UUID from side-components.json, the same data as the Main icons and Sub icons pages.
let sideComponentStatus={main:new Map(),sub:new Map()},sideComponents=null;
// The latest Combine all side pairs run (side-combination64.json) and review states, shared with Experiment and Icon review.
let sideRun=null,sideReviews={};
// The pair size: 64 (a 48 main + a 32 sub) or 72 (a main-54 + a sub-36), ?grid=72.
SideData.setSize(sideParams.get('grid')==='72'?72:64);
const sideSizes=()=>SideData.sizes();
let sideFilter=SIDE_FILTERS[sideParams.get('side')]?sideParams.get('side'):'', sidePageSize=[24,48,96].includes(Number(sideParams.get('size')))?Number(sideParams.get('size')):24;

async function loadSidePairs(){
  if(sideLoading)return;sideLoading=true;
  try{
    // From D1 (side-pairs-data.js): every side pair with its picked main and sub, the components, reviews and statuses.
    const data=await SideData.load();
    combinationCatalog=data.catalog;sidePairs=data.pairs;sidePreviews=data.previews;sideError='';
    const components=sideComponents=data.components;
    sideReviews=data.reviews;
    if(Object.keys(sideReviews).length)window.SideRepairFlags?.setReviews(sideReviews);
    sideRun=data.run;sideStatuses=data.statuses;
    const usable=sideUsable;
    for(const item of [...components.mains,...components.subs])item.status=item.drawings.some(usable)?'done':item.drawings.length?'failing':'missing';
    for(const [role,list] of [['main',components.mains],['sub',components.subs]])for(const item of list)for(const id of item.source_ids)sideComponentStatus[role].set(id,item.status);
    sideMadeStatuses();
  }catch(error){sideError=error.message;}
  finally{sideLoading=false;sideCombineChecked=false;}
  if(state.view==='side')renderCombinations();
  if(!sideError)sideFollowLink();
}
// ?edit=<pair> opens the pair's layout editor; ?make=<primitive>[&position=] makes its side pair and opens its main /
// sub picker (links from Combinations, Experiment and side-pairs.html). Once per page.
let sideLinkDone=false;
async function sideFollowLink(){
  if(sideLinkDone)return;sideLinkDone=true;
  // Read when this script loaded: the page rewrites its URL from its own state before the pairs arrive.
  const params=sideParams,edit=params.get('edit'),make=params.get('make');
  const strip=()=>{const u=new URL(location.href);u.searchParams.delete('edit');u.searchParams.delete('make');u.searchParams.delete('position');history.replaceState(null,'',u);};
  if(make){
    try{
      if(!sidePairs.has(make)){
        const response=await fetch('/api/combinations/pair',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({reference_id:make,position:params.get('position')||'br'})});
        const data=await response.json().catch(()=>({}));if(!response.ok)throw Error(data.error||'Could not make the side pair.');
        await sideMadeRefresh(make);
      }
      state.q=make;page=1;strip();renderCombinations();
      document.querySelector('.side-row[data-pair-id="'+CSS.escape(make)+'"] .side-pair-editor button')?.click();
    }catch(error){sideStatus='Could not make the side pair: '+error.message;strip();renderCombinations();}
    return;
  }
  if(edit&&sidePairs.has(edit)){
    state.q=edit;page=1;strip();renderCombinations();
    document.querySelector('.side-row[data-pair-id="'+CSS.escape(edit)+'"] .side-layout-open')?.click();
  }
}
// A pair whose main / sub has no catalog drawing (picked by key, or made here): its status is the picked drawing's.
function sideMadeStatuses(){
  for(const pair of sidePairs.values())for(const role of ['main','sub']){
    const id=pair[role+'_id'],item=pair[role+'s'][0];
    if(!id||!item||sideComponentStatus[role].get(id)==='done')continue;
    sideComponentStatus[role].set(id,sideUsable({key:item.model_key,status:'pass'})?'done':'failing');
  }
}
// After a pair changed here (a build, a pick, a layout): read it again from D1 and redraw its row.
async function sideMadeRefresh(pairId){
  // null: the pair is gone from D1; undefined: it could not be read (kept as it was).
  const got=await SideData.refresh(pairId).catch(error=>{sideStatus=error.message;return undefined;});
  if(got){
    sidePairs.set(pairId,got.pair);Object.assign(combinationCatalog.references,got.references);
    const rows=combinationCatalog.rows,at=rows.findIndex(r=>r.id===pairId);if(at<0)rows.unshift(got.row);else rows[at]=got.row;
    if(got.preview)sidePreviews[pairId]=got.preview;else delete sidePreviews[pairId];
    sideMadeStatuses();
  }else if(got===null){
    // Removed (a pair made here and taken back): it leaves the list.
    sidePairs.delete(pairId);delete sidePreviews[pairId];
    combinationCatalog.rows=combinationCatalog.rows.filter(r=>r.id!==pairId);
  }
  for(const key of [...sideRendered.keys()])if(key.startsWith(pairId+'|'))sideRendered.delete(key);
  renderCombinations();
}
// Same rule as side-components.js: a passing drawing marked needs fix (review pending) or rejected does not count;
// a failing drawing counts once a reviewer approved it as an exception.
const sideUsable=d=>(d.status==='pass'||sideReviews[d.key]==='approve')&&!['pending','rejected'].includes(sideReviews[d.key]);
// Why a drawing shown on a tile does not count: failed checks or its review state.
function sideDrawingProblems(d){
  if(!d||sideUsable(d))return [];
  if(d.status!=='pass')return d.errors?.length?d.errors:['Fails validation'];
  return [sideReviews[d.key]==='rejected'?'Rejected in Icon review':'Disapproved — needs fix'];
}
const sideSubKey=s=>s.model_key||s.family+'/'+s.icon;
const sideDataURL=svg=>'data:image/svg+xml;charset=utf-8,'+encodeURIComponent(svg);
const sideRound=n=>Math.round(n*10)/10;
// Ink box including the 4px stroke; subs report their normalized 32px ink directly.
function sideInk(item,sub){if(sub&&item.ink32)return [item.ink32.ink_width,item.ink32.ink_height];const b=item.bounds;
  // A made pair's items are measured by the combine engine only; its sub is a sub-family icon, checked at 32 by its build.
  if(!b)return [0,0];return [b[2]-b[0]+4,b[3]-b[1]+4];}
function sideSubProblems(s){
  const problems=[],[w,h]=sideInk(s,true);
  if(s.model_validation&&s.model_validation!=='pass')problems.push('Model validation: '+s.model_validation);
  if(['needs_redraw','needs_review'].includes(s.sub32_status))problems.push(s.sub32_reason||'Needs a SUB32 redraw');
  if(!s.native_text&&(w>32.01||h>32.01))problems.push(`Ink ${sideRound(w)}×${sideRound(h)} exceeds 32×32`);
  if(window.SideRepairFlags?.flagged(s))problems.push('Disapproved — needs fix');
  return problems;
}
const sideCurrentSub=pair=>pair.subs.find(s=>s.icon===sidePreviewSub.get(pair.id))||pair.subs[0];
// The main a row shows and combines (the server picks the same one when none is named).
const sideMain=pair=>pair.mains.find(m=>m.family==='solo'||m.family==='combination_main')||pair.mains[0];
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
  // A drawn main that fails is a fix, not a missing main; the tile still shows that drawing.
  if(main==='failing')return 'fixmain';
  if(main!=='done')return sub==='missing'?(textSub?'both-text':'both'):'main';
  if(sub==='missing')return textSub?'textsub':'sub';
  if(sub==='failing')return 'fix';
  if(pair?.mains.length&&pair.subs.length)return sideSubProblems(sideCurrentSub(pair)).length?'fix':'ready';
  return 'waiting';
}
function sideCategory(row){
  const pair=sidePairs.get(row.id),key=sideKey(row);
  const both=key.startsWith('both');
  // Not combined: main and sub are both drawn, but the last Combine all run made no icon for the pair.
  const uncombined=!['main','fixmain','sub','textsub'].includes(key)&&!both&&!sidePreviews[row.id];
  const subNeeded=key==='fixmain'&&sideComponentStatus.sub.get(row.sub_id)==='missing'?(sideSubIsText(row,pair)?'textsub':'sub'):null;
  // The pair's build in D1: built, stale (a part redrawn since) or not built.
  const build=SideData.item(row.id)?.state;
  return {[build||'unbuilt']:true,made:!!pair?.custom&&!pair.published,changed:!!pair?.published,[both?'main':key]:true,...(both?{[key==='both'?'sub':'textsub']:true}:{}),...(subNeeded?{[subNeeded]:true}:{}),uncombined,multi:(pair?.subs.length||0)>1,text:sideSubIsText(row,pair)};
}

// The pair's stored combined icon (D1), else the one composed here from the current drawings.
function sideCombined(pair,sub){
  const prebuilt=sidePreviews[pair.id];
  if(prebuilt?.built)return prebuilt;
  return sideRendered.get(pair.id+'|'+sub.icon);
}
// The pair's hand-set layout (D1), when it has one.
function sideAdjusted(pair,sub){return SideData.handLayout(pair.id);}
function sideFillCombined(media,pair,sub){
  const found=sideCombined(pair,sub);media.replaceChildren();
  if(found?.error){media.append(node('span','side-combined-empty',found.error));return;}
  if(!found){media.append(node('span','side-combined-empty','Rendering…'));sideRequestRender(pair,sub,media);return;}
  const img=node('img');img.src=found.url||sideDataURL(found.result.svg);img.alt=pair.concept+' — combined';img.width=img.height=128;
  media.append(img);
  // The popup shows the main and sub bounds of the drawing composed here (a stored icon has none of its own).
  if(found.result)window.SideCombinationPopup?.attach(img,pair.concept,found.result);
  else{img.setAttribute('role','button');img.tabIndex=0;img.setAttribute('aria-label','Inspect '+pair.concept);
    const open=async()=>{try{const c=await SideData.compose(pair.id);window.SideCombinationPopup?.open(pair.concept,{...c.result,svg:c.svg});}catch(e){img.title=e.message;}};
    img.onclick=open;img.onkeydown=e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();open();}};}
}
// Composes previews of pairs not built yet in the browser, two at a time, and fills the tile if it is still shown.
function sideRequestRender(pair,sub,media){
  const key=pair.id+'|'+sub.icon;
  if(!sideRenderTargets.has(key))sideQueue.push({key,pair,sub});
  sideRenderTargets.set(key,media);sideDrain();
}
function sideDrain(){
  while(sideActiveRenders<2&&sideQueue.length){
    const {key,pair,sub}=sideQueue.shift();sideActiveRenders++;
    SideData.compose(pair.id)
      .then(c=>sideRendered.set(key,{result:{...c.result,svg:c.svg}}))
      .catch(error=>sideRendered.set(key,{error:error.message}))
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
function sideMarkDrawing(figure,label,drawing){
  const problems=figure.querySelector('.side-part-missing')?[]:sideDrawingProblems(drawing);
  if(!problems.length)return;
  figure.classList.add('needs-fix');figure.title=problems.join(' · ');
  const badge=node('span','side-fix-badge','Fix '+label.toLowerCase());badge.title=figure.title;
  figure.querySelector('.side-part-art').append(badge);
  figure.querySelector('figcaption').textContent=`${label} · ${drawing.status==='pass'?'needs fix':'fails validation'}`;
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
  const key=sideKey(row),hasMain=!['main','fixmain','both','both-text'].includes(key);
  const hasSub=!['sub','textsub','both','both-text'].includes(key)&&!(key==='fixmain'&&sideComponentStatus.sub.get(row.sub_id)==='missing');
  if(pair?.mains.length&&pair.subs.length&&hasMain&&hasSub)return {pair,key,main:sideMain(pair),sub:sideCurrentSub(pair),ready:true};
  const main=combinationMain(row).generated.find(g=>/^(solo|combination_main)\//.test(g.key)),sub=(row.sub_generated??refs[row.sub_id].generated).find(g=>/^(sub|text)\//.test(g.key));
  return {pair,key,main:hasMain&&main&&{icon:main.icon_id,preview_url:main.preview_url,pending:true},sub:hasSub&&sub&&{icon:sub.icon_id,preview_url:sub.preview_url,pending:true},ready:false};
}
// Resolve the exact displayed variant; use the live failed drawing when no passing one exists.
function sideEditableDrawing(row,role,item){
  const source=row[role+'_id'],list=sideComponents?.[role==='main'?'mains':'subs']||[];
  const component=list.find(c=>c.id===source||c.source_ids.includes(source));
  const drawings=component?.drawings||[],key=item?.model_key||item?.key;
  return (key?drawings.find(d=>d.key===key):null)||
    (item?.icon?drawings.find(d=>d.icon_id===item.icon):drawings[0]);
}
function sideEditButton(row,role,item){
  const drawing=sideEditableDrawing(row,role,item);
  if(!drawing||drawing.profile==='TEXT_NATIVE_V2'||!window.SideComponentEditor)return null;
  const wrap=node('div','requires-login'),button=node('button','side-edit-component',`Edit ${role} icon`),message=node('p','side-editor-message');
  button.type='button';message.setAttribute('role','status');
  button.onclick=async()=>{
    button.disabled=true;message.textContent='';
    try{await window.SideComponentEditor.open(drawing,`${role==='main'?'Main':'Sub'} · ${drawing.icon_id}`);}
    catch(error){message.textContent=error.message;}finally{button.disabled=false;}
  };
  wrap.append(button,message);return wrap;
}
window.addEventListener('side-component-approved',()=>{
  sideRendered.clear();sideComponentStatus={main:new Map(),sub:new Map()};
  loadSidePairs();
});
function sideState(row,parts){
  const key=parts.key.startsWith('both')?'main':parts.key,subMissing=key==='fixmain'&&sideComponentStatus.sub.get(row.sub_id)==='missing';
  const label=parts.key==='both'?'Needs main + sub':parts.key==='both-text'?'Needs main + text sub':subMissing?'Fix main + needs sub':SIDE_STATES[key];
  return [label,{ready:'ready',fix:'fix',fixmain:'fix',waiting:'waiting',textsub:'info'}[key]||'needed',SIDE_STATE_HINTS[key]];
}
function sideStep(label,content,name){
  const step=node('div','side-step');step.append(node('p','side-step-label',label),content);
  if(name)step.append(node('p','side-step-name',name));return step;
}
function sideRow(row){
  const refs=combinationCatalog.references,ref=refs[row.id],parts=sideParts(row),{pair,main,sub}=parts;
  const card=node('article','side-row'),head=node('div','side-row-head'),[label,tone,hint]=sideState(row,parts);card.dataset.pairId=row.id;
  head.append(node('h3','',row.concept),node('span','side-meta',(SIDE_POSITIONS[pair?.position]||pair?.position||'Side')+' · '+(pair?.native_text?`${sideRound(pair.canvas_width)}×${sideRound(pair.canvas_height)}`:`${sideSizes().canvas}×${sideSizes().canvas}`)),Object.assign(node('span','side-state '+tone,label),{title:hint}));
  if(sideSubIsText(row,pair))head.append(node('span','side-state info','Text sub'));
  if(pair?.published)head.append(Object.assign(node('span','side-state info','Main / sub changed'),{title:'The published main / sub was changed here: '+row.main_id+' + '+row.sub_id+'.'}));
  else if(pair?.custom)head.append(Object.assign(node('span','side-state info','From review'),{title:'Made from a combination primitive on the review page: '+row.main_id+' + '+row.sub_id+'.'}));
  if(pair?.mains.length>1)head.append(node('span','side-state info',`${pair.mains.length} mains · showing first`));
  if(parts.ready&&sideAdjusted(pair,sub))head.append(Object.assign(node('span','side-state info','Adjusted layout'),{title:'Main / sub positions and sizes were set by hand.'}));
  // A main or sub picked since this pair was combined (here or in Icon review): the combined icon still shows the old one.
  const changed=parts.ready&&sidePreviews[pair.id]?.built?SideData.staleRoles(pair.id):[];
  if(parts.ready&&changed.length)head.append(Object.assign(node('span','side-state info','Outdated: recombine'),{title:`The ${changed.join(' and ')} changed after this icon was combined. Use Recombine this icon (or Adjust layout) to rebuild it from the current drawings.`}));
  card.append(head);
  const original=node('div','side-original');
  if(ref?.reference_url){const img=node('img');img.src=ref.reference_url;img.alt=row.concept+' — original';img.loading='lazy';original.append(img);}
  else original.append(node('span','side-combined-empty','Reference missing'));
  const media=node('div','side-combined');
  if(parts.ready)sideFillCombined(media,pair,sub);else media.append(node('span','side-combined-empty','Not combined yet'));
  const steps=node('div','side-steps');
  const display=(role,item)=>{
    const drawing=sideEditableDrawing(row,role,item);
    if(item&&drawing&&item.sha256===drawing.svg_sha256&&!drawing.preview_url?.includes('/api/icon-artwork/'))return item;
    return drawing?{...item,icon:drawing.icon_id,key:drawing.key,model_key:drawing.key,family:drawing.family,
      preview_url:drawing.preview_url,document:null,pending:item?.pending??true}:item;
  };
  const shownMain=display('main',main),shownSub=display('sub',sub);
  const mainPart=sidePart('Main',shownMain,sideSizes().main,false),subPart=sidePart('Sub',shownSub,sideSizes().sub,true);
  // A failing drawing is still shown so it can be fixed; flag it so it does not look finished.
  sideMarkDrawing(mainPart,'Main',sideEditableDrawing(row,'main',main));
  if(!subPart.classList.contains('needs-fix'))sideMarkDrawing(subPart,'Sub',sideEditableDrawing(row,'sub',sub));
  if(shownMain)sideInspectable(mainPart,'Main',shownMain,sideSizes().main,row.concept);if(shownSub)sideInspectable(subPart,'Sub',shownSub,sideSizes().sub,row.concept);
  const combinedStep=sideStep(pair?.native_text?'Combined · native':'Combined · '+sideSizes().canvas,media);
  if(parts.ready&&!pair.mapped_native){
    const label=changed.length?'Recombine (outdated)':'Recombine this icon';
    const wrap=node('div','requires-login'),button=node('button','side-edit-component',label),message=node('p','side-editor-message');
    button.type='button';button.title='Use the latest saved main and sub with automatic placement';message.setAttribute('role','status');
    button.onclick=async()=>{
      button.disabled=true;button.textContent='Recombining…';message.textContent='';
      try{
        // Composed here from the current drawings with automatic placement, then stored.
        const done=await SideData.buildPairs([pair.id]),result=done.results[0];
        if(done.skipped.length)throw Error(done.skipped[0].error);
        if(!result.ok)throw Error(result.error);
        await sideMadeRefresh(pair.id);
      }catch(error){message.textContent=error.message;}
      finally{button.disabled=false;button.textContent=label;}
    };
    wrap.append(button,message);combinedStep.append(wrap);
    const prompt=node('p','login-prompt');prompt.innerHTML='<a href="login.html">Log in</a> to recombine this icon or adjust its layout.';combinedStep.append(prompt);
  }
  // Editing the layout sits right under the combined icon it changes.
  // Native text pairs too, except the ones only mapped in this page (they have no combination row to render).
  if(parts.ready&&window.SideLayoutEditor&&!pair.mapped_native)combinedStep.append(SideLayoutEditor.button(pair,main,sub,()=>{
    // The saved layout (or, after a reset, the automatic result) is the pair's stored icon everywhere from now on.
    sideMadeRefresh(pair.id);
  },sideAdjusted(pair,sub)));
  const mainStep=sideStep('Main · '+sideSizes().main,mainPart,shownMain?.icon),subStep=sideStep(sub?.native_text?'Sub · native':'Sub · '+sideSizes().sub,subPart,shownSub?.icon);
  // A part with no icon yet can name the one still to draw (Change main / sub › None of these).
  if(pair)for(const [role,step] of [['main',mainStep],['sub',subStep]])if(!pair[role+'s'].length&&pair[role+'_name'])step.append(node('p','side-step-name','To draw: '+pair[role+'_name']));
  const editMain=sideEditButton(row,'main',main),editSub=sideEditButton(row,'sub',sub);
  if(editMain)mainStep.append(editMain);if(editSub)subStep.append(editSub);
  steps.append(sideStep('Original',original),mainStep,subStep,combinedStep);
  card.append(steps);
  // Change the main or sub of any pair here, with the review page's picker (side-pair-maker.js). A published
  // pair opens with what it uses now; native text pairs keep their typeface layout.
  if(window.SidePairMaker&&pair&&!pair.native_text&&!pair.mapped_native){
    const redraw=()=>document.querySelector('.side-row[data-pair-id="'+CSS.escape(row.id)+'"]')?.replaceWith(sideRow(row));
    const current=(item,family)=>{const key=item?item.model_key||item.key||item.family+'/'+item.icon:'';
      return key?.startsWith(family+'/')?{key,icon_id:item.icon,name:item.icon.replace(/-/g,' '),preview_url:item.document?sideDataURL(item.document):item.preview_url}:null;};
    const published=!pair.custom||!!pair.published;
    card.append(SidePairMaker.editor({uuid:row.id,concept:row.concept,published,position:pair.position,
      current:published&&!pair.custom?{main:current(main,'solo'),sub:current(sub,'sub')}:null},redraw,data=>sideMadeRefresh(row.id,data)));
  }
  if(pair?.subs.length>1){
    const resolve=node('details','side-resolve');resolve.append(node('summary','',`${pair.subs.length} subs · keep one`),sidePicker(pair,sub,()=>card.replaceWith(sideRow(row))));
    resolve.open=sidePreviewSub.has(pair.id);card.append(resolve);
  }
  if(parts.ready){
    const actions=node('div','pair-card-actions'),found=sideCombined(pair,sub);
    const href=found?.url||(found?.result?.svg&&sideDataURL(found.result.svg));
    if(href){const a=node('a');a.href=href;a.download=pair.id+'.svg';window.SideRepairFlags?.download(a);actions.append(a);}
    const reviewItem=(role,item)=>{
      const drawing=sideEditableDrawing(row,role,item);
      return drawing?{...item,model_key:drawing.key,sha256:drawing.svg_sha256}:item;
    };
    if(window.SideRepairFlags&&!pair.native_text)actions.append(SideRepairFlags.button('main',reviewItem('main',main),pair),SideRepairFlags.button('sub',reviewItem('sub',sub),pair));
    const combined=sideCombinedReview(pair,main,sub);if(combined)actions.append(combined);
    if(actions.childElementCount)card.append(actions);
  }
  return card;
}

// The combined icon's review in Icon review (POST /api/reviews): its state, Approve (once its main and sub are
// approved) and Disapprove with a note.
const SIDE_REVIEW_LABELS={approve:'Approved',ready:'To review','re-generated':'To review',pending:'Needs fix',disapprove:'Needs fix',claimed:'Being fixed',rejected:'Rejected'};
function sideCombinedReview(pair,main,sub){
  const icon=SideData.item(pair.id)?.icon;if(!icon)return null;
  const box=node('span','side-review side-combined-review'),status=sideReviews[icon.key]||icon.review||'ready',chip=node('span','side-review-chip');
  const label=node('b','','Combined');chip.append(label,' '+(SIDE_REVIEW_LABELS[status]||status));box.dataset.status=status;box.append(chip);
  const waiting=[['main',main],['sub',sub]].filter(([,item])=>item&&!['approve'].includes(sideReviews[item.model_key])).map(([role])=>role);
  const message=node('span','side-editor-message');message.setAttribute('role','status');
  const send=async(button,body)=>{
    button.disabled=true;message.textContent='Saving…';
    try{
      const response=await fetch('/api/reviews',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({icon:icon.key,svg_sha256:icon.svg_sha256,...body})});
      const data=await response.json().catch(()=>({}));if(!response.ok)throw Error(data.error||'Could not save the review.');
      sideReviews[icon.key]=body.status;await sideMadeRefresh(pair.id);
    }catch(error){message.textContent=error.message;button.disabled=false;}
  };
  const approve=node('button','requires-login','Approve');approve.type='button';approve.dataset.action='approve';
  approve.disabled=status==='approve'||waiting.length>0;if(waiting.length)approve.title='Approve the '+waiting.join(' and ')+' first';
  approve.onclick=()=>send(approve,{status:'approve'});
  const disapprove=node('button','requires-login','Disapprove');disapprove.type='button';disapprove.dataset.action='disapprove';disapprove.disabled=status==='pending';
  disapprove.onclick=()=>{const note=prompt('What needs fixing in the combined icon?');if(note)send(disapprove,{status:'pending',reason:'other',feedback:note});};
  box.append(approve,disapprove,message);return box;
}

/* The layout editor lists the other ready pairs that use the same main, so one fix can be
   applied to several of them; after applying, their previews update here. */
window.SideLayoutEditor?.configure({
  pairsWithMain(icon,exceptId){
    if(!sidePairs)return [];
    return [...sidePairs.values()].filter(p=>p.id!==exceptId&&!p.mapped_native&&p.subs.length&&p.mains.some(m=>m.icon===icon)).map(p=>{
      const sub=sideCurrentSub(p),found=sideCombined(p,sub);
      return {id:p.id,concept:p.concept,position:p.position,sub:sub.icon,adjusted:!!sideAdjusted(p,sub),
        preview:found?.url||(found?.result?.svg?sideDataURL(found.result.svg):null)};
    });
  },
  // After an apply: every pair that took the layout is read again from D1.
  async applied(results){
    for(const r of results)if(r.ok)await SideData.refresh(r.pair_id).then(got=>{if(!got)return;sidePairs.set(r.pair_id,got.pair);
      if(got.preview)sidePreviews[r.pair_id]=got.preview;for(const k of [...sideRendered.keys()])if(k.startsWith(r.pair_id+'|'))sideRendered.delete(k);}).catch(()=>{});
    renderCombinations();
  }
});

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
  const size=sideGroup==='main'?sideSizes().main:sideSizes().sub,info=node('span','container-group-label');
  const detail=!item?`${sideGroup==='main'?'Main':'Sub'} needed`:item.pending?`Drawn ${sideGroup} · waiting`:item.document?`Shared ${sideGroup} · ${sideRound(sideInk(item,sideGroup==='sub')[0])}×${sideRound(sideInk(item,sideGroup==='sub')[1])} / ${size}`:`Shared ${sideGroup}`;
  info.append(node('strong','',group.title),node('span','muted',detail));
  heading.append(info,node('span','chip',`${group.rows.length.toLocaleString()} pair${group.rows.length===1?'':'s'}`));
  const children=node('div','side-list container-group-items');section.append(heading,children);
  const fill=()=>{if(section.open&&!children.childElementCount)children.append(...group.rows.map(sideRow));};
  section.open=sideOpenGroups.has(group.key);fill();
  section.addEventListener('toggle',()=>{if(!section.isConnected)return;if(section.open)sideOpenGroups.add(group.key);else sideOpenGroups.delete(group.key);fill();});
  return section;
}

/* Build all composes, in this browser, every side pair whose main and sub are drawn and that is not built yet or was
   built from older drawings, each with its own saved layout, and stores them (50 a request). */
let sideCombine={status:'idle',message:''},sideCombineChecked=false;
// The pairs Build all builds: main and sub usable (the Ready state) and no current build.
const sideBuildable=()=>combinationCatalog.rows.filter(r=>sideKey(r)==='ready'&&(!sidePreviews[r.id]?.built||SideData.staleRoles(r.id).length)).map(r=>r.id);
function sideCombineShow(){
  const button=document.getElementById('sideCombineAll'),status=document.getElementById('sideCombineStatus');
  const count=sidePairs?sideBuildable().length:null;
  if(button){button.textContent=count==null?'Count side pairs to build…':`Build ${count.toLocaleString()} side pair${count===1?'':'s'}`;button.disabled=sideCombine.status==='running'||!count;}
  if(status)status.textContent=sideCombine.status==='running'?sideCombine.message:sideCombine.status==='error'?sideCombine.message+' You can retry.'
    :`${count==null?'Counting':count.toLocaleString()} ready side pairs not built yet or built from older drawings · ${(sideRun?.count||0).toLocaleString()} built`;
}
async function sideCombineAll(){
  const ids=sideBuildable();
  sideCombine={status:'running',message:`Building 0 / ${ids.length}…`};sideCombineShow();
  try{
    const {results,skipped}=await SideData.buildPairs(ids,(n,total)=>{sideCombine.message=`Building ${n.toLocaleString()} / ${total.toLocaleString()}…`;sideCombineShow();});
    const failed=results.filter(r=>!r.ok);
    sideStatus=`Built ${results.filter(r=>r.ok).length.toLocaleString()} side pairs.`+(failed.length?` ${failed.length} refused (${failed[0].reference_id}: ${failed[0].error}).`:'')
      +(skipped.length?` ${skipped.length} could not be drawn (${skipped[0].reference_id}: ${skipped[0].error}).`:'');
    sideCombine={status:'idle',message:''};sidePairs=null;sidePreviews={};sideRendered.clear();combinationCatalog=null;loadSidePairs();
  }catch(error){sideCombine={status:'error',message:error.message};sideCombineShow();}
}
function sideCombineCheck(){sideCombineChecked=true;}
// Rebuild every stale pair: built before a main or sub was redrawn; each rebuilt with its own saved layout.
const sideStale=()=>combinationCatalog.rows.filter(r=>SideData.item(r.id)?.state==='stale').map(r=>r.id);
async function sideRebuildStale(button){
  const ids=sideStale();if(!ids.length)return;
  if(!confirm(`Rebuild all ${ids.length} stale side pairs from their parts' current drawings?`))return;
  button.disabled=true;sideCombine={status:'running',message:`Rebuilding 0 / ${ids.length}…`};sideCombineShow();
  try{
    const {results,skipped}=await SideData.buildPairs(ids,(n,total)=>{sideCombine.message=`Rebuilding ${n.toLocaleString()} / ${total.toLocaleString()}…`;sideCombineShow();});
    const failed=results.filter(r=>!r.ok);
    sideStatus=`Rebuilt ${results.filter(r=>r.ok).length.toLocaleString()} stale side pairs.`+(failed.length?` ${failed.length} refused (${failed[0].reference_id}: ${failed[0].error}).`:'')
      +(skipped.length?` ${skipped.length} could not be drawn (${skipped[0].reference_id}: ${skipped[0].error}).`:'');
    sideCombine={status:'idle',message:''};sidePairs=null;sidePreviews={};sideRendered.clear();combinationCatalog=null;loadSidePairs();
  }catch(error){sideCombine={status:'error',message:error.message};sideCombineShow();button.disabled=false;}
}

function writeSideURL(){
  const u=new URL(location.href);
  if(sideFilter)u.searchParams.set('side',sideFilter);else u.searchParams.delete('side');
  if(sidePageSize!==24)u.searchParams.set('size',sidePageSize);else u.searchParams.delete('size');
  if(sideGroup)u.searchParams.set('group',sideGroup);else u.searchParams.delete('group');
  if(SideData.size()===72)u.searchParams.set('grid','72');else u.searchParams.delete('grid');
  history.replaceState(null,'',u);
}
// Side pairs are built from X main icons and Y sub icons; count the icons, the same way the Main icons and Sub icons pages do.
function sideIconSummary(pairCount){
  const isText=i=>[i.id,...i.source_ids].some(id=>sideStatuses[id]?.reason==='text_number');
  const mains=sideComponents.mains,subs=sideComponents.subs,textSubs=subs.filter(isText),iconSubs=subs.filter(i=>!isText(i));
  const count=(list,status)=>list.filter(i=>i.status===status).length;
  const wrap=node('section','side-icon-summary');
  // One source icon can have several drawings (alternative redraws or revised versions) and one drawing can serve
  // several sources; a pair uses one. Icon review lists distinct drawings, so these counts match its Side main / Side sub families.
  const drawings=list=>[...new Map(list.flatMap(i=>i.drawings).filter(d=>d.status!=='fail'&&d.svg_sha256).map(d=>[d.key,d])).values()];
  const mainDrawings=drawings(mains),subDrawings=drawings(subs);
  wrap.append(node('p','side-icon-total',`${pairCount.toLocaleString()} side pairs, made from ${mains.length.toLocaleString()} main icons (${mainDrawings.length.toLocaleString()} drawings) and ${subs.length.toLocaleString()} sub icons (${subDrawings.length.toLocaleString()} drawings). A source with several drawings has alternative redraws or versions; each pair uses one.`));
  const cells=(row,page,items)=>{for(const [label,value,status,tone] of items){const a=node('a','side-icon-cell '+tone);a.href=page+(page.includes('?')?'&':'?')+'status='+status;a.append(node('strong','',value.toLocaleString()),node('span','',label));row.append(a);}};
  const group=(title,total,page,items)=>{
    const box=node('div','side-icon-group'),head=node('a','side-icon-head');head.href=page;head.append(node('strong','',title),node('span','',total.toLocaleString()+' icons →'));box.append(head);
    const row=node('div','side-icon-cells');cells(row,page,items);
    box.append(row);return box;
  };
  // Review decisions per drawing, the same states as Icon review (iconState there); cells open its Side main / Side sub family.
  const reviewState=d=>{const s=sideReviews[d.key]||'ready';return s==='re-generated'?'ready':s==='disapprove'||s==='claimed'?'pending':s;};
  const reviewRow=(box,list,family)=>{
    const tally=Object.fromEntries(['approve','ready','pending','rejected'].map(s=>[s,0]));for(const d of list)tally[reviewState(d)]=(tally[reviewState(d)]||0)+1;
    const head=node('a','side-icon-subhead');head.href='index.html?family='+family;head.append(node('strong','','Icon review'),node('span','',`${list.length.toLocaleString()} drawings →`));
    const row=node('div','side-icon-cells');cells(row,'index.html?family='+family,[['Approved',tally.approve,'approve','ok'],['To review',tally.ready,'ready','todo'],['Needs fix',tally.pending,'pending','fix'],['Rejected',tally.rejected,'rejected','rej']]);
    box.append(head,row);return box;
  };
  wrap.append(
    reviewRow(group(SideData.size()===72?'Main icons · 54':'Main icons',mains.length,SideData.size()===72?'index.html?family=main-54':'side-mains.html',[['Generated',count(mains,'done'),'done','ok'],['Needs fix',count(mains,'failing'),'failing','fix'],['Not generated',count(mains,'missing'),'missing','todo']]),mainDrawings,SideData.size()===72?'main-54':'side_main'),
    reviewRow(group(SideData.size()===72?'Sub icons · 36':'Sub icons',subs.length,SideData.size()===72?'index.html?family=sub-36':'side-subs.html',[['Generated',count(iconSubs,'done'),'done','ok'],['Text',textSubs.length,'text','text'],['Needs fix',count(iconSubs,'failing'),'failing','fix'],['Not generated',count(iconSubs,'missing'),'missing','todo']]),subDrawings,SideData.size()===72?'sub-36':'side_sub'));
  if(sideRun){
    // Combined icons: the count links to Experiment, the review cells to Icon review's Side combination 64 family.
    const state=icon=>({approve:'approve','re-generated':'ready',disapprove:'pending',claimed:'pending'})[sideReviews[icon.key]]||sideReviews[icon.key]||'ready';
    const reviewed=s=>sideRun.icons.filter(i=>state(i)===s).length,review='index.html?family='+sideSizes().combined;
    const box=group('Combined · '+sideSizes().canvas,sideRun.count,SideData.size()===72?review:'experiment.html?type=combination',[]),cells=box.querySelector('.side-icon-cells');
    box.querySelector('.side-icon-head span').textContent=sideRun.count.toLocaleString()+' combined icons →';
    for(const [label,value,status,tone] of [['Approved',reviewed('approve'),'approve','ok'],['To review',reviewed('ready'),'ready','todo'],['Needs fix',reviewed('pending'),'pending','fix']]){
      const a=node('a','side-icon-cell '+tone);a.href=review+'&status='+status;a.append(node('strong','',value.toLocaleString()),node('span','',label));cells.append(a);
    }
    wrap.append(box);
  }
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
  const combine=node('div','toolbar side-combine'),combineButton=node('button','','Count side pairs to build…'),combineStatus=node('span','muted');
  combineButton.id='sideCombineAll';combineButton.type='button';combineButton.classList.add('requires-login');combineButton.onclick=sideCombineAll;
  const staleCount=sideStale().length,rebuild=node('button','requires-login',`Rebuild ${staleCount.toLocaleString()} stale pair${staleCount===1?'':'s'}`);
  rebuild.type='button';rebuild.disabled=!staleCount;rebuild.title='Pairs built before a main or sub was redrawn';rebuild.onclick=()=>sideRebuildStale(rebuild);
  combineStatus.id='sideCombineStatus';combineStatus.setAttribute('role','status');combine.append(combineButton,rebuild,combineStatus);host.append(combine);
  sideCombineShow();sideCombineCheck();
  const gallery=node('section');gallery.id='pairGallery';host.append(gallery);
  if(sideStatus){const status=node('p','side-status',sideStatus);status.setAttribute('role','status');gallery.append(status);}
  const toolbar=node('div','toolbar'),search=node('input'),filter=node('select'),group=node('select'),size=node('select'),grid=node('select');
  grid.setAttribute('aria-label','Pair size');grid.append(new Option('64 · 48 main + 32 sub','64'),new Option('72 · 54 main + 36 sub','72'));grid.value=String(SideData.size());
  grid.onchange=()=>{SideData.setSize(Number(grid.value));sidePairs=null;sidePreviews={};sideRendered.clear();combinationCatalog=null;sideComponentStatus={main:new Map(),sub:new Map()};page=1;writeSideURL();renderCombinations();};
  search.type='search';search.placeholder='Search concept, component ID or icon name';search.setAttribute('aria-label','Search side pairs');search.value=state.q;
  filter.setAttribute('aria-label','Side pair filter');filter.append(...Object.entries(SIDE_FILTERS).map(([k,v])=>new Option(v,k)));filter.value=sideFilter;
  group.setAttribute('aria-label','Group side pairs');group.append(...Object.entries(SIDE_GROUPS).map(([k,v])=>new Option(v,k)));group.value=sideGroup;
  size.setAttribute('aria-label','Items per page');size.append(...[24,48,96].map(n=>new Option(n+(sideGroup?' groups':' pairs')+' per page',n)));size.value=sidePageSize;
  filter.onchange=()=>{sideFilter=filter.value;page=1;renderCombinations();};
  group.onchange=()=>{sideGroup=group.value;page=1;renderCombinations();};
  size.onchange=()=>{sidePageSize=Number(size.value);page=1;renderCombinations();};
  let timer;search.oninput=()=>{clearTimeout(timer);timer=setTimeout(()=>{const cursor=search.selectionStart;state.q=search.value;page=1;renderCombinations();const next=host.querySelector('input[type=search]');next.focus();if(cursor!==null)next.setSelectionRange(cursor,cursor);},180);};
  toolbar.append(grid,search,filter,group,size);gallery.append(toolbar);
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

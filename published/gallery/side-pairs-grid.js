/* Side pairs as a grid of combined 64×64 icons. Subs are shown on the 32×32 system;
   a pair with several subs keeps one and removes the others from the set. */
let sidePairs=null, sidePreviews={}, sideLoading=false, sideError='', sideStatus='';
const sidePreviewSub=new Map(), sideRendered=new Map(), sideRenderTargets=new Map(), sideQueue=[], sideFixItems=new WeakMap();
let sideActiveRenders=0;
const SIDE_POSITIONS={br:'Bottom-right',bl:'Bottom-left',tr:'Top-right',tl:'Top-left',ri:'Right',le:'Left',bo:'Bottom',to:'Top'};
const SIDE_FILTERS={'':'All side pairs',fix:'Needs sub fix',multi:'Pairs with 2+ subs',ready:'Ready to combine',main:'Main needed',sub:'Sub needed'};
const sideParams=new URLSearchParams(location.search);
let sideFilter=SIDE_FILTERS[sideParams.get('side')]?sideParams.get('side'):'', sidePageSize=[24,48,96].includes(Number(sideParams.get('size')))?Number(sideParams.get('size')):24;

async function loadSidePairs(){
  if(sideLoading)return;sideLoading=true;
  try{
    const [pairs,previews]=await Promise.all(['experiment-combination.json','experiment-combination-results.json'].map(async url=>{const r=await fetch(url,{cache:'no-store'});if(!r.ok)throw Error('Could not load side pair artwork.');return r.json();}));
    sidePairs=new Map(pairs.rows.map(r=>[r.id,r]));sidePreviews=previews.results||{};sideError='';
  }catch(error){sideError=error.message;}
  finally{sideLoading=false;}
  if(state.view==='side')renderCombinations();
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
  if(w>32.01||h>32.01)problems.push(`Ink ${sideRound(w)}×${sideRound(h)} exceeds 32×32`);
  if(window.SideRepairFlags?.flagged(s))problems.push('Flagged for repair');
  return problems;
}
const sideCurrentSub=pair=>pair.subs.find(s=>s.icon===sidePreviewSub.get(pair.id))||pair.subs[0];
function sideCategory(row){
  const pair=sidePairs.get(row.id);
  if(pair?.mains.length&&pair.subs.length)return {ready:true,fix:pair.subs.some(s=>sideSubProblems(s).length),multi:pair.subs.length>1};
  const refs=combinationCatalog.references;
  return {main:!combinationMain(row).generated.length,sub:!(row.sub_generated??refs[row.sub_id].generated).length};
}

function sideCombined(pair,sub){
  const prebuilt=sidePreviews[pair.id],placed=role=>prebuilt?.result?.placements?.find(p=>p.role===role)?.icon;
  if(prebuilt&&placed('sub')===sub.icon&&placed('main')===pair.mains[0].icon)return prebuilt;
  return sideRendered.get(pair.id+'|'+sub.icon);
}
function sideFillCombined(media,pair,sub){
  const found=sideCombined(pair,sub);media.replaceChildren();
  if(found?.error){media.append(node('span','side-combined-empty',found.error));return;}
  if(!found){media.append(node('span','side-combined-empty','Rendering…'));sideRequestRender(pair,sub,media);return;}
  const img=node('img');img.src=found.url||sideDataURL(found.result.svg);img.alt=pair.concept+' — combined';img.width=img.height=128;
  media.append(img);window.SideCombinationPopup?.attach(img,pair.concept,found.result);
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
    const caption=item.document?`${label} ${sideRound(sideInk(item,isSub)[0])}×${sideRound(sideInk(item,isSub)[1])} / ${size}`:`${label} · generated`;
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

function sideTile(row){
  const pair=sidePairs.get(row.id),card=node('article','side-tile'),media=node('div','side-combined');
  if(!pair?.mains.length||!pair.subs.length){
    const refs=combinationCatalog.references,ref=refs[row.id];
    if(ref?.reference_url){const img=node('img');img.src=ref.reference_url;img.alt=row.concept+' — reference';img.loading='lazy';media.append(img);}
    else media.append(node('span','side-combined-empty','Reference missing'));
    card.classList.add('side-tile-missing');
    const main=combinationMain(row).generated[0],sub=(row.sub_generated??refs[row.sub_id].generated)[0];
    const parts=node('div','side-parts');
    parts.append(sidePart('Main',main&&{icon:main.icon_id,preview_url:main.preview_url},48,false),sidePart('Sub',sub&&{icon:sub.icon_id,preview_url:sub.preview_url},32,true));
    card.append(media,node('h3','',row.concept),node('p','side-meta','Reference · '+(main&&sub?'not in the 32×32 pair data yet':'components needed')),parts);
    return card;
  }
  const current=sideCurrentSub(pair),rerender=()=>card.replaceWith(sideTile(row));
  sideFillCombined(media,pair,current);
  const parts=node('div','side-parts');parts.append(sidePart('Main',pair.mains[0],48,false),sidePart('Sub',current,32,true));
  card.append(media,node('h3','',row.concept),node('p','side-meta',(SIDE_POSITIONS[pair.position]||pair.position)+' · 64×64'),parts);
  if(pair.subs.length>1)card.append(sidePicker(pair,current,rerender));
  const actions=node('div','pair-card-actions'),found=sideCombined(pair,current);
  if(found?.url){const a=node('a');a.href=found.url;a.download=pair.id+'.svg';window.SideRepairFlags?.download(a);actions.append(a);}
  if(window.SideRepairFlags)actions.append(SideRepairFlags.button('main',pair.mains[0],pair),SideRepairFlags.button('sub',current,pair));
  card.append(actions);return card;
}

function writeSideURL(){
  const u=new URL(location.href);
  if(sideFilter)u.searchParams.set('side',sideFilter);else u.searchParams.delete('side');
  if(sidePageSize!==24)u.searchParams.set('size',sidePageSize);else u.searchParams.delete('size');
  history.replaceState(null,'',u);
}
function renderSideGrid(host,all,summary){
  if(!sidePairs){
    host.append(node('p','muted',sideError||'Loading combined icons…'));
    if(sideError){const retry=node('button','','Retry');retry.onclick=()=>{sideError='';loadSidePairs();renderCombinations();};host.append(retry);}
    else loadSidePairs();
    return;
  }
  const categories=new Map(all.map(r=>[r.id,sideCategory(r)])),count=key=>[...categories.values()].filter(c=>c[key]).length;
  for(const [label,value] of [['Ready to combine',count('ready')],['Subs needing fix',count('fix')],['Pairs with 2+ subs',count('multi')]]){
    const item=node('div');item.append(node('strong','',value.toLocaleString()),node('span','',label));summary.append(item);
  }
  const gallery=node('section');gallery.id='pairGallery';host.append(gallery);
  if(sideStatus){const status=node('p','side-status',sideStatus);status.setAttribute('role','status');gallery.append(status);}
  const toolbar=node('div','toolbar'),search=node('input'),filter=node('select'),size=node('select');
  search.type='search';search.placeholder='Search concept or component ID';search.setAttribute('aria-label','Search side pairs');search.value=state.q;
  filter.setAttribute('aria-label','Side pair filter');filter.append(...Object.entries(SIDE_FILTERS).map(([k,v])=>new Option(v,k)));filter.value=sideFilter;
  size.setAttribute('aria-label','Icons per page');size.append(...[24,48,96].map(n=>new Option(n+' per page',n)));size.value=sidePageSize;
  filter.onchange=()=>{sideFilter=filter.value;page=1;renderCombinations();};
  size.onchange=()=>{sidePageSize=Number(size.value);page=1;renderCombinations();};
  let timer;search.oninput=()=>{clearTimeout(timer);timer=setTimeout(()=>{const cursor=search.selectionStart;state.q=search.value;page=1;renderCombinations();const next=host.querySelector('input[type=search]');next.focus();if(cursor!==null)next.setSelectionRange(cursor,cursor);},180);};
  toolbar.append(search,filter,size);gallery.append(toolbar);
  const q=state.q.trim().toLowerCase(),refs=combinationCatalog.references;
  const rows=all.filter(r=>{
    if(sideFilter&&!categories.get(r.id)[sideFilter])return false;if(!q)return true;
    const pair=sidePairs.get(r.id);
    return [r.concept,r.id,r.main_id,r.sub_id,refs[r.main_id]?.concept,refs[r.sub_id]?.concept,...(pair?[...pair.mains,...pair.subs].map(m=>m.icon):[])].join(' ').toLowerCase().includes(q);
  });
  const pages=Math.max(1,Math.ceil(rows.length/sidePageSize));page=Math.min(page,pages);writeURL();writeSideURL();
  function pager(){const bar=node('div','pager'),prev=node('button','','← Previous'),next=node('button','','Next →');prev.disabled=page<=1;next.disabled=page>=pages;prev.onclick=()=>{page--;renderCombinations();host.scrollIntoView();};next.onclick=()=>{page++;renderCombinations();host.scrollIntoView();};bar.append(prev,node('span','muted',`${rows.length.toLocaleString()} matches · Page ${page} of ${pages}`),next);return bar;}
  const grid=node('div','side-grid');
  for(const row of rows.slice((page-1)*sidePageSize,page*sidePageSize))grid.append(sideTile(row));
  if(!rows.length)grid.append(node('p','muted','No side pairs match these filters.'));
  gallery.append(pager(),grid,pager());
  window.SideRepairFlags?.setRows([...sidePairs.values()]);
}

/* Main icons / Sub icons pages. Both read side-components.json (staged by side_components.py)
   and, for subs, the live text / number marks from /api/primitives/status. */
(()=>{
const ROLE=document.body.dataset.role, PAGE_SIZE=48, $=id=>document.getElementById(id);
const BUCKETS=ROLE==='sub'
  ?[['done','Generated','A 32×32 sub drawing passes'],['text','Text','Text or a number · generated separately'],['failing','Needs fix','Fails validation or marked needs fix · /fix-icon-sub'],['missing','Not generated','No 32×32 drawing yet · /icon-sub'],['variants','Extra versions failing','Generated, but other versions fail or need fix'],['all','All sub icons','']]
  :[['done','Generated','A 48×48 solo drawing passes'],['missing','Not generated','No 48×48 solo drawing yet · /icon-solo'],['failing','Needs fix','Fails validation or marked needs fix'],['all','All main icons','']];
const HANDOFF={missing:ROLE==='sub'?'Generate each as a SUB32 sub icon with /icon-sub from its source reference.':'Generate each as a SOLO48 main icon with /icon-solo from its source reference.',
  failing:ROLE==='sub'?'Repair each with /fix-icon-sub: keep the reference meaning, produce a variant that passes the SUB32 gate.':'Repair each drawing so it passes validation, keeping the reference meaning.',
  text:'Each sub is readable text or a number. Generate as a text sub, not a pictogram.',variants:'These subs already pass; their extra variants fail. Fix or discard the failing variants.',done:'Reference list only.',all:'Reference list only.'};
let items=[],statuses={},reviews={},counts={},page=1;
// A drawing counts as generated only when it passes validation and no reviewer marked it Needs fix
// (review status pending) or rejected it. Same rule as the Side pairs summary in side-pairs-grid.js.
const flagged=d=>['pending','rejected'].includes(reviews[d.key]);
const usable=d=>d.status==='pass'&&!flagged(d);
function restatus(item){item.failing_variants=item.drawings.filter(d=>!usable(d)).length;item.status=item.drawings.some(usable)?'done':item.drawings.length?'failing':'missing';}
const params=new URLSearchParams(location.search);
const state={status:BUCKETS.some(b=>b[0]===params.get('status'))?params.get('status'):'missing',q:params.get('q')||'',sort:params.get('sort')==='name'?'name':'uses'};
page=Math.max(1,parseInt(params.get('page'))||1);

function node(tag,cls,text){const n=document.createElement(tag);if(cls)n.className=cls;if(text!==undefined)n.textContent=text;return n;}
function isText(item){return ROLE==='sub'&&[item.id,...item.source_ids].some(id=>statuses[id]?.reason==='text_number');}
function textMarkId(item){return [item.id,...item.source_ids].find(id=>statuses[id]?.reason==='text_number');}
// The page's bucket for an item: text marks override drawing status so the two queues never overlap.
function bucket(item){return isText(item)?'text':item.status;}
function inBucket(item,b){const k=bucket(item);return b==='all'||(b==='variants'?k==='done'&&item.failing_variants>0:k===b);}
function tally(){const t={};for(const [b] of BUCKETS)t[b]=items.filter(i=>inBucket(i,b)).length;return t;}
function filtered(){
  const q=state.q.trim().toLowerCase();
  const rows=items.filter(i=>inBucket(i,state.status)&&(!q||[i.concept,i.id,...i.source_ids,...i.drawings.map(d=>d.icon_id),...i.pairs.map(p=>p.concept)].join(' ').toLowerCase().includes(q)));
  return state.sort==='name'?rows.sort((a,b)=>a.concept.localeCompare(b.concept)):rows.sort((a,b)=>b.uses-a.uses||a.concept.localeCompare(b.concept));
}
function writeURL(){const u=new URL(location.href);u.search='';if(state.status!=='missing')u.searchParams.set('status',state.status);if(state.q)u.searchParams.set('q',state.q);if(state.sort!=='uses')u.searchParams.set('sort',state.sort);if(page>1)u.searchParams.set('page',page);history.replaceState(null,'',u);}

function renderStats(){
  const t=tally(),host=$('stats');host.replaceChildren();
  for(const [b,label,hint] of BUCKETS){
    const box=node('button','sc-stat'+(b==='missing'||b==='failing'?' key':''));box.type='button';box.setAttribute('aria-pressed',String(state.status===b));
    box.append(node('span','',label),node('strong','',t[b].toLocaleString()));if(hint)box.append(node('small','',hint));
    box.onclick=()=>{state.status=b;page=1;render();};host.append(box);
  }
  const total=items.length||1,bar=$('bar');bar.replaceChildren();
  for(const b of ['done','text','failing','missing']){if(!(b in t))continue;const i=node('i',b);i.style.width=(t[b]/total*100)+'%';i.title=`${b}: ${t[b]}`;bar.append(i);}
  const n=b=>t[b].toLocaleString();
  $('headline').textContent=ROLE==='sub'?`${items.length.toLocaleString()} sub icons: ${n('done')} generated, ${n('text')} text, ${n('failing')} need fix, ${n('missing')} not generated.`
    :`${items.length.toLocaleString()} main icons: ${n('done')} generated, ${n('missing')} not generated`+(t.failing?`, ${n('failing')} need fix.`:'.');
}

// Drawings sit on their native unit grid: 32×32 for subs, 48×48 for mains (1-unit minor, 8-unit major lines).
const GRID=ROLE==='sub'?32:48;
function drawingFigure(item,d){
  const fig=node('figure','sc-drawing '+d.status),a=node('a','sc-grid sc-grid-'+GRID);a.href=d.preview_url||'#';a.target='_blank';a.rel='noopener';a.title=d.python_source||d.icon_id;
  const img=document.createElement('img');img.loading='lazy';img.alt=d.icon_id;img.src=d.preview_url;a.append(img);
  if(d.preview_url)centerlineObserver.observe(a);a.dataset.src=d.preview_url||'';
  fig.append(a,node('figcaption','',`${d.icon_id} · ${reviews[d.key]==='pending'?'needs fix':d.status}`));
  if(reviews[d.key]==='pending')fig.classList.add('flagged');
  if(d.svg_sha256&&d.status==='pass')fig.append(fixButton(item,d));
  if(d.svg_sha256){fig.append(removeButton(item,d));fig.append(selectBox(item,d,fig));}
  return fig;
}
// Centerline: each drawing is inlined as its artwork plus a thin copy of the same paths (CSS .sc-cl).
const svgCache=new Map();
const loadSVG=url=>{if(!svgCache.has(url))svgCache.set(url,fetch(url).then(r=>{if(!r.ok)throw Error();return r.text();}));return svgCache.get(url);};
const centerlineObserver=new IntersectionObserver(entries=>{for(const e of entries)if(e.isIntersecting){centerlineObserver.unobserve(e.target);inlineCenterline(e.target);}},{rootMargin:'300px'});
async function inlineCenterline(host){
  try{
    const svg=new DOMParser().parseFromString(await loadSVG(host.dataset.src),'image/svg+xml').documentElement;
    if(svg.nodeName!=='svg')return;
    svg.querySelectorAll('title,script').forEach(n=>n.remove());
    const art=document.createElementNS('http://www.w3.org/2000/svg','g');art.setAttribute('class','sc-art-layer');art.append(...svg.childNodes);
    const line=art.cloneNode(true);line.setAttribute('class','sc-cl');line.querySelectorAll('[id]').forEach(n=>n.removeAttribute('id'));
    svg.append(art,line);svg.removeAttribute('width');svg.removeAttribute('height');svg.setAttribute('aria-hidden','true');
    host.replaceChildren(svg);
  }catch{/* keep the plain image */}
}
// Needs fix = the review system's disapproval (status pending, reason manual-fix-request); Clear sets it back to ready.
function fixButton(item,d){
  const on=reviews[d.key]==='pending',wrap=node('div','sc-fix login-only'),button=node('button',on?'on':'',on?'Clear needs fix':'Mark needs fix'),msg=node('span');button.type='button';
  button.onclick=async()=>{
    button.disabled=true;msg.textContent='';
    const body=on?{icon:d.key,svg_sha256:d.svg_sha256,status:'ready'}:{icon:d.key,svg_sha256:d.svg_sha256,status:'pending',reason:'manual-fix-request',feedback:`Marked needs fix from the side ${ROLE} icons page (${item.concept}).`};
    try{const r=await fetch('/api/reviews',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}),data=await r.json().catch(()=>({}));
      if(!r.ok)throw Error(data.error||'Could not save.');reviews[d.key]=on?'ready':'pending';restatus(item);render();
    }catch(e){msg.textContent=e.message;button.disabled=false;}
  };
  wrap.append(button,msg);return wrap;
}
// Batch delete: pick drawings across pages, then reject + discard them together.
const selected=new Map();
function selectBox(item,d,fig){
  const label=node('label','sc-pick login-only'),box=document.createElement('input');box.type='checkbox';box.checked=selected.has(d.key);fig.classList.toggle('picked',box.checked);
  box.onchange=()=>{box.checked?selected.set(d.key,{item,d}):selected.delete(d.key);fig.classList.toggle('picked',box.checked);renderBatch();};
  label.append(box,' Select');return label;
}
function renderBatch(){
  $('batchCount').textContent=`${selected.size} selected`;$('batchClear').disabled=!selected.size;
  const del=$('batchDelete');del.disabled=!selected.size;if(!del.dataset.armed)del.textContent=`Delete ${selected.size} selected`;
}
function pageRows(){const rows=filtered(),pages=Math.max(1,Math.ceil(rows.length/PAGE_SIZE));return rows.slice((Math.min(page,pages)-1)*PAGE_SIZE,Math.min(page,pages)*PAGE_SIZE);}
async function batchDelete(){
  const del=$('batchDelete'),msg=$('batchMsg');
  if(!del.dataset.armed){del.dataset.armed='1';del.textContent=`Click again to delete ${selected.size}`;del.classList.add('armed');setTimeout(()=>{delete del.dataset.armed;del.classList.remove('armed');renderBatch();},4000);return;}
  delete del.dataset.armed;del.classList.remove('armed');del.disabled=true;
  const picks=[...selected.values()],post=async(url,body)=>{const r=await fetch(url,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});const data=await r.json().catch(()=>({}));if(!r.ok)throw Error(data.error||'Could not delete.');return data;};
  const errors=[];let done=0;
  try{
    // Discard only takes rejected (or failed-build) icons, so reject the rest first.
    for(const [i,{d}] of picks.entries()){
      msg.textContent=`Rejecting ${i+1}/${picks.length}…`;
      if(d.status!=='fail')await post('/api/reviews',{icon:d.key,svg_sha256:d.svg_sha256,status:'rejected'}).catch(e=>{if(!/rejected/i.test(e.message))errors.push(`${d.icon_id}: ${e.message}`);});
    }
    for(let start=0;start<picks.length;start+=500){
      msg.textContent=`Deleting ${Math.min(start+500,picks.length)}/${picks.length}…`;
      const chunk=picks.slice(start,start+500),result=await post('/api/icons/discard',{icons:chunk.map(({d})=>({icon:d.key,svg_sha256:d.svg_sha256})),detach_variants:true});
      const gone=new Set(result.discarded.map(r=>r.icon));
      for(const {item,d} of chunk)if(gone.has(d.key)){item.drawings=item.drawings.filter(x=>x.key!==d.key);restatus(item);selected.delete(d.key);done++;}
      for(const f of result.failed||[])errors.push(`${f.name||f.icon}: ${f.error}`);
    }
  }catch(e){errors.push(e.message);}
  msg.textContent=`Deleted ${done}.`+(errors.length?` Not deleted (${errors.length}): ${errors.slice(0,5).join(' · ')}${errors.length>5?' …':''}`:'');
  render();
}
// Remove = reject, then discard: deletes the Python model and its exports (archived in icon_set/state/discarded-icons).
function removeButton(item,d){
  const wrap=node('div','sc-remove login-only'),button=node('button','','Remove'),msg=node('span');button.type='button';let armed=0;
  button.onclick=async()=>{
    if(!armed){armed=setTimeout(()=>{armed=0;button.textContent='Remove';button.classList.remove('armed');},4000);button.textContent='Click again to delete';button.classList.add('armed');return;}
    clearTimeout(armed);armed=0;button.disabled=true;button.textContent='Removing…';msg.textContent='';
    try{
      const post=async(url,body)=>{const r=await fetch(url,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});const data=await r.json().catch(()=>({}));if(!r.ok)throw Error(data.error||'Could not remove.');return data;};
      if(d.status!=='fail')await post('/api/reviews',{icon:d.key,svg_sha256:d.svg_sha256,status:'rejected'}).catch(e=>{if(!/rejected/i.test(e.message))throw e;});
      await post('/api/icons/discard',{icon:d.key,svg_sha256:d.svg_sha256,detach_variants:true});
      item.drawings=item.drawings.filter(x=>x.key!==d.key);
      restatus(item);
      render();
    }catch(e){msg.textContent=e.message;button.disabled=false;button.textContent='Remove';button.classList.remove('armed');}
  };
  wrap.append(button,msg);return wrap;
}
function tile(item){
  const b=bucket(item),el=node('article','sc-tile');el.dataset.status=b;
  const art=node('div','sc-art'),ref=node('figure');
  if(item.reference_url){const a=node('a');a.href=item.reference_url;a.target='_blank';a.rel='noopener';const img=document.createElement('img');img.loading='lazy';img.alt=item.concept;img.src=item.reference_url;a.append(img);ref.append(a);}
  else ref.append(node('div','ph','Reference unavailable'));
  ref.append(node('figcaption','','Original reference'));art.append(ref);
  if(item.drawings.length)for(const d of item.drawings)art.append(drawingFigure(item,d));
  else{const f=node('figure');f.append(node('div','ph',b==='text'?'Text · generate separately':'Not generated'));art.append(f);}
  el.append(art);
  const badges=node('div','sc-badges');badges.append(node('span','sc-badge '+b,{missing:'Not generated',failing:'Needs fix',done:'Generated',text:'Text'}[b]));
  if(item.failing_variants&&item.status==='done')badges.append(node('span','sc-badge fail',`${item.failing_variants} failing variant${item.failing_variants===1?'':'s'}`));
  for(const f of item.other_drawings||[])badges.append(node('span','sc-badge',`${f} exists`));
  el.append(badges,node('h3','',item.concept),node('p','',`Used by ${item.uses.toLocaleString()} side pair${item.uses===1?'':'s'}: ${item.pairs.map(p=>p.concept).join(', ')}${item.uses>item.pairs.length?'…':''}`));
  const id=node('p','',item.id);id.title=[item.source_path,...item.source_ids].filter(Boolean).join('\n');el.append(id);
  const failing=item.drawings.filter(d=>d.status!=='pass'&&d.errors.length);
  const marked=item.drawings.filter(d=>reviews[d.key]==='pending');
  if(marked.length)badges.append(node('span','sc-badge fail',`${marked.length} marked needs fix`));
  if(failing.length){const det=node('details','sc-errors');det.append(node('summary','',`Validation errors · ${failing.length} drawing${failing.length===1?'':'s'}`));const ul=node('ul');
    for(const d of failing)for(const e of d.errors)ul.append(node('li','',`${d.icon_id}: ${e}`));det.append(ul);el.append(det);}
  const links=node('div','sc-links'),pairs=node('a','','View side pairs');pairs.href='primitives.html?view=side&q='+encodeURIComponent(item.source_ids[0]||item.id);links.append(pairs);
  if(item.source_path){const s=node('a','','Source SVG');s.href=item.reference_url||'#';s.title=item.source_path;s.target='_blank';s.rel='noopener';links.append(s);}
  el.append(links);if(ROLE==='sub')el.append(classify(item));return el;
}
function classify(item){
  const text=isText(item),section=node('div','sc-classify login-only'),button=node('button','',text?'Not text — mark as icon':'Mark text / number'),msg=node('span');button.type='button';
  const mark=statuses[textMarkId(item)];if(mark)msg.textContent=[mark.updated_by,mark.updated_at?.slice(0,10)].filter(Boolean).join(' · ');
  button.onclick=async()=>{
    button.disabled=true;msg.textContent='Saving…';
    const body=text?{uuids:[textMarkId(item)],status:'todo'}:{uuids:[item.id],status:'skip',reason:'text_number',note:'Side-combination sub component is readable text or a number.'};
    try{const r=await fetch('/api/primitives/status',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}),data=await r.json();
      if(!r.ok)throw Error(data.error||'Could not save.');
      for(const uuid of body.uuids){if(data.decisions?.[uuid])statuses[uuid]=data.decisions[uuid];else delete statuses[uuid];}
      render();
    }catch(e){msg.textContent=e.message;button.disabled=false;}
  };
  section.append(button,msg);return section;
}
function pager(pages,total){const wrap=node('div','sc-pager'),prev=node('button','','← Previous'),next=node('button','','Next →');prev.disabled=page<=1;next.disabled=page>=pages;
  prev.onclick=()=>{page--;render();scrollTo(0,0);};next.onclick=()=>{page++;render();scrollTo(0,0);};
  wrap.append(prev,node('span','sc-note',`${total.toLocaleString()} icons · page ${page} of ${pages}`),next);return wrap;}
function render(){
  renderStats();renderBatch();
  const rows=filtered(),pages=Math.max(1,Math.ceil(rows.length/PAGE_SIZE));page=Math.min(page,pages);
  const visible=rows.slice((page-1)*PAGE_SIZE,page*PAGE_SIZE);
  $('grid').replaceChildren(...(visible.length?visible.map(tile):[node('div','sc-empty','Nothing in this list.')]));
  $('pagerTop').replaceChildren(pager(pages,rows.length));$('pagerBottom').replaceChildren(pager(pages,rows.length));
  $('copy').textContent=`Copy ${rows.length.toLocaleString()} as JSON`;$('copy').disabled=!rows.length;
  writeURL();
}
async function copy(){
  const rows=filtered(),payload={task:HANDOFF[state.status],role:ROLE,status:state.status,count:rows.length,items:rows.map(i=>({
    uuid:i.id,concept:i.concept,reference_path:i.source_path,source_ids:i.source_ids,uses:i.uses,
    ...(i.drawings.length?{drawings:i.drawings.map(d=>({icon_id:d.icon_id,status:d.status,review:reviews[d.key]||null,python_source:d.python_source,errors:d.errors}))}:{}),
    ...(i.other_drawings?.length?{other_drawings:i.other_drawings}:{})}))};
  const text=JSON.stringify(payload,null,2);
  try{await navigator.clipboard.writeText(text);$('copyNote').textContent=`Copied ${rows.length} ${state.status} ${ROLE} icons.`;}
  catch{$('copyText').value=text;$('copyDialog').showModal();$('copyText').select();}
}
let timer;
$('search').value=state.q;$('sort').value=state.sort;
$('search').oninput=()=>{clearTimeout(timer);timer=setTimeout(()=>{state.q=$('search').value;page=1;render();},180);};
$('sort').onchange=()=>{state.sort=$('sort').value;render();};
$('copy').onclick=copy;
$('batchDelete').onclick=batchDelete;$('batchClear').onclick=()=>{selected.clear();$('batchMsg').textContent='';render();};
$('batchPickFailing').onclick=()=>{for(const item of pageRows())for(const d of item.drawings)if(d.svg_sha256&&!usable(d))selected.set(d.key,{item,d});render();};
const clToggle=$('centerline');let showCl=true;try{showCl=localStorage.getItem('sc-centerline')!=='off';}catch{}
const applyCl=()=>{document.body.classList.toggle('sc-no-cl',!showCl);clToggle.setAttribute('aria-pressed',String(showCl));};applyCl();
clToggle.onclick=()=>{showCl=!showCl;try{localStorage.setItem('sc-centerline',showCl?'on':'off');}catch{}applyCl();};$('closeCopy').onclick=()=>$('copyDialog').close();
(async()=>{
  try{
    const [data,status,review]=await Promise.all([fetch('side-components.json',{cache:'no-store'}),ROLE==='sub'?fetch('/api/primitives/status',{cache:'no-store'}).catch(()=>null):null,fetch('/api/reviews',{cache:'no-store'}).catch(()=>null)]);
    if(!data.ok)throw Error('side-components.json is not built yet. Run the gallery build.');
    const json=await data.json();items=ROLE==='sub'?json.subs:json.mains;counts=json.counts[ROLE]||{};
    if(review?.ok)reviews=await review.json();items.forEach(restatus);
    if(status?.ok)statuses=await status.json();else if(ROLE==='sub')$('copyNote').textContent='Text marks unavailable. Reload to retry.';
    $('built').textContent='Data built '+new Date(json.generated_at).toLocaleString()+'.';
    render();
  }catch(e){$('headline').textContent='Could not load: '+e.message;}
})();
})();

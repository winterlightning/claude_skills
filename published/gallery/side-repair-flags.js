(()=>{
 // Main / sub review controls for side pairs. Each component shows its current review status
 // (the same /api/reviews state as Icon review) with Disapprove / Undisapprove beside it.
 // Disapproved = needs a fix; it enters the fix queue like any icon disapproved on Icon review.
 // A static file: gallery has no server, so there a disapproval is only remembered in this browser.
 const offline=location.protocol==='file:';
 const storage='pictographic-side-repair-flags-v1';let rows=[],flags={};if(offline)try{flags=JSON.parse(localStorage.getItem(storage)||'{}');}catch{}
 const clickedKey='pictographic-side-actions-clicked-v1';let clicked={};try{clicked=JSON.parse(localStorage.getItem(clickedKey)||'{}');}catch{}
 let reviews={},reviewsLoaded=offline,reviewsRequest=null;
 const style=document.createElement('style');style.textContent='.side-action-clicked,.pair-card-actions .side-action-clicked,.side-inspect .side-action-clicked{background:#fee2e2!important;border:1px solid #dc2626!important;color:#b91c1c!important}.side-result-actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}.side-result-actions button,.side-result-actions a{font:600 12px system-ui;padding:8px 10px;border:1px solid #bbc9c4;border-radius:6px;background:#f4f7f5;color:#243830;text-decoration:none;cursor:pointer}.side-result-actions,.pair-card-actions,.popup-repair-actions{display:flex!important;flex-wrap:wrap!important;gap:4px!important;align-items:center;min-width:0}.side-result-actions button,.side-result-actions a,.pair-card-actions button,.pair-card-actions a{white-space:nowrap!important;font-size:10px!important;padding:7px 5px!important;text-align:center;min-width:0}.side-review{display:inline-flex;align-items:center;gap:4px;flex:1 1 auto;min-width:0}.side-review button{flex:1 1 auto}.side-review-chip{font:600 10px system-ui;padding:4px 6px;border-radius:999px;white-space:nowrap;border:1px solid #cfd8d4;background:#f4f7f5;color:#43534c}.side-review-chip[data-status=approve]{background:#e3f3e9;border-color:#69a581;color:#22623c}.side-review-chip[data-status=pending],.side-review-chip[data-status=claimed]{background:#fee2e2;border-color:#dc2626;color:#b91c1c}.side-review-chip[data-status=rejected]{background:#ececec;border-color:#b5b5b5;color:#666}.side-review button[data-action=undisapprove]{background:#fee2e2!important;border:1px solid #dc2626!important;color:#b91c1c!important}.side-repair-notes{display:flex;flex-wrap:wrap;gap:4px 10px;margin-top:5px}.side-repair-notes button{font:11px system-ui!important;border:0!important;background:transparent!important;color:#7b4137!important;padding:2px 0!important;cursor:pointer;text-decoration:underline}@media(max-width:540px){.pair-results-grid{grid-template-columns:1fr!important}}';document.head.append(style);
 function mark(action,element){clicked[action]=true;try{localStorage.setItem(clickedKey,JSON.stringify(clicked));}catch{}element.classList.add('side-action-clicked');}
 document.addEventListener('click',e=>{const a=e.target.closest('a[download]');if(a)mark('svg:'+a.download,a);});
 function download(link){link.textContent='SVG';link.classList.toggle('side-action-clicked',!!clicked['svg:'+link.download]);return link;}
 const status=document.createElement('p');status.className='side-flag-status';status.setAttribute('role','status');const toolbar=document.createElement('div');toolbar.className='side-flag-summary';const count=document.createElement('span');toolbar.append(count,status);
 const dialog=document.createElement('dialog');dialog.className='side-inspect';dialog.innerHTML='<form><h2>Repair feedback</h2><p class="component-name"></p><label>What needs fixing? (optional)<textarea rows="3" maxlength="2000" placeholder="Describe the drawing problem"></textarea></label><p class="save-note"></p><div class="pair-actions"><button type="button" class="cancel">Close</button><button type="submit">Save feedback</button></div><p role="status" class="flag-error"></p></form>';document.body.append(dialog);dialog.querySelector('.cancel').onclick=()=>dialog.close();let pending;
 const labels={ready:'Ready',approve:'Approved',pending:'Disapproved',claimed:'Disapproved · fixing',rejected:'Rejected'};

 function iconKey(item){return item.model_key||item.family+'/'+item.icon;}
 function key(item){return iconKey(item)+'@'+item.sha256;}
 // Same mapping as Icon review: re-generated counts as Ready, disapprove as Disapproved; claimed stays distinct (a worker holds it).
 function state(item){if(offline)return flags[key(item)]?'pending':'ready';const s=reviews[iconKey(item)]||'ready';return s==='re-generated'?'ready':s==='disapprove'?'pending':s;}
 const disapproved=item=>['pending','claimed'].includes(state(item));
 function setStatus(text){status.textContent=text;toolbar.hidden=false;}
 function note(text){setStatus(text);}

 function loadReviews(){
  if(offline||reviewsLoaded||reviewsRequest)return reviewsRequest;
  reviewsRequest=fetch('/api/reviews',{cache:'no-store'}).then(r=>{if(!r.ok)throw Error();return r.json();}).then(data=>{reviews=data;reviewsLoaded=true;update();}).catch(()=>{setStatus('Review statuses are unavailable — reload to try again.');}).finally(()=>{reviewsRequest=null;});
  return reviewsRequest;
 }
 function update(){
  const items=new Map();for(const r of rows)for(const item of [...(r.mains||[]),...(r.subs||[])])items.set(iconKey(item),item);
  const n=[...items.values()].filter(disapproved).length;count.textContent=reviewsLoaded?n+' disapproved':'';toolbar.hidden=!n&&!status.textContent;
  for(const box of document.querySelectorAll('.side-review'))paint(box);
  document.dispatchEvent(new CustomEvent('side-repair-flags-change'));
 }

 function request(role,item,pair){pending={role,item,pair};dialog.querySelector('.component-name').textContent=role+': '+item.icon;dialog.querySelector('textarea').value='';dialog.querySelector('.save-note').textContent=offline?'Saved in this browser.':'Adds this note to the icon’s disapproval feedback.';dialog.querySelector('.flag-error').textContent='';dialog.showModal();}
 const pendingSaves=new Map(),contexts=new WeakMap();
 function feedbackLink(box){
  const context=contexts.get(box);if(!context)return;const actions=box.parentElement;if(!actions)return;
  let notes=actions.nextElementSibling;const show=disapproved(context.item)&&!offline;
  const existing=notes?.classList.contains('side-repair-notes')?[...notes.children].find(x=>x.dataset.repairNote===box.dataset.repairKey&&x.dataset.role===context.role):null;
  if(!show){if(existing){existing.remove();if(!notes.children.length)notes.remove();}return;}
  if(existing)return;
  if(!notes?.classList.contains('side-repair-notes')){notes=document.createElement('div');notes.className='side-repair-notes';actions.after(notes);}
  const link=document.createElement('button');link.type='button';link.dataset.repairNote=box.dataset.repairKey;link.dataset.role=context.role;link.textContent='Add '+context.role+' feedback (optional)';link.onclick=()=>request(context.role,context.item,context.pair);notes.append(link);
 }
 async function post(url,body){const r=await fetch(url,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});const d=await r.json().catch(()=>({}));if(r.status===409&&/Icon changed/.test(d.error||''))throw Error('this side pair shows an older drawing than the current icon. Run Combine all side pairs (or change it on Icon review).');if(!r.ok)throw Error(d.error||'Could not save review status');return d;}
 async function disapprove(role,item,pair,text){
  if(offline){flags={...flags,[key(item)]:{icon:iconKey(item),svg_sha256:item.sha256,role,pair_id:pair.id,note:text,flagged_at:new Date().toISOString()}};localStorage.setItem(storage,JSON.stringify(flags));}
  else{const d=await post('/api/feedback',{icon:iconKey(item),svg_sha256:item.sha256,reason:'bad-stroke',feedback:`Flagged ${role} for repair from side combination: ${pair.concept} (${pair.id}).${text?'\n'+text:''}`});reviews={...reviews,[iconKey(item)]:d.status||'pending'};}
  update();note(`${item.icon} disapproved${offline?' in this browser':''}.`);
 }
 async function undisapprove(item){
  if(offline){const next={...flags};delete next[key(item)];flags=next;localStorage.setItem(storage,JSON.stringify(flags));}
  else{const d=await post('/api/reviews',{icon:iconKey(item),svg_sha256:item.sha256,status:'ready'});reviews={...reviews,[iconKey(item)]:d.status||'ready'};}
  update();note(`${item.icon} is back to Ready.`);
 }
 dialog.querySelector('form').onsubmit=async e=>{e.preventDefault();const {role,item,pair}=pending;const submit=dialog.querySelector('[type=submit]');submit.disabled=true;try{await disapprove(role,item,pair,dialog.querySelector('textarea').value.trim());dialog.close();}catch(err){dialog.querySelector('.flag-error').textContent=err.message;}finally{submit.disabled=false;}};

 function paint(box){
  const context=contexts.get(box);if(!context)return;const {role,item}=context,s=state(item),busy=pendingSaves.has(key(item));
  const chip=box.querySelector('.side-review-chip'),b=box.querySelector('button');
  const name=role[0].toUpperCase()+role.slice(1);
  chip.dataset.status=s;chip.textContent=name+' · '+(reviewsLoaded?labels[s]||s:'…');chip.title=item.icon+' — review status '+(labels[s]||s);
  const action=s==='pending'?'undisapprove':['ready','approve'].includes(s)?'disapprove':'';
  b.hidden=!action;b.dataset.action=action;b.textContent=action==='undisapprove'?'Undisapprove':'Disapprove';
  b.disabled=!reviewsLoaded||busy||!action;b.toggleAttribute('aria-busy',busy);
  b.setAttribute('aria-label',(action==='undisapprove'?'Undisapprove ':'Disapprove ')+role+' '+item.icon);
  if(s==='claimed')chip.title+=' — a worker is fixing it';
  feedbackLink(box);
 }
 function button(role,item,pair){
  const box=document.createElement('span');box.className='side-review';box.dataset.repairKey=key(item);box.dataset.repairRole=role;
  const chip=document.createElement('span');chip.className='side-review-chip';
  const b=document.createElement('button');b.type='button';box.append(chip,b);contexts.set(box,{role,item,pair});
  b.onclick=async()=>{
   if(pendingSaves.has(key(item)))return;
   const task=b.dataset.action==='undisapprove'?undisapprove(item):disapprove(role,item,pair,'');
   pendingSaves.set(key(item),task);for(const x of document.querySelectorAll('.side-review'))if(x.dataset.repairKey===key(item))paint(x);
   try{await task;}catch(err){setStatus(item.icon+': '+err.message);}finally{pendingSaves.delete(key(item));for(const x of document.querySelectorAll('.side-review'))if(x.dataset.repairKey===key(item))paint(x);}
  };
  paint(box);queueMicrotask(()=>paint(box));loadReviews();return box;
 }

 window.SideRepairFlags={flagged:disapproved,status:state,
  setReviews(value){if(offline||!value||typeof value!=='object')return;reviews=value;reviewsLoaded=true;update();},
  setRows(value){rows=value;if(!toolbar.isConnected)(document.getElementById('pairGallery')||document.querySelector('header')||document.body).prepend(toolbar);loadReviews();update();},
  button,download,
  popup(target,result){target.querySelector('.popup-repair-actions')?.remove();const pair=rows.find(r=>r.id===result.filename?.replace(/\.svg$/,''));if(!pair)return;const actions=document.createElement('div');actions.className='pair-actions popup-repair-actions';for(const role of ['main','sub']){const uid=result.placements.find(p=>p.role===role)?.icon;const item=pair[role==='main'?'mains':'subs'].find(x=>x.icon===uid);if(item)actions.append(button(role,item,pair));}target.append(actions);const a=target.querySelector('a[download]');if(a)download(a);}};
})();

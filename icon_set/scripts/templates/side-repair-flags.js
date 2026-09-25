(()=>{
 // Main / sub review controls for side pairs. Each component shows its current review status
 // (the same /api/reviews state as Icon review) with direct Approve / Disapprove actions beside it.
 // Disapproved = needs a fix; it enters the fix queue like any icon disapproved on Icon review.
 // A static file: gallery has no server, so there a disapproval is only remembered in this browser.
 const offline=location.protocol==='file:';
 const storage='pictographic-side-repair-flags-v1';let rows=[],flags={};if(offline)try{flags=JSON.parse(localStorage.getItem(storage)||'{}');}catch{}
 const clickedKey='pictographic-side-actions-clicked-v1';let clicked={};try{clicked=JSON.parse(localStorage.getItem(clickedKey)||'{}');}catch{}
 let reviews={},reviewsLoaded=offline,reviewsRequest=null;
 const style=document.createElement('style');style.textContent='a.side-action-clicked{color:#6b3f8f!important}.side-result-actions,.pair-card-actions,.popup-repair-actions{display:flex!important;flex-wrap:wrap!important;gap:8px!important;align-items:center;min-width:0}.side-result-actions{margin-top:14px}.side-result-actions>a[download],.pair-card-actions>a[download],.popup-repair-actions a[download]{font:600 12px system-ui;padding:6px 12px;border:1px solid #c9d4cf;border-radius:6px;background:#fff;color:#2f4a3e;text-decoration:none;white-space:nowrap}.side-result-actions>a[download]:hover,.pair-card-actions>a[download]:hover{background:#f1f6f3}.side-review{display:inline-flex;align-items:stretch;border:1px solid #c9d4cf;border-radius:8px;background:#fff;overflow:hidden;font:12px system-ui;white-space:nowrap;box-shadow:0 1px 0 rgba(20,40,30,.04)}.side-review-chip{display:inline-flex;align-items:center;gap:6px;padding:6px 10px;color:#43534c}.side-review-chip b{font-weight:600;color:#1f2e27}.side-review-chip::before{content:"";width:8px;height:8px;border-radius:50%;background:#9aa8a2;flex:none}.side-review[data-status=approve]{border-color:#8cc3a0}.side-review[data-status=approve] .side-review-chip{background:#eef8f1;color:#22623c}.side-review[data-status=approve] .side-review-chip::before{background:#2f9a57}.side-review[data-status=pending],.side-review[data-status=claimed]{border-color:#eba8a0}.side-review[data-status=pending] .side-review-chip,.side-review[data-status=claimed] .side-review-chip{background:#fdf0ee;color:#a1291d}.side-review[data-status=pending] .side-review-chip::before,.side-review[data-status=claimed] .side-review-chip::before{background:#d63c2c}.side-review[data-status=rejected] .side-review-chip{background:#f1f1f1;color:#666}.side-review[data-status=rejected] .side-review-chip::before{background:#999}.side-review button{font:600 12px system-ui;padding:6px 12px;border:0;background:#fff;cursor:pointer;margin:0;border-radius:0}.side-review button[hidden]{display:none}.side-review button[data-action=disapprove]{color:#b42318;border-left:1px solid #c9d4cf}.side-review button[data-action=disapprove]:hover{background:#fdecea}.side-review[data-status=approve] button[data-action=disapprove]{border-left-color:#8cc3a0}.side-review button[data-action=approve]{color:#25653a;border-left:1px solid #eba8a0}.side-review button[data-action=approve]:hover{background:#eef8f1}.side-review button:disabled{opacity:.55;cursor:default}.side-review button[aria-busy]{cursor:progress}.side-review button:focus-visible{outline:2px solid #2f7d4a;outline-offset:-2px}.side-repair-notes{display:flex;flex-wrap:wrap;justify-content:flex-end;gap:4px 12px;margin-top:6px;width:100%}.side-repair-notes button{font:12px system-ui;border:0;background:transparent;color:#8a3b2f;padding:2px 0;cursor:pointer;text-decoration:underline;text-underline-offset:2px}@media(max-width:540px){.pair-results-grid{grid-template-columns:1fr!important}.side-review{flex:1 1 100%}.side-review button{margin-left:auto}}';document.head.append(style);
 function mark(action,element){clicked[action]=true;try{localStorage.setItem(clickedKey,JSON.stringify(clicked));}catch{}element.classList.add('side-action-clicked');}
 document.addEventListener('click',e=>{const a=e.target.closest('a[download]');if(a)mark('svg:'+a.download,a);});
 function download(link){link.textContent='SVG';link.classList.toggle('side-action-clicked',!!clicked['svg:'+link.download]);return link;}
 const status=document.createElement('p');status.className='side-flag-status';status.setAttribute('role','status');const toolbar=document.createElement('div');toolbar.className='side-flag-summary';const count=document.createElement('span');toolbar.append(count,status);
 const dialog=document.createElement('dialog');dialog.className='side-inspect';dialog.innerHTML='<form><h2>Repair feedback</h2><p class="component-name"></p><label>What needs fixing? (optional)<textarea rows="3" maxlength="2000" placeholder="Describe the drawing problem"></textarea></label><p class="save-note"></p><div class="pair-actions"><button type="button" class="cancel">Close</button><button type="submit">Save feedback</button></div><p role="status" class="flag-error"></p></form>';document.body.append(dialog);dialog.querySelector('.cancel').onclick=()=>dialog.close();let pending;
 const labels={ready:'Ready',approve:'Approved',pending:'Disapproved',claimed:'Being fixed',rejected:'Rejected'};

 function iconKey(item){return item.model_key||item.family+'/'+item.icon;}
 function key(item){return iconKey(item)+'@'+item.sha256;}
 // Same mapping as Icon review: re-generated counts as Ready, disapprove as Disapproved; claimed stays distinct (a worker holds it).
 function state(item){if(offline)return flags[key(item)]?.status||(flags[key(item)]?'pending':'ready');const s=reviews[iconKey(item)]||'ready';return s==='re-generated'?'ready':s==='disapprove'?'pending':s;}
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
 async function post(url,body){const r=await fetch(url,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});const d=await r.json().catch(()=>({}));if(r.status===409&&/Icon changed/.test(d.error||''))throw Error('this side pair shows an older drawing than the current icon. Reload the gallery to review the latest saved drawing.');if(!r.ok)throw Error(d.error||'Could not save review status');return d;}
 async function disapprove(role,item,pair,text){
  if(offline){flags={...flags,[key(item)]:{icon:iconKey(item),svg_sha256:item.sha256,role,pair_id:pair.id,note:text,flagged_at:new Date().toISOString()}};localStorage.setItem(storage,JSON.stringify(flags));}
  else{const d=await post('/api/feedback',{icon:iconKey(item),svg_sha256:item.sha256,reason:'bad-stroke',feedback:`Flagged ${role} for repair from side combination: ${pair.concept} (${pair.id}).${text?'\n'+text:''}`});reviews={...reviews,[iconKey(item)]:d.status||'pending'};}
  update();note(`${item.icon} disapproved${offline?' in this browser':''}.`);
 }
 async function approve(item){
  if(offline){flags={...flags,[key(item)]:{status:'approve'}};localStorage.setItem(storage,JSON.stringify(flags));}
  else{const d=await post('/api/reviews',{icon:iconKey(item),svg_sha256:item.sha256,status:'approve'});reviews={...reviews,[iconKey(item)]:d.status||'approve'};}
  update();note(`${item.icon} approved${offline?' in this browser':''}.`);
 }
 dialog.querySelector('form').onsubmit=async e=>{e.preventDefault();const {role,item,pair}=pending;const submit=dialog.querySelector('[type=submit]');submit.disabled=true;try{await disapprove(role,item,pair,dialog.querySelector('textarea').value.trim());dialog.close();}catch(err){dialog.querySelector('.flag-error').textContent=err.message;}finally{submit.disabled=false;}};

 function paint(box){
  const context=contexts.get(box);if(!context)return;const {role,item}=context,s=state(item),busy=pendingSaves.has(key(item));
  const chip=box.querySelector('.side-review-chip');
  const name=role[0].toUpperCase()+role.slice(1);
  box.dataset.status=s;const role_=document.createElement('b');role_.textContent=name;chip.replaceChildren(role_,' '+(reviewsLoaded?labels[s]||s:'Loading…'));chip.title=item.icon+' — review status '+(labels[s]||s);
  for(const b of box.querySelectorAll('button')){
   const approving=b.dataset.action==='approve';
   b.hidden=false;b.textContent=approving?'Approve':'Disapprove';
   b.disabled=!reviewsLoaded||busy||['claimed','rejected'].includes(s)||(approving?s==='approve':s==='pending');
   b.toggleAttribute('aria-busy',busy);
   b.setAttribute('aria-label',(approving?'Approve ':'Disapprove ')+role+' '+item.icon);
  }
  if(s==='claimed')chip.title+=' — a worker is fixing it';
  feedbackLink(box);
 }
 function button(role,item,pair){
  const box=document.createElement('span');box.className='side-review';box.dataset.repairKey=key(item);box.dataset.repairRole=role;
  const chip=document.createElement('span');chip.className='side-review-chip';
  box.append(chip);contexts.set(box,{role,item,pair});
  for(const action of ['approve','disapprove']){
   const b=document.createElement('button');b.type='button';b.dataset.action=action;box.append(b);
   b.onclick=async()=>{
    if(pendingSaves.has(key(item)))return;
    const task=action==='approve'?approve(item):disapprove(role,item,pair,'');
    pendingSaves.set(key(item),task);for(const x of document.querySelectorAll('.side-review'))if(x.dataset.repairKey===key(item))paint(x);
    try{await task;}catch(err){setStatus(item.icon+': '+err.message);}finally{pendingSaves.delete(key(item));for(const x of document.querySelectorAll('.side-review'))if(x.dataset.repairKey===key(item))paint(x);}
   };
  }
  paint(box);queueMicrotask(()=>paint(box));loadReviews();return box;
 }

 window.SideRepairFlags={flagged:disapproved,status:state,
  setReviews(value){if(offline||!value||typeof value!=='object')return;reviews=value;reviewsLoaded=true;update();},
  setRows(value){rows=value;if(!toolbar.isConnected)(document.getElementById('pairGallery')||document.querySelector('header')||document.body).prepend(toolbar);loadReviews();update();},
  button,download,
  popup(target,result){target.querySelector('.popup-repair-actions')?.remove();const pair=rows.find(r=>r.id===result.filename?.replace(/\.svg$/,''));if(!pair)return;const actions=document.createElement('div');actions.className='pair-actions popup-repair-actions';for(const role of ['main','sub']){const uid=result.placements.find(p=>p.role===role)?.icon;const item=pair[role==='main'?'mains':'subs'].find(x=>x.icon===uid);if(item)actions.append(button(role,item,pair));}target.append(actions);const a=target.querySelector('a[download]');if(a)download(a);}};
})();

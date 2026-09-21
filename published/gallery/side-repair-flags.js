(()=>{
 const storage='pictographic-side-repair-flags-v1';let rows=[],flags={};try{flags=JSON.parse(localStorage.getItem(storage)||'{}');}catch{}
 const clickedKey='pictographic-side-actions-clicked-v1';let clicked={};try{clicked=JSON.parse(localStorage.getItem(clickedKey)||'{}');}catch{}
 const style=document.createElement('style');style.textContent='.side-action-clicked,.pair-card-actions .side-action-clicked,.side-inspect .side-action-clicked{background:#fee2e2!important;border:1px solid #dc2626!important;color:#b91c1c!important}.side-result-actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}.side-result-actions button,.side-result-actions a{font:600 12px system-ui;padding:8px 10px;border:1px solid #bbc9c4;border-radius:6px;background:#f4f7f5;color:#243830;text-decoration:none;cursor:pointer}.side-result-actions,.pair-card-actions,.popup-repair-actions{display:flex!important;flex-wrap:nowrap!important;gap:4px!important;align-items:center;min-width:0}.side-result-actions button,.side-result-actions a,.pair-card-actions button,.pair-card-actions a{white-space:nowrap!important;font-size:10px!important;padding:7px 5px!important;flex:1 1 auto;text-align:center;min-width:0}.side-repair-notes{display:flex;flex-wrap:wrap;gap:4px 10px;margin-top:5px}.side-repair-notes button{font:11px system-ui!important;border:0!important;background:transparent!important;color:#7b4137!important;padding:2px 0!important;cursor:pointer;text-decoration:underline}@media(max-width:540px){.pair-results-grid{grid-template-columns:1fr!important}}[data-repair-key]:not(.side-action-clicked){background:#e3f3e9!important;border-color:#69a581!important;color:#22623c!important}';document.head.append(style);
 function mark(action,element){clicked[action]=true;try{localStorage.setItem(clickedKey,JSON.stringify(clicked));}catch{}element.classList.add('side-action-clicked');}
 document.addEventListener('click',e=>{const a=e.target.closest('a[download]');if(a)mark('svg:'+a.download,a);});
 function download(link){link.textContent='SVG';link.classList.toggle('side-action-clicked',!!clicked['svg:'+link.download]);return link;}
 const status=document.createElement('p');status.className='side-flag-status';status.setAttribute('role','status');const toolbar=document.createElement('div');toolbar.className='side-flag-summary';const count=document.createElement('span');toolbar.append(count,status);
 const dialog=document.createElement('dialog');dialog.className='side-inspect';dialog.innerHTML='<form><h2>Repair feedback</h2><p class="component-name"></p><label>What needs fixing? (optional)<textarea rows="3" maxlength="2000" placeholder="Describe the drawing problem"></textarea></label><p class="save-note"></p><div class="pair-actions"><button type="button" class="cancel">Close</button><button type="submit">Save feedback</button></div><p role="status" class="flag-error"></p></form>';document.body.append(dialog);dialog.querySelector('.cancel').onclick=()=>dialog.close();let pending;
 function update(){count.textContent=Object.keys(flags).length+' flagged';toolbar.hidden=!Object.keys(flags).length&&!status.textContent;for(const b of document.querySelectorAll('[data-repair-key]')){b.textContent='REPAIR '+b.dataset.repairRole.toUpperCase();b.classList.toggle('side-action-clicked',!!flags[b.dataset.repairKey]);b.setAttribute('aria-pressed',String(!!flags[b.dataset.repairKey]));if(flags[b.dataset.repairKey])addFeedbackLink(b);}}

 function key(item){return (item.model_key||item.family+'/'+item.icon)+'@'+item.sha256;}
 function request(role,item,pair){pending={role,item,pair};dialog.querySelector('.component-name').textContent=role+': '+item.icon;dialog.querySelector('textarea').value=flags[key(item)]?.note||'';dialog.querySelector('.save-note').textContent=location.protocol==='file:'?'Saved in this browser.':'Saves to the component’s repair-feedback record. A browser copy is kept after saving.';dialog.querySelector('.flag-error').textContent='';dialog.showModal();}
 const pendingSaves=new Map(),contexts=new WeakMap();
 function addFeedbackLink(b){
  const context=contexts.get(b);if(!context||!b.parentElement)return;
  const actions=b.parentElement;let notes=actions.nextElementSibling;
  if(!notes?.classList.contains('side-repair-notes')){notes=document.createElement('div');notes.className='side-repair-notes';actions.after(notes);}
  if([...notes.children].some(x=>x.dataset.repairNote===b.dataset.repairKey))return;
  const link=document.createElement('button');link.type='button';link.dataset.repairNote=b.dataset.repairKey;link.textContent=context.role+' feedback (optional)';link.onclick=()=>request(context.role,context.item,context.pair);notes.append(link);
 }
 async function clearFlag(item){
  const previous=flags[key(item)];if(!previous)return;
  localStorage.setItem(storage,JSON.stringify(flags));
  if(previous.saved_to==='server'){
   if(location.protocol==='file:')throw Error('Open the served gallery to clear this saved review flag.');
   const response=await fetch('/api/reviews',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({icon:previous.icon,svg_sha256:previous.svg_sha256,status:'ready'})});
   const data=await response.json();if(!response.ok)throw Error(data.error||'Could not clear repair flag');
  }
  const next={...flags};delete next[key(item)];localStorage.setItem(storage,JSON.stringify(next));flags=next;
  delete clicked['repair:'+key(item)];try{localStorage.setItem(clickedKey,JSON.stringify(clicked));}catch{}
  for(const link of document.querySelectorAll('[data-repair-note]'))if(link.dataset.repairNote===key(item)){const notes=link.parentElement;link.remove();if(!notes.children.length)notes.remove();}
  update();status.textContent=item.icon+' repair flag cleared.';toolbar.hidden=false;
 }
 async function save(role,item,pair,note){
  const record={icon:item.model_key||item.family+'/'+item.icon,svg_sha256:item.sha256,role,pair_id:pair.id,concept:pair.concept,note,flagged_at:flags[key(item)]?.flagged_at||new Date().toISOString(),saved_to:'browser'};
  localStorage.setItem(storage,JSON.stringify(flags));
  if(location.protocol!=='file:'){const r=await fetch('/api/feedback',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({icon:record.icon,svg_sha256:record.svg_sha256,reason:'bad-stroke',feedback:`Flagged ${role} for repair from side combination: ${pair.concept} (${pair.id}).${note?'\n'+note:''}`})});const d=await r.json();if(!r.ok)throw Error(d.error||'Could not save repair feedback');record.saved_to='server';}
  const next={...flags,[key(item)]:record};localStorage.setItem(storage,JSON.stringify(next));flags=next;update();status.textContent=`${item.icon} flagged — ${record.saved_to==='server'?'saved':'saved in this browser'}.`;toolbar.hidden=false;
 }
 dialog.querySelector('form').onsubmit=async e=>{e.preventDefault();const {role,item,pair}=pending;const submit=dialog.querySelector('[type=submit]');submit.disabled=true;try{await save(role,item,pair,dialog.querySelector('textarea').value.trim());dialog.close();}catch(err){dialog.querySelector('.flag-error').textContent=err.message;}finally{submit.disabled=false;}};
 function button(role,item,pair){
  const b=document.createElement('button');b.type='button';b.dataset.repairKey=key(item);b.dataset.repairRole=role;b.textContent='REPAIR '+role.toUpperCase();b.classList.toggle('side-action-clicked',!!flags[key(item)]);b.setAttribute('aria-pressed',String(!!flags[key(item)]));contexts.set(b,{role,item,pair});
  b.onclick=async()=>{b.disabled=true;b.setAttribute('aria-busy','true');try{let task=pendingSaves.get(key(item));if(!task){task=flags[key(item)]?clearFlag(item):save(role,item,pair,'');pendingSaves.set(key(item),task);}await task;if(flags[key(item)])addFeedbackLink(b);}catch(err){status.textContent=err.message;toolbar.hidden=false;}finally{pendingSaves.delete(key(item));b.disabled=false;b.removeAttribute('aria-busy');}};

  // Restore optional-note access when a previously flagged card is rendered again.
  queueMicrotask(()=>{if(flags[key(item)])addFeedbackLink(b);});return b;
 }

 window.SideRepairFlags={setRows(value){rows=value;if(!toolbar.isConnected)(document.getElementById('pairGallery')||document.querySelector('header')||document.body).prepend(toolbar);update();},button,download,popup(target,result){target.querySelector('.popup-repair-actions')?.remove();const pair=rows.find(r=>r.id===result.filename?.replace(/\.svg$/,''));if(!pair)return;const actions=document.createElement('div');actions.className='pair-actions popup-repair-actions';for(const role of ['main','sub']){const uid=result.placements.find(p=>p.role===role)?.icon;const item=pair[role==='main'?'mains':'subs'].find(x=>x.icon===uid);if(item)actions.append(button(role,item,pair));}target.append(actions);const a=target.querySelector('a[download]');if(a)download(a);}};
})();

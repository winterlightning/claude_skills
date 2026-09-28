/* Edits belong to one placement in one example, never to the source SVG. */
window.PreviewIconEditor = function({icons, example}) {
  let byId=new Map(icons.map(i=>[i.icon_id,i]));
  const storageKey='pictographic-preview-icons-v1:'+example;
  const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const label=i=>(i?.name||i?.icon_id||'Icon').replaceAll('-',' ');
  let replacements={},counter=0,selected=null,page=0,returnFocus=null,busy=false,mode='side';
  try{const saved=JSON.parse(localStorage.getItem(storageKey)||'{}');replacements=approvedPreviewReplacements(saved,icons);}catch{}
  // Combination mode keeps its own picks ('side:'+slot) so choosing a combined
  // icon never changes the solo view of the same placement, and vice versa.
  // Views: 'solo' (Primitive 48), 'p72' (best name match in Primitive 72), 'side'
  // (side combination) and 'shuffle' (a random pick per placement, never saved).
  const keyFor=slot=>mode==='side'?'side:'+slot:mode==='p72'?'p72:'+slot:mode==='shuffle'?'':slot;
  const FILLER=new Set(['with','and','the','of','in','on','a','an','simple','round','rounded','symbol','icon','reference']);
  const words=text=>String(text).toLowerCase().split(/[^a-z0-9]+/).filter(w=>w.length>1&&!/\d/.test(w)&&!FILLER.has(w));
  const same=(a,b)=>a===b||a===b+'s'||b===a+'s'||a===b+'es'||b===a+'es';
  let matches=new Map(),shuffled=new Map();
  function match72(id){
    if(!matches.has(id)){
      const wanted=words(id);let best=null,bestScore=0,bestExtra=0;
      for(const i of icons){
        if(i.family!=='icon-72')continue;
        const have=words(i.name||i.icon_id),score=wanted.filter(w=>have.some(h=>same(w,h))).length,extra=have.length-score;
        if(score>bestScore||(score&&score===bestScore&&(extra<bestExtra||(extra===bestExtra&&i.icon_id<best))))[best,bestScore,bestExtra]=[i.icon_id,score,extra];
      }
      matches.set(id,best);
    }
    return matches.get(id);
  }
  const pool=()=>icons.filter(i=>['solo','icon-72','combination'].includes(i.family));
  function shuffledFor(slot){if(!shuffled.has(slot)){const p=pool();shuffled.set(slot,p.length?p[Math.floor(Math.random()*p.length)].icon_id:'');}return shuffled.get(slot);}
  const baseline=(original,variant)=>mode==='side'?variant||original:mode==='p72'?match72(original)||original:original;
  function resolve(slot,original,variant){
    if(mode==='shuffle')return shuffledFor(slot);
    if(mode==='side')return replacements['side:'+slot]||variant||replacements[slot]||original;
    if(mode==='p72')return replacements['p72:'+slot]||match72(original)||replacements[slot]||original;
    return replacements[slot]||original;
  }
  function resolveEl(el){return resolve(el.dataset.slot,el.dataset.original,el.dataset.variant);}
  function icon(id,cls='',slot,variant){
    slot=slot||'position-'+counter++;
    const current=byId.get(resolve(slot,id,variant))||byId.get(baseline(id,variant));
    if(!current)return `<span class="icon-swap empty-placement" data-slot="${esc(slot)}" data-original="${esc(id)}" data-variant="${esc(variant||'')}" data-icon="" role="button" tabindex="0" aria-label="Choose an approved icon" title="Choose an approved icon"><span class="p-icon ${cls}" aria-hidden="true"></span></span>`;
    return `<span class="icon-swap" data-slot="${esc(slot)}" data-original="${esc(id)}" data-variant="${esc(variant||'')}" data-icon="${esc(current.icon_id)}" role="button" tabindex="0" aria-label="Change ${esc(label(current))} icon" title="Change ${esc(label(current))}"><span class="p-icon ${cls}" aria-hidden="true" style="--icon:url('${esc(encodeURI(current.preview_url))}')"></span></span>`;
  }
  const bar=document.createElement('div');bar.className='scene-editbar';
  bar.innerHTML='<span>Approved icons · click to change</span><div><span id="editCount" role="status"></span><button id="resetExampleIcons" type="button">Reset icons</button></div>';
  const dialog=document.createElement('dialog');dialog.className='icon-picker';dialog.setAttribute('aria-labelledby','iconPickerTitle');
  dialog.innerHTML=`<div class="picker-heading"><div><p>MAKE IT YOURS</p><h2 id="iconPickerTitle">Choose an approved icon</h2></div><button type="button" id="closeIconPicker" aria-label="Close icon picker">✕</button></div><p id="pickerCurrent" class="picker-current"></p><label class="picker-search"><span class="sr-only">Search icons</span><input type="search" id="iconPickerSearch" placeholder="Search ${icons.length.toLocaleString()} approved icons…" autocomplete="off"></label><div class="picker-filters"><label>Family<select id="iconPickerFamily"><option value="" selected>All families</option><option value="solo">Primitive 48</option><option value="icon-72">Primitive 72</option><option value="sub">Sub</option><option value="container">Container</option><option value="combination">Combination</option></select></label><label>Category<select id="iconPickerCategory"><option value="">All categories</option></select></label></div><p id="pickerResultsStatus" role="status"></p><div id="pickerResults" class="picker-results"></div><div class="picker-footer"><button id="restorePlacement" type="button">Restore original</button><div><button id="pickerPrev" aria-label="Previous icons" type="button">←</button><span id="pickerPage"></span><button id="pickerNext" aria-label="Next icons" type="button">→</button></div></div>`;
  const $=id=>dialog.querySelector('#'+id);
  for(const category of [...new Set(icons.map(i=>i.category).filter(Boolean))].sort()){const o=document.createElement('option');o.value=category;o.textContent=category;$('iconPickerCategory').append(o);}
  const count=()=>{const n=Object.keys(replacements).length;bar.querySelector('#editCount').textContent=n?`${n} changed`:'';bar.querySelector('#resetExampleIcons').disabled=!n;};
  function save(){try{localStorage.setItem(storageKey,JSON.stringify(replacements));return true;}catch{return false;}}
  function announce(){count();if(parent!==window)parent.postMessage({type:'preview-icons-used',example,ids:[...new Set([...document.querySelectorAll('.icon-swap')].map(el=>el.dataset.icon))]},location.origin);}
  function apply(el,id){const i=byId.get(id);if(!i){el.dataset.icon='';el.classList.add('empty-placement');el.setAttribute('aria-label','Choose an approved icon');el.title='Choose an approved icon';el.querySelector('.p-icon').style.removeProperty('--icon');return;}el.classList.remove('empty-placement');el.dataset.icon=id;el.setAttribute('aria-label','Change '+label(i)+' icon');el.title='Change '+label(i);el.querySelector('.p-icon').style.setProperty('--icon',`url("${encodeURI(i.preview_url).replaceAll('"','%22')}")`);}
  function render(){
    const terms=$('iconPickerSearch').value.trim().toLowerCase().split(/\s+/).filter(Boolean),family=$('iconPickerFamily').value,category=$('iconPickerCategory').value;
    const rows=icons.filter(i=>(!family||i.family===family)&&(!category||i.category===category)&&terms.every(t=>[i.name,i.icon_id,i.category].join(' ').replaceAll('-',' ').toLowerCase().includes(t.replaceAll('-',' '))));
    const pages=Math.max(1,Math.ceil(rows.length/60));page=Math.max(0,Math.min(page,pages-1));
    $('pickerResultsStatus').textContent=rows.length?`${rows.length.toLocaleString()} ${family==='combination'?'combined':'approved'} icons · select one to replace this placement`:'No matching icons. Try another word or clear the filters.';
    $('pickerResults').replaceChildren();
    for(const i of rows.slice(page*60,(page+1)*60)){
      const b=document.createElement('button');b.type='button';b.className='picker-choice';b.setAttribute('aria-label','Use '+label(i));b.setAttribute('aria-pressed',String(selected?.dataset.icon===i.icon_id));
      const img=document.createElement('img');img.src=i.preview_url;img.alt='';img.loading='lazy';const name=document.createElement('span');name.textContent=label(i);b.append(img,name);b.onclick=()=>choose(i.icon_id);$('pickerResults').append(b);
    }
    $('pickerPage').textContent=`${page+1} / ${pages}`;$('pickerPrev').disabled=page===0;$('pickerNext').disabled=page===pages-1;
    $('restorePlacement').disabled=!selected||mode==='shuffle'||!replacements[keyFor(selected.dataset.slot)]||!byId.has(baseline(selected.dataset.original,selected.dataset.variant));
  }
  async function refreshApproved(){
    try{icons=await loadApprovedPreviewIcons();}catch(error){icons=[];byId=new Map();document.querySelectorAll('.icon-swap').forEach(el=>apply(el,''));announce();throw error;}
    byId=new Map(icons.map(i=>[i.icon_id,i]));matches=new Map();
    replacements=approvedPreviewReplacements(replacements,icons);
    document.querySelectorAll('.icon-swap').forEach(el=>apply(el,resolveEl(el)));
    $('iconPickerSearch').placeholder=`Search ${icons.length.toLocaleString()} approved icons…`;announce();
  }
  async function choose(id){
    if(!selected||busy)return;busy=true;
    $('pickerResultsStatus').textContent='Checking approval…';
    try{
      await refreshApproved();
      if(!selected)return;
      if(!byId.has(id)){render();$('pickerResultsStatus').textContent='That icon is no longer approved. Choose another icon.';return;}
      if(mode==='shuffle'){shuffled.set(selected.dataset.slot,id);apply(selected,id);announce();dialog.close();return;}
      const key=keyFor(selected.dataset.slot);if(id===baseline(selected.dataset.original,selected.dataset.variant))delete replacements[key];else replacements[key]=id;
      apply(selected,resolveEl(selected));const saved=save();announce();dialog.close();if(!saved)bar.querySelector('#editCount').textContent='Changed for this visit · browser storage unavailable';
    }catch{if(dialog.open){$('pickerResults').replaceChildren();$('pickerResultsStatus').textContent='Could not verify approval. Close the picker and try again.';}}
    finally{busy=false;}
  }
  async function open(el){selected=el;returnFocus=el;document.querySelectorAll('.icon-swap.is-selected').forEach(x=>x.classList.remove('is-selected'));el.classList.add('is-selected');$('pickerCurrent').textContent='Replacing '+label(byId.get(el.dataset.icon))+({side:' in the combination view',p72:' in the Primitive 72 view',shuffle:' in the shuffled view (not saved)'}[mode]||'')+'. Only this placement will change.';$('iconPickerTitle').textContent=mode==='side'?'Choose a combined icon':'Choose an approved icon';$('iconPickerSearch').value='';$('iconPickerFamily').value={side:'combination',p72:'icon-72'}[mode]||'';$('iconPickerCategory').value='';page=0;$('pickerResults').replaceChildren();$('restorePlacement').disabled=true;dialog.showModal();$('iconPickerSearch').focus();busy=true;$('pickerResultsStatus').textContent='Loading approved icons…';try{await refreshApproved();if(dialog.open)render();}catch{if(dialog.open)$('pickerResultsStatus').textContent='Could not verify approval. Close the picker and try again.';}finally{busy=false;}}
  for(const id of ['iconPickerSearch','iconPickerFamily','iconPickerCategory'])$(id).addEventListener(id==='iconPickerSearch'?'input':'change',()=>{page=0;render();});
  $('pickerPrev').onclick=()=>{page--;render();$('pickerResults').scrollTop=0;};$('pickerNext').onclick=()=>{page++;render();$('pickerResults').scrollTop=0;};
  $('closeIconPicker').onclick=()=>dialog.close();$('restorePlacement').onclick=()=>choose(baseline(selected.dataset.original,selected.dataset.variant));
  dialog.addEventListener('close',()=>{selected?.classList.remove('is-selected');if(returnFocus?.isConnected)returnFocus.focus({preventScroll:true});selected=null;});
  bar.querySelector('#resetExampleIcons').onclick=async()=>{if(busy)return;busy=true;replacements={};save();try{await refreshApproved();}catch{bar.querySelector('#editCount').textContent='Could not verify approval. Reload to try again.';}finally{busy=false;}};
  function mount(){
    document.body.prepend(bar);document.body.append(dialog);announce();
    document.addEventListener('click',e=>{const el=e.target.closest('.icon-swap');if(!el||busy)return;e.preventDefault();e.stopImmediatePropagation();open(el);},true);
    document.addEventListener('keydown',e=>{const el=e.target.closest('.icon-swap');if(!el||!['Enter',' '].includes(e.key))return;e.preventDefault();e.stopImmediatePropagation();open(el);},true);
  }
  function reapply(){document.querySelectorAll('.icon-swap').forEach(el=>apply(el,resolveEl(el)));announce();}
  function setMode(next){mode=['solo','p72','side'].includes(next)?next:'side';reapply();}
  function shuffle(){mode='shuffle';shuffled=new Map();reapply();}
  return {icon,mount,announce,setMode,shuffle};
};

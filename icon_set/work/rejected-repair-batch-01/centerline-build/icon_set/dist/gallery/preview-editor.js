/* Edits belong to one placement in one example, never to the source SVG. */
window.PreviewIconEditor = function({icons, example}) {
  let byId=new Map(icons.map(i=>[i.icon_id,i]));
  const storageKey='pictographic-preview-icons-v1:'+example;
  const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const label=i=>(i?.name||i?.icon_id||'Icon').replaceAll('-',' ');
  let replacements={},counter=0,selected=null,page=0,returnFocus=null,busy=false;
  try{const saved=JSON.parse(localStorage.getItem(storageKey)||'{}');replacements=approvedPreviewReplacements(saved,icons);}catch{}
  function icon(id,cls='',slot){
    slot=slot||'position-'+counter++;
    const current=byId.get(replacements[slot])||byId.get(id);
    if(!current)return `<span class="icon-swap empty-placement" data-slot="${esc(slot)}" data-original="${esc(id)}" data-icon="" role="button" tabindex="0" aria-label="Choose an approved icon" title="Choose an approved icon"><span class="p-icon ${cls}" aria-hidden="true"></span></span>`;
    return `<span class="icon-swap" data-slot="${esc(slot)}" data-original="${esc(id)}" data-icon="${esc(current.icon_id)}" role="button" tabindex="0" aria-label="Change ${esc(label(current))} icon" title="Change ${esc(label(current))}"><span class="p-icon ${cls}" aria-hidden="true" style="--icon:url('${esc(encodeURI(current.preview_url))}')"></span></span>`;
  }
  const bar=document.createElement('div');bar.className='scene-editbar';
  bar.innerHTML='<span>Approved icons · click to change</span><div><span id="editCount" role="status"></span><button id="resetExampleIcons" type="button">Reset icons</button></div>';
  const dialog=document.createElement('dialog');dialog.className='icon-picker';dialog.setAttribute('aria-labelledby','iconPickerTitle');
  dialog.innerHTML=`<div class="picker-heading"><div><p>MAKE IT YOURS</p><h2 id="iconPickerTitle">Choose an approved icon</h2></div><button type="button" id="closeIconPicker" aria-label="Close icon picker">✕</button></div><p id="pickerCurrent" class="picker-current"></p><label class="picker-search"><span class="sr-only">Search icons</span><input type="search" id="iconPickerSearch" placeholder="Search ${icons.length.toLocaleString()} approved icons…" autocomplete="off"></label><div class="picker-filters"><label>Family<select id="iconPickerFamily"><option value="">All families</option><option value="solo" selected>Solo</option><option value="sub">Sub</option><option value="container">Container</option></select></label><label>Category<select id="iconPickerCategory"><option value="">All categories</option></select></label></div><p id="pickerResultsStatus" role="status"></p><div id="pickerResults" class="picker-results"></div><div class="picker-footer"><button id="restorePlacement" type="button">Restore original</button><div><button id="pickerPrev" aria-label="Previous icons" type="button">←</button><span id="pickerPage"></span><button id="pickerNext" aria-label="Next icons" type="button">→</button></div></div>`;
  const $=id=>dialog.querySelector('#'+id);
  for(const category of [...new Set(icons.map(i=>i.category).filter(Boolean))].sort()){const o=document.createElement('option');o.value=category;o.textContent=category;$('iconPickerCategory').append(o);}
  const count=()=>{const n=Object.keys(replacements).length;bar.querySelector('#editCount').textContent=n?`${n} changed`:'';bar.querySelector('button').disabled=!n;};
  function save(){try{localStorage.setItem(storageKey,JSON.stringify(replacements));return true;}catch{return false;}}
  function announce(){count();if(parent!==window)parent.postMessage({type:'preview-icons-used',example,ids:[...new Set([...document.querySelectorAll('.icon-swap')].map(el=>el.dataset.icon))]},location.origin);}
  function apply(el,id){const i=byId.get(id);if(!i){el.dataset.icon='';el.classList.add('empty-placement');el.setAttribute('aria-label','Choose an approved icon');el.title='Choose an approved icon';el.querySelector('.p-icon').style.removeProperty('--icon');return;}el.classList.remove('empty-placement');el.dataset.icon=id;el.setAttribute('aria-label','Change '+label(i)+' icon');el.title='Change '+label(i);el.querySelector('.p-icon').style.setProperty('--icon',`url("${encodeURI(i.preview_url).replaceAll('"','%22')}")`);}
  function render(){
    const terms=$('iconPickerSearch').value.trim().toLowerCase().split(/\s+/).filter(Boolean),family=$('iconPickerFamily').value,category=$('iconPickerCategory').value;
    const rows=icons.filter(i=>(!family||i.family===family)&&(!category||i.category===category)&&terms.every(t=>[i.name,i.icon_id,i.category].join(' ').replaceAll('-',' ').toLowerCase().includes(t.replaceAll('-',' '))));
    const pages=Math.max(1,Math.ceil(rows.length/60));page=Math.max(0,Math.min(page,pages-1));
    $('pickerResultsStatus').textContent=rows.length?`${rows.length.toLocaleString()} approved icons · select one to replace this placement`:'No matching icons. Try another word or clear the filters.';
    $('pickerResults').replaceChildren();
    for(const i of rows.slice(page*60,(page+1)*60)){
      const b=document.createElement('button');b.type='button';b.className='picker-choice';b.setAttribute('aria-label','Use '+label(i));b.setAttribute('aria-pressed',String(selected?.dataset.icon===i.icon_id));
      const img=document.createElement('img');img.src=i.preview_url;img.alt='';img.loading='lazy';const name=document.createElement('span');name.textContent=label(i);b.append(img,name);b.onclick=()=>choose(i.icon_id);$('pickerResults').append(b);
    }
    $('pickerPage').textContent=`${page+1} / ${pages}`;$('pickerPrev').disabled=page===0;$('pickerNext').disabled=page===pages-1;
    $('restorePlacement').disabled=!selected||!replacements[selected.dataset.slot]||!byId.has(selected.dataset.original);
  }
  async function refreshApproved(){
    try{icons=await loadApprovedPreviewIcons();}catch(error){icons=[];byId=new Map();document.querySelectorAll('.icon-swap').forEach(el=>apply(el,''));announce();throw error;}
    byId=new Map(icons.map(i=>[i.icon_id,i]));
    replacements=approvedPreviewReplacements(replacements,icons);
    document.querySelectorAll('.icon-swap').forEach(el=>apply(el,replacements[el.dataset.slot]||el.dataset.original));
    $('iconPickerSearch').placeholder=`Search ${icons.length.toLocaleString()} approved icons…`;announce();
  }
  async function choose(id){
    if(!selected||busy)return;busy=true;
    $('pickerResultsStatus').textContent='Checking approval…';
    try{
      await refreshApproved();
      if(!selected)return;
      if(!byId.has(id)){render();$('pickerResultsStatus').textContent='That icon is no longer approved. Choose another icon.';return;}
      if(id===selected.dataset.original)delete replacements[selected.dataset.slot];else replacements[selected.dataset.slot]=id;
      apply(selected,id);const saved=save();announce();dialog.close();if(!saved)bar.querySelector('#editCount').textContent='Changed for this visit · browser storage unavailable';
    }catch{if(dialog.open){$('pickerResults').replaceChildren();$('pickerResultsStatus').textContent='Could not verify approval. Close the picker and try again.';}}
    finally{busy=false;}
  }
  async function open(el){selected=el;returnFocus=el;document.querySelectorAll('.icon-swap.is-selected').forEach(x=>x.classList.remove('is-selected'));el.classList.add('is-selected');$('pickerCurrent').textContent='Replacing '+label(byId.get(el.dataset.icon))+'. Only this placement will change.';$('iconPickerSearch').value='';$('iconPickerFamily').value='solo';$('iconPickerCategory').value='';page=0;$('pickerResults').replaceChildren();$('restorePlacement').disabled=true;dialog.showModal();$('iconPickerSearch').focus();busy=true;$('pickerResultsStatus').textContent='Loading approved icons…';try{await refreshApproved();if(dialog.open)render();}catch{if(dialog.open)$('pickerResultsStatus').textContent='Could not verify approval. Close the picker and try again.';}finally{busy=false;}}
  for(const id of ['iconPickerSearch','iconPickerFamily','iconPickerCategory'])$(id).addEventListener(id==='iconPickerSearch'?'input':'change',()=>{page=0;render();});
  $('pickerPrev').onclick=()=>{page--;render();$('pickerResults').scrollTop=0;};$('pickerNext').onclick=()=>{page++;render();$('pickerResults').scrollTop=0;};
  $('closeIconPicker').onclick=()=>dialog.close();$('restorePlacement').onclick=()=>choose(selected.dataset.original);
  dialog.addEventListener('close',()=>{selected?.classList.remove('is-selected');if(returnFocus?.isConnected)returnFocus.focus({preventScroll:true});selected=null;});
  bar.querySelector('button').onclick=async()=>{if(busy)return;busy=true;replacements={};save();try{await refreshApproved();}catch{bar.querySelector('#editCount').textContent='Could not verify approval. Reload to try again.';}finally{busy=false;}};
  function mount(){
    document.body.prepend(bar);document.body.append(dialog);announce();
    document.addEventListener('click',e=>{const el=e.target.closest('.icon-swap');if(!el||busy)return;e.preventDefault();e.stopImmediatePropagation();open(el);},true);
    document.addEventListener('keydown',e=>{const el=e.target.closest('.icon-swap');if(!el||!['Enter',' '].includes(e.key))return;e.preventDefault();e.stopImmediatePropagation();open(el);},true);
  }
  return {icon,mount,announce};
};

/* Editing subtabs and persistent source selection. */
(() => {
  'use strict';
  const $=id=>document.getElementById(id), tabs=['browser','manual','pick'];
  let icon=null, data=null, file=null, token=0, busy=false;
  const labels={use_org:'Original',use_upload:'Manual Edit',use_edited:'Browser Edit'};
  const current=()=>data?.choice?.source_mode || data?.source_mode || icon?.artwork_source || 'use_org';
  const preview=variant=>'../api/icon-artwork/svg?icon='+encodeURIComponent(icon.key)+'&variant='+variant+'&v='+(data?.choice?.revision || 0)+'-'+(data?.edit_revision || 0);
  function tab(name,focus=false){
    if(name==='browser' && icon?.uploaded_icon)name='manual';
    for(const key of tabs){$(key+'EditPanel').hidden=key!==name;$(key+'EditTab').setAttribute('aria-selected',String(key===name));$(key+'EditTab').tabIndex=key===name?0:-1;}
    if(focus)$(name+'EditTab').focus();
    if(name==='browser')window.StrokeEditor?.refresh?.();
    if(name==='pick')controls();
  }
  function controls(){
    const blocked=busy || !data, uploaded=data?.choice?.uploaded;
    $('artworkMode').disabled=blocked;$('artworkFile').disabled=blocked;
    $('artworkApply').disabled=blocked;$('artworkUpload').disabled=blocked || !file;
    $('artworkReload').disabled=busy;
    $('artworkApply').textContent=busy?'Saving…':'Use and approve selected version';
    $('artworkUpload').textContent=busy?'Saving…':'Save manual edit';
    $('artworkUploadName').textContent=file?file.name:uploaded?'Saved: '+uploaded.name:'SVG only · up to 1 MB · keep the original canvas size.';
    $('artworkDownload').href=data?.preview_url || icon?.preview_url || '';
    $('artworkDownload').download=(icon?.icon_id || 'icon')+'.svg';
    $('artworkCurrent').textContent='Currently displayed: '+labels[current()];
    $('manualEditPreview').hidden=!uploaded;$('manualEditEmpty').hidden=!!uploaded;
    if(uploaded)$('manualEditPreview').src=preview('use_upload');
    for(const mode of Object.keys(labels)){
      const available=!!data && (mode==='use_org' || (mode==='use_upload'?!!uploaded:!!data.edit_revision));
      const input=$('pick_'+mode),image=$('pickPreview_'+mode),card=$('pickCard_'+mode);
      input.disabled=blocked || !available;input.checked=$('artworkMode').value===mode;
      image.hidden=!available;if(available)image.src=preview(mode==='use_edited'?'browser_edit':mode);
      const newer=mode==='use_upload'?uploaded?.svg_sha256!==(data?.choice?.selected_upload || uploaded)?.svg_sha256:mode==='use_edited' && data?.choice?.edited?.revision!==data?.edit_revision;
      const displayed=current()===mode && !newer;card.dataset.current=String(displayed);
      $('pickNote_'+mode).textContent=!available?(mode==='use_upload'?'Upload and save an SVG in Manual Edit.':'Save your changes in Browser Edit.'):
        displayed?'Currently displayed':mode==='use_org'?(icon?.uploaded_icon?'Uploaded original':'Python-generated original'):mode==='use_edited'?'Latest saved browser edit':'Latest saved manual edit';
      if(mode==='use_edited' && window.StrokeEditor?.hasUnsavedChanges())$('pickNote_'+mode).textContent='Unsaved changes in Browser Edit. Save them before picking this version.';
    }
  }
  async function load(){
    if(!icon)return;
    const request=++token;busy=true;controls();
    try{
      const response=await fetch('../api/icon-artwork?icon='+encodeURIComponent(icon.key));
      const result=await response.json();if(!response.ok)throw Error(result.error || 'Could not load artwork choices.');
      if(request!==token)return;
      data=result;$('artworkMode').value=current();
      $('artworkStatus').textContent=result.choice?'Saved by '+result.choice.updated_by+' · '+new Date(result.choice.updated_at).toLocaleString():'';
    }catch(error){if(request===token)$('artworkStatus').textContent=error.message;}
    finally{if(request===token){busy=false;controls();}}
  }
  async function save(uploadOnly=false){
    if(!icon || !data || busy)return;
    const mode=uploadOnly?current():$('artworkMode').value,request=token,status=$(uploadOnly?'manualEditStatus':'artworkStatus');
    if(uploadOnly && !file){status.textContent='Choose an SVG file first.';return;}
    if(!uploadOnly && mode==='use_edited' && window.StrokeEditor?.hasUnsavedChanges()){status.textContent='Save your changes in Browser Edit before picking this version.';return;}
    if(!uploadOnly && mode==='use_upload' && !data.choice?.uploaded){status.textContent='Upload and save an SVG in Manual Edit first.';return;}
    busy=true;controls();status.textContent=uploadOnly?'Saving manual edit…':'Saving display choice…';
    try{
      if(!uploadOnly && window.flushIconFeedback && !await window.flushIconFeedback())throw Error('Finish saving feedback before picking this version.');
      if(request!==token)return;
      const body={icon:icon.key,svg_sha256:data.svg_sha256,revision:data.choice?.revision || 0,source_mode:mode,edit_revision:data.edit_revision};
      if(uploadOnly){body.action='upload';body.svg=await file.text();body.filename=file.name;}
      if(request!==token)return;
      const response=await fetch('../api/icon-artwork',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
      const result=await response.json();if(!response.ok)throw Error(result.error || 'Could not save artwork.');
      // A completed pick belongs to the gallery even if another inspector is now open.
      if(!uploadOnly)window.dispatchEvent(new CustomEvent('icon-artwork-saved',{detail:result.record}));
      if(request!==token)return;
      data=result;
      if(uploadOnly){file=null;$('artworkFile').value='';$('artworkMode').value='use_upload';}
      else $('artworkMode').value=current();
      status.textContent=uploadOnly?'Manual edit saved. Open Pick to display it.':'Approved and displaying: '+labels[current()]+'.';
    }catch(error){if(request===token)status.textContent=error.message;}
    finally{if(request===token){busy=false;controls();}}
  }
  function open(next){icon=next;data=null;file=null;token++;busy=false;$('artworkFile').value='';$('manualEditStatus').textContent='';$('artworkStatus').textContent='';$('artworkMode').value=next.artwork_source || 'use_org';$('browserEditTab').disabled=!!next.uploaded_icon;tab(next.uploaded_icon?'manual':'browser');controls();load();}
  document.addEventListener('DOMContentLoaded',()=>{
    for(const [i,name] of tabs.entries()){
      $(name+'EditTab').onclick=()=>tab(name);
      $(name+'EditTab').onkeydown=event=>{const index=event.key==='ArrowRight'?(i+1)%3:event.key==='ArrowLeft'?(i+2)%3:event.key==='Home'?0:event.key==='End'?2:-1;if(index>=0){event.preventDefault();tab(tabs[index],true);}};
    }
    for(const mode of Object.keys(labels))$('pick_'+mode).onchange=()=>{$('artworkMode').value=mode;controls();return save();};
    $('artworkApply').onclick=()=>save();$('artworkUpload').onclick=()=>save(true);$('artworkReload').onclick=load;
    $('artworkFile').onchange=()=>{
      const selected=$('artworkFile').files?.[0];if(!selected)return;
      if(!selected.name.toLowerCase().endsWith('.svg') || selected.size>1024*1024){$('manualEditStatus').textContent='Choose an SVG file up to 1 MB.';$('artworkFile').value='';file=null;controls();return;}
      file=selected;controls();$('manualEditStatus').textContent='Ready to save this manual edit.';
    };
  });
  window.IconArtwork={open,editSaved:(key,revision)=>{if(icon?.key===key && data){data.edit_revision=revision;controls();}}};
})();

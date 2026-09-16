/* Persistent source selection: Python original, uploaded SVG, or saved editor graph. */
(() => {
  'use strict';
  const $=id=>document.getElementById(id);
  let icon=null, data=null, file=null, token=0, busy=false;
  const labels={use_org:'Original · Python generated',use_upload:'Uploaded · manually edited',use_edited:'Gallery edited'};
  function controls(){
    const blocked=busy || !data;
    $('artworkMode').disabled=blocked;
    $('artworkFile').disabled=blocked;
    $('artworkApply').disabled=blocked;
    $('artworkReload').disabled=busy;
    $('artworkApply').textContent=busy?'Saving…':'Use this version';
    const uploaded=data?.choice?.uploaded;
    $('artworkUploadName').textContent=file?file.name:uploaded?'Saved upload: '+uploaded.name:'SVG only · up to 1 MB · keep the original canvas size.';
    $('artworkPreview').src=data?.preview_url || icon?.preview_url || '';
    $('artworkDownload').href=data?.preview_url || icon?.preview_url || '';
    $('artworkDownload').download=(icon?.icon_id || 'icon')+'.svg';
    $('artworkCurrent').textContent='Currently using: '+labels[data?.choice?.source_mode || icon?.artwork_source || 'use_org'];
  }
  async function load(){
    if(!icon)return;
    const request=++token;busy=true;controls();
    try{
      const response=await fetch('../api/icon-artwork?icon='+encodeURIComponent(icon.key));
      const result=await response.json();if(!response.ok)throw Error(result.error || 'Could not load artwork choices.');
      if(request!==token)return;
      data=result;file=null;$('artworkFile').value='';$('artworkMode').value=result.choice?.source_mode || 'use_org';
      $('artworkStatus').textContent=result.choice?'Saved by '+result.choice.updated_by+' · '+new Date(result.choice.updated_at).toLocaleString():'';
    }catch(error){if(request===token)$('artworkStatus').textContent=error.message;}
    finally{if(request===token){busy=false;controls();}}
  }
  async function apply(){
    if(!icon || !data || busy)return;
    const mode=$('artworkMode').value, request=token;
    if(mode==='use_edited' && window.StrokeEditor?.hasUnsavedChanges()){$('artworkStatus').textContent='Save your gallery edits below before using this version.';return;}
    if(mode==='use_upload' && !file && !data.choice?.uploaded){$('artworkStatus').textContent='Choose an SVG file first.';return;}
    busy=true;controls();$('artworkStatus').textContent='Saving artwork and source choice…';
    try{
      const body={icon:icon.key,svg_sha256:data.svg_sha256,revision:data.choice?.revision || 0,source_mode:mode,edit_revision:data.edit_revision};
      if(file){body.svg=await file.text();body.filename=file.name;}
      if(request!==token)return;
      const response=await fetch('../api/icon-artwork',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
      const result=await response.json();if(!response.ok)throw Error(result.error || 'Could not save artwork.');
      if(request!==token)return;
      data=result;file=null;$('artworkFile').value='';$('artworkMode').value=result.choice.source_mode;
      $('artworkStatus').textContent='Saved. The gallery and Python builds will use '+labels[result.choice.source_mode]+'.';
      window.dispatchEvent(new CustomEvent('icon-artwork-saved',{detail:result.record}));
    }catch(error){if(request===token)$('artworkStatus').textContent=error.message;}
    finally{if(request===token){busy=false;controls();}}
  }
  function open(next){icon=next;data=null;file=null;token++;busy=false;controls();load();}
  document.addEventListener('DOMContentLoaded',()=>{
    $('artworkApply').onclick=apply;$('artworkReload').onclick=load;
    $('artworkFile').onchange=()=>{
      const selected=$('artworkFile').files?.[0];
      if(!selected)return;
      if(!selected.name.toLowerCase().endsWith('.svg') || selected.size>1024*1024){$('artworkStatus').textContent='Choose an SVG file up to 1 MB.';$('artworkFile').value='';file=null;controls();return;}
      file=selected;$('artworkMode').value='use_upload';controls();
      $('artworkStatus').textContent='Upload selected. Click Use this version to save it.';
    };
  });
  window.IconArtwork={open,editSaved:(key,revision)=>{if(icon?.key===key && data)data.edit_revision=revision;}};
})();

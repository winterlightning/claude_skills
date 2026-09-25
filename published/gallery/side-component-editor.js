/* Shared geometry editor hosted directly by the side-pairs page. */
(()=>{
  const $=id=>document.getElementById(id);
  let opening=false;
  async function api(url,body){
    const response=await fetch(url,body===undefined?{cache:'no-store'}:{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    const data=await response.json();if(!response.ok)throw Error(data.error||'Could not load the editor.');return data;
  }
  window.SideComponentEditor={async open(drawing,label){
    if(opening)return;opening=true;
    try{
      const data=await api('/api/icon-artwork?icon='+encodeURIComponent(drawing.key));
      if(!data.record.primitives?.length)throw Error('Editable geometry is unavailable for this drawing. Republish it first.');
      $('editorTitle').textContent=label;
      window.StrokeEditor.open(data.record);window.IconArtwork.open(data.record);
      $('detail').showModal();$('editingTab').click();
    }finally{opening=false;}
  }};
  window.beforeIconArtworkApprove=async icon=>{
    const reviews=await api('/api/reviews');
    if(reviews[icon.key]==='rejected')await api('/api/reject-combination/restore',{icon:icon.key,svg_sha256:icon.svg_sha256});
  };
  $('closeEditor').onclick=()=>$('detail').close();
  window.addEventListener('icon-artwork-saved',()=>{
    window.dispatchEvent(new CustomEvent('side-component-approved'));
  });
})();

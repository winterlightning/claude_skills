function approvedIcons(catalog, reviews) {
  return catalog.icons.filter(icon => reviews[icon.key] === 'approve');
}
(async()=>{
  const status=document.getElementById('approvedStatus');
  const grid=document.getElementById('approvedGrid');
  try {
    const responses=await Promise.all([fetch('icons.json',{cache:'no-store'}),fetch('/api/reviews',{cache:'no-store'})]);
    if(responses.some(response=>!response.ok))throw Error('Could not load the approved collection. Please reload to try again.');
    const [catalog,reviews]=await Promise.all(responses.map(response=>response.json()));
    const icons=approvedIcons(catalog,reviews);
    status.textContent=icons.length ? icons.length.toLocaleString()+' approved icon'+(icons.length===1?'':'s') : 'No approved icons yet. Approved icons will appear here after review.';
    const fragment=document.createDocumentFragment();
    for(const icon of icons){
      const card=document.createElement('article');card.className='approved-card';
      const preview=document.createElement('div');preview.className='approved-preview';
      const img=document.createElement('img');img.src=icon.preview_url;img.alt=icon.name;img.loading='lazy';img.width=64;img.height=64;preview.append(img);
      const name=document.createElement('h2');name.textContent=icon.name;
      const download=document.createElement('a');download.className='site-button';download.href=icon.preview_url;download.download=icon.icon_id+'.svg';download.textContent='Download SVG';download.setAttribute('aria-label','Download '+icon.name+' SVG');
      card.append(preview,name,download);fragment.append(card);
    }
    grid.replaceChildren(fragment);
  }catch(error){grid.replaceChildren();status.textContent=error.message||'Could not load the approved collection. Please reload to try again.';}
})();

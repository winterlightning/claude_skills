/* Approval is read from the live review API, never baked into a build or saved edit. */
window.approvedPreviewIcons = function(catalog, reviews) {
  if(!Array.isArray(catalog?.icons)||!reviews||typeof reviews!=='object'||Array.isArray(reviews))throw Error('Approval status is unavailable.');
  return catalog.icons.filter(icon=>reviews[icon.family+'/'+icon.icon_id]==='approve');
};
window.approvedPreviewReplacements = function(saved, icons) {
  if(!saved||typeof saved!=='object'||Array.isArray(saved))return {};
  const allowed=new Set(icons.map(i=>i.icon_id));
  return Object.fromEntries(Object.entries(saved).filter(([,id])=>typeof id==='string'&&allowed.has(id)));
};
window.loadApprovedPreviewIcons = async function() {
  const responses=await Promise.all([fetch('preview-icons.json',{cache:'no-store'}),fetch('/api/reviews',{cache:'no-store'})]);
  if(responses.some(r=>!r.ok))throw Error('Could not verify approved icons. Reload to try again.');
  const [catalog,reviews]=await Promise.all(responses.map(r=>r.json()));
  const approved=window.approvedPreviewIcons(catalog,reviews);
  // Side- and container-combination icons come from the combination experiments,
  // not the review pipeline, so they are appended without an approval gate.
  let extra=[];
  for(const file of ['preview-combination-icons.json','preview-container-combination-icons.json']){
    try{
      const combo=await fetch(file,{cache:'no-store'});
      if(combo.ok){const data=await combo.json();if(Array.isArray(data?.icons))extra=extra.concat(data.icons);}
      else console.warn(file+' is missing ('+combo.status+'); its combined icons are not offered.');
    }catch(error){console.warn(file+' could not be loaded; its combined icons are not offered.',error);}
  }
  return approved.concat(extra);
};

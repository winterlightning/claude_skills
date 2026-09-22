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
  // Side-combination icons come from the combination experiment, not the review
  // pipeline, so they are appended without an approval gate.
  try{
    const combo=await fetch('preview-combination-icons.json',{cache:'no-store'});
    if(combo.ok){const data=await combo.json();if(Array.isArray(data?.icons))return approved.concat(data.icons);}
  }catch{}
  return approved;
};

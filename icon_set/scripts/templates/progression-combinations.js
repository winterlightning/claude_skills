/* Combination views share the progression page's navigation and URL state. */
let combinationCatalog=null, combinationLoading=false, combinationError='';
const combinationLabels={missing:'Components needed',partial:'One component generated',ready:'Both components generated',generated:'Generated'};
function combinationState(row){
  const refs=combinationCatalog.references;
  if(refs[row.id].generated.length || row.generated?.length)return 'generated';
  const count=Number(!!refs[row.main_id].generated.length)+Number(!!refs[row.sub_id].generated.length);
  return count===2?'ready':count===1?'partial':'missing';
}
async function renderCombinations(){
  const host=$('combinations');
  if(!combinationCatalog){
    host.replaceChildren(node('p','muted',combinationError||'Loading combinations…'));
    if(combinationError){const retry=node('button','','Retry');retry.onclick=()=>{combinationError='';renderCombinations();};host.append(retry);return;}
    if(combinationLoading)return;
    combinationLoading=true;
    try{const response=await fetch('combinations.json',{cache:'no-store'});if(!response.ok)throw Error('Could not load the combination catalog.');combinationCatalog=await response.json();}
    catch(error){combinationError=error.message;}
    finally{combinationLoading=false;}
    if(['container','side'].includes(state.view))renderCombinations();return;
  }
  const all=combinationCatalog.rows.filter(r=>r.kind===state.view), counts={missing:0,partial:0,ready:0,generated:0};
  all.forEach(r=>counts[combinationState(r)]++);
  host.replaceChildren();
  host.append(node('h2','',state.view==='container'?'Container combination':'Side combination'),node('p','muted','Generate the main and sub separately, then combine them to remake the reference. Linked artwork is shown below each component; check its size and family before combining.'));
  const summary=node('div','combination-summary');
  for(const [label,value] of [['Total',all.length],...Object.entries(counts).map(([k,v])=>[combinationLabels[k],v])]){
    const item=node('div');item.append(node('strong','',value.toLocaleString()),node('span','',label));summary.append(item);
  }
  host.append(summary);
  const toolbar=node('div','toolbar'), search=node('input');search.type='search';search.placeholder='Search concept or component ID';search.setAttribute('aria-label','Search combinations');search.value=state.q;
  const filter=node('select');filter.setAttribute('aria-label','Combination progress');filter.append(new Option('All progress','todo'),...Object.entries(combinationLabels).map(([k,v])=>new Option(v,k)));filter.value=state.status;
  filter.onchange=()=>{state.status=filter.value;page=1;writeURL();renderCombinations();};
  let timer;search.oninput=()=>{clearTimeout(timer);timer=setTimeout(()=>{const cursor=search.selectionStart;state.q=search.value;page=1;writeURL();renderCombinations();const next=host.querySelector('input');next.focus();if(cursor!==null)next.setSelectionRange(cursor,cursor);},180);};
  toolbar.append(search,filter);host.append(toolbar);
  const q=state.q.trim().toLowerCase(),refs=combinationCatalog.references;
  const rows=all.filter(r=>(!combinationLabels[state.status]||combinationState(r)===state.status)&&(!q||[r.concept,r.id,r.main_id,r.sub_id,refs[r.main_id].concept,refs[r.sub_id].concept].join(' ').toLowerCase().includes(q)));
  const pages=Math.max(1,Math.ceil(rows.length/30));page=Math.min(page,pages);writeURL();
  function pager(){const bar=node('div','pager'),prev=node('button','','← Previous'),next=node('button','','Next →');prev.disabled=page<=1;next.disabled=page>=pages;prev.onclick=()=>{page--;renderCombinations();host.scrollIntoView();};next.onclick=()=>{page++;renderCombinations();host.scrollIntoView();};bar.append(prev,node('span','muted',`${rows.length.toLocaleString()} matches · Page ${page} of ${pages}`),next);return bar;}
  host.append(pager());
  const list=node('div','combination-list');
  function imageLink(url,label){const link=node('a');link.href=url;link.target='_blank';link.rel='noopener';link.title=label;const img=node('img');img.src=url;img.alt=label;img.loading='lazy';img.onerror=()=>link.replaceWith(node('span','muted','Artwork unavailable'));link.append(img);return link;}
  function artwork(title,ref,generatedOnly=false,extra=[]){
    const panel=node('section','combination-artwork');panel.append(node('h4','',title));
    if(!generatedOnly){panel.append(ref.reference_url?imageLink(ref.reference_url,ref.concept+' — original'):node('div','combination-empty','Reference missing'));panel.append(node('p','component-name',ref.concept));}
    const generated=[...ref.generated,...extra];
    if(generated.length){const previews=node('div','combination-generated');for(const g of generated){const figure=node('figure');figure.append(imageLink(g.preview_url,g.icon_id),node('figcaption','',g.label||g.icon_id));previews.append(figure);}panel.append(node('p','combination-label','Generated'),previews);}
    else panel.append(node('div','combination-empty',generatedOnly?'Not combined yet':'Not generated yet'));
    return panel;
  }
  for(const row of rows.slice((page-1)*30,page*30)){
    const card=node('article','combination-card'),head=node('div','combination-heading');head.append(node('h3','',row.concept),node('span','chip',combinationLabels[combinationState(row)]));card.append(head);
    const grid=node('div','combination-artworks');
    const original=artwork('Reference combination',{...refs[row.id],concept:row.concept,generated:[]});original.lastChild.remove();
    const subRef={...refs[row.sub_id],generated:refs[row.sub_id].generated.map(g=>{const reuse=(row.sub_exports||[]).find(e=>e.icon===g.icon_id);return reuse?{...g,preview_url:reuse.export_url,label:g.icon_id+' · 32px reuse export'}:g;})};
    grid.append(original,artwork('Main',refs[row.main_id]),artwork('Sub',subRef),artwork('Generated combination',refs[row.id],true,row.generated||[]));card.append(grid);
    for(const mapping of row.remappings||[])card.append(node('p','muted',`${mapping.role==='main'?'Main':'Sub'} remapped to an existing source: ${mapping.reason}.`));
    const details=node('details','combination-identities');details.append(node('summary','','Source IDs'));for(const [name,id] of [['Combination',row.id],['Main',row.main_id],['Sub',row.sub_id]])details.append(node('p','',name+': '+id));card.append(details);list.append(card);
  }
  if(!rows.length)list.append(node('p','muted','No combinations match these filters.'));
  host.append(list,pager());
}

/* Combination views share the progression page's navigation and URL state. */
let combinationCatalog=null, combinationLoading=false, combinationError='';
let containerResults=null, containerResultError='', containerResultsLoading=false, combineRunning=false, combineProgress='';
const containerPreviews=new Map(), expandedContainers=new Set();
async function loadContainerResults(){
  if(containerResultsLoading)return;
  containerResultsLoading=true;
  try{
    const response=await fetch('/api/combinations/container/results',{cache:'no-store'});
    const data=await response.json();if(!response.ok)throw Error(data.error||'Could not load combination results.');
    containerResults=data;containerPreviews.clear();for(const pair of data.pairs)containerPreviews.set(pair.pair_id,pair);
    containerResultError='';
  }catch(error){containerResultError=error.message;}
  finally{containerResultsLoading=false;}
  if(state.view==='container')renderCombinations();
}
async function combineAllPairs(){
  if(combineRunning)return;
  combineRunning=true;combineProgress='Preparing all container pairs…';renderCombinations();
  try{
    const response=await fetch('/api/combinations/container/results',{cache:'no-store'});
    const start=await response.json();if(!response.ok)throw Error(start.error||'Could not prepare pairs.');
    containerResults=start;containerPreviews.clear();let offset=0;
    do{
      const response=await fetch('/api/combinations/container/combine',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({limit:100,offset,snapshot:start.snapshot})});
      const batch=await response.json();if(!response.ok)throw Error(batch.error||'Could not combine pairs.');
      for(const pair of batch.pairs)containerPreviews.set(pair.pair_id,pair);
      const done=Math.min(batch.offset+batch.limit,batch.total);
      combineProgress=`Processed ${done.toLocaleString()} of ${batch.total.toLocaleString()} pairs`;
      offset=batch.next_offset;if(state.view==='container')renderCombinations();
    }while(offset!==null);
    combineProgress='All pairs processed. Missing components and fit problems are listed below.';
  }catch(error){combineProgress=error.message+' Completed batches are saved; you can retry.';}
  finally{combineRunning=false;await loadContainerResults();}
}
const combinationLabels={missing:'Components needed',partial:'One component generated',ready:'Both components generated',generated:'Generated'};
function combinationMain(row){
  const ref=combinationCatalog.references[row.main_id];
  if(row.kind!=='container')return ref;
  // A solo remake does not fulfill a container-main requirement. Keep this
  // fallback for older catalogs, while honoring an explicit empty build result.
  const generated=(row.main_generated??ref.generated).filter(g=>g.key?.startsWith('container/'));
  return {...ref,generated};
}
function containerGroups(rows){
  const groups=new Map();
  for(const row of rows){
    const main=combinationMain(row), generated=main.generated[0];
    const iconId=row.main_icon_id||generated?.icon_id;
    const key=iconId?'container/'+iconId:'reference/'+row.main_id;
    if(!groups.has(key))groups.set(key,{key,iconId,main,title:iconId?iconId.replace(/[-_]/g,' '):main.concept,rows:[]});
    groups.get(key).rows.push(row);
  }
  return [...groups.values()].sort((a,b)=>a.title.localeCompare(b.title)||a.key.localeCompare(b.key));
}
function combinationState(row){
  if(row.kind==='container'&&containerResults?.selections?.[row.id]){const selected=containerResults.selections[row.id];const n=Number(!!selected.main_key)+Number(!!selected.symbol_key);return n===2?'ready':n===1?'partial':'missing';}
  const refs=combinationCatalog.references;
  if((row.component_selection!=='explicit'&&refs[row.id].generated.length) || row.generated?.length)return 'generated';
  const count=Number(!!combinationMain(row).generated.length)+Number(!!(row.sub_generated??refs[row.sub_id].generated).length);
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
  if(state.view==='container'&&!containerResults&&!containerResultError&&!containerResultsLoading)loadContainerResults();
  const all=combinationCatalog.rows.filter(r=>r.kind===state.view), counts={missing:0,partial:0,ready:0,generated:0};
  all.forEach(r=>counts[combinationState(r)]++);
  host.replaceChildren();
  host.append(node('h2','',state.view==='container'?'Container combination':'Side combination'),node('p','muted',state.view==='container'?'Combine each container with its latest standard 32×32 symbol. Expand a container to compare the original and combined preview.':'Work on each pair as Original → Main → Sub → Combined: one 48-unit main and one 32×32 sub. Group by main or sub to see where an icon is reused. Finished outputs live on Experiment › Side combination.'));
  const summary=node('div','combination-summary');
  // The side grid adds its own plain status counts (Ready, Fix sub, Waiting, Needs main, Needs sub).
  const summaryItems=state.view==='side'?[['Side pairs',all.length]]:[['Total',all.length],...Object.entries(counts).map(([k,v])=>[combinationLabels[k],v])];
  for(const [label,value] of summaryItems){
    const item=node('div');item.append(node('strong','',value.toLocaleString()),node('span','',label));summary.append(item);
  }
  if(state.view!=='container'){
    host.append(summary);
    if(state.view==='side'){
      const needed=node('p','muted');needed.append('Pair badges: Waiting = main and sub are drawn but not combined yet. Lists: ');const link=node('a','','Main icons →'),subs=node('a','','Sub icons →');link.href='side-mains.html';subs.href='side-subs.html';needed.append(link,' · ',subs);host.append(needed);
    }
  }
  if(state.view==='side'){renderSideGrid(host,all,summary);return;}
  else{
    const area=node('div','container-combine-controls');
    if(containerResults){
      const stats=node('div','combination-summary');
      for(const [label,value] of [['Container pairs',containerResults.total],['Container icons',containerResults.containers.total],['Containers needed',containerResults.containers.missing],['Symbol requirements · 32×32',containerResults.symbols.total],['Symbols needed',containerResults.symbols.missing]]){
        const item=node('div');item.append(node('strong','',value.toLocaleString()),node('span','',label));stats.append(item);
      }
      area.append(stats,node('p','muted',`${containerResults.containers.ready} containers and ${containerResults.symbols.ready} symbol requirements have eligible artwork. Symbols are counted once per source requirement; equivalent sources may share a drawing.`));
      const needed=node('p');const link=node('a','','Browse the symbols still needed →');link.href='symbols-needed.html';needed.append(link);area.append(needed);
    }
    const actions=node('div','toolbar'),button=node('button','','Combine all pairs');button.disabled=combineRunning;button.onclick=combineAllPairs;
    actions.append(button,node('span','muted','Latest published containers + standard 32×32 symbols. Applies to all pairs, including other pages.'));
    area.append(actions);
    const progress=node('p','muted',combineProgress||containerResultError||(containerResults?`${containerResults.processed.toLocaleString()} of ${containerResults.total.toLocaleString()} pairs processed. Saved previews appear when you expand a container.`:'Loading component counts…'));progress.setAttribute('role','status');area.append(progress);
    if(containerResults&&!combineRunning){const c=containerResults.counts;area.append(node('p','muted',`${c.pass||0} fit checks passed · ${c.fail||0} need fit changes · ${c.review||0} need review · ${c.missing||0} missing components · ${c.blocked||0} blocked`));}
    host.append(area);
  }
  const toolbar=node('div','toolbar'), search=node('input');search.type='search';search.placeholder='Search concept or component ID';search.setAttribute('aria-label','Search combinations');search.value=state.q;
  const filter=node('select');filter.setAttribute('aria-label','Combination progress');filter.append(new Option('All progress','todo'),...Object.entries(combinationLabels).map(([k,v])=>new Option(v,k)));filter.value=state.status;
  filter.onchange=()=>{state.status=filter.value;page=1;writeURL();renderCombinations();};
  let timer;search.oninput=()=>{clearTimeout(timer);timer=setTimeout(()=>{const cursor=search.selectionStart;state.q=search.value;page=1;writeURL();renderCombinations();const next=host.querySelector('input');next.focus();if(cursor!==null)next.setSelectionRange(cursor,cursor);},180);};
  toolbar.append(search,filter);host.append(toolbar);
  const q=state.q.trim().toLowerCase(),refs=combinationCatalog.references;
  const rows=all.filter(r=>(!combinationLabels[state.status]||combinationState(r)===state.status)&&(!q||[r.concept,r.id,r.main_id,r.sub_id,refs[r.main_id].concept,refs[r.sub_id].concept,r.main_icon_id,r.main_icon_id?.replace(/[-_]/g,' ')].join(' ').toLowerCase().includes(q)));
  const grouped=state.view==='container', groups=grouped?containerGroups(rows):[], pageSize=grouped?12:30;
  const pages=Math.max(1,Math.ceil((grouped?groups.length:rows.length)/pageSize));page=Math.min(page,pages);writeURL();
  function pager(){const bar=node('div','pager'),prev=node('button','','← Previous'),next=node('button','','Next →');prev.disabled=page<=1;next.disabled=page>=pages;prev.onclick=()=>{page--;renderCombinations();host.scrollIntoView();};next.onclick=()=>{page++;renderCombinations();host.scrollIntoView();};bar.append(prev,node('span','muted',`${rows.length.toLocaleString()} matches${grouped?' · '+groups.length+' main container'+(groups.length===1?'':'s'):''} · Page ${page} of ${pages}`),next);return bar;}
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
  function combinationCard(row){
    const card=node('article','combination-card'),head=node('div','combination-heading');head.append(node('h3','',row.concept),node('span','chip',combinationLabels[combinationState(row)]));card.append(head);
    const grid=node('div','combination-artworks');
    const original=artwork('Reference combination',{...refs[row.id],concept:row.concept,generated:[]});original.lastChild.remove();
    const subRef={...refs[row.sub_id],generated:(row.sub_generated||refs[row.sub_id].generated).map(g=>{const reuse=(row.sub_exports||[]).find(e=>e.icon===g.icon_id);return reuse?{...g,preview_url:reuse.export_url,label:g.icon_id+' · 32px reuse export'}:g;})};
    const combined=artwork('Generated combination',row.component_selection==='explicit'?{...refs[row.id],generated:[]}:refs[row.id],true,row.generated||[]);
    if(row.kind!=='container'&&row.trial_preview){
      const trial=row.trial_preview, empty=combined.querySelector('.combination-empty');if(empty)empty.remove();
      combined.append(node('p','combination-label','Trial preview'),imageLink(trial.preview_url,row.concept+' — trial'),node('p','muted',trial.status==='clearance-estimate-pass'?'Solo artwork fitted inside container · review before approval':'Solo artwork fitted inside container · placement needs review'));
    }else if(row.trial_status==='stale')combined.append(node('p','muted','Trial needs rebuilding because a linked source or pairing changed.'));
    const latest=containerPreviews.get(row.id);
    const selection=containerResults?.selections?.[row.id]||latest;
    if(row.kind==='container'){
      combined.replaceChildren(node('h4','','Combined preview'));
      if(latest?.svg_url){
        combined.append(imageLink(latest.svg_url,row.concept+' — combined'));
        combined.append(node('p','',({pass:'Fit check passed',fail:'Needs fit changes',review:'Needs review'})[latest.status]||latest.status));
        combined.append(node('p','muted','64×64 · symbol at 32×32 · not yet approved'));
      }else combined.append(node('p','combination-empty',latest?.reason||'Use Combine all pairs to generate this preview.'));
    }
    const selectedMain=selection?.main_key?{...combinationMain(row),generated:[{icon_id:'Container · 64×64',preview_url:'../container64/'+encodeURIComponent(selection.main_key.split('/')[1])+'.svg'}]}:combinationMain(row);
    const selectedSub=selection?.symbol_key?{...subRef,generated:[{icon_id:'Symbol · 32×32',preview_url:'../symbol32/'+encodeURIComponent(selection.symbol_key.split('/')[1])+'.svg'}]}:{...subRef,generated:row.kind==='container'?[]:subRef.generated};
    grid.append(original,artwork(row.kind==='container'?'Container · 64×64':'Main',selectedMain),artwork(row.kind==='container'?'Symbol · 32×32':'Sub',selectedSub),combined);card.append(grid);
    for(const mapping of row.remappings||[])card.append(node('p','muted',`${mapping.role==='main'?'Main':'Sub'} remapped to an existing source: ${mapping.reason}.`));
    const details=node('details','combination-identities');details.append(node('summary','','Source IDs'));for(const [name,id] of [['Combination',row.id],['Main',row.main_id],['Sub',row.sub_id]])details.append(node('p','',name+': '+id));card.append(details);return card;
  }
  if(grouped){
    host.append(node('p','muted','Grouped by main container. Expand a container to see its combinations.'));
    for(const group of groups.slice((page-1)*pageSize,page*pageSize)){
      const section=node('details','container-group'), heading=node('summary','container-group-heading');
      const generated=group.main.generated[0];
      if(generated){const img=node('img');img.src=generated.preview_url;img.alt='';img.loading='lazy';heading.append(img);}
      const label=node('span','container-group-label');label.append(node('strong','',group.title),node('span','muted',generated?'Main · Container 64px':'Main · Container needed'));
      heading.append(label,node('span','chip',`${group.rows.length.toLocaleString()} combination${group.rows.length===1?'':'s'}`));section.append(heading);
      const children=node('div','combination-list container-group-items');section.append(children);
      function fill(){if(section.open&&!children.childElementCount)for(const row of group.rows)children.append(combinationCard(row));}
      section.open=expandedContainers.has(group.key);fill();
      section.addEventListener('toggle',()=>{if(!section.isConnected)return;if(section.open)expandedContainers.add(group.key);else expandedContainers.delete(group.key);fill();});
      list.append(section);
    }
  }else for(const row of rows.slice((page-1)*pageSize,page*pageSize))list.append(combinationCard(row));
  if(!rows.length)list.append(node('p','muted','No combinations match these filters.'));
  host.append(list,pager());
}

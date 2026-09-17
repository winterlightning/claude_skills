(()=>{
  'use strict';
  const host=document.getElementById('combinationExperiment');if(!host)return;
  const labels={br:'Bottom-right',bl:'Bottom-left',tr:'Top-right',tl:'Top-left',ri:'Right',le:'Left',bo:'Bottom',to:'Top'};
  let centerlineView='overlay',gridPage=0,gridPageSize=24;
  const pageControls=where=>`<nav class="pair-pagination" aria-label="Combination pages ${where}"><button id="pairPrevious${where}" type="button">← Previous</button><label>Page<select id="pairPage${where}" aria-label="Combination page ${where}"></select></label><span id="pairPageTotal${where}"></span><button id="pairNext${where}" type="button">Next →</button></nav>`;
  const imageURL=s=>'data:image/svg+xml;charset=utf-8,'+encodeURIComponent(s);
  let rows=[],row=null,result=null,loaded=false,busy=false,previews={},uploads={},approved=[],pickRole=null,pickPage=0;
  host.innerHTML=`<section id="pairGallery"><div class="pair-gallery-heading"><div><h2>Combined icons</h2><p id="pairGridCount">Loading combined icons…</p></div><div class="pair-actions"><button id="pairRefresh" class="site-button">Refresh combinations</button><button id="pairTry" class="site-button">Try combine</button></div></div><p>After generating new icons, refresh to find matching pairs and build their previews.</p><p id="pairRefreshStatus" role="status" aria-live="polite"></p><label class="pair-grid-search">View<select id="pairView"><option value="icon">Icon</option><option value="overlay" selected>Icon + centerline</option><option value="centerline">Centerline only</option></select></label><p class="pair-note">Red traces the combined paths after clearance is applied.</p><label class="pair-grid-search">Find a combined icon<input id="pairGridSearch" type="search" placeholder="Search concepts or component names"></label><label class="pair-grid-search">Icons per page<select id="pairPageSize"><option value="24">24</option><option value="48">48</option><option value="96">96</option></select></label>${pageControls('Top')}<div id="pairResultsGrid" class="pair-results-grid"></div>${pageControls('Bottom')}<p id="pairGridStatus" role="status"></p></section>
  <section id="pairEditor" hidden><button id="pairBack" class="site-button">← Back to combined icons</button><div class="combination-heading"><h2>Combine main + sub</h2><p><span id="pairAvailableCount"></span> available pairs · 48×48 main · 32×32 sub · 64×64 output.</p><p>Position aligns the sub’s visible content to its edge and the main to the opposite edge, regardless of keyshape. Default clearance is 8 units with 2 units of outer padding. Adjust offsets in canvas units.</p></div>
  <p id="pairError" role="alert" hidden></p>
  <div class="pair-controls"><label>Find a pair<input id="pairSearch" type="search" placeholder="Concept or component name"></label><label>Combination<select id="pairSelect"></select></label><label>Sub position<select id="pairPosition"></select></label></div>
  <div class="pair-workspace"><div><div class="pair-component"><img id="pairMainImage" alt="Main icon"><label>Main component<select id="pairMain"></select></label></div><div class="pair-component"><img id="pairSubImage" alt="Sub icon"><label>Sub component<select id="pairSub"></select></label></div>
  <div class="pair-offsets"><label>Main X<input id="pairMainX" type="number" min="-64" max="64" step="0.5" value="0"></label><label>Main Y<input id="pairMainY" type="number" min="-64" max="64" step="0.5" value="0"></label><label>Sub X<input id="pairSubX" type="number" min="-64" max="64" step="0.5" value="0"></label><label>Sub Y<input id="pairSubY" type="number" min="-64" max="64" step="0.5" value="0"></label></div>
  <label>Buffer clearance<input id="pairMargin" type="number" min="0" max="64" step="0.5" value="8"></label><label>Canvas padding<input id="pairPadding" type="number" min="0" max="8" step="0.5" value="2"></label>
  <div class="pair-actions"><button id="pairRun">Combine pair</button><button id="pairReset">Reset placement</button><button id="pairSave">Save adjustments</button></div><p class="pair-note">Offsets save per pair in this browser. Uploaded and selected replacement SVGs are kept for this session only. Use stroked SVGs with a square viewBox; main fits 48×48 and sub fits 32×32.</p></div>
  <div><div id="pairPreview" class="pair-preview"><p>Choose a pair and press Combine pair.</p></div><div class="pair-actions"><label>View<select id="pairEditorView"><option value="icon">Icon</option><option value="overlay" selected>Icon + centerline</option><option value="centerline">Centerline only</option></select></label><label class="pair-guides"><input id="pairGuides" type="checkbox" checked> Show component canvases</label><a id="pairDownload" hidden>Download SVG</a></div><p id="pairPlacement" class="pair-note"></p><p id="pairStatus" role="status" aria-live="polite"></p></div></div></section>`;
  const $=id=>document.getElementById(id), option=(v,t)=>{const e=document.createElement('option');e.value=v;e.textContent=t;return e;};
  for(const [role,title,id] of [['main','Main','pairMain'],['sub','Sub','pairSub']]){
    const actions=document.createElement('div');actions.className='pair-source-actions';
    const pick=document.createElement('button');pick.textContent='Choose approved '+role;pick.onclick=()=>openApproved(role);
    const label=document.createElement('label');label.textContent='Upload '+role+' SVG';
    const input=document.createElement('input');input.type='file';input.accept='.svg,image/svg+xml';input.setAttribute('aria-label','Upload '+role+' SVG');input.id='pairUpload'+title;
    const note=document.createElement('span');note.id='pairSource'+title;note.className='pair-note';
    input.onchange=async()=>{const file=input.files[0];if(!file)return;if(file.size>1024*1024){error('Choose an SVG up to 1 MB.');return;}setCustom(role,await file.text(),file.name);};
    const restore=document.createElement('button');restore.textContent='Use pair '+role;restore.onclick=()=>{delete uploads[role];input.value='';note.textContent='';invalidate();componentImages();};
    label.append(input);actions.append(pick,label,restore,note);$(id).closest('.pair-component').after(actions);
  }
  const picker=document.createElement('section');picker.id='pairApprovedPicker';picker.hidden=true;
  picker.innerHTML='<h3 id="pairApprovedTitle"></h3><label>Search approved icons<input id="pairApprovedSearch" type="search" placeholder="Name, category, or family"></label><p id="pairApprovedStatus" role="status"></p><div id="pairApprovedGrid"></div><div class="pair-actions"><button id="pairApprovedPrevious">Previous</button><button id="pairApprovedNext">Next</button><button id="pairApprovedClose">Close picker</button></div>';
  $('pairEditor').prepend(picker);
  function setCustom(role,document,name){uploads[role]={document,name};$('pairSource'+(role==='main'?'Main':'Sub')).textContent=name;invalidate();componentImages();}
  function approvedGrid(){
    const q=$('pairApprovedSearch').value.toLowerCase().trim();const list=approved.filter(i=>[i.name,i.icon_id,i.category,i.family].join(' ').toLowerCase().includes(q));
    pickPage=Math.max(0,Math.min(pickPage,Math.ceil(list.length/24)-1));$('pairApprovedGrid').replaceChildren();
    for(const icon of list.slice(pickPage*24,(pickPage+1)*24)){
      const button=document.createElement('button');button.className='pair-approved-icon';button.setAttribute('aria-label','Select '+icon.name+' as '+pickRole);
      const img=document.createElement('img');img.src=icon.preview_url;img.alt=icon.name;img.width=48;img.height=48;img.loading='lazy';
      const name=document.createElement('span');name.textContent=icon.name;button.append(img,name);
      button.onclick=async()=>{const role=pickRole;button.disabled=true;try{const r=await fetch(icon.preview_url,{cache:'no-store'});if(!r.ok)throw Error('Could not load this icon.');setCustom(role,await r.text(),icon.name+' · approved');picker.hidden=true;$('pairSource'+(role==='main'?'Main':'Sub')).scrollIntoView({block:'center'});}catch(e){error(e.message);button.disabled=false;}};
      $('pairApprovedGrid').append(button);
    }
    $('pairApprovedStatus').textContent=list.length+' approved icons · page '+(pickPage+1)+' of '+Math.max(1,Math.ceil(list.length/24));$('pairApprovedPrevious').disabled=pickPage===0;$('pairApprovedNext').disabled=(pickPage+1)*24>=list.length;
  }
  async function openApproved(role){picker.hidden=false;pickRole=role;pickPage=0;$('pairApprovedTitle').textContent='Choose approved '+role+' icon';$('pairApprovedSearch').value='';$('pairApprovedStatus').textContent='Loading approved icons…';picker.scrollIntoView({block:'start'});try{const responses=await Promise.all([fetch('icons.json',{cache:'no-store'}),fetch('/api/reviews',{cache:'no-store'})]);if(responses.some(r=>!r.ok))throw Error('Could not load approved icons.');const [catalog,reviews]=await Promise.all(responses.map(r=>r.json()));approved=catalog.icons.filter(i=>reviews[i.key]==='approve');approvedGrid();}catch(e){$('pairApprovedStatus').textContent=e.message;}}
  $('pairApprovedSearch').oninput=()=>{pickPage=0;approvedGrid();};$('pairApprovedPrevious').onclick=()=>{pickPage--;approvedGrid();};$('pairApprovedNext').onclick=()=>{pickPage++;approvedGrid();};$('pairApprovedClose').onclick=()=>picker.hidden=true;
  for(const [key,label]of Object.entries(labels))$('pairPosition').append(option(key,label));
  const fields={position:'pairPosition',main:'pairMain',sub:'pairSub',mainX:'pairMainX',mainY:'pairMainY',subX:'pairSubX',subY:'pairSubY',margin:'pairMargin',padding:'pairPadding'};
  function error(text){$('pairError').textContent=text;$('pairError').hidden=!text;}
  function settings(){return {id:row.id,settingsVersion:2,mainUpload:uploads.main,subUpload:uploads.sub,...Object.fromEntries(Object.entries(fields).map(([k,id])=>[k,$(id).value]))};}
  function invalidate(){result=null;$('pairDownload').hidden=true;$('pairPreview').replaceChildren();const p=document.createElement('p');p.textContent='Press Combine pair to preview this placement.';$('pairPreview').append(p);$('pairPlacement').textContent='';$('pairStatus').textContent='';$('pairSave').textContent='Save adjustments';error('');}
  function componentImages(){for(const [key,id,group]of [['main','pairMainImage','mains'],['sub','pairSubImage','subs']]){const select=$(fields[key]);let custom=select.querySelector('option[value="__custom__"]');if(uploads[key]){if(!custom){custom=option('__custom__',uploads[key].name);select.append(custom);}custom.textContent=uploads[key].name;select.value='__custom__';}else custom?.remove();const m=row[group].find(m=>m.icon===select.value)||row[group][0];$(id).src=imageURL(uploads[key]?.document||m.document);}}
  function reset(keepSources=false){if(!row)return;if(!keepSources){uploads={};for(const name of ['Main','Sub']){$('pairSource'+name).textContent='';$('pairUpload'+name).value='';}}for(const [key,id]of Object.entries(fields))$(id).value=key==='position'?row.position:key==='main'?row.mains[0].icon:key==='sub'?row.subs[0].icon:key==='margin'?8:key==='padding'?2:0;invalidate();componentImages();}
  function choose(){row=rows.find(r=>r.id===$('pairSelect').value);if(!row)return;
    for(const [id,group]of [['pairMain','mains'],['pairSub','subs']])$(id).replaceChildren(...row[group].map(m=>option(m.icon,m.icon)));
    reset();try{const saved=JSON.parse(localStorage.getItem('pictographic-combination:'+row.id)||'null');if(saved){if(!saved.settingsVersion && Number(saved.margin)===4)saved.margin=8;for(const [key,id]of Object.entries(fields))if(saved[key]!==undefined)$(id).value=saved[key];componentImages();$('pairSave').textContent='Adjustments saved';}}catch{}
  }
  function filter(){const text=$('pairSearch').value.toLowerCase().trim(),selected=row?.id;const visible=rows.filter(r=>[r.concept,r.id,...r.mains.map(m=>m.icon),...r.subs.map(m=>m.icon)].join(' ').toLowerCase().includes(text));$('pairSelect').replaceChildren(...visible.map(r=>option(r.id,r.concept+' · '+r.id.slice(0,8))));if(selected&&!visible.some(r=>r.id===selected))$('pairSelect').append(option(selected,row.concept+' (selected)'));if(selected)$('pairSelect').value=selected;}
  function displaySVG(documentText){
    if(centerlineView==='icon')return documentText;
    const document=new DOMParser().parseFromString(documentText,'image/svg+xml');
    const svg=document.documentElement;
    const groups=Array.from(svg.children).filter(e=>e.localName==='g');
    for(const group of groups){
      const trace=group.cloneNode(true);
      trace.removeAttribute('id');
      for(const shape of [trace,...trace.querySelectorAll('*')]){
        shape.removeAttribute('id');
        shape.setAttribute('stroke','#e33444');
        shape.setAttribute('stroke-width','0.5');
        shape.setAttribute('fill','none');
      }
      if(centerlineView==='centerline')group.remove();else group.setAttribute('opacity','0.22');
      svg.append(trace);
    }
    return new XMLSerializer().serializeToString(svg);
  }
  function changeView(event){
    centerlineView=event.target.value;
    $('pairView').value=centerlineView;$('pairEditorView').value=centerlineView;
    grid();draw();
  }
  $('pairView').onchange=changeView;$('pairEditorView').onchange=changeView;
  function draw(){if(!result)return;const ns='http://www.w3.org/2000/svg',svg=document.createElementNS(ns,'svg');svg.setAttribute('viewBox','-1 -1 66 66');svg.setAttribute('role','img');svg.setAttribute('aria-label','Combined icon on 64 by 64 canvas');
    function element(tag,attrs){const e=document.createElementNS(ns,tag);for(const [k,v]of Object.entries(attrs))e.setAttribute(k,v);svg.append(e);}
    element('rect',{x:0,y:0,width:64,height:64,fill:'white',stroke:'#bcc5bb','stroke-width':.15});element('image',{href:imageURL(displaySVG(result.svg)),x:0,y:0,width:64,height:64});
    if($('pairGuides').checked)for(const p of result.placements)element('rect',{x:p.canvas_box.x,y:p.canvas_box.y,width:p.canvas_box.w,height:p.canvas_box.h,fill:'none',stroke:p.role==='main'?'#cf604d':'#4776aa','stroke-width':.2,'stroke-dasharray':'1 1'});
    $('pairPreview').replaceChildren(svg);$('pairDownload').href=imageURL(result.svg);$('pairDownload').download=result.filename;$('pairDownload').hidden=false;
    $('pairPlacement').textContent=result.placements.map(p=>`${p.role}: ${p.canvas_box.w}×${p.canvas_box.h} canvas at (${p.canvas_box.x}, ${p.canvas_box.y}); ink starts at (${p.painted_box.x.toFixed(2)}, ${p.painted_box.y.toFixed(2)})`).join(' · ');
    $('pairStatus').textContent=result.warnings.join(' ');
  }
  $('pairRun').onclick=async()=>{if(!row||busy)return;busy=true;invalidate();for(const e of $('pairEditor').querySelectorAll('button,input,select'))e.disabled=true;$('pairRun').textContent='Combining…';$('pairStatus').textContent='Combining on a 64×64 canvas…';
    try{const response=await fetch('/api/combination-experiment',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(settings())});const data=await response.json();if(!response.ok||data.error)throw Error(data.error||'Could not combine this pair.');result=data;draw();}
    catch(e){error(location.protocol==='file:'?'Open this Experiment tab through the local Pictographic server to combine icons.':e.message);$('pairStatus').textContent='';}
    finally{busy=false;for(const e of $('pairEditor').querySelectorAll('button,input,select'))e.disabled=false;$('pairRun').textContent='Combine pair';}
  };
  $('pairReset').onclick=()=>reset(true);$('pairSave').onclick=()=>{if(!row)return;try{localStorage.setItem('pictographic-combination:'+row.id,JSON.stringify({...settings(),main:uploads.main?row.mains[0].icon:$('pairMain').value,sub:uploads.sub?row.subs[0].icon:$('pairSub').value,mainUpload:undefined,subUpload:undefined}));$('pairSave').textContent='Adjustments saved';}catch{error('Could not save adjustments in this browser.');}};
  $('pairGuides').onchange=draw;$('pairSearch').oninput=filter;$('pairSelect').onchange=choose;
  for(const id of Object.values(fields))$(id).addEventListener('change',()=>{invalidate();if(id==='pairMain'){delete uploads.main;$('pairSourceMain').textContent='';}if(id==='pairSub'){delete uploads.sub;$('pairSourceSub').textContent='';}if(row)componentImages();});

  function showEditor(id){
    if(busy)return;
    $('pairSearch').value='';filter();if(id)$('pairSelect').value=id;choose();
    const current=settings();
    const defaults=row && current.position===row.position && current.main===row.mains[0].icon && current.sub===row.subs[0].icon && !uploads.main && !uploads.sub && ['mainX','mainY','subX','subY'].every(k=>Number(current[k])===0) && Number(current.margin)===8 && Number(current.padding)===2;
    if(previews[row?.id] && defaults){result=previews[row.id].result;draw();}
    $('pairGallery').hidden=true;$('pairEditor').hidden=false;$('pairBack').focus();
  }
  function showGrid(){if(busy)return;$('pairEditor').hidden=true;$('pairGallery').hidden=false;$('pairTry').focus();}
  function grid(){
    const q=$('pairGridSearch').value.trim().toLowerCase();
    const visible=rows.filter(r=>[r.concept,r.id,...r.mains.map(m=>m.icon),...r.subs.map(m=>m.icon)].join(' ').toLowerCase().includes(q));
    const pages=Math.max(1,Math.ceil(visible.length/gridPageSize));
    gridPage=Math.min(gridPage,pages-1);
    const start=gridPage*gridPageSize;
    for(const where of ['Top','Bottom']){
      $('pairPage'+where).replaceChildren(...Array.from({length:pages},(_,i)=>option(i,i+1)));
      $('pairPage'+where).value=gridPage;
      $('pairPage'+where).disabled=!visible.length;
      $('pairPageTotal'+where).textContent='of '+pages;
      $('pairPrevious'+where).disabled=gridPage===0;
      $('pairNext'+where).disabled=gridPage===pages-1;
    }
    $('pairResultsGrid').replaceChildren();
    for(const r of visible.slice(start,start+gridPageSize)){
      const card=document.createElement('article');card.className='pair-result-card';
      const image=document.createElement('img');image.alt=r.concept+' — combined icon';image.width=96;image.height=96;image.loading='lazy';
      const preview=previews[r.id];
      if(preview)image.src=centerlineView==='icon'?preview.url:imageURL(displaySVG(preview.result.svg));else image.alt='Preview unavailable';
      const title=document.createElement('h3');title.textContent=r.concept;
      const detail=document.createElement('p');detail.textContent='64×64 · '+labels[r.position];
      const actions=document.createElement('div');actions.className='pair-card-actions';

      if(preview){const download=document.createElement('a');download.href=preview.url;download.download=r.id+'.svg';download.textContent='SVG';download.setAttribute('aria-label','Download '+r.concept+' SVG');actions.append(download);}
      card.append(image,title,detail,actions);$('pairResultsGrid').append(card);
    }
    $('pairGridCount').textContent=visible.length+' combined icons · 64×64 · clearance 8 · padding 2';
    $('pairGridStatus').textContent=visible.length?'Showing '+(start+1)+'–'+Math.min(start+gridPageSize,visible.length)+' of '+visible.length+' combined icons.':'No combined icons match your search.';
  }
  $('pairTry').onclick=()=>showEditor(row?.id);$('pairBack').onclick=showGrid;$('pairGridSearch').oninput=()=>{gridPage=0;grid();};
  $('pairPageSize').onchange=()=>{gridPageSize=Number($('pairPageSize').value);gridPage=0;grid();};
  function goPage(page){gridPage=page;grid();$('pairPageTop').focus({preventScroll:true});$('pairPageTop').scrollIntoView({block:'center'});}
  for(const where of ['Top','Bottom']){
    $('pairPrevious'+where).onclick=()=>goPage(gridPage-1);
    $('pairNext'+where).onclick=()=>goPage(gridPage+1);
    $('pairPage'+where).onchange=e=>goPage(Number(e.target.value));
  }
  async function load(){if(loaded)return;loaded=true;try{const response=await fetch('experiment-combination.json',{cache:'no-store'});if(!response.ok)throw Error('Could not load available pairs.');rows=(await response.json()).rows;const rendered=await fetch('experiment-combination-results.json',{cache:'no-store'});if(!rendered.ok)throw Error('Combined previews could not be loaded. Reload to try again.');previews=(await rendered.json()).results;grid();$('combinationCount').textContent=rows.length;$('pairAvailableCount').textContent=rows.length;filter();$('pairSelect').value=rows.find(r=>r.concept==='surveillance cctv wifi')?.id||rows[0]?.id;choose();}catch(e){loaded=false;$('pairGridStatus').textContent=e.message;error(e.message);}}
  let refreshTimer;
  async function refreshStatus(start=false){
    clearTimeout(refreshTimer);
    try{
      const response=await fetch('/api/combination-refresh',start?{method:'POST',headers:{'Content-Type':'application/json'},body:'{}'}:{cache:'no-store'});
      if(!response.ok)throw Error('Could not refresh combinations. Please try again.');
      const state=await response.json();
      $('pairRefresh').disabled=state.status==='running';
      $('pairRefresh').textContent=state.status==='running'?'Refreshing…':'Refresh combinations';
      $('pairRefreshStatus').textContent=state.message||'';
      if(state.status==='running')refreshTimer=setTimeout(()=>refreshStatus(),1500);
      else if(state.status==='complete'){loaded=false;await load();}
    }catch(e){$('pairRefresh').disabled=false;$('pairRefresh').textContent='Refresh combinations';$('pairRefreshStatus').textContent=e.message;}
  }
  $('pairRefresh').onclick=()=>refreshStatus(true);
  window.addEventListener('show-combinations',()=>refreshStatus());
  if(new URLSearchParams(location.search).get('type')==='combination')refreshStatus();
  window.addEventListener('show-combinations',load);if(new URLSearchParams(location.search).get('type')==='combination')load();
})();

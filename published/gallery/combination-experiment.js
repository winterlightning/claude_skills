(()=>{
  'use strict';
  const host=document.getElementById('combinationExperiment');if(!host)return;
  const labels={br:'Bottom-right',bl:'Bottom-left',tr:'Top-right',tl:'Top-left',ri:'Right',le:'Left',bo:'Bottom',to:'Top'};
  let centerlineView='sub-overlay',displayStroke=4,gridPage=0,gridPageSize=24;
  const pageControls=where=>`<nav class="pair-pagination" aria-label="Combination pages ${where}"><button id="pairPrevious${where}" type="button">← Previous</button><label>Page<select id="pairPage${where}" aria-label="Combination page ${where}"></select></label><span id="pairPageTotal${where}"></span><button id="pairNext${where}" type="button">Next →</button></nav>`;
  const imageURL=s=>'data:image/svg+xml;charset=utf-8,'+encodeURIComponent(s);
  let rows=[],row=null,result=null,loaded=false,busy=false,previews={},uploads={},approved=[],pickRole=null,pickPage=0;
  host.innerHTML=`<section id="pairGallery"><p id="pairRunSummary" class="pair-note" role="status"></p><div class="pair-view-toolbar"><label class="pair-grid-search">View<select id="pairView"><option value="sub-overlay" selected>Stroke + sub centerline</option><option value="icon">Full stroke</option><option value="overlay">Stroke + centerline</option><option value="centerline">Centerline only</option></select></label><label class="pair-grid-search">Display stroke width<select id="pairStrokeWidth"><option value="4" selected>4px · original stroke</option></select></label><label class="pair-grid-search">Find a combined icon<input id="pairGridSearch" type="search" placeholder="Search concepts or component names"></label><label class="pair-grid-search">Sub readiness<select id="pairReadiness"><option value="">All combined icons</option><option value="pass">Passing sub icons</option><option value="text">Text sub</option><option value="native_sub32">Native SUB32</option><option value="needs_redraw">Needs SUB32 redraw</option></select></label><label class="pair-grid-search">Icons per page<select id="pairPageSize"><option value="24">24</option><option value="48">48</option><option value="96">96</option></select></label></div>${pageControls('Top')}<div id="pairResultsGrid" class="pair-results-grid"></div>${pageControls('Bottom')}<p id="pairGridStatus" role="status"></p></section>
  <section id="pairEditor" hidden><button id="pairBack" class="site-button">← Back to combined icons</button><div class="combination-heading"><h2>Combine main + sub</h2><p><span id="pairAvailableCount"></span> available pairs · 48×48 main · 32×32 sub · 64×64 output.</p><p>Position places the sub canvas at its chosen edge and the main at the opposite edge. Automatic sizing keeps solo proportions and rounds the ink-box dimensions. Default clearance is 8 units with 2 units of outer padding. Adjust offsets in canvas units.</p></div>
  <p id="pairError" role="alert" hidden></p>
  <div class="pair-controls"><label>Find a pair<input id="pairSearch" type="search" placeholder="Concept or component name"></label><label>Combination<select id="pairSelect"></select></label><label>Sub position<select id="pairPosition"></select></label></div>
  <div class="pair-workspace"><div><div class="pair-component"><img id="pairMainImage" alt="Main icon"><label>Main component<select id="pairMain"></select></label></div><div class="pair-component"><img id="pairSubImage" alt="Sub icon"><label>Sub component<select id="pairSub"></select></label></div>
  <div class="pair-offsets"><label>Main X<input id="pairMainX" type="number" min="-64" max="64" step="0.5" value="0"></label><label>Main Y<input id="pairMainY" type="number" min="-64" max="64" step="0.5" value="0"></label><label>Sub X<input id="pairSubX" type="number" min="-64" max="64" step="0.5" value="0"></label><label>Sub Y<input id="pairSubY" type="number" min="-64" max="64" step="0.5" value="0"></label></div>
  <div class="pair-offsets"><label>Sub size lock<select id="pairSubSizeLock"><option value="auto">Auto · rounded proportions</option><option value="width">Lock width</option><option value="height">Lock height</option><option value="none">Original scale</option></select></label><label>Visible size (px)<input id="pairSubBoundSize" type="number" min="5" max="32" step="1" placeholder="Nearest whole number"></label></div><p class="pair-note">32×32 is the maximum ink box, including the 4px stroke. Automatic scaling uses whole-number dimensions without imposing a SUB32 keyshape. Changing size or fractional offsets may move strokes off the grid; rounding the outer box alone does not validate the geometry.</p>
  <label>Buffer clearance<input id="pairMargin" type="number" min="0" max="64" step="0.5" value="8"></label><label>Canvas padding<input id="pairPadding" type="number" min="0" max="8" step="0.5" value="2"></label>
  <div class="pair-actions"><button id="pairRun" data-development-only>Combine pair</button><button id="pairReset">Reset placement</button><button id="pairSave">Save adjustments</button></div><p class="pair-note">Offsets save per pair in this browser. Uploaded and selected replacement SVGs are kept for this session only. Use stroked SVGs with a square viewBox; main fits 48×48 and sub fits 32×32.</p></div>
  <div><div id="pairPreview" class="pair-preview"><p>Choose a pair and press Combine pair.</p></div><div class="pair-actions"><label>View<select id="pairEditorView"><option value="sub-overlay" selected>Stroke + sub centerline</option><option value="icon">Full stroke</option><option value="overlay">Stroke + centerline</option><option value="centerline">Centerline only</option></select></label><label>Display stroke width<select id="pairEditorStrokeWidth"><option value="4" selected>4px · original stroke</option></select></label><label class="pair-guides"><input id="pairGuides" type="checkbox" checked> Show canvases and sub bounds</label><a id="pairDownload" hidden>Download SVG</a></div><p id="pairPlacement" class="pair-note"></p><p id="pairStatus" role="status" aria-live="polite"></p></div></div></section>`;
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
  async function openApproved(role){picker.hidden=false;pickRole=role;pickPage=0;$('pairApprovedTitle').textContent='Choose approved '+role+' icon';$('pairApprovedSearch').value='';$('pairApprovedStatus').textContent='Loading approved icons…';picker.scrollIntoView({block:'start'});try{const responses=await Promise.all([fetch('icons.json',{cache:'no-store'}),fetch('/api/reviews',{cache:'no-store'})]);if(responses.some(r=>!r.ok))throw Error('Could not load approved icons.');const [catalog,reviews]=await Promise.all(responses.map(r=>r.json()));approved=catalog.icons.filter(i=>reviews[i.key]==='approve'&&i.reference_fidelity?.status!=='superseded');approvedGrid();}catch(e){$('pairApprovedStatus').textContent=e.message;}}
  $('pairApprovedSearch').oninput=()=>{pickPage=0;approvedGrid();};$('pairApprovedPrevious').onclick=()=>{pickPage--;approvedGrid();};$('pairApprovedNext').onclick=()=>{pickPage++;approvedGrid();};$('pairApprovedClose').onclick=()=>picker.hidden=true;
  for(const [key,label]of Object.entries(labels))$('pairPosition').append(option(key,label));
  const fields={position:'pairPosition',main:'pairMain',sub:'pairSub',mainX:'pairMainX',mainY:'pairMainY',subX:'pairSubX',subY:'pairSubY',margin:'pairMargin',padding:'pairPadding',subSizeLock:'pairSubSizeLock',subBoundSize:'pairSubBoundSize'};
  function error(text){$('pairError').textContent=text;$('pairError').hidden=!text;}
  function settings(){return {id:row.id,settingsVersion:3,mainUpload:uploads.main,subUpload:uploads.sub,...Object.fromEntries(Object.entries(fields).map(([k,id])=>[k,$(id).value]))};}
  function invalidate(){result=null;$('pairDownload').hidden=true;$('pairPreview').replaceChildren();const p=document.createElement('p');p.textContent='Press Combine pair to preview this placement.';$('pairPreview').append(p);$('pairPlacement').textContent='';$('pairStatus').textContent='';$('pairSave').textContent='Save adjustments';error('');}
  function componentImages(){for(const [key,id,group]of [['main','pairMainImage','mains'],['sub','pairSubImage','subs']]){const select=$(fields[key]);let custom=select.querySelector('option[value="__custom__"]');if(uploads[key]){if(!custom){custom=option('__custom__',uploads[key].name);select.append(custom);}custom.textContent=uploads[key].name;select.value='__custom__';}else custom?.remove();const m=row[group].find(m=>m.icon===select.value)||row[group][0];$(id).src=imageURL(uploads[key]?.document||m.document);if(key==='sub'){let link=document.getElementById('pairSubExport');if(!link){link=document.createElement('a');link.id='pairSubExport';link.textContent='Download 32px sub SVG';link.setAttribute('download','');$(id).parentElement.append(link);}link.hidden=!!uploads[key]||!m.export_url;if(m.export_url)link.href=m.export_url;}}}
  function reset(keepSources=false){if(!row)return;if(!keepSources){uploads={};for(const name of ['Main','Sub']){$('pairSource'+name).textContent='';$('pairUpload'+name).value='';}}for(const [key,id]of Object.entries(fields))$(id).value=key==='position'?row.position:key==='main'?row.mains[0].icon:key==='sub'?row.subs[0].icon:key==='margin'?8:key==='padding'?2:key==='subSizeLock'?'auto':key==='subBoundSize'?'':0;invalidate();componentImages();}
  function choose(){row=rows.find(r=>r.id===$('pairSelect').value);if(!row)return;
    for(const [id,group]of [['pairMain','mains'],['pairSub','subs']])$(id).replaceChildren(...row[group].map(m=>option(m.icon,m.icon+(m.family==='sub'?' · Native SUB32':' · Needs SUB32 redraw'))));
    reset();try{const saved=JSON.parse(localStorage.getItem('pictographic-combination:'+row.id)||'null');if(saved){if(!saved.settingsVersion && Number(saved.margin)===4)saved.margin=8;for(const [key,id]of Object.entries(fields))if(saved[key]!==undefined)$(id).value=saved[key];componentImages();$('pairSave').textContent='Adjustments saved';}}catch{}
  }
  function filter(){const text=$('pairSearch').value.toLowerCase().trim(),selected=row?.id;const visible=rows.filter(r=>[r.concept,r.id,...r.mains.map(m=>m.icon),...r.subs.map(m=>m.icon)].join(' ').toLowerCase().includes(text));$('pairSelect').replaceChildren(...visible.map(r=>option(r.id,r.concept+' · '+r.id.slice(0,8))));if(selected&&!visible.some(r=>r.id===selected))$('pairSelect').append(option(selected,row.concept+' (selected)'));if(selected)$('pairSelect').value=selected;}
  function displaySVG(documentText){
    const document=new DOMParser().parseFromString(documentText,'image/svg+xml');
    const svg=document.documentElement;
    // Preserve original stroke widths and placement-scale compensation.
    if(centerlineView==='sub-overlay'){SideCombinationPopup.addSubCenterline(svg);return new XMLSerializer().serializeToString(svg);}
    if(centerlineView==='icon')return new XMLSerializer().serializeToString(svg);
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
  function changeStroke(e){displayStroke=Number(e.target.value);$('pairStrokeWidth').value=displayStroke;$('pairEditorStrokeWidth').value=displayStroke;grid();draw();}
  $('pairStrokeWidth').onchange=changeStroke;$('pairEditorStrokeWidth').onchange=changeStroke;
  $('pairView').onchange=changeView;$('pairEditorView').onchange=changeView;
  function draw(){if(!result)return;const ns='http://www.w3.org/2000/svg',svg=document.createElementNS(ns,'svg');svg.setAttribute('viewBox','-1 -1 66 66');svg.setAttribute('role','img');svg.setAttribute('aria-label','Combined icon on 64 by 64 canvas');
    function element(tag,attrs){const e=document.createElementNS(ns,tag);for(const [k,v]of Object.entries(attrs))e.setAttribute(k,v);svg.append(e);}
    element('rect',{x:0,y:0,width:64,height:64,fill:'white',stroke:'#bcc5bb','stroke-width':.15});for(let n=1;n<64;n++){const attrs={stroke:n%8===0?'#9eafb8':'#d7e1e5','stroke-width':n%8===0?.18:.08};element('line',{x1:n,y1:0,x2:n,y2:64,...attrs});element('line',{x1:0,y1:n,x2:64,y2:n,...attrs});}element('image',{href:imageURL(displaySVG(result.svg)),x:0,y:0,width:64,height:64});
    if($('pairGuides').checked)for(const p of result.placements)element('rect',{x:p.canvas_box.x,y:p.canvas_box.y,width:p.canvas_box.w,height:p.canvas_box.h,fill:'none',stroke:p.role==='main'?'#cf604d':'#4776aa','stroke-width':.2,'stroke-dasharray':'1 1'});
    if($('pairGuides').checked){const b=result.placements.find(p=>p.role==='sub')?.painted_box;if(b)element('rect',{x:b.x,y:b.y,width:b.w,height:b.h,fill:'none',stroke:'#23835b','stroke-width':.3,'stroke-dasharray':'1 .5'});}
    $('pairPreview').replaceChildren(svg);$('pairDownload').href=imageURL(result.svg);$('pairDownload').download=result.filename;$('pairDownload').hidden=false;
    $('pairPlacement').textContent=result.placements.map(p=>`${p.role}: ${p.canvas_box.w}×${p.canvas_box.h} canvas at (${p.canvas_box.x}, ${p.canvas_box.y}); visible bounds ${p.painted_box.w.toFixed(2)}×${p.painted_box.h.toFixed(2)}${p.target_keyshape?' · '+p.target_keyshape+' fit':p.locked_axis?' · '+p.locked_axis+' locked to '+Math.round(p.locked_size)+'px':''}; ink starts at (${p.painted_box.x.toFixed(2)}, ${p.painted_box.y.toFixed(2)})`).join(' · ');
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
    const defaults=row && current.position===row.position && current.main===row.mains[0].icon && current.sub===row.subs[0].icon && !uploads.main && !uploads.sub && ['mainX','mainY','subX','subY'].every(k=>Number(current[k])===0) && Number(current.margin)===8 && Number(current.padding)===2 && current.subSizeLock==='auto' && !current.subBoundSize;
    if(previews[row?.id]?.result?.subSizeLock==='auto' && defaults){result=previews[row.id].result;draw();}
    $('pairGallery').hidden=true;$('pairEditor').hidden=false;$('pairBack').focus();
  }
  function showGrid(){if(busy)return;$('pairEditor').hidden=true;$('pairGallery').hidden=false;$('pairGridSearch').focus();}
  function grid(){
    const q=$('pairGridSearch').value.trim().toLowerCase();
    const visible=rows.filter(r=>previews[r.id]&&(!$('pairReadiness').value || ($('pairReadiness').value==='pass' ? r.subs[0].model_validation==='pass' : $('pairReadiness').value==='text' ? r.subs.some(s=>s.native_text||s.family==='text'||s.sizing_kind==='text') : r.subs[0].sub32_status===$('pairReadiness').value)) && [r.concept,r.id,...r.mains.map(m=>m.icon),...r.subs.map(m=>m.icon)].join(' ').toLowerCase().includes(q));
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
      if(preview)image.src=centerlineView==='icon'&&displayStroke===4?preview.url:imageURL(displaySVG(preview.result.svg));else image.alt='Preview unavailable';
      const title=document.createElement('h3');title.textContent=r.concept;
      const detail=document.createElement('p');detail.textContent=(preview?.result?.canvas||64)+'×'+(preview?.result?.canvas||64)+' · '+labels[r.position]+' · '+(r.native_text?'Native text':r.subs[0].model_validation==='pass'?'Passing sub':'Needs review');detail.title=r.subs[0].sub32_reason||'';
      const actions=document.createElement('div');actions.className='pair-card-actions';

      if(preview){const download=document.createElement('a');download.href=preview.url;download.download=r.id+'.svg';SideRepairFlags.download(download);download.setAttribute('aria-label','Download '+r.concept+' SVG');actions.append(download);}
      actions.append(SideRepairFlags.button('main',r.mains[0],r),SideRepairFlags.button('sub',r.subs[0],r));card.append(image,title,detail,actions);if(preview)window.SideCombinationPopup.attach(image,r.concept,preview.result);$('pairResultsGrid').append(card);
    }
    $('pairGridStatus').textContent=visible.length?'Showing '+(start+1)+'–'+Math.min(start+gridPageSize,visible.length)+' of '+visible.length+' combined icons.':'No combined icons match your search.';
  }
  $('pairBack').onclick=showGrid;$('pairGridSearch').oninput=()=>{gridPage=0;grid();};
  $('pairReadiness').onchange=()=>{gridPage=0;grid();};
  $('pairPageSize').onchange=()=>{gridPageSize=Number($('pairPageSize').value);gridPage=0;grid();};
  function goPage(page){gridPage=page;grid();$('pairPageTop').focus({preventScroll:true});$('pairPageTop').scrollIntoView({block:'center'});}
  for(const where of ['Top','Bottom']){
    $('pairPrevious'+where).onclick=()=>goPage(gridPage-1);
    $('pairNext'+where).onclick=()=>goPage(gridPage+1);
    $('pairPage'+where).onchange=e=>goPage(Number(e.target.value));
  }
  // The count is the latest Combine all side pairs run, the same set the Progression page and Icon review show.
  function summary(run){
    const count=run?run.count:rows.filter(r=>previews[r.id]).length,box=$('pairRunSummary');
    $('combinationCount').textContent=count;box.replaceChildren();
    box.append(count.toLocaleString()+' combined icons'+(run?.generated_at?' · last combined '+new Date(run.generated_at).toLocaleString():'')+' · '+(rows.length-count).toLocaleString()+' of '+rows.length.toLocaleString()+' drawn pairs could not be combined · ');
    const link=document.createElement('a');link.href='index.html?family=side_combination64';link.textContent='Review in Icon review →';box.append(link);
  }
  async function load(){if(loaded)return;loaded=true;const params=new URLSearchParams(location.search);$('pairGridSearch').value=params.get('q')||'';if(params.get('sub')==='text')$('pairReadiness').value='text';try{const response=await fetch('experiment-combination.json',{cache:'no-store'});if(!response.ok)throw Error('Could not load available pairs.');rows=(await response.json()).rows;SideRepairFlags.setRows(rows);const rendered=await fetch('experiment-combination-results.json',{cache:'no-store'});if(!rendered.ok)throw Error('Combined previews could not be loaded. Reload to try again.');previews=Object.fromEntries(Object.entries((await rendered.json()).results).filter(([,p])=>!p.error));const run=await fetch('side-combination64.json',{cache:'no-store'}).then(r=>r.ok?r.json():null).catch(()=>null);summary(run);grid();$('pairAvailableCount').textContent=rows.length;filter();$('pairSelect').value=rows.find(r=>r.concept==='surveillance cctv wifi')?.id||rows[0]?.id;choose();}catch(e){loaded=false;$('pairGridStatus').textContent=e.message;error(e.message);}}
  window.addEventListener('show-combinations',load);if(new URLSearchParams(location.search).get('type')==='combination')load();
})();

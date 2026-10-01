(()=>{
  'use strict';
  const host=document.getElementById('combinationExperiment');if(!host)return;
  const labels={br:'Bottom-right',bl:'Bottom-left',tr:'Top-right',tl:'Top-left',ri:'Right',le:'Left',bo:'Bottom',to:'Top'};
  let centerlineView='sub-overlay',displayStroke=4,gridPage=0,gridPageSize=24;
  const pageControls=where=>`<nav class="pair-pagination" aria-label="Combination pages ${where}"><button id="pairPrevious${where}" type="button">← Previous</button><label>Page<select id="pairPage${where}" aria-label="Combination page ${where}"></select></label><span id="pairPageTotal${where}"></span><button id="pairNext${where}" type="button">Next →</button></nav>`;
  const imageURL=s=>'data:image/svg+xml;charset=utf-8,'+encodeURIComponent(s);
  let rows=[],loaded=false,previews={};
  host.innerHTML=`<section id="pairGallery"><p id="pairRunSummary" class="pair-note" role="status"></p><div class="pair-view-toolbar"><label class="pair-grid-search">View<select id="pairView"><option value="sub-overlay" selected>Stroke + sub centerline</option><option value="icon">Full stroke</option><option value="overlay">Stroke + centerline</option><option value="centerline">Centerline only</option></select></label><label class="pair-grid-search">Display stroke width<select id="pairStrokeWidth"><option value="4" selected>4px · original stroke</option></select></label><label class="pair-grid-search">Find a combined icon<input id="pairGridSearch" type="search" placeholder="Search concepts or component names"></label><label class="pair-grid-search">Sub readiness<select id="pairReadiness"><option value="">All combined icons</option><option value="pass">Passing sub icons</option><option value="text">Text sub</option><option value="native_sub32">Native SUB32</option><option value="needs_redraw">Needs SUB32 redraw</option></select></label><label class="pair-grid-search">Icons per page<select id="pairPageSize"><option value="24">24</option><option value="48">48</option><option value="96">96</option></select></label></div>${pageControls('Top')}<div id="pairResultsGrid" class="pair-results-grid"></div>${pageControls('Bottom')}<p id="pairGridStatus" role="status"></p></section>`;
  const $=id=>document.getElementById(id), option=(v,t)=>{const e=document.createElement('option');e.value=v;e.textContent=t;return e;};
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
  function changeView(event){centerlineView=event.target.value;$('pairView').value=centerlineView;grid();}
  function changeStroke(e){displayStroke=Number(e.target.value);$('pairStrokeWidth').value=displayStroke;grid();}
  $('pairStrokeWidth').onchange=changeStroke;$('pairView').onchange=changeView;
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
      // Edit: this pair's editor on Side pairs (combined in the browser and saved to the cloud).
      const edit=document.createElement('a');edit.className='site-button requires-login';edit.textContent='Edit';
      edit.href='side-pairs.html?q='+encodeURIComponent(r.id)+'&edit='+encodeURIComponent(r.id);actions.prepend(edit);
      actions.append(SideRepairFlags.button('main',r.mains[0],r),SideRepairFlags.button('sub',r.subs[0],r));card.append(image,title,detail,actions);if(preview)window.SideCombinationPopup.attach(image,r.concept,preview.result);$('pairResultsGrid').append(card);
    }
    $('pairGridStatus').textContent=visible.length?'Showing '+(start+1)+'–'+Math.min(start+gridPageSize,visible.length)+' of '+visible.length+' combined icons.':'No combined icons match your search.';
  }
  $('pairGridSearch').oninput=()=>{gridPage=0;grid();};
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
  async function load(){if(loaded)return;loaded=true;const params=new URLSearchParams(location.search);$('pairGridSearch').value=params.get('q')||'';if(params.get('sub')==='text')$('pairReadiness').value='text';try{const response=await fetch('experiment-combination.json',{cache:'no-store'});if(!response.ok)throw Error('Could not load available pairs.');rows=(await response.json()).rows;SideRepairFlags.setRows(rows);const rendered=await fetch('experiment-combination-results.json',{cache:'no-store'});if(!rendered.ok)throw Error('Combined previews could not be loaded. Reload to try again.');previews=Object.fromEntries(Object.entries((await rendered.json()).results).filter(([,p])=>!p.error));const run=await fetch('side-combination64.json',{cache:'no-store'}).then(r=>r.ok?r.json():null).catch(()=>null);summary(run);grid();}catch(e){loaded=false;$('pairGridStatus').textContent=e.message;}}
  window.addEventListener('show-combinations',load);if(new URLSearchParams(location.search).get('type')==='combination')load();
})();

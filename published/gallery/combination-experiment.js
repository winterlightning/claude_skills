(()=>{
  'use strict';
  const host=document.getElementById('combinationExperiment');if(!host)return;
  const labels={br:'Bottom-right',bl:'Bottom-left',tr:'Top-right',tl:'Top-left',ri:'Right',le:'Left',bo:'Bottom',to:'Top'};
  let centerlineView='sub-overlay',displayStroke=4,gridPage=0,gridPageSize=24;
  const pageControls=where=>`<nav class="pair-pagination" aria-label="Combination pages ${where}"><button id="pairPrevious${where}" type="button">← Previous</button><label>Page<select id="pairPage${where}" aria-label="Combination page ${where}"></select></label><span id="pairPageTotal${where}"></span><button id="pairNext${where}" type="button">Next →</button></nav>`;
  const imageURL=s=>'data:image/svg+xml;charset=utf-8,'+encodeURIComponent(s);
  let rows=[],loaded=false,previews={};
  host.innerHTML=`<section id="pairGallery"><p id="pairRunSummary" class="pair-note" role="status"></p><div class="pair-view-toolbar"><label class="pair-grid-search">View<select id="pairView"><option value="sub-overlay" selected>Stroke + sub centerline</option><option value="icon">Full stroke</option><option value="overlay">Stroke + centerline</option><option value="centerline">Centerline only</option></select></label><label class="pair-grid-search">Display stroke width<select id="pairStrokeWidth"><option value="4" selected>4px · original stroke</option></select></label><label class="pair-grid-search">Find a combined icon<input id="pairGridSearch" type="search" placeholder="Search concepts or component names"></label><label class="pair-grid-search">Sub readiness<select id="pairReadiness"><option value="">All combined icons</option><option value="pass">Drawn sub icons</option><option value="text">Text sub</option></select></label><label class="pair-grid-search">Icons per page<select id="pairPageSize"><option value="24">24</option><option value="48">48</option><option value="96">96</option></select></label></div>${pageControls('Top')}<div id="pairResultsGrid" class="pair-results-grid"></div>${pageControls('Bottom')}<p id="pairGridStatus" role="status"></p></section>`;
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
    const visible=rows.filter(r=>previews[r.id]&&(!$('pairReadiness').value || ($('pairReadiness').value==='text')===isText(r)) && [r.concept,r.id,...r.mains.map(m=>m.icon),...r.subs.map(m=>m.icon)].join(' ').toLowerCase().includes(q));
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
    $('pairResultsGrid').replaceChildren();const shown=[];
    for(const r of visible.slice(start,start+gridPageSize)){
      const card=document.createElement('article');card.className='pair-result-card';
      const image=document.createElement('img');image.alt=r.concept+' — combined icon';image.width=96;image.height=96;image.loading='lazy';
      const preview=previews[r.id];
      if(preview&&centerlineView==='icon'&&displayStroke===4)image.src=preview.url;else if(preview?.result.svg)image.src=imageURL(displaySVG(preview.result.svg));else if(!preview)image.alt='Preview unavailable';
      const title=document.createElement('h3');title.textContent=r.concept;
      const detail=document.createElement('p');detail.textContent=(preview?.result?.canvas||64)+'×'+(preview?.result?.canvas||64)+' · '+labels[r.position]+(r.native_text?' · Native text':'')+' · Approved';
      // Output only: no edit, download or review actions here (edit on Progression › Side, review on Icon review).
      card.append(image,title,detail);$('pairResultsGrid').append(card);if(preview)shown.push({r,image,preview});
    }
    fill(shown);
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
  // Live from production: the finished side combinations, the combined icons approved in Icon review
  // (index.html?family=side_combination64&status=approve), each with its pair's parts for the review buttons and bounds.
  const REVIEWS={approve:'Approved',pending:'Needs fix',claimed:'Being fixed',rejected:'Rejected',ready:'To review','re-generated':'To review'};
  const isText=r=>!!r.native_text;
  let drawings=new Map(),pairsTotal=0;
  async function api(path){const response=await fetch(path,{cache:'no-store'});const data=await response.json().catch(()=>({}));if(!response.ok)throw Error(data.error||'Could not load the side pairs.');return data;}
  const formKey=f=>f&&!f.native_text?(f.model_key||f.family+'/'+f.icon):null;
  // A part as the review buttons and search read it: the picked icon, its current drawing's sha and its stored form.
  function partItem(p){
    if(!p.icon)return p.form?.native_text?{...p.form,native_text:true}:null;
    const [family,icon]=p.icon.split('/');
    return {...(p.form&&formKey(p.form)===p.icon?p.form:{}),icon,family,model_key:p.icon,sha256:p.current_sha};
  }
  function summary(){
    const count=rows.length,box=$('pairRunSummary');
    $('combinationCount').textContent=count;box.replaceChildren();
    box.append(count.toLocaleString()+' approved side combinations, of '+pairsTotal.toLocaleString()+' side pairs · read live from Icon review · ');
    const link=document.createElement('a');link.href='index.html?family=side_combination64';link.textContent='Review in Icon review →';box.append(link);
  }
  // The shown cards' stored drawings, and where the engine places their main and sub (the bounds overlay).
  async function fill(shown){
    try{
      const want=[...new Set(shown.flatMap(({r})=>r.item.parts.map(p=>p.icon)).filter(k=>k&&!drawings.has(k)))];
      for(let i=0;i<want.length;i+=100){const got=await api('/api/combinations/drawings?keys='+encodeURIComponent(want.slice(i,i+100).join(',')));for(const [k,d] of Object.entries(got))drawings.set(k,d);}
    }catch(e){$('pairGridStatus').textContent=e.message;}
    await Promise.all(shown.map(async({r,image,preview})=>{
      try{
        if(!preview.result.svg){const response=await fetch(preview.url);if(!response.ok)throw Error('Preview could not be loaded');preview.result.svg=await response.text();}
        if(!preview.result.placements){const c=CombineSide.pairRequest(r.item,drawings,{size:64});Object.assign(preview.result,{placements:c.result.placements,canvas:c.result.canvas||64});}
        if(!image.isConnected)return;
        if(!(centerlineView==='icon'&&displayStroke===4))image.src=imageURL(displaySVG(preview.result.svg));
        window.SideCombinationPopup.attach(image,r.concept,preview.result);
      }catch(e){image.title=e.message;}
    }));
  }
  async function load(){if(loaded)return;loaded=true;const params=new URLSearchParams(location.search);$('pairGridSearch').value=params.get('q')||'';if(params.get('sub')==='text')$('pairReadiness').value='text';
    try{
      const query=offset=>'/api/combinations?'+new URLSearchParams({kind:'side',size:'64',forms:'1',limit:'500',offset:String(offset)});
      const approvedPage=offset=>'/api/icons?'+new URLSearchParams({family:'side_combination64',status:'approve',limit:'192',offset:String(offset)});
      const [first,firstApproved]=await Promise.all([api(query(0)),api(approvedPage(0))]);
      const pages=[first],rest=[],approvedPages=[firstApproved],more=[];
      for(let o=500;o<first.total;o+=500)rest.push(api(query(o)));
      for(let o=192;o<firstApproved.total;o+=192)more.push(api(approvedPage(o)));
      pages.push(...await Promise.all(rest));approvedPages.push(...await Promise.all(more));
      pairsTotal=first.total||0;
      const approved=new Set(approvedPages.flatMap(p=>p.items.map(i=>i.key)));
      rows=[];previews={};
      for(const item of pages.flatMap(p=>p.items)){
        const m=item.parts.find(p=>p.role==='main'),s=item.parts.find(p=>p.role==='sub');
        if(!item.icon||!m||!s||!approved.has(item.icon.key))continue;
        const main=partItem(m),sub=partItem(s);if(!main||!sub)continue;
        const id=item.reference_id;
        rows.push({id,item,concept:item.concept,position:s.position,native_text:!!sub.native_text,mains:[main],subs:[sub],review:item.icon.review||'ready'});
        previews[id]={url:item.icon.preview_url,result:{canvas:64,filename:id+'.svg'}};
      }
      rows.sort((a,b)=>a.concept.localeCompare(b.concept));
      
      summary();grid();
    }catch(e){loaded=false;$('pairGridStatus').textContent=e.message;}}
  window.addEventListener('show-combinations',load);if(new URLSearchParams(location.search).get('type')==='combination')load();
})();

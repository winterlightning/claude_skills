(()=>{
  'use strict';
  const $=id=>document.getElementById(id), cache=new Map(), tabs=[...document.querySelectorAll('[data-type]')];
  let type='color',rows=[],page=1,request=0;
  const pageSize=50;
  const embedded=document.getElementById('typefaceExperimentData');
  if(embedded){try{const data=JSON.parse(embedded.textContent);if(Array.isArray(data.icons))cache.set('typeface',data.icons);}catch{ /* Server-loaded JSON remains the fallback. */ }}
  const embeddedV2=document.getElementById('typefaceV2ExperimentData');
  if(embeddedV2){try{const data=JSON.parse(embeddedV2.textContent);if(Array.isArray(data.icons))cache.set('typeface-v2',data.icons);}catch{}}
  let typefaceVersion='v1';
  // The typeface tab keeps two collections; v2 is the natural-width uppercase set.
  const collection=()=>type==='typeface'&&typefaceVersion==='v2'?'typeface-v2':type;
  const containerData=document.getElementById('containerExperimentData');
  // The container tab is read live from production (liveContainers), not from the data embedded in the page.
  const imageURL=svg=>'data:image/svg+xml;charset=utf-8,'+encodeURIComponent(svg);
  // Container tab: every part side by side, or only the combined output in a dense grid.
  const combinedOnly=()=>type==='container'&&$('experimentLayout').value==='combined';
  function writeURL(){const p=new URLSearchParams({type});if(combinedOnly())p.set('layout','combined');if(type==='typeface'&&typefaceVersion==='v2')p.set('version','v2');if($('experimentSearch').value)p.set('q',$('experimentSearch').value);if(page>1)p.set('page',page);history.replaceState(null,'','experiment.html?'+p);}
  function render(){
    const q=$('experimentSearch').value.trim().toLowerCase();
    const filtered=rows.filter(i=>!q||i.name.toLowerCase().replaceAll('-',' ').includes(q)||i.name.toLowerCase().includes(q)||String(i.icon_id||'').includes(q)||String(i.number)===q.replace(/^#/,''));
    const perPage=type==='typeface'?Math.max(1,filtered.length):pageSize;
    const pages=Math.max(1,Math.ceil(filtered.length/perPage));page=Math.max(1,Math.min(page,pages));
    const start=(page-1)*perPage,visible=filtered.slice(start,start+perPage),grid=$('experimentGrid');grid.replaceChildren();grid.classList.toggle('combined-grid',combinedOnly());
    for(const icon of visible){
      const card=document.createElement('article');card.className='experiment-card';card.style.setProperty('--icon-size',($('experimentSize').value==='native'?icon.canvas_size:$('experimentSize').value)+'px');
      const head=document.createElement('header'),number=document.createElement('span'),name=document.createElement('h2');number.className='sample-number';number.textContent=String(icon.number).padStart(3,'0');name.textContent=icon.name.replaceAll('-',' ');head.append(number,name);card.append(head);
      const art=document.createElement('div');art.className='experiment-art';
      const comparisons=type==='typeface'
        ? [[icon.original,'Original',icon.original_preview],[icon.outline,'Iconized',icon.outline_preview],[icon.result,'Centerline',null]]
        : combinedOnly()?[[icon.result,'',icon.result_url]]
        : type==='container'?[[icon.outline,'Container',icon.outline_url],[icon.content,'Content',icon.content_url],[icon.result,'Combination',icon.result_url]]
        : [[icon.outline,'Original',null],[icon.result,type==='color'?'Color':type==='duotone'?'Duotone':type==='animation'?'Animated':'Fill',null]];
      art.classList.toggle('typeface-comparison',type==='typeface'||(type==='container'&&!combinedOnly()));
      for(const [svg,label,preview] of comparisons){
        const figure=document.createElement('figure'),box=document.createElement('div'),caption=document.createElement('figcaption');box.className='icon-image';
        if(svg){const img=document.createElement('img');img.src=preview||imageURL(svg);img.alt=icon.name.replaceAll('-',' ')+' — '+label;img.loading='lazy';box.append(img);}
        else{const empty=document.createElement('span');empty.className='missing-original';empty.textContent=type==='container'?'Typeface text':'No supplied original';box.append(empty);}
        caption.textContent=label;figure.append(box,caption);art.append(figure);
      }
      card.append(art);
      if((type==='container'&&!combinedOnly())||type==='animation'){const note=document.createElement('p');note.className='pair-note';note.textContent=type==='animation'?icon.motion:icon.status_label;card.append(note);}
      const foot=document.createElement('footer'),detail=document.createElement('span'),download=document.createElement('a');detail.textContent=icon.canvas_size+' px'+(type==='fill'&&!icon.fill_applicable?' · Kept as strokes':'')+(type==='animation'?' · '+icon.source:'');download.textContent=type==='typeface'?'Download centerline':'Download SVG';download.href=icon.result_url||imageURL(icon.result);download.download=icon.name+'-'+type+'.svg';foot.append(detail,download);if(!combinedOnly())card.append(foot);grid.append(card);
    }
    $('experimentStatus').textContent=filtered.length?`${start+1}–${start+visible.length} of ${filtered.length} ${type} samples`:'0 samples';$('experimentEmpty').hidden=filtered.length>0;
    const select=$('samplePage');select.replaceChildren();for(let n=1;n<=pages;n++){const o=document.createElement('option');o.value=n;o.textContent=n;select.append(o);}select.value=page;$('pageTotal').textContent='of '+pages;$('previousSamples').disabled=page<=1;$('nextSamples').disabled=page>=pages;writeURL();
  }
  // Live from production: the container combinations approved in Icon review, each with its container and symbol.
  async function liveContainers(){
    const api=async path=>{const r=await fetch(path,{cache:'no-store'});const d=await r.json().catch(()=>({}));if(!r.ok)throw Error(d.error||'Could not load');return d;};
    const approvedPage=o=>'/api/icons?'+new URLSearchParams({family:'container_combination64',status:'approve',limit:'192',offset:String(o)});
    const pairPage=o=>'/api/combinations?'+new URLSearchParams({kind:'container',size:'64',limit:'500',offset:String(o)});
    const [firstApproved,firstPairs]=await Promise.all([api(approvedPage(0)),api(pairPage(0))]);
    const approvedPages=[firstApproved],pairPages=[firstPairs],more=[],rest=[];
    for(let o=192;o<firstApproved.total;o+=192)more.push(api(approvedPage(o)));
    for(let o=500;o<firstPairs.total;o+=500)rest.push(api(pairPage(o)));
    approvedPages.push(...await Promise.all(more));pairPages.push(...await Promise.all(rest));
    const approved=new Set(approvedPages.flatMap(p=>p.items.map(i=>i.key)));
    const url=(key,sha)=>'/api/icon-artwork/svg?'+new URLSearchParams({icon:key,...(sha?{v:sha.slice(0,12)}:{})});
    const name=key=>key?key.split('/').pop():'none';
    return pairPages.flatMap(p=>p.items).filter(i=>i.icon&&approved.has(i.icon.key)).sort((a,b)=>a.concept.localeCompare(b.concept)).map((i,n)=>{
      const c=i.parts.find(p=>p.role==='container')||{},s=i.parts.find(p=>p.role==='symbol')||{};
      return {number:n+1,name:i.concept,canvas_size:64,outline:!!c.icon,content:!!s.icon,result:true,
              outline_url:c.icon?url(c.icon,c.current_sha):null,content_url:s.icon?url(s.icon,s.current_sha):null,result_url:i.icon.preview_url,
              status_label:'Approved · '+name(c.icon)+' + '+name(s.icon)};
    });
  }
  async function selectType(next,{restore=false}={}){
    const token=++request;type=next;rows=[];
    const combining=type==='combination';
    $('containerRules').hidden=type!=='container';
    $('combinationExperiment').hidden=!combining;
    document.querySelector('.experiment-controls').hidden=combining;
    $('experimentGrid').hidden=combining;
    if(combining){
      for(const tab of tabs){if(tab.dataset.type===type)tab.setAttribute('aria-current','page');else tab.removeAttribute('aria-current');}
      $('typefaceLegend').hidden=true;$('reviewCollection').hidden=true;$('experimentEmpty').hidden=true;
      document.querySelector('.experiment-pagination').hidden=true;
      if(!new URLSearchParams(location.search).has('type')||new URLSearchParams(location.search).get('type')!=='combination')history.replaceState(null,'','experiment.html?type=combination');
      window.dispatchEvent(new Event('show-combinations'));return;
    }
    if(!restore){page=1;$('experimentSearch').value='';}
    for(const tab of tabs){if(tab.dataset.type===type)tab.setAttribute('aria-current','page');else tab.removeAttribute('aria-current');}
    $('experimentGrid').setAttribute('aria-label',type==='container'?'Container combinations':type==='typeface'?'Typeface and centerlines':type==='color'?'Color icons':type==='duotone'?'Duotone icons':type==='animation'?'Animated icons':'Fill icons');
    $('typefaceLegend').hidden=type!=='typeface';$('typefaceVersionLabel').hidden=type!=='typeface';
    $('typefaceLegend').textContent=typefaceVersion==='v2'
      ?'Version 2: uppercase letters and digits use the supplied Letters/new SVG paths and native canvases without resizing or curve repair. Text combine uppercases lowercase input and borrows keyboard symbols from v1.'
      :'Version 1: original reference, iconized lettering, and centerline for every character. Original and iconized previews trim empty margins and preserve proportions for comparison. Red traces the iconized letter\u2019s exact centerline. Uppercase letters have no supplied originals.';
    $('experimentGrid').classList.toggle('typeface-grid',type==='typeface'||type==='container');$('experimentLayoutLabel').hidden=type!=='container';
    document.querySelector('.experiment-pagination').hidden=type==='typeface';$('experimentGrid').replaceChildren();$('experimentEmpty').hidden=true;$('experimentStatus').textContent='Loading samples…';$('previousSamples').disabled=true;$('nextSamples').disabled=true;$('samplePage').disabled=true;$('experimentSearch').disabled=true;$('experimentSize').disabled=true;
    const review=$('reviewCollection');review.hidden=true;
    review.textContent=type==='typeface'?'Text combine ↗':'Review this collection ↗';
    if(type==='typeface'){review.href='text-combine.html'+(typefaceVersion==='v2'?'?version=v2':'');review.hidden=false;}
    else if(type==='fill'){review.href='fill-review-500.html';review.hidden=false;}
    else if(type==='color'&&['localhost','127.0.0.1'].includes(location.hostname)){review.href=`http://${location.hostname}:8010/`;review.hidden=false;}
    try{
      const key=collection();
      if(!cache.has(key)&&key==='container')cache.set(key,await liveContainers());
      if(!cache.has(key)){const response=await fetch('experiment-'+key+'.json');if(!response.ok)throw Error();const data=await response.json();if(!Array.isArray(data.icons))throw Error();cache.set(key,data.icons);}
      if(token!==request)return;rows=cache.get(key);$(type+'Count').textContent=rows.length;render();
    }catch{if(token!==request)return;rows=[];$('experimentStatus').textContent='This collection could not be loaded. Select its tab to try again.';}
    finally{if(token===request){$('samplePage').disabled=!rows.length;$('experimentSearch').disabled=false;$('experimentSize').disabled=false;}}
  }
  for(const tab of tabs)tab.addEventListener('click',event=>{if(event.metaKey||event.ctrlKey||event.shiftKey||event.altKey)return;event.preventDefault();selectType(tab.dataset.type);});
  $('experimentSearch').addEventListener('input',()=>{page=1;render();});$('experimentSize').addEventListener('change',render);
  $('experimentLayout').addEventListener('change',()=>{page=1;render();});
  $('typefaceVersion').addEventListener('change',()=>{typefaceVersion=$('typefaceVersion').value==='v2'?'v2':'v1';if(type==='typeface'){page=1;selectType('typeface',{restore:true});}});
  function go(n){page=n;render();window.scrollTo({top:0,behavior:'smooth'});}
  $('previousSamples').onclick=()=>go(page-1);$('nextSamples').onclick=()=>go(page+1);$('samplePage').onchange=()=>go(Number($('samplePage').value));
  function restore(){const p=new URLSearchParams(location.search);page=Math.max(1,Number.parseInt(p.get('page'),10)||1);$('experimentSearch').value=p.get('q')||'';typefaceVersion=p.get('version')==='v2'?'v2':'v1';$('typefaceVersion').value=typefaceVersion;$('experimentLayout').value=p.get('layout')==='combined'?'combined':'parts';selectType(['fill','duotone','typeface','combination','container','animation'].includes(p.get('type'))?p.get('type'):'color',{restore:true});}
  window.addEventListener('popstate',restore);restore();
  // The approved container and side combinations, counted live (their tabs list them from Icon review).
  for(const [kind,family] of [['container','container_combination64'],['combination','side_combination64']])fetch('/api/icons?family='+family+'&status=approve&limit=24',{cache:'no-store'}).then(r=>r.ok?r.json():null).then(d=>{if(d&&!$(kind+'Count').textContent)$(kind+'Count').textContent=d.total;}).catch(()=>{});
  fetch('experiments.json',{cache:'no-store'}).then(r=>{if(!r.ok)throw Error();return r.json();}).then(data=>{for(const kind of ['color','duotone','fill','typeface','animation']){const key=kind==='typeface'&&typefaceVersion==='v2'?'typeface-v2':kind;if(key in data&&!(kind==='combination'&&$(kind+'Count').textContent))$(kind+'Count').textContent=data[key];}}).catch(()=>{});
})();

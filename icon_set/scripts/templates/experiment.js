(()=>{
  'use strict';
  const $=id=>document.getElementById(id), cache=new Map(), tabs=[...document.querySelectorAll('[data-type]')];
  let type='color',rows=[],page=1,request=0;
  const pageSize=50;
  const embedded=document.getElementById('typefaceExperimentData');
  if(embedded){try{const data=JSON.parse(embedded.textContent);if(Array.isArray(data.icons))cache.set('typeface',data.icons);}catch{ /* Server-loaded JSON remains the fallback. */ }}
  const containerData=document.getElementById('containerExperimentData');
  if(containerData){try{cache.set('container',JSON.parse(containerData.textContent).icons);}catch{}}
  const imageURL=svg=>'data:image/svg+xml;charset=utf-8,'+encodeURIComponent(svg);
  function writeURL(){const p=new URLSearchParams({type});if($('experimentSearch').value)p.set('q',$('experimentSearch').value);if(page>1)p.set('page',page);history.replaceState(null,'','experiment.html?'+p);}
  function render(){
    const q=$('experimentSearch').value.trim().toLowerCase();
    const filtered=rows.filter(i=>!q||i.name.toLowerCase().replaceAll('-',' ').includes(q)||i.name.toLowerCase().includes(q)||String(i.icon_id||'').includes(q)||String(i.number)===q.replace(/^#/,''));
    const perPage=type==='typeface'?Math.max(1,filtered.length):pageSize;
    const pages=Math.max(1,Math.ceil(filtered.length/perPage));page=Math.max(1,Math.min(page,pages));
    const start=(page-1)*perPage,visible=filtered.slice(start,start+perPage),grid=$('experimentGrid');grid.replaceChildren();
    for(const icon of visible){
      const card=document.createElement('article');card.className='experiment-card';card.style.setProperty('--icon-size',($('experimentSize').value==='native'?icon.canvas_size:$('experimentSize').value)+'px');
      const head=document.createElement('header'),number=document.createElement('span'),name=document.createElement('h2');number.className='sample-number';number.textContent=String(icon.number).padStart(3,'0');name.textContent=icon.name.replaceAll('-',' ');head.append(number,name);card.append(head);
      const art=document.createElement('div');art.className='experiment-art';
      const comparisons=type==='typeface'
        ? [[icon.original,'Original',icon.original_preview],[icon.outline,'Iconized',icon.outline_preview],[icon.result,'Centerline',null]]
        : type==='container'?[[icon.outline,'Container',null],[icon.content,'Content',null],[icon.result,'Combination',null]]
        : [[icon.outline,'Original',null],[icon.result,type==='color'?'Color':type==='duotone'?'Duotone':type==='animation'?'Animated':'Fill',null]];
      art.classList.toggle('typeface-comparison',type==='typeface'||type==='container');
      for(const [svg,label,preview] of comparisons){
        const figure=document.createElement('figure'),box=document.createElement('div'),caption=document.createElement('figcaption');box.className='icon-image';
        if(svg){const img=document.createElement('img');img.src=preview||imageURL(svg);img.alt=icon.name.replaceAll('-',' ')+' — '+label;img.loading='lazy';box.append(img);}
        else{const empty=document.createElement('span');empty.className='missing-original';empty.textContent='No supplied original';box.append(empty);}
        caption.textContent=label;figure.append(box,caption);art.append(figure);
      }
      card.append(art);
      if(type==='container'||type==='animation'){const note=document.createElement('p');note.className='pair-note';note.textContent=type==='animation'?icon.motion:icon.status_label;card.append(note);}
      const foot=document.createElement('footer'),detail=document.createElement('span'),download=document.createElement('a');detail.textContent=icon.canvas_size+' px'+(type==='fill'&&!icon.fill_applicable?' · Kept as strokes':'')+(type==='animation'?' · '+icon.source:'');download.textContent=type==='typeface'?'Download centerline':'Download SVG';download.href=imageURL(icon.result);download.download=icon.name+'-'+type+'.svg';foot.append(detail,download);card.append(foot);grid.append(card);
    }
    $('experimentStatus').textContent=filtered.length?`${start+1}–${start+visible.length} of ${filtered.length} ${type} samples`:'0 samples';$('experimentEmpty').hidden=filtered.length>0;
    const select=$('samplePage');select.replaceChildren();for(let n=1;n<=pages;n++){const o=document.createElement('option');o.value=n;o.textContent=n;select.append(o);}select.value=page;$('pageTotal').textContent='of '+pages;$('previousSamples').disabled=page<=1;$('nextSamples').disabled=page>=pages;writeURL();
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
      history.replaceState(null,'','experiment.html?type=combination');
      window.dispatchEvent(new Event('show-combinations'));return;
    }
    if(!restore){page=1;$('experimentSearch').value='';}
    for(const tab of tabs){if(tab.dataset.type===type)tab.setAttribute('aria-current','page');else tab.removeAttribute('aria-current');}
    $('experimentGrid').setAttribute('aria-label',type==='container'?'Container combinations':type==='typeface'?'Typeface and centerlines':type==='color'?'Color icons':type==='duotone'?'Duotone icons':type==='animation'?'Animated icons':'Fill icons');
    $('typefaceLegend').hidden=type!=='typeface';
    $('experimentGrid').classList.toggle('typeface-grid',type==='typeface'||type==='container');
    document.querySelector('.experiment-pagination').hidden=type==='typeface';$('experimentGrid').replaceChildren();$('experimentEmpty').hidden=true;$('experimentStatus').textContent='Loading samples…';$('previousSamples').disabled=true;$('nextSamples').disabled=true;$('samplePage').disabled=true;$('experimentSearch').disabled=true;$('experimentSize').disabled=true;
    const review=$('reviewCollection');review.hidden=true;
    review.textContent=type==='typeface'?'Text combine ↗':'Review this collection ↗';
    if(type==='typeface'){review.href='text-combine.html';review.hidden=false;}
    else if(type==='fill'){review.href='fill-review-500.html';review.hidden=false;}
    else if(type==='color'&&['localhost','127.0.0.1'].includes(location.hostname)){review.href=`http://${location.hostname}:8010/`;review.hidden=false;}
    try{
      if(!cache.has(type)){const response=await fetch('experiment-'+type+'.json');if(!response.ok)throw Error();const data=await response.json();if(!Array.isArray(data.icons))throw Error();cache.set(next,data.icons);}
      if(token!==request)return;rows=cache.get(type);$(type+'Count').textContent=rows.length;render();
    }catch{if(token!==request)return;rows=[];$('experimentStatus').textContent='This collection could not be loaded. Select its tab to try again.';}
    finally{if(token===request){$('samplePage').disabled=!rows.length;$('experimentSearch').disabled=false;$('experimentSize').disabled=false;}}
  }
  for(const tab of tabs)tab.addEventListener('click',event=>{if(event.metaKey||event.ctrlKey||event.shiftKey||event.altKey)return;event.preventDefault();selectType(tab.dataset.type);});
  $('experimentSearch').addEventListener('input',()=>{page=1;render();});$('experimentSize').addEventListener('change',render);
  function go(n){page=n;render();window.scrollTo({top:0,behavior:'smooth'});}
  $('previousSamples').onclick=()=>go(page-1);$('nextSamples').onclick=()=>go(page+1);$('samplePage').onchange=()=>go(Number($('samplePage').value));
  function restore(){const p=new URLSearchParams(location.search);page=Math.max(1,Number.parseInt(p.get('page'),10)||1);$('experimentSearch').value=p.get('q')||'';selectType(['fill','duotone','typeface','combination','container','animation'].includes(p.get('type'))?p.get('type'):'color',{restore:true});}
  window.addEventListener('popstate',restore);restore();
  if(cache.has('container'))$('containerCount').textContent=cache.get('container').length;
  fetch('experiments.json').then(r=>{if(!r.ok)throw Error();return r.json();}).then(data=>{for(const kind of ['color','duotone','fill','typeface','container','animation'])if(kind in data)$(kind+'Count').textContent=data[kind];}).catch(()=>{});
})();

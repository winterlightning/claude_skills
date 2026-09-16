(()=>{
  'use strict';
  const $=id=>document.getElementById(id), cache=new Map(), tabs=[...document.querySelectorAll('[data-type]')];
  let type='color',rows=[],page=1,request=0;
  const pageSize=50;
  const imageURL=svg=>'data:image/svg+xml;charset=utf-8,'+encodeURIComponent(svg);
  function writeURL(){const p=new URLSearchParams({type});if($('experimentSearch').value)p.set('q',$('experimentSearch').value);if(page>1)p.set('page',page);history.replaceState(null,'','experiment.html?'+p);}
  function render(){
    const q=$('experimentSearch').value.trim().toLowerCase();
    const filtered=rows.filter(i=>!q||i.name.replaceAll('-',' ').includes(q)||i.name.includes(q)||String(i.number)===q.replace(/^#/,''));
    const pages=Math.max(1,Math.ceil(filtered.length/pageSize));page=Math.max(1,Math.min(page,pages));
    const start=(page-1)*pageSize,visible=filtered.slice(start,start+pageSize),grid=$('experimentGrid');grid.replaceChildren();
    for(const icon of visible){
      const card=document.createElement('article');card.className='experiment-card';card.style.setProperty('--icon-size',($('experimentSize').value==='native'?icon.canvas_size:$('experimentSize').value)+'px');
      const head=document.createElement('header'),number=document.createElement('span'),name=document.createElement('h2');number.className='sample-number';number.textContent=String(icon.number).padStart(3,'0');name.textContent=icon.name.replaceAll('-',' ');head.append(number,name);card.append(head);
      const art=document.createElement('div');art.className='experiment-art';
      for(const [svg,label] of [[icon.outline,'Original'],[icon.result,type==='color'?'Color':'Fill']]){const figure=document.createElement('figure'),box=document.createElement('div'),img=document.createElement('img'),caption=document.createElement('figcaption');box.className='icon-image';img.src=imageURL(svg);img.alt=icon.name.replaceAll('-',' ')+' — '+label;img.loading='lazy';box.append(img);caption.textContent=label;figure.append(box,caption);art.append(figure);}card.append(art);
      const foot=document.createElement('footer'),detail=document.createElement('span'),download=document.createElement('a');detail.textContent=icon.canvas_size+' px'+(type==='fill'&&!icon.fill_applicable?' · Kept as strokes':'');download.textContent='Download SVG';download.href=imageURL(icon.result);download.download=icon.name+'-'+type+'.svg';foot.append(detail,download);card.append(foot);grid.append(card);
    }
    $('experimentStatus').textContent=filtered.length?`${start+1}–${start+visible.length} of ${filtered.length} ${type} samples`:'0 samples';$('experimentEmpty').hidden=filtered.length>0;
    const select=$('samplePage');select.replaceChildren();for(let n=1;n<=pages;n++){const o=document.createElement('option');o.value=n;o.textContent=n;select.append(o);}select.value=page;$('pageTotal').textContent='of '+pages;$('previousSamples').disabled=page<=1;$('nextSamples').disabled=page>=pages;writeURL();
  }
  async function selectType(next,{restore=false}={}){
    const token=++request;type=next;rows=[];
    if(!restore){page=1;$('experimentSearch').value='';}
    for(const tab of tabs){if(tab.dataset.type===type)tab.setAttribute('aria-current','page');else tab.removeAttribute('aria-current');}
    $('experimentGrid').setAttribute('aria-label',type==='color'?'Color icons':'Fill icons');$('experimentGrid').replaceChildren();$('experimentEmpty').hidden=true;$('experimentStatus').textContent='Loading samples…';$('previousSamples').disabled=true;$('nextSamples').disabled=true;$('samplePage').disabled=true;$('experimentSearch').disabled=true;$('experimentSize').disabled=true;
    const review=$('reviewCollection');review.hidden=true;
    if(type==='fill'){review.href='fill-review-500.html';review.hidden=false;}
    else if(['localhost','127.0.0.1'].includes(location.hostname)){review.href=`http://${location.hostname}:8010/`;review.hidden=false;}
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
  function restore(){const p=new URLSearchParams(location.search);page=Math.max(1,Number.parseInt(p.get('page'),10)||1);$('experimentSearch').value=p.get('q')||'';selectType(p.get('type')==='fill'?'fill':'color',{restore:true});}
  window.addEventListener('popstate',restore);restore();
  fetch('experiments.json').then(r=>{if(!r.ok)throw Error();return r.json();}).then(data=>{for(const kind of ['color','fill'])$(kind+'Count').textContent=data[kind];}).catch(()=>{});
})();

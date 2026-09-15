function approvedIcons(catalog, reviews) {
  return catalog.icons.filter(icon => reviews[icon.key] === 'approve');
}
(async()=>{
  const $=id=>document.getElementById(id);
  const status=$('approvedStatus'),grid=$('approvedGrid'),pagination=$('approvedPagination');
  let icons=[],page=1,pageSize=48;
  function readURL(){const params=new URLSearchParams(window.location.search);const requested=Number(params.get('page'));page=Number.isSafeInteger(requested)&&requested>0?requested:1;const size=Number(params.get('page_size'));pageSize=[24,48,96].includes(size)?size:48;}
  function writeURL(replace=false){const url=new URL(window.location.href);url.searchParams.set('page',page);url.searchParams.set('page_size',pageSize);if(url.href!==window.location.href)window.history[replace?'replaceState':'pushState'](null,'',url);}
  function render(){
    const pages=Math.max(1,Math.ceil(icons.length/pageSize));page=Math.min(Math.max(1,page),pages);
    const start=(page-1)*pageSize,visible=icons.slice(start,start+pageSize);
    status.textContent=icons.length?`Showing ${start+1}–${start+visible.length} of ${icons.length.toLocaleString()} approved icons`:'No approved icons yet. Approved icons will appear here after review.';
    pagination.hidden=!icons.length;$('approvedPageSize').value=String(pageSize);$('approvedPrevious').disabled=page===1;$('approvedNext').disabled=page===pages;
    $('approvedPage').replaceChildren();for(let n=1;n<=pages;n++){const option=document.createElement('option');option.value=String(n);option.textContent=String(n);$('approvedPage').append(option);}
    $('approvedPage').value=String(page);$('approvedPage').disabled=pages===1;$('approvedPageCount').textContent='of '+pages;
    const fragment=document.createDocumentFragment();
    for(const icon of visible){
      const card=document.createElement('article');card.className='approved-card';
      const preview=document.createElement('div');preview.className='approved-preview';
      const img=document.createElement('img');img.src=icon.preview_url;img.alt=icon.name;img.loading='lazy';img.width=64;img.height=64;preview.append(img);
      const name=document.createElement('h2');name.textContent=icon.name;
      const download=document.createElement('a');download.className='site-button approved-download';download.href=icon.preview_url;download.download=icon.icon_id+'.svg';download.title='Download SVG';download.setAttribute('aria-label','Download '+icon.name+' SVG');
      const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');for(const [key,value] of Object.entries({viewBox:'0 0 24 24',width:'20',height:'20',fill:'none',stroke:'currentColor','stroke-width':'1.8','stroke-linecap':'round','stroke-linejoin':'round','aria-hidden':'true'}))svg.setAttribute(key,value);
      const path=document.createElementNS('http://www.w3.org/2000/svg','path');path.setAttribute('d','M12 3v12m-5-5 5 5 5-5M4 16v5h16v-5');svg.append(path);download.append(svg);
      card.append(preview,name,download);fragment.append(card);
    }
    grid.replaceChildren(fragment);
  }
  function changePage(next){page=next;render();writeURL();grid.scrollIntoView({block:'start',behavior:'smooth'});}
  $('approvedPrevious').onclick=()=>changePage(page-1);$('approvedNext').onclick=()=>changePage(page+1);$('approvedPage').onchange=()=>changePage(Number($('approvedPage').value));
  $('approvedPageSize').onchange=()=>{pageSize=Number($('approvedPageSize').value);changePage(1);};
  try {
    const responses=await Promise.all([fetch('icons.json',{cache:'no-store'}),fetch('/api/reviews',{cache:'no-store'})]);
    if(responses.some(response=>!response.ok))throw Error('Could not load the approved collection. Please reload to try again.');
    const [catalog,reviews]=await Promise.all(responses.map(response=>response.json()));icons=approvedIcons(catalog,reviews);readURL();render();writeURL(true);
    window.addEventListener('popstate',()=>{readURL();render();writeURL(true);});
  }catch(error){grid.replaceChildren();pagination.hidden=true;status.textContent=error.message||'Could not load the approved collection. Please reload to try again.';}
})();

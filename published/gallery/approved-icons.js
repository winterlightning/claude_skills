function approvedIcons(catalog, reviews) {
  return catalog.icons.filter(icon => reviews[icon.key] === 'approve' && icon.reference_fidelity?.status !== 'superseded');
}
function approvedCategory(value) {
  const category=(value||'').trim();
  return !category||/^_?uncategorized(?:_\d+)?$/i.test(category)?'Uncategorized':category;
}
(async()=>{
  const $=id=>document.getElementById(id);
  const status=$('approvedStatus'),grid=$('approvedGrid'),pagination=$('approvedPagination');
  let totalApproved=0,page=1,pageSize=48,query='',category='',family='';
  function storedFamily(){try{return localStorage.getItem('approvedFamily')||'';}catch{return '';}}
  function storeFamily(){try{if(family)localStorage.setItem('approvedFamily',family);else localStorage.removeItem('approvedFamily');}catch{}}
  function readURL(){const params=new URLSearchParams(window.location.search);const requested=Number(params.get('page'));page=Number.isSafeInteger(requested)&&requested>0?requested:1;const size=Number(params.get('page_size'));pageSize=[24,48,96].includes(size)?size:48;query=params.get('q')||'';family=params.has('family')?params.get('family'):storedFamily();if(![...$('approvedFamily').options].some(option=>option.value===family))family='';$('approvedFamily').value=family;category=params.get('category')||'';if(category)category=approvedCategory(category);if(category!=='Uncategorized'&&!allCategories.has(category))category='';$('approvedSearch').value=query;$('approvedCategory').value=category;}
  function writeURL(replace=false){const url=new URL(window.location.href);url.searchParams.set('page',page);url.searchParams.set('page_size',pageSize);for(const [key,value] of [['q',query],['family',family],['category',category]]){if(value)url.searchParams.set(key,value);else url.searchParams.delete(key);}if(url.href!==window.location.href)window.history[replace?'replaceState':'pushState'](null,'',url);}
  // The categories shown in the list (every approved icon's, grouped as approvedCategory groups them), from the
  // first answer; their counts follow the search and family (the server counts ignore the category filter).
  let allCategories=new Set(['Uncategorized']),listed={items:[],total:0,categories:{}},request=0,loaded='';
  const grouped=counts=>{const out=new Map();for(const [value,n] of Object.entries(counts||{}))out.set(approvedCategory(value),(out.get(approvedCategory(value))||0)+n);return out;};
  function renderCategories(){
    const counts=grouped(listed.categories),total=[...counts.values()].reduce((a,b)=>a+b,0);
    const term=$('approvedCategorySearch').value.trim().toLowerCase(),fragment=document.createDocumentFragment();
    for(const value of ['',...allCategories].sort()){
      if(value&&term&&!value.toLowerCase().includes(term))continue;
      const count=value?(counts.get(value)||0):total,button=document.createElement('button');button.type='button';button.className='category-item';button.setAttribute('aria-pressed',String(category===value));button.setAttribute('aria-label',(value||'All categories')+', '+count+' icons');
      const label=document.createElement('span');label.textContent=value||'All categories';const badge=document.createElement('span');badge.className='category-count';badge.textContent=count.toLocaleString();button.append(label,badge);
      button.onclick=()=>{category=value;$('approvedCategory').value=value;page=1;render();writeURL();};fragment.append(button);
    }
    $('approvedCategoryList').replaceChildren(fragment);
  }
  $('approvedCategorySearch').oninput=()=>renderCategories();
  function listQuery(){const q=new URLSearchParams({status:'approve',family,limit:String(pageSize),offset:String((page-1)*pageSize)});if(query.trim())q.set('terms',query.trim());if(category==='Uncategorized')q.set('category_group','uncategorized');else if(category)q.set('category',category);return q.toString();}
  async function load(){
    const asked=listQuery(),mine=++request;
    try{const response=await fetch('../api/icons?'+asked,{cache:'no-store'});if(!response.ok)throw Error();const data=await response.json();if(mine!==request)return;
      listed={...data,items:data.items.filter(icon=>icon.reference_fidelity?.status!=='superseded')};page=Math.floor((data.offset||0)/pageSize)+1;loaded=listQuery();}
    catch{if(mine!==request)return;listed={items:[],total:0,categories:{},failed:true};loaded=asked;}
    render();
  }
  function render(){
    if(listQuery()!==loaded){loaded=listQuery();load();}
    renderCategories();
    const pages=Math.max(1,Math.ceil(listed.total/pageSize)),start=listed.offset||0,visible=listed.items;
    status.textContent=listed.failed?'Could not load the approved collection. Please reload to try again.':listed.total?`Showing ${start+1}–${start+visible.length} of ${listed.total.toLocaleString()} approved icons`:totalApproved?'No icons match your search, family and category. Try another search or clear the filters.':'No approved icons yet. Approved icons will appear here after review.';
    pagination.hidden=!listed.total;$('approvedClear').disabled=!query&&!category&&!family;$('approvedPageSize').value=String(pageSize);$('approvedPrevious').disabled=page===1;$('approvedNext').disabled=page>=pages;
    $('approvedPage').replaceChildren();for(let n=1;n<=pages;n++){const option=document.createElement('option');option.value=String(n);option.textContent=String(n);$('approvedPage').append(option);}
    $('approvedPage').value=String(page);$('approvedPage').disabled=pages===1;$('approvedPageCount').textContent='of '+pages;
    const fragment=document.createDocumentFragment();
    for(const icon of visible){
      const card=document.createElement('article');card.className='approved-card';
      const preview=document.createElement('div');preview.className='approved-preview';
      const img=document.createElement('img');img.src=icon.preview_url;img.alt=icon.name;img.loading='lazy';img.width=32;img.height=32;preview.append(img);
      const name=document.createElement('h2');name.textContent=icon.name;name.title=icon.name;
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
  $('approvedSearch').oninput=()=>{query=$('approvedSearch').value;page=1;render();writeURL(true);};
  $('approvedFamily').onchange=()=>{family=$('approvedFamily').value;storeFamily();page=1;render();writeURL();};
  $('approvedCategory').onchange=()=>{category=$('approvedCategory').value;page=1;render();writeURL();};
  $('approvedClear').onclick=()=>{query='';category='';family='';storeFamily();$('approvedFamily').value='';$('approvedSearch').value='';$('approvedCategory').value='';page=1;render();writeURL();};
  try {
    const response=await fetch('../api/icons?'+new URLSearchParams({status:'approve',family:'',limit:'24'}),{cache:'no-store'});
    if(!response.ok)throw Error('Could not load the approved collection. Please reload to try again.');
    const first=await response.json();totalApproved=first.total;
    allCategories=new Set(['Uncategorized',...Object.keys(first.categories||{}).map(approvedCategory)]);
    for(const value of [...allCategories].sort()){const option=document.createElement('option');option.value=value;option.textContent=value;$('approvedCategory').append(option);}
    for(const option of $('approvedFamily').options)if(option.value)option.textContent=option.textContent.replace(/ \(.*$/,'')+' ('+((first.families||{})[option.value]||0).toLocaleString()+')';
    $('approvedSearch').disabled=false;$('approvedFamily').disabled=false;$('approvedCategory').disabled=false;readURL();render();writeURL(true);
    window.addEventListener('popstate',()=>{readURL();render();writeURL(true);});
  }catch(error){grid.replaceChildren();pagination.hidden=true;status.textContent=error.message||'Could not load the approved collection. Please reload to try again.';}
})();

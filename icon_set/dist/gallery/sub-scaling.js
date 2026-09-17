(()=>{'use strict';
const $=id=>document.getElementById(id),esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const fmt=n=>Number(n.toFixed(2)).toString();let rows=[],shapes=[],page=0;const pageSize=12;
function guide(shape,size){
 const b=size===48?shape.solo_bounds:shape.sub_bounds,[l,t,r,d]=b,w=r-l,h=d-t;
 return `<rect x="0" y="0" width="${size}" height="${size}" fill="none" stroke="#9baba5" stroke-width=".2"/>`+(shape.radial?
 `<circle cx="${size/2}" cy="${size/2}" r="${w/2}" fill="none" stroke="#2483cd" stroke-width=".35"/><circle cx="${size/2}" cy="${size/2}" r="${w/2-2}" fill="none" stroke="#2483cd" stroke-width=".25" stroke-dasharray="1 1"/>`:
 `<rect x="${l}" y="${t}" width="${w}" height="${h}" fill="none" stroke="#2483cd" stroke-width=".35"/><rect x="${l+2}" y="${t+2}" width="${w-4}" height="${h-4}" fill="none" stroke="#2483cd" stroke-width=".25" stroke-dasharray="1 1"/>`);
}
function art(text,size,uid,shape){
 const xml=new DOMParser().parseFromString(text,'image/svg+xml'),svg=xml.documentElement;
 const ns='http://www.w3.org/2000/svg';svg.setAttribute('width',size*Number($('zoom').value));svg.setAttribute('height',size*Number($('zoom').value));svg.setAttribute('role','img');svg.setAttribute('aria-label',uid);
 // Root display dimensions on reuse exports are 32; the solo source viewBox stays 48.
 if($('grid').checked){
  const defs=xml.createElementNS(ns,'defs'),pattern=xml.createElementNS(ns,'pattern');pattern.setAttribute('id','grid-'+uid);pattern.setAttribute('width','1');pattern.setAttribute('height','1');pattern.setAttribute('patternUnits','userSpaceOnUse');
  const path=xml.createElementNS(ns,'path');path.setAttribute('d','M 1 0 L 0 0 0 1');path.setAttribute('stroke',$('dark').checked?'#718369':'#9db090');path.setAttribute('stroke-width','.09');path.setAttribute('fill','none');pattern.append(path);defs.append(pattern);
  const rect=xml.createElementNS(ns,'rect');rect.setAttribute('width',size);rect.setAttribute('height',size);rect.setAttribute('fill','url(#grid-'+uid+')');rect.setAttribute('stroke','none');
  const traces=[];for(const shape of svg.querySelectorAll('path,line,polyline,polygon,circle,ellipse,rect')){
   const copy=shape.cloneNode(false);copy.removeAttribute('id');copy.setAttribute('fill','none');copy.setAttribute('stroke','#e33b52');copy.setAttribute('stroke-width','.8');copy.setAttribute('vector-effect','non-scaling-stroke');
   // Retain inherited geometry transforms from the inspection wrapper.
   let node=copy;for(let p=shape.parentElement;p&&p!==svg;p=p.parentElement){const g=xml.createElementNS(ns,'g');if(p.hasAttribute('transform'))g.setAttribute('transform',p.getAttribute('transform'));g.append(node);node=g;}traces.push(node);
  }
  svg.prepend(defs,rect);svg.append(...traces);
 }
 if(shape&&$('guides').checked){const overlay=new DOMParser().parseFromString(`<svg xmlns="${ns}">${guide(shape,size)}</svg>`,'image/svg+xml');for(const child of [...overlay.documentElement.children])svg.append(xml.importNode(child,true));}
 return new XMLSerializer().serializeToString(svg);
}
function render(){
 const query=$('search').value.toLowerCase().trim(),usage=$('usage').value,geometry=$('geometry').value;
 const visible=rows.filter(r=>(!query||[r.icon_id,...r.pairs.map(p=>p.concept)].join(' ').toLowerCase().includes(query))&&(!usage||(usage==='used'?r.default_count>0:usage==='alternative'?r.default_count===0:!!r.native))&&(!geometry||(geometry==='off'?r.off_grid.length>0:!r.off_grid.length)));
 const pages=Math.max(1,Math.ceil(visible.length/pageSize));page=Math.min(page,pages-1);$('cards').classList.toggle('dark',$('dark').checked);$('cards').style.setProperty('--inspection-zoom',$('zoom').value);
 $('cards').innerHTML=visible.slice(page*pageSize,(page+1)*pageSize).map((r,i)=>{
  const id='r'+(page*pageSize+i),hasIssues=r.off_grid.length>0;
  const selected=$('keyshape').value==='auto'?r.target_keyshape:$('keyshape').value,shape=shapes.find(s=>s.name===selected),sourceShape=shapes.find(s=>s.name===r.target_keyshape),fit=r.keyshape_fits?.[selected];
  const fitLabel={matches:'Matches keyshape envelope',inside:'Inside guide · does not fill keyshape',exceeds:'Exceeds keyshape guide'}[fit]||'No standard keyshape assigned';
  return `<article class="card"><header><h2>${esc(r.icon_id)}</h2><p><strong>${r.default_count}</strong> combinations currently use this solo · available in ${r.pairs.length} pairs</p><span class="badge ${hasIssues?'':'ready'}">${hasIssues?'Scaled nodes / radii off grid':'Scaled nodes / radii on grid'}</span> ${r.native?'<span class="badge ready">Native SUB32 available</span>':''}</header>
  <div class="artwork"><figure><div class="stage">${art(r.original,48,id+'solo',sourceShape)}</div><figcaption><strong>Solo original · 48×48</strong>Ink ${fmt(r.source_ink[0])} × ${fmt(r.source_ink[1])}<br>${esc(r.source_keyshape)}</figcaption></figure><figure><div class="stage">${art(r.scaled,32,id+'scaled',shape)}</div><figcaption><strong>Scaled · 32×32 maximum</strong>Ink ${fmt(r.ink_width)} × ${fmt(r.ink_height)}<br>4px stroke</figcaption></figure><figure><div class="stage">${r.native?art(r.native,32,id+'native',shape):'<span class="empty-native">No native replacement</span>'}</div><figcaption><strong>Native SUB32</strong>${r.native?'Separate grid-aligned version':'No separate SUB32 version'}</figcaption></figure></div>
  <p class="keyshape-verdict"><span class="badge ${fit==='matches'?'ready':''}">${esc(fitLabel)}</span> ${shape?`${esc(shape.name)} · ${shape.sub_bounds[2]-shape.sub_bounds[0]} × ${shape.sub_bounds[3]-shape.sub_bounds[1]} ink`:esc(selected)}</p><div class="dimensions">Geometry scale <strong>${fmt(r.scale*100)}%${Math.abs(r.scale-r.scale_y)>1e-8?' × '+fmt(r.scale_y*100)+'%':''}</strong> · Proportion change <strong>${fmt(r.proportion_change||0)}%</strong> · Centerline box <strong>${fmt(r.centerline_width)} × ${fmt(r.centerline_height)}</strong> · Ink box <strong>${fmt(r.ink_width)} × ${fmt(r.ink_height)}</strong></div>
  <p class="note">${hasIssues?'Fractional authored nodes or radii appear in this centered scaled preview.':'Integer nodes and radii only; this is not a complete spacing or keyshape approval.'} ${r.native?'The native version is shown separately; it does not make the scaled preview grid-safe.':''}</p>
  <details><summary>Scaling checks${hasIssues?' · '+r.off_grid.length+' fractional coordinates':''}</summary><p>Checks below use this rounded proportional preview. Whole-number outer dimensions do not guarantee integer internal coordinates or sufficient spacing.</p>${hasIssues?'<ul class="diagnostic">'+r.off_grid.map(s=>'<li>'+esc(s)+'</li>').join('')+'</ul>':''}</details>
  <details><summary>Used in / available for ${r.pairs.length} combinations</summary><ul>${r.pairs.map(p=>`<li><a href="combination-previews/${encodeURIComponent(p.id)}.svg" target="_blank" rel="noopener">${esc(p.concept)}</a> — ${p.default?'uses this solo':'currently uses '+esc(p.selected_sub)}</li>`).join('')}</ul></details></article>`;
 }).join('');
 $('status').textContent=visible.length?`${visible.length} solo icons · showing ${page*pageSize+1}–${Math.min((page+1)*pageSize,visible.length)}`:'No solo icons match these filters.';$('page').textContent=`Page ${page+1} of ${pages}`;$('prev').disabled=page===0;$('next').disabled=page===pages-1;
}
for(const id of ['search','usage','geometry','zoom','grid','dark','keyshape','guides'])$(id).addEventListener(id==='search'?'input':'change',()=>{page=0;render();});
$('prev').onclick=()=>{page--;render();};$('next').onclick=()=>{page++;render();};
fetch('sub-scaling.json',{cache:'no-store'}).then(r=>{if(!r.ok)throw Error('Could not load scaling data.');return r.json();}).then(data=>{rows=data.rows;shapes=data.keyshapes||[];for(const s of shapes){const o=document.createElement('option');o.value=s.name;o.textContent=s.name.replace('_',' ')+' · '+(s.sub_bounds[2]-s.sub_bounds[0])+'×'+(s.sub_bounds[3]-s.sub_bounds[1]);$('keyshape').append(o);}$('keyshapeLegend').innerHTML=shapes.map(s=>`<figure><svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 36 36" width="90" height="90">${guide(s,32)}</svg><figcaption><strong>${esc(s.name.replace('_',' '))}</strong><br>${s.sub_bounds[2]-s.sub_bounds[0]} × ${s.sub_bounds[3]-s.sub_bounds[1]} ink<br>${s.sub_bounds[2]-s.sub_bounds[0]-4} × ${s.sub_bounds[3]-s.sub_bounds[1]-4} centerline</figcaption></figure>`).join('');const stats=[[rows.filter(r=>r.default_count>0).length,'Solo icons currently used'],[data.solo_default_pairs,'Combinations using solo subs'],[rows.length,'Unique solo options'],[rows.filter(r=>r.native).length,'Native replacements available']];$('summary').innerHTML=stats.map(([n,label])=>`<div class="stat"><strong>${n}</strong><span>${label}</span></div>`).join('');render();}).catch(e=>{$('status').textContent=e.message;});
})();

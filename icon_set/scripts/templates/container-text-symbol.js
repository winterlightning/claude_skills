// Text symbols for container pairs (primitives.html?view=container): a symbol source marked
// "Text / number" is drawn with typeface v2 (text-combine.js `Typeface.layout`, grid-hinted sizes)
// instead of a hand-drawn symbol. Each pair gets its own text drawing (the same text can need a
// different size in each container): saving uploads it for that pair only (POST /api/icons/upload
// with reference {id: combination id, role: symbol}, approved), keeps the pair's position, and
// combines that pair.
// The settings travel inside the uploaded SVG's <desc>, so the editor reopens where it was left.
(function(){
'use strict';
const SIZES_URL='typeface-v2-sizes.json', DEFAULTS_URL='container-text-v2.json';
const BOX=32, STROKE=4, SPACE_RATIO=.55;  // text-combine.js: a space advances xHeight * 0.55
let sizes=null, defaults={}, loading=null;

function load(){
  loading??=Promise.all([
    fetch(SIZES_URL,{cache:'no-cache'}).then(r=>{if(!r.ok)throw Error('Typeface v2 sizes are unavailable.');return r.json();}),
    fetch(DEFAULTS_URL,{cache:'no-cache'}).then(r=>r.ok?r.json():{icons:[]}).catch(()=>({icons:[]}))
  ]).then(([s,d])=>{sizes=s;for(const e of [...(d.icons||[]),...(d.lowercase_later||[])])defaults[e.source_id]={text:e.text,underline:!!e.underline};});
  return loading;
}
const isText=subId=>typeof statuses!=='undefined'&&statuses[subId]?.reason==='text_number';
const sizeList=()=>Object.keys(sizes?.sizes||{}).map(Number).sort((a,b)=>a-b);

// Ink box of the text at one hinted size; every spacing is even so the ink stays on whole units.
function layout(s,size){
  const cap=size-STROKE;
  return Typeface.layout(s.text.toUpperCase(),sizes.sizes[String(size)],{xHeight:s.wordSpace/SPACE_RATIO,capHeight:cap,nativeSize:true,
    tracking:s.tracking,lineGap:s.lineGap,stroke:STROKE,underline:s.underline,padding:0,trimInk:true,align:'center'});
}
// "auto": the largest size up to 24 whose ink fits the 28-unit symbol area, else the smallest.
function resolve(s){
  if(s.size!=='auto')return {size:Number(s.size),result:layout(s,Number(s.size))};
  const fits=sizeList().filter(n=>n<=24).reverse();
  for(const n of fits){const r=layout(s,n);if(r.width<=BOX-4&&r.height<=BOX-4)return {size:n,result:r};}
  const n=sizeList()[0];return {size:n,result:layout(s,n)};
}
// Letters moved one by one (the layout popup's Letters panel): offsets[i] = [dx, dy] in whole units for the
// i-th drawn glyph (spaces are not glyphs). The ink box is measured again and trimmed back to 0, 0.
function offsetResult(result,offsets){
  if(!offsets?.some(o=>o&&(o[0]||o[1])))return result;
  const r={...result,placements:result.placements.map((p,i)=>{const o=offsets[i]||[0,0];return {...p,x:p.x+o[0],y:p.y+o[1]};}),
           decorations:(result.decorations||[]).map(d=>({...d}))};
  const half=r.stroke/2,boxes=r.placements.map(p=>{const [l,t,rt,b]=p.glyph.bounds;return [l*p.scale+p.x-half,t*p.scale+p.y-half,rt*p.scale+p.x+half,b*p.scale+p.y+half];});
  for(const d of r.decorations)boxes.push([d.x1-half,d.y-half,d.x2+half,d.y+half]);
  const left=Math.min(...boxes.map(b=>b[0])),top=Math.min(...boxes.map(b=>b[1]));
  for(const p of r.placements){p.x-=left;p.y-=top;}for(const d of r.decorations){d.x1-=left;d.x2-=left;d.y-=top;}
  r.width=Math.max(...boxes.map(b=>b[2]))-left;r.height=Math.max(...boxes.map(b=>b[3]))-top;
  return r;
}
const textResult=s=>{const {size,result}=resolve(s);return {size,result:offsetResult(result,s.offsets)};};
const inner=(result,text)=>Typeface.svg(result,text).replace(/^<svg[^>]*>/,'').replace(/<\/svg>$/,'').replace(/<title>.*?<\/title>/,'').replaceAll('#202820','#000');
const esc=t=>t.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));

// The symbol document: a 32 × 32 canvas when the ink fits (kept at natural size in the standard box),
// otherwise a canvas exactly the ink box, combined with ink = [W, H] so it is never scaled.
function symbolDocument(s){
  // Hinted glyph bounds carry float noise (23.000000000000007); the ink box itself is whole units.
  const {size,result}=textResult(s), W=+result.width.toFixed(3), H=+result.height.toFixed(3), fits=W<=BOX&&H<=BOX;
  if(W>BOX*2-4||H>BOX*2-4)throw Error(`Ink ${W} × ${H} does not fit the 64 × 64 container canvas. Use a smaller size, fewer letters per line, or tighter spacing.`);
  if(!fits&&(W%2||H%2))throw Error(`Ink ${W} × ${H} is not even, so it cannot be combined at its exact size. Change the spacing or size.`);
  const cw=fits?BOX:W, ch=fits?BOX:H, x=fits?(BOX-W)/2:0, y=fits?(BOX-H)/2:0;
  const meta={typeface:'v2',text:s.text,size:s.size,resolved_size:size,tracking:s.tracking,word_space:s.wordSpace,line_gap:s.lineGap,underline:s.underline,offsets:s.offsets||[],ink:[W,H]};
  const svg=`<svg xmlns="http://www.w3.org/2000/svg" width="${cw}" height="${ch}" viewBox="0 0 ${cw} ${ch}" fill="none" stroke="#000" stroke-width="${STROKE}" stroke-linecap="round" stroke-linejoin="round">`
    +`<title>${esc(s.text.replace(/\n/g,' '))}</title><desc>${esc(JSON.stringify(meta))}</desc><g transform="translate(${x} ${y})">${inner(result,s.text)}</g></svg>`;
  return {svg,size,W,H,fits,ink:fits?null:[W,H],meta};
}

async function savedSettings(art){
  if(!art?.uploaded)return null;
  try{const t=await fetch(art.preview_url,{cache:'no-cache'}).then(r=>r.ok?r.text():'');
    const desc=new DOMParser().parseFromString(t,'image/svg+xml').querySelector('desc')?.textContent;const m=desc&&JSON.parse(desc);
    return m?.typeface==='v2'?{text:m.text,size:String(m.size),tracking:m.tracking,wordSpace:m.word_space,lineGap:m.line_gap,underline:!!m.underline,offsets:m.offsets||[],manual:!!m.manual_elements}:null;
  }catch{return null;}
}

const containerCache=new Map();
function containerGroup(url){
  if(!containerCache.has(url))containerCache.set(url,fetch(url,{cache:'no-cache'}).then(r=>r.ok?r.text():Promise.reject(Error('Container artwork unavailable.'))).then(t=>{
    const svg=new DOMParser().parseFromString(t,'image/svg+xml').documentElement;svg.querySelector('title')?.remove();
    const attrs=['fill','stroke','stroke-width','stroke-linecap','stroke-linejoin'].filter(a=>svg.hasAttribute(a)).map(a=>`${a}="${svg.getAttribute(a)}"`).join(' ');
    return `<g ${attrs} color="#000">${svg.innerHTML}</g>`;}));
  return containerCache.get(url);
}
function grid(){let g='';for(let i=4;i<64;i+=4)g+=`<path d="M${i} 0V64M0 ${i}H64" stroke="${i%16?'#e3eae6':'#c3d1c9'}" stroke-width="${i%16?.15:.25}"/>`;return g;}

async function save(row,s,message){
  const doc=symbolDocument(s), before=pairParts(row);
  message.textContent='Uploading the text…';
  const response=await fetch('/api/icons/upload',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({
    name:'Text '+s.text.replace(/\n/g,' ').slice(0,100),family:'symbol',category:'text',svg:doc.svg,approve:true,reference:{id:row.id,role:'symbol'}})});
  const data=await response.json().catch(()=>({}));if(!response.ok)throw Error(data.error||'Could not upload the text.');
  await loadReferenceUploads();
  const icon=data.record.icon_id;pairReviews[data.record.key]='approve';
  // Keep the pair where it was: a pair-scope position moves to the new drawing; text wider than 32 gets its exact
  // ink size (also when the pair had no symbol before, so nothing to carry over).
  const mainId=before?.mainId||row.main_icon_id||containerMain(row,containerResults?.selections?.[row.id]||containerPreviews.get(row.id))?.icon_id;
  if(mainId){const e=effectiveCenter(mainId,before?.symbol.icon_id||'');
    if((before&&e.scope==='pair')||doc.ink){message.textContent='Keeping the position…';await saveCenter(mainId,icon,'pair',e.center.map(Math.round),doc.ink);}}
  if(!pairParts(row))throw Error('Uploaded '+icon+', but this pair has no container to combine with.');
  message.textContent='Combining…';await createCombined(row);
  refreshCards(r=>r.id===row.id);
  return icon;
}

// The editor shown inside a text pair's symbol panel.
function panel(row){
  const box=node('details','text-symbol'),summary=node('summary','','Text symbol · typeface v2');box.open=true;box.append(summary);
  const body=node('div','text-symbol-body');box.append(body);
  if(!window.Typeface){body.append(node('p','muted','The typeface engine (text-combine.js) is not loaded.'));return box;}
  body.append(node('p','muted','Loading typeface v2…'));
  load().then(async()=>{
    const art=containerSymbol(row,containerResults?.selections?.[row.id]||containerPreviews.get(row.id));
    const saved=await savedSettings(uploadedArt(row.id)), d=defaults[row.sub_id]||{};
    const start=saved||{text:d.text||'',size:'auto',tracking:4,wordSpace:8,lineGap:4,underline:!!d.underline,offsets:[]};
    body.replaceChildren();
    const f={};
    const field=(label,el)=>{const l=node('label','text-symbol-field');l.append(node('span','',label),el);return l;};
    f.text=node('textarea');f.text.rows=2;f.text.spellcheck=false;f.text.value=start.text;f.text.setAttribute('aria-label','Text');
    f.size=node('select');f.size.append(new Option('Auto (fit 28)','auto'),...sizeList().map(n=>new Option(n+' · hinted',String(n))));f.size.value=start.size in sizes.sizes||start.size==='auto'?start.size:'auto';
    const num=(v,min,max)=>{const i=node('input');i.type='number';i.min=min;i.max=max;i.step=2;i.value=v;return i;};
    f.tracking=num(start.tracking,0,24);f.wordSpace=num(start.wordSpace,2,24);f.lineGap=num(start.lineGap,0,24);
    f.underline=node('input');f.underline.type='checkbox';f.underline.checked=start.underline;
    const under=node('label','text-symbol-check');under.append(f.underline,' Underline');
    const row1=node('div','text-symbol-row');row1.append(field('Size',f.size),field('Letter',f.tracking),field('Word',f.wordSpace),field('Line',f.lineGap));
    const preview=node('div','text-symbol-preview'),status=node('p','text-symbol-status'),message=node('p','side-editor-message');message.setAttribute('role','status');
    const saveButton=node('button','side-edit-component','');saveButton.type='button';
    const actions=node('div','requires-login');actions.append(saveButton);
    body.append(field('Text (A–Z, 0–9, space, Enter for a new line)',f.text),row1,under,preview,status,actions,message);
    body.prepend(node('p','muted',saved?.manual?'Letters of this pair were moved or resized in the combined popup. Uploading from here draws the text again without those edits.'
      :saved?'This pair uses the text below. Change it and upload again to update only this pair.'
      :`Only this pair: the text is uploaded as this pair's own symbol${art?' (replacing '+art.icon_id+')':''} and combined with this container.`));
    const read=()=>({text:f.text.value.replace(/\r/g,''),size:f.size.value,tracking:+f.tracking.value,wordSpace:+f.wordSpace.value,lineGap:+f.lineGap.value,underline:f.underline.checked,
      // Letter moves belong to the text they were made on.
      offsets:f.text.value.replace(/\r/g,'')===start.text?start.offsets||[]:[]});
    saveButton.textContent='Upload text & combine this pair';
    let doc=null;
    async function draw(){
      const s=read();doc=null;saveButton.disabled=true;
      if(!s.text.trim()){status.textContent='Type the text.';preview.replaceChildren();return;}
      if([s.tracking,s.wordSpace,s.lineGap].some(v=>!Number.isFinite(v)||v<0||v%2)){status.textContent='Spacing must be even whole units.';return;}
      try{doc=symbolDocument(s);}catch(error){status.textContent=error.message;preview.replaceChildren();return;}
      const parts=pairParts(row),main=parts?.main||containerMain(row,null);
      const center=parts?effectiveCenter(parts.mainId,parts.symbol.icon_id).center:[32,32];
      const x=center[0]-doc.W/2,y=center[1]-doc.H/2;
      const text=`<g transform="translate(${x} ${y})" fill="none" stroke="#000" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">${inner(textResult(s).result,s.text)}</g>`;
      const container=main?await containerGroup(main.preview_url).catch(()=>''):'';
      preview.innerHTML=`<svg viewBox="0 0 64 64" class="text-symbol-big">${grid()}${container}${text}<rect x="${x}" y="${y}" width="${doc.W}" height="${doc.H}" fill="none" stroke="#d9534f" stroke-width=".3" stroke-dasharray="1 .8"/></svg>`
        +`<svg viewBox="0 0 64 64" class="text-symbol-small">${container}${text}</svg><svg viewBox="0 0 ${doc.fits?32:doc.W} ${doc.fits?32:doc.H}" class="text-symbol-alone">${doc.svg.replace(/^<svg[^>]*>|<\/svg>$/g,'')}</svg>`;
      const warn=[];if(x<4||y<4||x+doc.W>60||y+doc.H>60)warn.push('ink comes within 4 units of the canvas edge');
      status.textContent=`Size ${doc.size} · ink ${doc.W} × ${doc.H} · ${doc.fits?'natural size in the 32 × 32 symbol box':'wider than 32: combined at its exact ink size'} · center ${center.join(', ')}`+(warn.length?' · ⚠ '+warn.join(', '):'');
      status.classList.toggle('warn',warn.length>0);saveButton.disabled=false;
    }
    for(const el of Object.values(f))el.addEventListener('input',draw);
    saveButton.onclick=async()=>{
      if(!doc)return;saveButton.disabled=true;
      try{const icon=await save(row,read(),message);message.textContent=`Uploaded ${icon} and combined this pair.`;}
      catch(error){message.textContent=error.message;saveButton.disabled=false;}
    };
    draw();
  }).catch(error=>body.replaceChildren(node('p','muted',error.message)));
  return box;
}

if(!document.getElementById('text-symbol-style')){
  const style=document.createElement('style');style.id='text-symbol-style';
  style.textContent=`.text-symbol{margin-top:10px;border:1px solid #d9c9a3;border-radius:10px;background:#fffaf0;padding:8px 10px}.text-symbol summary{cursor:pointer;font-weight:600;font-size:13px;color:#7a5200}
.text-symbol-body{display:grid;gap:8px;margin-top:8px}.text-symbol textarea{font:600 18px/1.3 system-ui;letter-spacing:.06em;text-transform:uppercase;width:100%;padding:6px 8px;border:1px solid #c9b98f;border-radius:6px;resize:vertical}
.text-symbol-field{display:grid;gap:2px;font-size:11px;font-weight:600;color:#6b5a33}.text-symbol-field input,.text-symbol-field select{font:inherit;font-size:13px;font-weight:400;padding:4px 6px;border:1px solid #c9b98f;border-radius:6px;width:100%}
.text-symbol-row{display:grid;grid-template-columns:1.6fr 1fr 1fr 1fr;gap:6px}.text-symbol-check{font-size:12px;display:flex;gap:6px;align-items:center}
.text-symbol-preview{display:flex;gap:8px;align-items:end;flex-wrap:wrap}.text-symbol-preview svg{background:#fff;box-shadow:inset 0 0 0 1px #c6d1cb;border-radius:4px}.text-symbol-big{width:192px;height:192px}.text-symbol-small{width:64px;height:64px}.text-symbol-alone{width:48px;height:auto;max-height:48px}
.text-symbol-status{font-size:12px;margin:0;color:#4b5560}.text-symbol-status.warn{color:#b45309}`;
  document.head.append(style);
}
// For the combined layout popup: this pair's own text settings (null when the pair has no typeface text),
// and saving the text again with letters moved (offsets per drawn glyph, whole units).
const pairText=row=>isText(row.sub_id)?load().then(()=>savedSettings(uploadedArt(row.id))):Promise.resolve(null);
async function uploadText(row,settings){
  const doc=symbolDocument(settings);
  const response=await fetch('/api/icons/upload',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({
    name:'Text '+settings.text.replace(/\n/g,' ').slice(0,100),family:'symbol',category:'text',svg:doc.svg,approve:true,reference:{id:row.id,role:'symbol'}})});
  const data=await response.json().catch(()=>({}));if(!response.ok)throw Error(data.error||'Could not upload the text.');
  return {record:data.record,doc};
}
window.ContainerTextSymbol={isText,panel,load,symbolDocument,pairText,uploadText};
})();

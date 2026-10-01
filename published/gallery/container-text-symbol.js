// Text symbols for container pairs (container-pairs.html): a symbol drawn with typeface v2 (text-combine.js
// `Typeface.layout`, grid-hinted sizes) instead of a hand-drawn symbol. Each pair gets its own text drawing (the
// same text can need a different size in each container): the page uploads it for that pair only (POST
// /api/icons/upload with reference {id: combination id, role: symbol}, approved) and builds that pair.
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

// The text settings an uploaded symbol drawing was made with (from its <desc>), or null for any other drawing.
// `manual`: letters were moved or resized one by one in the pair editor after the text was drawn.
function settingsOf(svg){
  try{const desc=new DOMParser().parseFromString(svg||'','image/svg+xml').querySelector('desc')?.textContent;const m=desc&&JSON.parse(desc);
    return m?.typeface==='v2'?{text:m.text,size:String(m.size),tracking:m.tracking,wordSpace:m.word_space,lineGap:m.line_gap,underline:!!m.underline,offsets:m.offsets||[],manual:!!m.manual_elements}:null;
  }catch{return null;}
}
const defaultText=sourceId=>defaults[sourceId]||null;
window.ContainerTextSymbol={load,symbolDocument,settingsOf,defaultText,sizeList};
})();

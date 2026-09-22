const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const {layout,svg}=require('../scripts/templates/text-combine.js');
const {glyphs}=JSON.parse(fs.readFileSync(path.join(__dirname,'../../published/gallery/typeface.json'),'utf8'));
assert.equal(glyphs.length,96);
for (const currency of '$€£¥₿₹₩₴₭₤') assert.throws(()=>layout(currency,glyphs),/Unsupported/);
const v2=JSON.parse(fs.readFileSync(path.join(__dirname,'../../published/gallery/typeface-v2.json'),'utf8')).glyphs;
let result=layout('obdpqg',glyphs);
for(const p of result.placements){
 assert.ok(Math.abs(p.glyph.body_height*p.scale-36)<1e-8);
 assert.ok(Math.abs(p.glyph.baseline*p.scale+p.y-result.baseline)<1e-8);
}
assert.ok(result.placements[1].glyph.bounds[1]*result.placements[1].scale+result.placements[1].y<result.bodyTop);
const p=result.placements[3];
assert.ok(p.glyph.bounds[3]*p.scale+p.y>result.baseline);
result=layout('im 09',glyphs);
assert.ok(result.placements[0].width<result.placements[1].width);
assert.equal(result.placements[2].glyph.kind,'digit');
assert.ok(Math.abs(result.placements[2].scale*result.placements[2].glyph.body_height-52)<1e-8);
const tight=layout('oo',glyphs,{tracking:0}),spaced=layout('oo',glyphs,{tracking:9});
assert.ok(Math.abs(spaced.width-tight.width-9)<1e-8);
assert.throws(()=>layout('A&🙂',glyphs),/Unsupported/);
assert.throws(()=>layout('a',glyphs,{xHeight:0}),/Invalid/);
assert.equal(layout('  ',glyphs).placements.length,0);
assert.ok(!svg(layout('b',glyphs),'b').includes('stroke-dasharray'));
assert.ok(svg(layout('b',glyphs),'b',true).includes('stroke-dasharray'));
const exportText=svg(layout('b',glyphs),'b');
const width=Number(exportText.match(/stroke-width="([^"]+)"/)[1]);
assert.ok(Math.abs(width*layout('b',glyphs).placements[0].scale-4)<1e-8);
console.log('Typeface layout: aligned bowls/baselines, extensions, widths, spacing, digits, export and errors passed.');
const alphabet=layout('abcdefghijklmnopqrstuvwxyz0123456789',glyphs);
for(const p of alphabet.placements){
 const [left,top,right,bottom]=p.glyph.bounds;
 assert.ok(left*p.scale+p.x-2>=0);
 assert.ok(top*p.scale+p.y-2>=0);
 assert.ok(right*p.scale+p.x+2<=alphabet.width);
 assert.ok(bottom*p.scale+p.y+2<=alphabet.height);
}
// Explicit lines, blank lines, pasted CRLF and per-line guides survive export.
const multi=layout('ob\npq\n\nj',glyphs);
assert.equal(multi.lines.length,4);
assert.equal(multi.placements.length,5);
const inkLeft=p=>p.x+p.glyph.bounds[0]*p.scale-2;
assert.equal(inkLeft(multi.placements[0]),inkLeft(multi.placements[2]));
for(const p of multi.placements){
 assert.ok(Math.abs(p.glyph.baseline*p.scale+p.y-multi.lines[p.lineIndex].baseline)<1e-8);
 const [left,top,right,bottom]=p.glyph.bounds;
 assert.ok(top*p.scale+p.y-2>=0);
 assert.ok(bottom*p.scale+p.y+2<=multi.height);
}
assert.ok(Math.abs(multi.lines[3].baseline-multi.lines[1].baseline-2*multi.lineAdvance)<1e-8);
assert.equal((svg(multi,'ob\npq\n\nj',true).match(/stroke-dasharray/g)||[]).length,4);
assert.equal((svg(multi,'ob\npq\n\nj').match(/stroke-dasharray/g)||[]).length,0);
assert.deepEqual(layout('o\r\nb\rc',glyphs),layout('o\nb\nc',glyphs));
assert.equal(layout('o\n',glyphs).lines.length,2);
assert.equal(layout('\n\n',glyphs).placements.length,0);
assert.equal(layout('ooo\no',glyphs).width,layout('ooo',glyphs).width);
const normal=layout('g\nf',glyphs,{lineGap:0}),loose=layout('g\nf',glyphs,{lineGap:20});
assert.ok(Math.abs(loose.height-normal.height-20)<1e-8);
assert.throws(()=>layout('a\nb',glyphs,{lineGap:-1}),/Invalid/);
const lastBottom=Math.max(...normal.placements.filter(p=>p.lineIndex===0).map(p=>p.glyph.bounds[3]*p.scale+p.y+2));
const nextTop=Math.min(...normal.placements.filter(p=>p.lineIndex===1).map(p=>p.glyph.bounds[1]*p.scale+p.y-2));
assert.ok(nextTop>=lastBottom);
console.log('Multiline layout: newlines, blank lines, spacing, bounds and export passed.');
const caps=layout('ABCDEFGHIJKLMNOPQRSTUVWXYZ\nHello World',glyphs);
assert.equal(caps.placements.filter(p=>p.lineIndex===0).length,26);
for(const p of caps.placements){
 assert.ok(Math.abs(p.glyph.body_height*p.scale-(p.glyph.kind==='uppercase'?52:36))<1e-8);
 assert.ok(Math.abs(p.glyph.baseline*p.scale+p.y-caps.lines[p.lineIndex].baseline)<1e-8);
}
for(const stroke of [0.5,2,4,8,16]){
 const weighted=layout('AbQgy\nMWI',glyphs,{stroke});
 const document=svg(weighted,'AbQgy\nMWI');
 const widths=[...document.matchAll(/stroke-width="([^"]+)"/g)].map(m=>Number(m[1]));
 let index=0;
 for(const p of weighted.placements){
  for(const _ of p.glyph.paths)assert.ok(Math.abs(widths[index++]*p.scale-stroke)<1e-8);
  const [left,top,right,bottom]=p.glyph.bounds;
  assert.ok(left*p.scale+p.x-stroke/2>=-1e-8);
  assert.ok(right*p.scale+p.x+stroke/2<=weighted.width+1e-8);
  assert.ok(top*p.scale+p.y-stroke/2>=-1e-8);
  assert.ok(bottom*p.scale+p.y+stroke/2<=weighted.height+1e-8);
 }
}
assert.throws(()=>layout('A',glyphs,{stroke:0}),/Invalid/);
console.log('Uppercase A–Z, mixed-case cap heights and variable stroke exports passed.');
// Decorations follow each line's width, skip blank lines, and survive SVG export.
for(const stroke of [.5,4,16])for(const underline of [false,true])for(const strikethrough of [false,true]){
 const text='Abgy\n\nI\n  ',decorated=layout(text,glyphs,{stroke,underline,strikethrough,padding:0,lineGap:0});
 assert.equal(decorated.decorations.length,2*(Number(underline)+Number(strikethrough)));
 for(const d of decorated.decorations){
  const line=decorated.lines[d.lineIndex];
  assert.ok([0,2].includes(d.lineIndex));
  assert.ok(Math.abs(d.x1-stroke/2)<1e-8);
  assert.ok(Math.abs(d.x2+stroke/2-line.width)<1e-8);
  assert.ok(d.y-stroke/2>=0&&d.y+stroke/2<=decorated.height+1e-8);
  if(d.kind==='strikethrough')assert.equal(d.y,line.baseline-18);
  else {
   const inkBottom=Math.max(...decorated.placements.filter(p=>p.lineIndex===d.lineIndex).map(p=>p.y+p.glyph.bounds[3]*p.scale+stroke/2));
   assert.ok(d.y-stroke/2>inkBottom);
   if(d.lineIndex===0){
    const nextTop=Math.min(...decorated.placements.filter(p=>p.lineIndex===2).map(p=>p.y+p.glyph.bounds[1]*p.scale-stroke/2));
    assert.ok(d.y+stroke/2<=nextTop);
   }
  }
 }
 const exported=svg(decorated,text);
 assert.equal((exported.match(/data-effect=/g)||[]).length,decorated.decorations.length);
 assert.ok(!exported.includes('stroke-dasharray'));
 for(const lineTag of exported.match(/<line [^>]+>/g)||[])assert.ok(lineTag.includes(`stroke-width="${stroke}"`));
}
assert.equal(layout('\n  ',glyphs,{underline:true,strikethrough:true}).decorations.length,0);
console.log('Underline and strikethrough: individual/combined effects, multiline bounds, blank lines, stroke weights and export passed.');
// Fixed canvas height preserves every glyph's aspect ratio and the complete line box.
for(const text of ['INDD','gyp','FOR\nSALE','SHARE\nTHE\nROAD','Mg'])for(const underline of [false,true]){
 if(underline&&text.split('\n').length>=3){assert.throws(()=>layout(text,glyphs,{padding:4,underline,canvasHeight:28}),/cannot fit/);continue;}
 const original=layout(text,glyphs,{padding:4,underline,align:'center'});
 const fixed=layout(text,glyphs,{padding:4,underline,align:'center',canvasHeight:28});
 assert.equal(fixed.height,28);
 assert.equal(fixed.stroke,4);
 const ratios=fixed.placements.map((p,i)=>p.scale/original.placements[i].scale);
 assert.ok(ratios.every(r=>Math.abs(r-ratios[0])<1e-10));
 const widths=[...svg(fixed,text).matchAll(/<path[^>]*stroke-width="([^"]+)"/g)].map(m=>Number(m[1]));
 let wi=0;for(const p of fixed.placements)for(const _ of p.glyph.paths)assert.ok(Math.abs(widths[wi++]*p.scale-4)<1e-10);
 assert.ok(fixed.decorations.every(d=>d.y+2<=28));
 assert.ok(svg(fixed,text).includes('height="28"'));
 for(const p of fixed.placements){
  const [l,t,r,b]=p.glyph.bounds,h=fixed.stroke/2;
  assert.ok(l*p.scale+p.x-h>=-1e-7&&r*p.scale+p.x+h<=fixed.width+1e-7);
  assert.ok(t*p.scale+p.y-h>=-1e-7&&b*p.scale+p.y+h<=28+1e-7);
 }
}
assert.throws(()=>layout('A',glyphs,{canvasHeight:0}),/Invalid canvas height/);
console.log('Fixed 28-unit text canvas: multiline, underline, bounds and proportions passed.');
// Tight text canvases measure actual glyph/decorative ink, not the nominal body band.
const batch=JSON.parse(fs.readFileSync(path.join(__dirname,'../data/container-text-icons.json'),'utf8'));
for(const item of [...batch.icons,{text:'ooo',underline:false},{text:'gyp',underline:true}]){
 const r=layout(item.text,glyphs,{canvasHeight:28,padding:0,stroke:4,trimInk:true,underline:item.underline,align:'center'});
 const boxes=r.placements.map(p=>[p.x+p.glyph.bounds[0]*p.scale-2,p.y+p.glyph.bounds[1]*p.scale-2,p.x+p.glyph.bounds[2]*p.scale+2,p.y+p.glyph.bounds[3]*p.scale+2]);
 for(const d of r.decorations)boxes.push([d.x1-2,d.y-2,d.x2+2,d.y+2]);
 const bounds=[Math.min(...boxes.map(b=>b[0])),Math.min(...boxes.map(b=>b[1])),Math.max(...boxes.map(b=>b[2])),Math.max(...boxes.map(b=>b[3]))];
 for(const [i,v] of [0,0,r.width,28].entries())assert.ok(Math.abs(bounds[i]-v)<1e-8,`${item.text}: ink bounds ${bounds}`);
 assert.equal(r.stroke,4);
}
console.log('All text exports: zero padding on all four ink edges, 28-unit ink height, stroke 4 passed.');
// Keyboard characters except currency are accepted, with punctuation on a shared
// typographic band instead of scaling tiny marks to the full letter height.
const printable=Array.from({length:95},(_,i)=>String.fromCharCode(i+32)).filter(c=>c!=='$').join('');
for(const stroke of [.5,4,16]){
 const r=layout(printable,glyphs,{stroke,underline:true,strikethrough:true});
 assert.equal(r.placements.length,93);
 for(const p of r.placements){
  const [l,t,rr,b]=p.glyph.bounds;
  assert.ok([p.x,p.y,p.scale,...p.glyph.bounds].every(Number.isFinite));
  assert.ok(l*p.scale+p.x-stroke/2>=-1e-8);
  assert.ok(rr*p.scale+p.x+stroke/2<=r.width+1e-8);
  assert.ok(t*p.scale+p.y-stroke/2>=-1e-8);
  assert.ok(b*p.scale+p.y+stroke/2<=r.height+1e-8);
 }
}
const punct=layout('.o,\'_',glyphs),[period,o,comma,quote,underscore]=punct.placements;
const topOf=p=>p.y+p.glyph.bounds[1]*p.scale;
const bottomOf=p=>p.y+p.glyph.bounds[3]*p.scale;
assert.equal(topOf(period),punct.baseline);
assert.ok(bottomOf(comma)>punct.baseline);
assert.ok(bottomOf(quote)<topOf(o));
assert.ok(topOf(underscore)>punct.baseline);
const escaped=svg(layout('<&>"',glyphs),'<&>"');
assert.ok(escaped.includes('<title>&lt;&amp;&gt;&quot;</title>'));
assert.ok(!escaped.includes('<title><'));
const lockedSymbols=layout('Hello, World!\n19.99',glyphs,{canvasHeight:28,trimInk:true,padding:0});
assert.equal(lockedSymbols.height,28);
console.log('All printable keyboard characters, punctuation positions, escaping and locked-height layout passed.');

// v2: uppercased text over the UPPER and Numbers glyphs, with v1 symbols filling gaps.
{
 const covered=new Set(v2.map(g=>g.character));
 const merged=v2.concat(glyphs.filter(g=>g.kind!=='lowercase'&&!covered.has(g.character)));
 const text='Hash 1'.toUpperCase();
 const result=layout(text,merged);
 assert.equal(result.placements[0].glyph.icon_id,'letter-h-uppercase');
 assert.equal(result.placements[0].glyph.geometry_policy,'grid-centerline-15x19');
 assert.equal(result.placements[1].glyph.icon_id,'letter-a-uppercase');
 assert.equal(result.placements[1].glyph.geometry_policy,'grid-centerline-15x19');
 assert.equal(result.placements[1].glyph.body_height,15);
 assert.equal(result.placements[3].glyph.icon_id,'letter-h-uppercase');
 assert.equal(result.placements[4].glyph.kind,'digit');
 for(const p of result.placements)assert.ok(Math.abs(p.glyph.body_height*p.scale-52)<1e-8);
 const wide=layout('W',merged),narrow=layout('I',merged);
 assert.ok(wide.placements[0].width>narrow.placements[0].width);
 const native=layout('A1',merged,{xHeight:15*36/52,capHeight:15,canvasHeight:19,trimInk:true,padding:0});
 assert.equal(native.height,19);
 assert.throws(()=>layout('a',v2),/Unsupported/);
}
console.log('typeface cjs ok');

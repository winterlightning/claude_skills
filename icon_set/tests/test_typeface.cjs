const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const {layout,svg}=require('../scripts/templates/text-combine.js');
const {glyphs}=JSON.parse(fs.readFileSync(path.join(__dirname,'../dist/gallery/typeface.json'),'utf8'));
assert.equal(glyphs.length,63);
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

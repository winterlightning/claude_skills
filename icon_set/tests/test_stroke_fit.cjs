const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const context={window:{}};
vm.runInNewContext(fs.readFileSync(__dirname+'/../scripts/templates/stroke-fit.js','utf8'),context);
const {bounds,fit,monotoneSegments}=context.window.StrokeFit;
const target=[8,4,40,44];
const curve={kind:'bezier',element_id:'curve',start:[10,10],end:[38,38],segments:[[[0,40],[48,8],[38,38]]]};
const original=JSON.stringify(curve),result=fit([curve],target),b=bounds(result);
assert.ok(result[0].segments.length>1,'Interior extrema become explicit knots');
assert.deepEqual([b.x-2,b.y-2,b.x+b.width+2,b.y+b.height+2],target);
assert.equal(JSON.stringify(curve),original);
assert.ok([result[0].start,result[0].end,...result[0].segments.map(s=>s[2])].flat().every(Number.isInteger));
assert.equal(JSON.stringify(fit(result,target)),JSON.stringify(result),'Repeated fitting is stable');
const reverse={...curve,start:curve.end,end:curve.start,segments:[[curve.segments[0][1],curve.segments[0][0],curve.start]]};
const reversed=fit([reverse],target)[0];
assert.deepEqual(JSON.parse(JSON.stringify(reversed.start)),JSON.parse(JSON.stringify(result[0].end)));
assert.deepEqual(JSON.parse(JSON.stringify(reversed.end)),JSON.parse(JSON.stringify(result[0].start)));
// A split preserves the original curve before any intentional grid adjustment.
const halves=monotoneSegments([curve.start,...curve.segments[0]]);
assert.equal(halves[0][0],curve.start);assert.deepEqual(halves.at(-1)[3],curve.end);
for(let i=1;i<halves.length;i++)assert.deepEqual(halves[i-1][3],halves[i][0]);
// General SVG radii correction and sweep bounds agree with the known semicircle.
const arc={kind:'arc',element_id:'arc',start:[4,16],end:[28,16],radius_x:6,radius_y:6,large_arc:false,sweep:true};
const a=bounds([arc]);assert.ok(Math.abs(a.width-24)<1e-9);assert.ok(Math.abs(a.height-12)<1e-9);
assert.throws(()=>fit([{kind:'line',element_id:'flat',start:[2,2],end:[2,10]}],target),/flat dimension/);
assert.throws(()=>fit([curve],[8.1,4,40,44]),/whole-grid/);
console.log('Exact curve extrema, snapped knots, arc bounds, and repeat-fit stability passed.');

import test from 'node:test';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import {readFileSync} from 'node:fs';
const require = createRequire(import.meta.url);
const C = require('../../scripts/templates/combine.js');
const P = require('../../scripts/templates/container-placement.js');
const S = require('../../scripts/templates/combine-side.js');
const fixture = JSON.parse(readFileSync(new URL('./container-cutout-fixture.json', import.meta.url)));
const key = 'container/universal-prohibited-symbol';
const item = (symbol, layout = [{x:18,y:18,w:28,h:28,scope:'pair'}]) => ({reference_id:'pair', parts:[
  {role:'container',icon:key}, {role:'symbol',icon:symbol,layout}
]});
const group = (svg, id) => C.parse(svg).children.find(n => n.attrs?.id === id);
const mainSvg = result => C.serialize({tag:'svg',attrs:{viewBox:'0 0 64 64'},children:[group(result.svg,'container')]});

for (const [symbolKey, symbol] of Object.entries(fixture.symbols)) test('64px slash gap survives edit/save/reopen: '+symbolKey, () => {
  const row = item(symbolKey);
  const initial = P.placementOf(row);
  assert.equal(initial.overlay,true,'legacy saved boxes must recover the confirmed overlay mode');
  const before = C.container(fixture.main,symbol,initial);
  const editedPlacement = {...initial,box:{x:20,y:16,w:24,h:28},pinned:true};
  const edited = C.container(fixture.main,symbol,editedPlacement);
  assert.notEqual(mainSvg(before),mainSvg(edited),'the gap follows moved/resized symbol geometry');
  // Independent clearance check: no retained main-segment midpoint may remain in the side renderer's erasure area.
  const placed = S.engineSegments(C.serialize({tag:'svg',attrs:{viewBox:'0 0 64 64'},children:[group(edited.svg,'symbol')]}));
  const rings = placed.map(([a,b]) => S.capsule(a,b,8));
  const hull = S.internals.hull(placed.flat());
  if(hull) rings.push(hull);
  const area = new S.internals.Area(rings);
  const segments = S.engineSegments(mainSvg(edited));
  assert.ok(segments.length,'container is not erased entirely');
  assert.ok(S.engineSegments(fixture.main).some(([a,b])=> area.locate([(a[0]+b[0])/2,(a[1]+b[1])/2])===1),'unclipped baseline overlaps the symbol');
  for(const [a,b] of segments) assert.notEqual(area.locate([(a[0]+b[0])/2,(a[1]+b[1])/2]),1,'retained stroke is outside the gap');
  const unclipped = C.container(fixture.main,symbol,{...editedPlacement,overlay:false});
  assert.deepEqual(group(edited.svg,'symbol'),group(unclipped.svg,'symbol'),'cutout never changes symbol paths');
  row.parts[1].layout=P.builtLayout(edited.layout.symbol,editedPlacement);
  assert.equal(row.parts[1].layout[0].overlay,true);
  const reopened=C.container(fixture.main,symbol,P.placementOf(JSON.parse(JSON.stringify(row))));
  assert.equal(reopened.svg,edited.svg);
  assert.equal(C.serialize(C.parse(edited.svg)),edited.svg,'serialized gap uses explicit path geometry');
  assert.doesNotMatch(edited.svg,/<(?:mask|clipPath)|fill-rule=/);
});

test('overlay follows confirmed container identity, across placement scopes, without leaking to replacements',()=>{
  for(const layout of [null,[{x:18,y:18,w:28,h:28}], [{x:18,y:18,w:28,h:28,scope:'container',container:{center:[32,32],size:null}}]]) {
    const row=item('symbol/boot-sub32',layout);
    assert.equal(P.placementOf(row).overlay,true);
    assert.equal(P.placementOf(row,{},false).overlay,true);
    assert.equal(P.placementOf(row,{symbol:'symbol/replacement'}).overlay,true);
  }
  const saved=item('symbol/boot-sub32',[{x:18,y:18,w:28,h:28,scope:'pair',overlay:true}]);
  assert.equal(P.placementOf(saved,{container:'container/other'}).overlay,undefined);
  saved.parts[1].layout[0].overlay=false;
  assert.equal(P.placementOf(saved).overlay,false,'an explicit saved choice is retained');
  saved.parts[0].icon='container/other'; delete saved.parts[1].layout[0].overlay;
  assert.equal(P.placementOf(saved).overlay,undefined,'ordinary containment is unchanged');
});

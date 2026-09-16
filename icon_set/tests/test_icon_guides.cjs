const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const {execFileSync} = require('node:child_process');
const contracts = JSON.parse(execFileSync('python3', ['-c', 'import json; from icon_set.model import contracts; print(json.dumps({"profile": contracts.icon_profile(), "keyshapes": contracts.keyshapes()}))'], {cwd:__dirname+'/../..',encoding:'utf8'}));
class Element {
  constructor(tag){this.tag=tag;this.attrs={};this.children=[];this.style={};}
  setAttribute(key,value){this.attrs[key]=value;}
  append(child){this.children.push(child);}
  querySelector(){return null;}
}
const context = vm.createContext({window:{},fetch:async()=>({ok:true,json:async()=>contracts}),document:{createElementNS:(_,tag)=>new Element(tag)}});
vm.runInContext(fs.readFileSync(__dirname+'/../scripts/templates/icon-guides.js','utf8'),context);
(async()=>{
  const guides = context.window.IconGuides;
  await guides.ready;
  for(const [profile,shapes] of Object.entries(contracts.keyshapes.resolved)){
    for(const [keyshape,shape] of Object.entries(shapes)){
      const icon={profile,keyshape,keyshape_bounds:[0,0,1,1]}; // A stale build must not redefine today's profile.
      assert.deepEqual([...guides.resolve(icon).bounds],shape.visible_bounds);
      const canvas=new Element('span');guides.mount(canvas,icon);
      const size=contracts.profile.profiles[profile].canvas_size;
      assert.equal(canvas.children[0].attrs.viewBox,`0 0 ${size} ${size}`);
      assert.ok(decodeURIComponent(canvas.style.backgroundImage).includes(`viewBox="0 0 ${size} ${size}"`));
      assert.equal(canvas.children[0].children[0].tag,keyshape==='CIRCLE'?'ellipse':'rect');
    }
  }
  const free={profile:'SOLO48',keyshape:'FREE',keyshape_bounds:[3,8,27,42]};
  assert.deepEqual([...guides.resolve(free).bounds],[3,8,27,42]);
  assert.equal(guides.envelope(free).attrs.x,3);
  assert.equal(guides.envelope({profile:'SOLO48'}),null);
  assert.equal(guides.label({profile:'SOLO48',keyshape:'HRECT_M'}),'HRECT_M · 44 × 32 · SOLO48');
  console.log('All profile keyshapes, circle/rectangle guides, exact canvas grids, and off-center FREE bounds passed.');
})().catch(error=>{console.error(error);process.exitCode=1;});

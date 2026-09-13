// Run with: node icon_set/tests/test_laboratory_ui.cjs
const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict');
class Element {
 constructor(tag='div'){this.tag=tag;this.children=[];this.value='';this.dataset={};this.attrs={};this.checked=true;}
 append(...items){this.children.push(...items);}
 replaceChildren(...items){this.children=items;}
 setAttribute(key,value){this.attrs[key]=String(value);}
 addEventListener(){}
}
const elements=new Map(),document={getElementById(id){if(!elements.has(id))elements.set(id,new Element());return elements.get(id);},createElement:tag=>new Element(tag),createElementNS:(_,tag)=>new Element(tag)};
const root=path.join(__dirname,'..');
const data={profile:JSON.parse(fs.readFileSync(path.join(root,'model/contracts/icon-profile.v1.json'))),keyshapes:JSON.parse(fs.readFileSync(path.join(root,'model/contracts/keyshapes.v1.json')))};
const icons=[{key:'solo/example',name:'Example',icon_id:'example',profile:'SOLO48',family:'solo',keyshape:'VRECT_L',preview_url:'../solo48/example.svg'}];
const context=vm.createContext({document,URL,URLSearchParams,location:{href:'http://localhost/gallery/icon-laboratory.html',search:''},history:{replaceState(){}},data,fixtureIcons:icons});
const run=code=>vm.runInContext(code,context);
run(fs.readFileSync(path.join(root,'scripts/templates/icon-laboratory.js'),'utf8').replace(/loadLaboratory\(\);\s*$/,''));
run("contracts=data;icons=fixtureIcons;$('gap').value='2';selectProfile('SOLO48');");
assert.equal(elements.get('sizeTitle').textContent,'36 × 48');
assert.equal(elements.get('inspectLink').hidden,false);
assert.equal(elements.get('atlas').children.length,10);
assert.equal(elements.get('ruleCards').children.length,6);
assert.ok(elements.get('drawing').children[0].children.some(child=>child.tag==='image'));
run("$('showIcon').checked=false;renderDrawing()");
assert.ok(!elements.get('drawing').children[0].children.some(child=>child.tag==='image'));
for(const profile of Object.keys(data.profile.profiles)) {
 context.nextProfile=profile;
 run('selectProfile(nextProfile)');
 for(const name of Object.keys(data.keyshapes.resolved[profile])) {
  context.nextShape=name;
  run('shapeName=nextShape;renderShapes();renderExamples();');
  const shape=data.keyshapes.resolved[profile][name];
  assert.equal(elements.get('sizeTitle').textContent,`${shape.width} × ${shape.height}`);
  assert.equal(elements.get('drawing').children.length,1);
 }
}
run("selectProfile('SUB32');");
assert.equal(elements.get('example').disabled,true);
assert.equal(elements.get('inspectLink').hidden,true);
run("$('gap').value='1';renderGap();");
assert.equal(elements.get('gapResult').dataset.valid,'false');
run("$('gap').value='2';renderGap();");
assert.equal(elements.get('gapResult').dataset.valid,'true');
console.log('Laboratory: all 30 envelopes, family switching, artwork layers, empty examples, and spacing thresholds passed.');

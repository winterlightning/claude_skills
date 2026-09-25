const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const opened=[],events={};
const node=(tag,cls,text)=>({tag,cls,text,children:[],append(...children){this.children.push(...children)},setAttribute(){}});
const c=vm.createContext({URLSearchParams,location:{search:''},document:{addEventListener(){}},node,
 window:{addEventListener:(name,fn)=>events[name]=fn,SideComponentEditor:{open:async(d,label)=>opened.push([d.key,label])}}});
vm.runInContext(fs.readFileSync('icon_set/scripts/templates/side-pairs-grid.js','utf8'),c);
vm.runInContext(`sideComponents={mains:[{id:'m',source_ids:['alias'],drawings:[{key:'solo/a',icon_id:'a',profile:'SOLO48'},{key:'solo/b',icon_id:'b',profile:'SOLO48'}]}],subs:[{id:'s',source_ids:[],drawings:[{key:'sub/s',icon_id:'s',profile:'SUB32'}]}]};`,c);
assert.equal(vm.runInContext("sideEditableDrawing({main_id:'alias'},'main',{model_key:'solo/b',icon:'b'}).key",c),'solo/b');
assert.equal(vm.runInContext("sideEditableDrawing({main_id:'m'},'main',null).key",c),'solo/a');
assert.equal(vm.runInContext("sideEditButton({main_id:'unknown'},'main',null)",c),null);
assert.equal(vm.runInContext("sideEditableDrawing({main_id:'m'},'main',{icon:'different'})",c),undefined);
(async()=>{
 const main=vm.runInContext("sideEditButton({main_id:'m'},'main',{model_key:'solo/b',icon:'b'})",c);
 const sub=vm.runInContext("sideEditButton({sub_id:'s'},'sub',null)",c);
 assert.equal(main.children[0].text,'Edit main icon');assert.equal(sub.children[0].text,'Edit sub icon');
 await main.children[0].onclick();await sub.children[0].onclick();
 assert.deepEqual(opened,[['solo/b','Main · b'],['sub/s','Sub · s']]);
 assert.equal(main.children[0].disabled,false);
 vm.runInContext("sideComponents.subs[0].drawings[0].profile='TEXT_NATIVE_V2'",c);
 assert.equal(vm.runInContext("sideEditButton({sub_id:'s'},'sub',null)",c),null);
 assert.equal(typeof events['side-component-approved'],'function');
 console.log('Side pair edit buttons target the displayed variant, support failed drawings, and skip missing/native text.');
})().catch(error=>{console.error(error);process.exitCode=1;});

import test from 'node:test';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import {mkdtempSync, writeFileSync, rmSync} from 'node:fs';
import {tmpdir} from 'node:os';
import path from 'node:path';
import {keyshapeCheck, presetBoxes} from '../../scripts/side_keyshape_check.mjs';
const Side = createRequire(import.meta.url)('../../scripts/templates/combine-side.js');
const svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 19" fill="none" stroke="currentColor" stroke-width="4"><path d="M2 2H26V17H2Z"/></svg>';
const form = {icon:'label', family:'text', model_key:'text/label', native_text:true, sizing_mode:'typeface-native', document:svg, bounds:[2,2,26,17], canvas:28, canvas_width:28, canvas_height:19, sha256:Side.sha256(svg)};
const main = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="4"><path d="M6 6H42V42H6Z"/></svg>';
const pair = key => ({reference_id:'p',parts:[{role:'main',icon:'solo/main'}, {role:'sub',icon:key,position:'br',form}]});
const drawings = new Map([['solo/main',{svg:main,svg_sha256:Side.sha256(main)}],['text/label',{svg,svg_sha256:Side.sha256(svg)}]]);

test('linking native text for review preserves its exact artwork and native size',()=>{
  const legacy=Side.pairRequest(pair(null),drawings), linked=Side.pairRequest(pair('text/label'),drawings);
  assert.equal(linked.svg,legacy.svg);
  assert.equal(linked.request.parts.sub.icon,'text/label');
  assert.equal(linked.request.parts.sub.svg_sha256,Side.sha256(svg));
});
test('changed native text is never silently built from a stale form',()=>{
  const changed=new Map(drawings);changed.set('text/label',{svg:svg.replace('H26','H24'),svg_sha256:'changed'});
  assert.throws(()=>Side.pairRequest(pair('text/label'),changed),/native text drawing changed/);
});
test('native text requires canvas containment and unchanged anchored glyph size',()=>{
  const dir=mkdtempSync(path.join(tmpdir(),'native-text-keyshape-'));
  try {
    writeFileSync(path.join(dir,'item.json'),JSON.stringify(pair('text/label')));
    writeFileSync(path.join(dir,'elements.json'),JSON.stringify({main:[{source:[6,6,42,42]}],sub:[{source:[2,2,26,17]}]}));
    const layout={position:'br',main:[{paths:[0],x:6,y:6,w:36,h:36}],sub:[{paths:[0],x:34,y:43,w:24,h:15}]};
    assert.equal(keyshapeCheck(dir,layout).ok,true);
    assert.equal(keyshapeCheck(dir,layout).canvas.keyshape,'SQUARE');
    assert.equal(keyshapeCheck(dir,{...layout,sub:[{...layout.sub[0],x:36,y:45}]}).ok,false);
    assert.equal(keyshapeCheck(dir,{...layout,sub:[{...layout.sub[0],w:20}]}).ok,false);
    assert.ok(presetBoxes(dir,'sub','br').every(p=>p.box.split(',').slice(2).join(',')==='24,15'));
  } finally {rmSync(dir,{recursive:true,force:true});}
});

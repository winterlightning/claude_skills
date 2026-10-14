import {afterEach, expect, test, vi} from 'vitest';
import {cleanup, render, fireEvent} from '@testing-library/svelte';
import CombinedReview from '../src/components/CombinedReview.svelte';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
afterEach(() => { cleanup(); vi.unstubAllGlobals(); delete window.SideRepairFlags; });
const text = {native_text:true, model_key:'text/label', family:'text', icon:'label', document:'<svg/>', sha256:'text-sha', canvas_width:44, canvas_height:19};
const pair = {reference_id:'p', concept:'Text pair', parts:[
  {role:'main', icon:'solo/main', current_sha:'main-sha', built_sha:'main-sha', part_reference_id:'m'},
  {role:'sub', icon:'text/label', current_sha:'text-sha', built_sha:'text-sha', form:text, part_reference_id:'s', position:'br'}],
  icon:{key:'side_combination64/p', svg_sha256:'combined-sha'}};
function setup(change = p => p) {
  const item = change(structuredClone(pair));
  const store = {version:0, item:() => item, reviews:{'solo/main':'approve','text/label':'approve'}, refresh:vi.fn()};
  const rendered = render(CombinedReview, {store, pair:{id:'p'}, main:{model_key:'solo/main'}, sub:text});
  return {...rendered, store};
}
test('missing linked text cannot inherit approval from its form key', () => {
  const {getByRole} = setup(p => {p.parts[1].icon=null;return p;});
  expect(getByRole('button', {name:'Approve'}).disabled).toBe(true);
});
test('approved text still requires rebuilding the combined drawing', () => {
  const {getByRole} = setup(p => {p.parts[1].built_sha=null;return p;});
  const button=getByRole('button', {name:'Approve'});
  expect(button.disabled).toBe(true);
  expect(button.title).toContain('Recombine');
});
test('rebuilt pair approves the exact combined revision', async () => {
  const fetch=vi.fn().mockResolvedValue({ok:true,json:async()=>({saved:true})});vi.stubGlobal('fetch',fetch);
  const {getByRole}=setup();
  await fireEvent.click(getByRole('button', {name:'Approve'}));
  expect(JSON.parse(fetch.mock.calls[0][1].body)).toEqual({icon:'side_combination64/p',svg_sha256:'combined-sha',status:'approve'});
});
test('linked native text retains its dimensions and native form on the Side page', async () => {
  const context={window:{}, URLSearchParams, fetch:async path=>({ok:true,json:async()=>path.startsWith('/api/combinations?')?{items:[pair],total:1}:path==='/api/side-components'?{mains:[],subs:[]}: {}})};
  vm.runInNewContext(readFileSync('../icon_set/scripts/templates/side-pairs-data.js','utf8'),context);
  const data=await context.window.SideData.load();
  const shown=data.pairs.get('p');
  expect(shown.native_text).toBe(true);
  expect(shown.custom).toBe(false);
  expect(shown.subs[0].document).toBe(text.document);
  expect(shown.subs[0].canvas_width).toBe(44);
});

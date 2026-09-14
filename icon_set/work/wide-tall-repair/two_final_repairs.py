from more_repairs import *
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/wide-tall-repair/targets.json'
AUTHOR='gpt-6'
for id in ['ribbon-bow-with-tails','open-end-maintenance-wrench']:
 f=W/'candidates'/f'{id}.json';x=json.loads(f.read_text());r=x['record']
 if x.get('two_final'):continue
 if id.startswith('ribbon'):
  move(r,lambda x,y:(15,23) if (x,y)==(17,22) else (33,23) if (x,y)==(31,22) else (x,y));x['manual_note']+=' Spread the tail attachment nodes on the bow return edges.'
 else:
  reset(r,'VRECT_L');line(r,'outer-left',(8,4),(8,16));arc(r,'outer-bottom-left',(8,16),(24,32),16,16,False);arc(r,'outer-bottom-right',(24,32),(40,16),16,16,False);line(r,'outer-right',(40,16),(40,4));line(r,'right-tip',(40,4),(31,4));line(r,'inner-right',(31,4),(31,16));arc(r,'jaw-recess',(31,16),(17,16),7);line(r,'inner-left',(17,16),(17,4));line(r,'left-tip',(17,4),(8,4));contour(r,'jaw',*[p['element_id'] for p in r['primitives']],closed=True);line(r,'handle',(24,32),(24,44));rel(r,'jaw','handle');x['manual_note']='Reauthored upright with a broad open jaw, concentric circular returns, and a simple round-ended handle to preserve the wrench without narrow internal bands.'
 x['two_final']=True;q=check(f,x);print(id,q['status'],q['internal_spacing']['status'],q['errors']+q['warnings'],q['internal_spacing'].get('findings'),flush=True)

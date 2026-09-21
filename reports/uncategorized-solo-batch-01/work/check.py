import importlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
BATCH=ROOT/'reports/uncategorized-solo-batch-01'
entries=json.loads((BATCH/'manifest.json').read_text())['entries']
p=json.loads((BATCH/'progress.json').read_text())
p['model']='gpt-6-astra';p['author']='gpt-6-astra'
blocked={2:'Blank application panel is an enclosure; route to icon-container.',3:'Directional arrow glyph; route to icon-sub.',4:'Directional arrow glyph; route to icon-sub.',5:'Directional arrow glyph; route to icon-sub.',6:'Directional arrow glyph; route to icon-sub.',9:'Car plus separate reusable sensor-wave modifier; requires a component split.',10:'Vehicle plus separate reusable signal-wave modifier; requires a component split.'}
for e in entries:
 if len(sys.argv)>1 and e['number'] not in map(int,sys.argv[1:]): continue
 n=e['number'];r=dict(e);r['usage']=dict(p['usage']);r['source_visual_review']='Source rendered and inspected in numbered contact sheet.'
 if n in blocked:
  r.update(outcome='blocked',reason=blocked[n],module=None,validation=None,visual_review='Source triage only; no output generated.')
 else:
  path='icon_set/model/icons/solo/'+(e['icon_id']+'_'+e['source_uuid']).replace('-','_')+'.py'
  r['module']=path
  try:
   icon=create(e['icon_id']); report=icon.validate_icon()
   r.update(outcome='in-progress',validation={'status':report.status,'description':report.describe()},visual_review='Pending authored-output review.')
   (BATCH/'work'/f'{n:02}-validation.txt').write_text(report.describe())
   print(n,report.describe(),flush=True)
  except Exception as exc:
   r.update(outcome='in-progress',validation={'status':'error','description':str(exc)},visual_review='Pending authored-output review.');print(n,type(exc).__name__,str(exc),flush=True)
 p['entries']=[x for x in p['entries'] if x['number']!=n]+[r]
 p['entries'].sort(key=lambda x:x['number'])
 (BATCH/'progress.json').write_text(json.dumps(p,indent=2)+'\n')

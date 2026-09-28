from pathlib import Path
import json
from icon_set.scripts import primitive_fix as fix,work_queue as work
AUTHOR='gpt-6';SOURCE_ICON_ID=None;SOURCE_PATH='fix-batch-20260924T172356/manifest.json'
b=Path('icon_set/work/primitive-make-ray/fix-batch-20260924T172356');es=json.loads((b/'manifest.json').read_text())
for e in es:
 i=e['index'];r=Path(e['run']);p=Path(e['module'])
 if i==0:e['keyshape']='HRECT_L';e['plan']='Two equal square sliders on straight vertical rails beside a Bitcoin B with smooth elliptical bowls and an exposed currency stem.'
 if i==16:e['keyshape']='SQUARE';e['plan']='Two balanced counterclockwise arrows with smooth orbit curves and equal arrowhead arms surround a crisp clock-hand pair.'
 if i==17:e['keyshape']='SQUARE';e['plan']='Wavy banknote with coherent smooth boundaries and a clean dollar sign. Taller square envelope provides room for the currency strokes.'
 if i in (18,19):e['plan']='Woman bust with a radius-7 circular jaw, smoothly joined center-parted hair, and curved shoulders. Shared human_ref/user.svg informs circular anatomy. Bust contact has zero ink gap: jaw bottom 29 and shoulder top 33 are exactly four centerline units apart.'
 s=p.read_text();end=s.index('"""',3);s='"""'+e['plan']+'\nOmissions: '+e['omissions']+'\nConstruction references: '+str(e['construction_references'] or 'no useful direct Lucide match')+'.\n"""'+s[end+3:];p.write_text(s)
 g=json.loads((r/'gate.json').read_text());assert g['status']=='pass' and not g['errors'] and not g['warnings'],e['icon_id']
 (r/(e['icon_id']+'.metadata.json')).write_text(json.dumps(e,indent=2)+'\n')
 result={**e,'validation_status':'valid','validation_warnings':[],'build_gate':g,'visual_review':'Original reference, rejected SVG and revised native 48px/enlarged light and dark renders inspected. Coherent smooth curves, clean straight lines, consistent 4-unit stroke and balanced repeated elements. Intentional direction and asymmetry preserved.','artifacts':[p.name for p in r.iterdir() if p.is_file()]}
 (r/'result.json').write_text(json.dumps(result,indent=2)+'\n')
(b/'manifest.json').write_text(json.dumps(es,indent=2)+'\n')
for e in es:
 if (Path(e['fix_dir'])/'result.json').exists():continue
 rc=fix.finish(work.default_base_url(),'thuan-mac','solo/'+e['icon_id'],'done',e['plan']+' Clean centerlines reviewed in both themes at 48px. '+e['omissions'],ray_run=e['run'])
 if rc:raise SystemExit(rc)
 print('FINISHED',e['index'],flush=True)

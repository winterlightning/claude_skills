from pathlib import Path
import json,sys,subprocess,os,importlib.util
from icon_set.scripts.primitive_fix import load_icon
batch=Path(__file__).parent
runs=sorted(Path('icon_set/work/primitive-make-ray').glob('*/20260924T071000Z-thuan-mac'))
notes={
'girl-pigtails':'Rebuilt a smooth symmetric body arch and paired hair curves; retained round head and exact detached gap.',
'microphone-b72da6ab':'Replaced fragmented capsule and cradle with tangent semicircles; removed crowded grille notch.',
'oval-stadium-with-two-flags':'Rebuilt stadium rim and wall with coherent curves and exact pole attachment nodes; restored triangular flags; omitted crowded field arc.',
'peace-symbol':'Restored an exact circular rim and centered stem with paired diagonal branches.',
'pear-with-two-crossbars-on-diagonal-mark':'Smoothed pear shoulders using tangent arc pairs and rebalanced the two crossbars; leaf omitted for spacing.',
'people-giving-high-five':'Rebuilt mirrored curved raised arms and shoulders, retaining exact detached head spacing and shared hand contact.',
'person-silhouette-wavy':'Smoothed the round crown and shoulder joins while preserving the continuous neck silhouette.',
'person-using-laptop':'Rebuilt smooth back and head, corrected head/body clearance, and made laptop/arm contacts exact.',
'person-with-angular-heart-torso':'MIC head/heart warning: exact diagonal gap sqrt(12^2+16^2)-6-6=8 centerline (4 ink) is not certified; preserving the required human gap leaves review status. Rounded-heart attempt retained for manual review.',
'person-with-jagged-open-head':'Rebuilt smooth jaw and symmetric shoulders around the jagged head; removed peripheral rays and shirt mark for space.',
'radiating-gear':'Replaced square cross-like gear with six repeated teeth and evenly spaced cardinal rays reduced to dots.',
'recycle-arrows':'Rebuilt three coherent arrow strokes and opened inter-arrow spacing while preserving clockwise flow.',
'red-blood-cell-strem-1':'Replaced fragmented curves with tangent circular quarters for the diagonal cell and central depression.',
'red-blood-cell-three':'Replaced irregular segments with three clean ovals; retained triangular arrangement and simplified small tilts.',
'sauna-heat-stone':'Rebuilt three equal smooth two-arc heat waves and a symmetric elliptical stone bowl.',
'shield-9d1518e9':'Rebuilt shield with four symmetric circular arcs, replacing fractional fragmented curves.',
'shield-ba7b0c51':'Rebuilt shield with four symmetric circular arcs, replacing fractional fragmented curves.',
'shottkey-diode':'Rebuilt a clean diagonal rectangular component with centered leads and round joins.',
'skull-85266d86':'Rebuilt smooth circular cranium and symmetric cheeks; opened tooth clearance.',
'smart-glasses-with-raised-temple-arms':'Rebuilt mirrored temple curves with smooth horizontal tip joins while retaining the broad frame and nose bridge.'}
records=[]
for out in runs:
 meta=json.loads(next(out.glob('*.metadata.json')).read_text());name=meta['icon_id'];module=next(out.glob('*.py'));icon=load_icon(module);r=icon.validate_icon()
 outcome='done' if r.status=='valid' and not r.warnings else 'cannot-fix'
 note=notes[name]
 record={**meta,'key':'solo/'+name,'result_dir':str(out),'module':module.name,'svg':name+'.svg','keyshape':icon.keyshape.name,'validation_status':r.status,'validation_errors':r.errors,'validation_warnings':r.warnings,'visual_review':('Reviewed light and dark at native 48px and enlarged size; coherent curves, preserved defining arrangement and readable negative space.' if outcome=='done' else 'Manual review required: heart/body contour remains a constrained approximation with uncertified exact diagonal head clearance.'),'findings':note,'references_and_omissions':module.read_text().split('"""')[1],'outcome_requested':outcome,'artifacts':[p.name for p in sorted(out.iterdir()) if p.is_file() and p.name!='result.json']}
 (out/'result.json').write_text(json.dumps(record,indent=2)+'\n')
 records.append(record)
(batch/'manifest.json').write_text(json.dumps(records,indent=2)+'\n')
if '--upload' in sys.argv:
 for r in records:
  cmd=['python3','icon_set/scripts/primitive_fix.py','--worker','thuan-mac','finish','--icon',r['key'],'--run',r['result_dir'],'--outcome',r['outcome_requested'],'--note',r['findings']]
  p=subprocess.run(cmd,env={**os.environ,'SSL_CERT_FILE':'/etc/ssl/cert.pem'},text=True,capture_output=True)
  (batch/(r['icon_id']+'.finish.log')).write_text(p.stdout+p.stderr)
  print(r['key'],p.returncode,p.stdout.strip()[-500:],p.stderr.strip()[-500:],flush=True)

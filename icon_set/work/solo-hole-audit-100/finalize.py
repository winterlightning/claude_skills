from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-hole-audit-100/repairs.json'
AUTHOR='gpt-6'
W=Path(__file__).parent;B=ROOT/'icon_set/work/solo-failed-batch-100'
repairs=json.loads((W/'repairs.json').read_text());by_parent={r['parent']:r for r in repairs}
path=ROOT/'icon_set/model/contracts/spacing-reviews.v1.json';records=json.loads(path.read_text())
for parent in by_parent:records['icons'].pop('solo/'+parent,None)
# Existing visual decisions survive only if their exact drawing and pairs still
# match, and both the certified model and newly corrected hole/pinch gate pass.
for key,record in records['icons'].items():
 i=create(key.split('/',1)[1]);q=inspect_icon(i)
 assert i.validate_icon().status=='valid',key
 assert q['negative_space']['status']=='pass',key
 assert q['svg_sha256']==record['svg_sha256'],key
 assert {tuple(sorted(f['elements'])) for f in q['internal_spacing']['findings']}=={tuple(sorted(p)) for p in record['elements']},key
 record['rules_sha256']=q['rules_sha256'];record['hole_recheck']='2026-09-15: authored-stroke pinch check passed.'
path.write_text(json.dumps(records,indent=2)+'\n')
rows=json.loads((B/'review-decisions.json').read_text());oldrepairs=json.loads((B/'repairs.json').read_text());reasons={
'brick-firewall-v3':'Open the flame valley and merge the cramped counter into one broad opening.',
'crouching-mouse-v2':'Pull the curled tail clear of the back and belly, with a real shared attachment at the rump.',
'diver-beside-marker-buoy-v2':'Open the filled head circle, keep the exact head-to-body gap, and separate the flag from the float.',
'error-404-xxx-label-v2':'Open the left numeral four and rebalance the zero to remove the hidden pinched counter.'}
for row in rows:
 current=row.get('replacement',row['icon_id'])
 if current not in by_parent:continue
 r=by_parent[current];row.update(replacement=r['icon_id'],decision='reconstructed',reason=reasons[r['icon_id']])
 entry=dict(number=row['number'],parent=row['icon_id'],icon_id=r['icon_id'],file=r['file'])
 oldrepairs=[e for e in oldrepairs if e['number']!=row['number']]+[entry]
(B/'review-decisions.json').write_text(json.dumps(rows,indent=2)+'\n');(B/'repairs.json').write_text(json.dumps(oldrepairs,indent=2)+'\n')
p=B/'make_report.py';s=p.read_text()
s=s.replace("26:'Widen the right flame lobe by two units to open its small counter.'", "26:'Open the flame valley to create one broad counter.'")
s=s.replace("notes={", "notes={46:'Pull the curled tail clear of the back and belly.',58:'Open the head circle and clear the flag/float spacing.',70:'Open the left four and rebalance the zero to eliminate the hidden pocket.',")
s=s.replace('16 reconstructed','19 reconstructed').replace('84 preserved','81 preserved').replace('84 retained','81 retained').replace('16 originals','19 originals').replace('16 original','19 original').replace('The 16','The 19').replace('Only the flame lobe and chairlift elbow change visibly.','The flame, mouse tail, diver, 404 label and chairlift include visible geometry repairs.')
p.write_text(s)
print('Renewed',len(records['icons']),'unchanged visual decisions after the corrected hole/pinch gate.')

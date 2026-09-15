from pathlib import Path
import sys,json,hashlib,collections,re,csv,datetime
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import factories
W=Path(__file__).parent;D=ROOT/'icon_set/dist';registered=factories();summary={};rows=[]
for family,folder in [('solo','solo48'),('container','container64'),('sub','sub32')]:
 passed=json.loads((D/folder/'manifest.json').read_text())['icons'];failed=json.loads((D/'failed'/folder/'manifest.json').read_text())['icons'];allids={i for i,f in registered.items() if f.family==family}
 assert {r['icon_id'] for r in passed}|{r['icon_id'] for r in failed}==allids,(family,'coverage')
 overlaycounts=collections.Counter();failcounts=collections.Counter()
 for ident in sorted(allids):
  raw=(W/'inputs'/folder/(ident+'.svg')).read_bytes();sha=hashlib.sha256(raw).hexdigest();p=ROOT/'icon_set/work/qa_overlays'/folder/(ident+'.metrics.json');o=json.loads(p.read_text());assert o['svg_sha256']==sha,(ident,'overlay hash')
  assert (p.parent/(ident+'_distance_debug.png')).exists() and (p.parent/(ident+'_hole_debug.png')).exists(),(ident,'missing overlay')
  q=json.loads((D/'qa'/family/ident/'metrics.json').read_text());assert q['svg_sha256']==sha,(ident,'QA hash')
  ispass=any(r['icon_id']==ident for r in passed);file=D/(folder if ispass else 'failed/'+folder)/(ident+'.svg');assert file.exists() and hashlib.sha256(file.read_bytes()).hexdigest()==sha,(ident,'export hash')
  if ispass:assert q['status']=='pass' and o['distance_passed'] is True and o['negative_space_passed'] is True,ident
  if o.get('distance_passed') is False:overlaycounts['distance_failed']+=1
  if o.get('negative_space_passed') is False:overlaycounts['holes_or_pinches_failed']+=1
  if o.get('distance_passed') is None or o.get('negative_space_passed') is None:overlaycounts['measurement_errors']+=1
  if o.get('distance_passed') is True and o.get('negative_space_passed') is True:overlaycounts['pass']+=1
  if not ispass:
   for e in q['errors'] or q['warnings']:failcounts[e.split(':')[0].split(' [')[0]]+=1
  rows.append({'family':family,'icon':ident,'build_status':q['status'],'released':ispass,'overlay_distance_passed':o.get('distance_passed'),'overlay_holes_passed':o.get('negative_space_passed'),'lowest_distance':o.get('lowest_distance'),'failed_holes':o.get('failed_hole_count'),'pinches':o.get('pinch_count')})
 summary[family]={'total':len(allids),'released':len(passed),'failed':len(failed),'overlays':dict(overlaycounts),'finding_categories':dict(failcounts)}
result={'completed_at':datetime.datetime.now().isoformat(),'production_reference':4192,'previous_local_solo_release':5542,'families':summary,'solo_difference_from_production':summary['solo']['released']-4192,'solo_change_from_previous_release':summary['solo']['released']-5542}
(W/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
with (W/'results.csv').open('w') as f:
 writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
print(json.dumps(result,indent=2))

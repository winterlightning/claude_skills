import json,sys
from pathlib import Path
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts import work_queue as w
B=Path(__file__).parent;rows=json.loads((B/'staged.json').read_text())
results=[]
for r in rows:
 d=json.loads((Path(r['result_dir'])/'result.json').read_text())
 assert d['outcome']=='done' and d['validation_status']=='valid' and not d['validation_errors'] and not d['validation_warnings']
 assert d['build_gate']['status']=='pass' and not d['build_gate']['errors'] and not d['build_gate']['warnings'] and d['author']=='gpt-6'
 assert d['review_status']=='ready'
 results.append({'key':r['key'],'author':d['author'],'outcome':d['outcome'],'review_status':d['review_status'],'run':d['make_ray_run'],'finished_at':d['finished_at']})
d=w.call(w.default_base_url(),'GET','/api/work');keys={r['key'] for r in rows};states=[c for c in d['claims'] if c['icon'] in keys and c.get('current')]
assert len(states)==20
assert all(c['state']=='done' and c['status']=='ready' for c in states),states
(B/'verified-results.json').write_text(json.dumps({'results':results,'production':states},indent=2)+'\n')
p=B/'REPORT.md';p.write_text(p.read_text()+'\nProduction verification: all 20 current claims are done and all 20 review statuses are Ready.\n')
print('VERIFIED: 20/20 done, Ready, AUTHOR=gpt-6, valid and full gate pass; zero errors/warnings.')

"""Read-only production verification of this batch's reported outcomes."""
import json,sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT))
from icon_set.scripts import work_queue as w
HERE=Path(__file__).parent
rows=json.loads((HERE/'batch.json').read_text());base=w.default_base_url()
def get(row):return w.call(base,'GET','/api/work',query={'icon':row['key']})
with ThreadPoolExecutor(max_workers=4) as ex:
    for row,current in zip(rows,ex.map(get,rows)):
        row['verified_production']=current
        if row['production_outcome']=='done':
            f=json.loads((ROOT/row['fix']/'result.json').read_text())
            assert f.get('uploaded') and f.get('finished_at') and f['outcome']=='done'
            assert current['status'] in ('ready','approve'),(row['key'],current)
            if current['status']=='ready':assert current['work']['state']=='done'
        else:assert current['status']=='approve',(row['key'],current)
        run=ROOT/row['run'];p=run/'result.json';r=json.loads(p.read_text())
        r.update(production_outcome=row['production_outcome'],production_verification=current)
        r['artifacts']=sorted(x.name for x in run.iterdir() if x.is_file() and x.name!='result.json')
        p.write_text(json.dumps(r,indent=2)+'\n')
        print(row['key'],current['status'],current['work']['state'],flush=True)
(HERE/'batch.json').write_text(json.dumps(rows,indent=2)+'\n')
(HERE/'production-verification.json').write_text(json.dumps([r['verified_production'] for r in rows],indent=2)+'\n')

import json,sys,concurrent.futures
from pathlib import Path
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts import work_queue as w
B=Path(__file__).parent
rows=json.loads((B/'staged.json').read_text())
def check(r):
 d=w.call(w.default_base_url(),'GET','/api/work/history',query={'icon':r['key']});(B/(r['item']['icon_id']+'.history.json')).write_text(json.dumps(d,indent=2));return {'key':r['key'],'disapprovals':w.disapproval_count(d)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:results=list(ex.map(check,rows))
(B/'disapproval-audit.json').write_text(json.dumps(results,indent=2));print(results)

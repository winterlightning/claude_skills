"""Publish default 64px results for the Experiment combinations grid."""
import hashlib
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from .combination_experiment import DATA, ROOT, render


def build():
    rows=json.loads(DATA.read_text())['rows']
    folder=ROOT/'dist/gallery/combination-previews';folder.mkdir(parents=True,exist_ok=True)
    cache=ROOT/'data/combination-previews.json'
    old=json.loads(cache.read_text()) if cache.exists() else {}
    engine=''.join(p.read_text() for p in sorted((ROOT/'vendor/combination').rglob('*.py')))
    engine+=(ROOT/'scripts/combination_experiment.py').read_text()
    def one(row):
        key=hashlib.sha256((engine+json.dumps(row,sort_keys=True)).encode()).hexdigest()
        file=folder/(row['id']+'.svg')
        prior=old.get(row['id'],{})
        if prior.get('fingerprint')==key:return row['id'],prior
        result=render({'id':row['id']})
        print('Rendered '+row['concept'],flush=True)
        return row['id'],{'fingerprint':key,'url':'combination-previews/'+file.name,'result':result}
    results={}
    with ThreadPoolExecutor(max_workers=4) as pool:
        for key,item in pool.map(one,rows):
            results[key]=item
            old[key]=item
            cache.write_text(json.dumps(old))
            print(f'Prepared {len(results)} of {len(rows)} combinations', flush=True)
    cache.write_text(json.dumps(results))
    folder.mkdir(parents=True,exist_ok=True)
    for key,item in results.items():
        (folder/(key+'.svg')).write_text(item['result']['svg'])
    (ROOT/'dist/gallery/experiment-combination-results.json').write_text(json.dumps({'results':results}))
    print(f'Published {len(results)} combined icons.',flush=True)

if __name__=='__main__':build()

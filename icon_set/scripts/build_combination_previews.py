"""Publish default 64px results for the Experiment combinations grid."""
import hashlib
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from .combination_experiment import DATA, ROOT, render
from .experiment_gallery import stage_preview_combinations

if __package__:
    from .workspace import build_dist
else:
    from workspace import build_dist



def build(*, force=False):
    rows=json.loads(DATA.read_text())['rows']
    folder=build_dist(ROOT.parent) / 'gallery/combination-previews';folder.mkdir(parents=True,exist_ok=True)
    cache=ROOT/'data/combination-previews.json'
    old=json.loads(cache.read_text()) if cache.exists() else {}
    engine=''.join(p.read_text() for p in sorted((ROOT/'vendor/combination').rglob('*.py')))
    engine+=(ROOT/'scripts/combination_experiment.py').read_text()
    def one(row):
        key=hashlib.sha256((engine+json.dumps(row,sort_keys=True)).encode()).hexdigest()
        file=folder/(row['id']+'.svg')
        prior={} if force else old.get(row['id'],{})
        if prior.get('fingerprint')==key:return row['id'],prior
        # The runner previously dropped rounded_box. Uniform placements are
        # identical; only the small nonuniform rounding cases need rerendering.
        old_engine = engine.replace('            "rounded_box": bool(it.get("rounded_box")),\n', '')
        old_key = hashlib.sha256((old_engine+json.dumps(row,sort_keys=True)).encode()).hexdigest()
        if prior.get('fingerprint') == old_key:
            p = prior['result']['placements'][1]['painted_box']
            b = row['subs'][0]['bounds']
            width,height = b[2]-b[0], b[3]-b[1]
            if width <= 1e-9 or height <= 1e-9 or abs((p['w']-4)/width-(p['h']-4)/height) < 1e-9:
                return row['id'], {**prior, 'fingerprint':key}

        # Readiness labels and native download links do not alter the SVG.
        # Reuse the previous cache only when its exact pre-metadata fingerprint
        # matches; changed component lists or geometry still require rendering.
        legacy = json.loads(json.dumps(row))
        for item in legacy['subs']:
            item.pop('sub32_status', None)
            item.pop('sub32_reason', None)
            if item['family'] == 'sub':
                item.pop('export_url', None)
        legacy_key = hashlib.sha256((engine+json.dumps(legacy,sort_keys=True)).encode()).hexdigest()
        if prior.get('fingerprint') == legacy_key:
            return row['id'], {**prior, 'fingerprint': key}
        try:
            result=render({'id':row['id']}, row=row)
        except Exception as error:
            return row['id'], {'error': str(error), 'concept': row['concept']}
        print('Rendered '+row['concept'],flush=True)
        return row['id'],{'fingerprint':key,'url':'combination-previews/'+file.name,'result':result}
    results={}
    failures={}
    completed=0
    with ThreadPoolExecutor(max_workers=4) as pool:
        for key,item in pool.map(one,rows):
            completed+=1
            if 'error' in item:
                failures[key]=item
                old.pop(key,None)
                print(f'Failed {key}: {item["error"]}',flush=True)
                continue
            results[key]=item
            old[key]=item
            if len(results)%50 == 0:cache.write_text(json.dumps(old))
            print(f'Prepared {len(results)} of {len(rows)} combinations', flush=True)
    (ROOT/'data/combination-failures.json').write_text(json.dumps(failures,indent=2))
    cache.write_text(json.dumps(results))
    folder.mkdir(parents=True,exist_ok=True)
    for key,item in results.items():
        (folder/(key+'.svg')).write_text(item['result']['svg'])
    (build_dist(ROOT.parent) / 'gallery/experiment-combination-results.json').write_text(json.dumps({'results':results}))
    stage_preview_combinations(build_dist(ROOT.parent) / 'gallery')
    print(f'Published {len(results)} combined icons.',flush=True)

if __name__=='__main__':build()

"""Publish default 64px results for the Experiment combinations grid."""
import hashlib
import json
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from .combination_experiment import DATA, ROOT, render
from . import combination_layouts
from .experiment_gallery import stage_preview_combinations

if __package__:
    from .workspace import build_dist
else:
    from workspace import build_dist



_PUBLISH_LOCK=threading.Lock()


def _engine():
    engine=''.join(p.read_text() for p in sorted((ROOT/'vendor/combination').rglob('*.py')))
    return engine+(ROOT/'scripts/combination_experiment.py').read_text()


def _render_adjusted(row, args, engine, file):
    """A pair with a saved layout: its fingerprint also covers the layout and the baking helper."""
    key=hashlib.sha256((engine+(ROOT/'scripts/combination_layout_svg.py').read_text()
                        +json.dumps(row,sort_keys=True)+json.dumps(args,sort_keys=True)).encode()).hexdigest()
    return key, (lambda: {'fingerprint':key,'url':'combination-previews/'+file.name+'?v='+key[:12],
                          'result':render({'id':row['id'],**args},row=row)})


def build_one(pair_id, result=None):
    """Re-render one pair (after its layout was saved or reset) and publish it in place.

    `result` is an already rendered result for the saved layout, so it is not rendered twice.
    """
    row=next((r for r in json.loads(DATA.read_text())['rows'] if r['id']==pair_id),None)
    if row is None:
        raise ValueError('Choose an available icon pair.')
    folder=build_dist(ROOT.parent) / 'gallery/combination-previews';folder.mkdir(parents=True,exist_ok=True)
    file=folder/(pair_id+'.svg')
    args=combination_layouts.active(row,combination_layouts.load().get(pair_id))
    engine=_engine()
    if args:
        key,make=_render_adjusted(row,args,engine,file)
        item={'fingerprint':key,'url':'combination-previews/'+file.name+'?v='+key[:12],'result':result} if result else make()
    else:
        key=hashlib.sha256((engine+json.dumps(row,sort_keys=True)).encode()).hexdigest()
        # Versioned, so a browser that cached the adjusted SVG shows the reset one.
        item={'fingerprint':key,'url':'combination-previews/'+file.name+'?v='+key[:12],'result':render({'id':pair_id},row=row)}
    file.write_text(item['result']['svg'])
    with _PUBLISH_LOCK:
        for path in (ROOT/'data/combination-previews.json',build_dist(ROOT.parent) / 'gallery/experiment-combination-results.json'):
            data=json.loads(path.read_text()) if path.exists() else {}
            results=data.get('results',data) if path.name.startswith('experiment') else data
            results[pair_id]=item
            path.write_text(json.dumps({'results':results} if path.name.startswith('experiment') else results))
    return item


def build(*, force=False):
    rows=json.loads(DATA.read_text())['rows']
    folder=build_dist(ROOT.parent) / 'gallery/combination-previews';folder.mkdir(parents=True,exist_ok=True)
    cache=ROOT/'data/combination-previews.json'
    old=json.loads(cache.read_text()) if cache.exists() else {}
    engine=_engine()
    layouts=combination_layouts.load()
    def one(row):
        key=hashlib.sha256((engine+json.dumps(row,sort_keys=True)).encode()).hexdigest()
        file=folder/(row['id']+'.svg')
        prior={} if force else old.get(row['id'],{})
        args=combination_layouts.active(row,layouts.get(row['id']))
        if args:
            adjusted,make=_render_adjusted(row,args,engine,file)
            if prior.get('fingerprint')==adjusted:return row['id'],prior
            try:
                return row['id'],make()
            except Exception as error:
                # A layout the drawings no longer allow falls back to the automatic placement.
                print(f'Saved layout for {row["id"]} ignored: {error}',flush=True)
                prior={}
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

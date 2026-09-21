"""Recombine every available side pair with a geometry-passing current SUB32.

This selection policy is user-authorized; it does not grant human approval.
Preserve unavailable pairs and all alternative component choices.
"""
import sys,json,hashlib,html,io,contextlib,subprocess
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor

if __package__:
    from .workspace import build_dist
else:
    from workspace import build_dist

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))

def initialize():
    from icon_set.scripts import combination_experiment as ce
    sys.path.insert(0,str(ROOT/'icon_set/vendor/combination'))
    import run_combine
    original=subprocess.run
    def local_run(args,**kwargs):
        if len(args)>1 and str(args[1]).endswith('/run_combine.py'):
            output=io.StringIO();code=0
            with contextlib.redirect_stdout(output):
                try:run_combine.main(args[2:])
                except SystemExit as e:code=e.code
            return subprocess.CompletedProcess(args,code,output.getvalue(),'')
        return original(args,**kwargs)
    ce.subprocess.run=local_run

def render_one(row):
    from icon_set.scripts.combination_experiment import render
    try:return row['id'],render({'id':row['id']},row=row),None
    except Exception as e:return row['id'],None,str(e)

def main():
    data=ROOT/'icon_set/data';gallery=build_dist(ROOT) / 'gallery';out=ROOT/'icon_set/work/side-combinations-passing-sub'
    out.mkdir(parents=True,exist_ok=True);(out/'svg').mkdir(exist_ok=True)
    payload=json.loads((data/'combination-pairs.json').read_text());models=json.loads((data/'canonical-sub32.json').read_text())
    eligible=[];pending=[]
    for row in payload['rows']:
        good=[s for s in row['subs'] if models[s['icon']]['model_validation']=='pass']
        if not good:
            pending.append({'id':row['id'],'concept':row['concept'],'reason':'No geometry-passing sub icon','subs':[s['icon'] for s in row['subs']]});continue
        for s in good:
            assert s['sha256']==models[s['icon']]['sha256']==hashlib.sha256(s['document'].encode()).hexdigest()
        # Default preview and interactive first choice agree; preserve all alternatives.
        row['subs']=good+[s for s in row['subs'] if s not in good]
        eligible.append(row)
    results={};failures=[]
    with ProcessPoolExecutor(max_workers=4,initializer=initialize) as pool:
        for i,(uid,result,error) in enumerate(pool.map(render_one,eligible),1):
            if error:failures.append({'id':uid,'error':error})
            else:results[uid]=result
            if i%100==0:print(i,'/',len(eligible),flush=True)
    (out/'failures.json').write_text(json.dumps(failures,indent=2))
    if failures:raise RuntimeError(f'{len(failures)} rendering failures; production records unchanged')
    # Commit only after the entire eligible batch renders successfully.
    if not (out/'pairs-before.json').exists():(out/'pairs-before.json').write_bytes((data/'combination-pairs.json').read_bytes())
    if not (out/'previews-before.json').exists():(out/'previews-before.json').write_bytes((data/'combination-previews.json').read_bytes())
    cache=json.loads((data/'combination-previews.json').read_text())
    engine=''.join(p.read_text() for p in sorted((ROOT/'icon_set/vendor/combination').rglob('*.py')))+(ROOT/'icon_set/scripts/combination_experiment.py').read_text()
    records=[];cards=[]
    for row in eligible:
        uid=row['id'];result=results[uid];sub=row['subs'][0]
        assert result['placements'][1]['icon']==sub['icon'] and sub['model_validation']=='pass'
        assert not result['warnings'],(uid,result['warnings'])
        (out/'svg'/f'{uid}.svg').write_text(result['svg']);(gallery/'combination-previews'/f'{uid}.svg').write_text(result['svg'])
        cache[uid]={'fingerprint':hashlib.sha256((engine+json.dumps(row,sort_keys=True)).encode()).hexdigest(),'url':'combination-previews/'+uid+'.svg','result':result}
        records.append({'id':uid,'concept':row['concept'],'main':row['mains'][0]['icon'],'sub':sub['icon'],'sub_sha256':sub['sha256'],'position':row['position'],'selection_policy':'geometry-pass','warnings':result['warnings']})
        cards.append(f'<article><h2>{html.escape(row["concept"])}</h2><div class="art"><img loading="lazy" src="svg/{uid}.svg" width="128" height="128"><img loading="lazy" src="svg/{uid}.svg" width="64" height="64"><div class="dark"><img loading="lazy" src="svg/{uid}.svg" width="64" height="64"></div></div><p>{html.escape(sub["icon"])}</p><small>{html.escape(row["position"])} · geometry pass</small></article>')
    text=json.dumps(payload);(data/'combination-pairs.json').write_text(text);(gallery/'experiment-combination.json').write_text(text)
    (data/'combination-previews.json').write_text(json.dumps(cache));(gallery/'experiment-combination-results.json').write_text(json.dumps({'results':cache}))
    report={'policy':'Use current geometry-passing SUB32 models; human review statuses unchanged','passing_sub_models':sum(m['model_validation']=='pass' for m in models.values()),'available_side_pairs':len(payload['rows']),'recombined':len(records),'waiting':len(pending),'rows':records,'pending':pending}
    catalog=json.loads((gallery/'combinations.json').read_text())['rows']
    available={r['id'] for r in payload['rows']}
    missing=[{'id':r['id'],'concept':r['concept'],'reason':'Main icon has not been generated'} for r in catalog if r.get('kind')=='side' and r['id'] not in available]
    report.update(catalog_side_pairs=sum(r.get('kind')=='side' for r in catalog),missing_main=len(missing),unavailable=missing)
    (out/'report.json').write_text(json.dumps(report,indent=2))
    waits=''.join('<li>'+html.escape(r['concept'])+' — '+html.escape(', '.join(r['subs']))+'</li>' for r in pending)
    (out/'index.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Side combinations · passing sub icons</title><style>*{box-sizing:border-box}body{margin:0;background:#f2f5f1;color:#20302d;font:14px system-ui}header{padding:30px;max-width:1000px}p{line-height:1.6}main{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:16px;padding:20px}article{background:white;padding:20px;border-radius:12px;min-width:0}article[hidden]{display:none}h2{font-size:16px}.art{display:flex;align-items:center;justify-content:space-between;gap:8px}.dark{background:#18242b;padding:8px;border-radius:8px}.dark img{filter:brightness(0) invert(1)}article p{font-size:12px;overflow-wrap:anywhere}input{padding:12px;font:inherit;width:min(440px,100%)}li{margin:10px 0;overflow-wrap:anywhere}.art img{background-color:#fbfdfb;background-image:linear-gradient(to right,rgba(65,102,116,.24) .5px,transparent .5px),linear-gradient(to bottom,rgba(65,102,116,.24) .5px,transparent .5px),linear-gradient(to right,rgba(65,102,116,.13) .3px,transparent .3px),linear-gradient(to bottom,rgba(65,102,116,.13) .3px,transparent .3px);background-size:12.5% 12.5%,12.5% 12.5%,1.5625% 1.5625%,1.5625% 1.5625%;box-shadow:inset 0 0 0 1px #99adb4;}</style><header><h1>Side combinations · passing sub icons</h1><p>'''+f'<strong>{len(records):,} recombined</strong> using current geometry-passing sub icons. {len(pending):,} available pairs are waiting for a passing sub icon. “Passing” is the selection rule requested for this batch; human approval records have not changed.'+'''</p><p>Additional catalog pairs lack generated main icons and cannot yet be combined; they are listed in report.json. Saved main icons and side positions are preserved. Each combination is shown enlarged and at its native 64px size in light and dark themes.</p><input id="search" type="search" placeholder="Search concept or sub icon" aria-label="Search combinations"><p id="count"></p><details><summary>Pairs waiting for a passing sub icon</summary><ul>'''+waits+'</ul></details></header><main>'+''.join(cards)+'''</main><script>const input=document.getElementById('search'),cards=[...document.querySelectorAll('article')];function filter(){let n=0;for(const c of cards){c.hidden=!c.textContent.toLowerCase().includes(input.value.toLowerCase());if(!c.hidden)n++}document.getElementById('count').textContent=n+' combinations'}input.addEventListener('input',filter);filter();</script></html>''')
    from icon_set.scripts.side_combination_gallery import install_popup
    install_popup(out, records, results)
    print({k:v for k,v in report.items() if k not in ['rows','pending']},flush=True)
if __name__=='__main__':main()

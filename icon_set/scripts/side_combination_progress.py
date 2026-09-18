"""Report side-combination coverage and distinct missing source concepts."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def compact_html(d, report_href='sub-repair-review/index.html'):
    import html
    total=d['side_combinations'];done=d['recombined']
    stats=[(f"{done:,} / {total:,}", 'combinations ready'),(f"{total-done:,}", 'combinations left'),(f"{d['main_to_generate']:,} main + {d['sub_to_generate']:,} sub", 'new icons to generate'),(f"{d['sub_models']-d['passing_sub_models']:,}", 'sub icons to repair / review'),(f"{d['main_to_build_or_link']:,} main + {d['sub_to_build_or_link']:,} sub", 'existing sources to build / link')]
    cards=''.join('<span class="side-progress-stat"><strong>'+value+'</strong><small>'+label+'</small></span>' for value,label in stats)
    lists=''
    for role in ('main','sub'):
        lists+='<details><summary>See '+role+' generation / linking list</summary><ul>'+''.join('<li>'+html.escape(e['action']+': '+e['examples'][0])+' — '+str(e['combinations'])+' combinations</li>' for e in d['missing'][role])+'</ul></details>'
    return '<!-- side-progress:start --><style>.side-progress-compact{flex-basis:100%;width:100%;box-sizing:border-box;background:#f3f7f5;border:1px solid #d4e0da;border-radius:9px;padding:12px 14px;margin:0 0 10px;font:13px system-ui;color:#20302d}.side-progress-compact h2{font-size:14px!important;margin:0 0 8px!important}.side-progress-compact .side-progress-stats{display:flex;flex-wrap:wrap;gap:10px 24px}.side-progress-stat strong,.side-progress-stat small{display:block}.side-progress-stat strong{font-size:17px}.side-progress-stat small{font-size:11px;margin-top:3px}.side-progress-compact progress{display:block;width:100%;height:7px;margin:10px 0 6px;accent-color:#327763}.side-progress-compact p{font-size:11px;margin:4px 0!important;line-height:1.5}.side-progress-compact details{font-size:11px;margin:5px 16px 0 0;display:inline-block;vertical-align:top}.side-progress-compact details[open]{display:block}.side-progress-compact ul{max-height:220px;overflow:auto;line-height:1.7}</style><section class="side-progress-compact" aria-label="Combination progress"><h2>Progress · '+f'{done/total:.1%}'+'</h2><div class="side-progress-stats">'+cards+'</div><progress value="'+str(done)+'" max="'+str(total)+'" aria-label="Combinations ready"></progress><p>'+f"{d['main_models_in_sides']:,} main models available · {d['sub_models']:,} sub models generated, {d['passing_sub_models']:,} passing. Of the combinations left: {d['waiting_sub_repair']:,} need a passing sub; {d['waiting_components']:,} need components or pairing. Icon counts and combination counts are separate."+'</p>'+lists+'<p><a href="'+html.escape(report_href,quote=True)+'">View all '+str(d['sub_models']-d['passing_sub_models'])+' sub icons needing repair / review →</a></p></section><!-- side-progress:end -->'

def stage(target):
    catalog=json.loads((target/'combinations.json').read_text())['rows']
    sides=[r for r in catalog if r['kind']=='side']
    pairs=json.loads((ROOT/'icon_set/data/combination-pairs.json').read_text())['rows']
    models=json.loads((ROOT/'icon_set/data/canonical-sub32.json').read_text())
    # Side catalog 'generated' contains combinations, not standalone main models.
    # Resolve main source IDs from the same model/export registry as pair discovery.
    from icon_set.scripts.category_report import model_catalog, source_id
    available_main=set(); authored_sources=set()
    profiles={'solo':'solo48','container':'container64','combination_main':'combination_main48','sub':'sub32'}
    for model in model_catalog():
        ids={model['source_id'],source_id(model['source_path']) if model['source_path'] else None}
        for uid,reference in model['source_references']:
            ids.add(uid)
            if reference:ids.add(source_id(reference))
        authored_sources.update(x.lower() for x in ids if x)
        if (ROOT/'icon_set/dist'/profiles[model['family']]/(model['icon_id']+'.svg')).exists():
            available_main.update(x.lower() for x in ids if x)
    missing={role:{} for role in ['main','sub']}
    for r in sides:
        for role in missing:
            if (r['main_id'].lower() not in available_main if role=='main' else not r.get('sub_generated')):
                key=r[role+'_id'];entry=missing[role].setdefault(key,{'source_id':key,'examples':[],'combinations':0});entry['combinations']+=1
                if len(entry['examples'])<3:entry['examples'].append(r['concept'])
    ready=sum(any(models[s['icon']]['model_validation']=='pass' for s in r['subs']) for r in pairs)
    report={'side_combinations':len(sides),'recombined':ready,'available_pairs':len(pairs),'waiting_sub_repair':len(pairs)-ready,'waiting_components':len(sides)-len(pairs),'sub_models':len(models),'passing_sub_models':sum(m['model_validation']=='pass' for m in models.values()),'main_models_in_sides':len({(x['family'],x['icon']) for r in pairs for x in r['mains']}),'main_to_generate':len(missing['main']),'sub_to_generate':len(missing['sub']),'missing':{role:sorted(values.values(),key=lambda x:-x['combinations']) for role,values in missing.items()}}
    for role, entries in report['missing'].items():
        for entry in entries:entry['action']='build or link existing source model' if entry['source_id'].lower() in authored_sources else 'generate new icon'
        report[role+'_to_generate']=sum(e['action']=='generate new icon' for e in entries)
        report[role+'_to_build_or_link']=len(entries)-report[role+'_to_generate']
    (target/'side-combination-progress.html').write_text(compact_html(report))
    (target/'side-combination-progress.json').write_text(json.dumps(report,indent=2));return report
if __name__=='__main__':
    r=stage(ROOT/'icon_set/dist/gallery');print({k:v for k,v in r.items() if k!='missing'})

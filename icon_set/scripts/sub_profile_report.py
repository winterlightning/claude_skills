"""Portable review gallery of independently editable, linked sub profiles."""
import collections
import html
import json
import os
from pathlib import Path

if __package__:
    from .workspace import development_dist
else:
    from workspace import development_dist

ROOT=Path(__file__).resolve().parents[2]


def build(root=ROOT, target=None):
    gallery=development_dist(root) / 'gallery';data=root/'icon_set/data'
    migration=json.loads((data/'sub-profile-migration.json').read_text())['icons']
    models=json.loads((data/'canonical-sub32.json').read_text())
    qa=json.loads((root/'icon_set/work/sub-profile-migration/qa.json').read_text())
    cards=[]
    for original,entry in migration.items():
        uid=entry['model_key'].split('/',1)[1];r=models[uid];status=r['model_validation'];text=r['sizing_kind']=='text'
        sources=entry['sources'];source=sources[0] if sources else None
        source_url=os.path.relpath(root/(source['source_svg'] if source else entry['reference_export']),gallery)
        model_url=os.path.relpath(root/entry['python_source'],gallery)
        links=''.join('<li>'+html.escape(s['key'])+' · '+html.escape(s['relationship'])+'</li>' for s in sources)
        issues=qa[uid].get('errors',[])+qa[uid].get('warnings',[])
        note='<details><summary>Validation findings</summary><ul>'+''.join('<li>'+html.escape(v)+'</li>' for v in issues)+'</ul></details>' if issues else ''
        card=f'''<article data-status="{'pass' if status=='pass' else 'review'}" data-text="{str(text).lower()}"><h2>{html.escape(uid)}</h2><p class="status {'pass' if status=='pass' else 'review'}">{html.escape(status)} · {'Text, natural width × 32' if text else 'SUB32 · 32 × 32'}</p><div class="compare"><figure><div class="art"><img loading="lazy" src="{html.escape(source_url)}"></div><figcaption>{html.escape(source['profile'] if source else 'Previous 32px artwork')}</figcaption></figure><figure><div class="art"><img loading="lazy" src="{html.escape(r['export_url'])}"></div><figcaption>Independent sub model</figcaption></figure></div><p><a href="{html.escape(model_url)}">Python model</a> · <a href="{html.escape(r['export_url'])}">SVG</a></p><details><summary>{len(sources)} linked source profiles</summary><ul>{links}</ul></details>{note}</article>'''
        cards.append(card)
    counts=collections.Counter(r['model_validation'] for r in models.values())
    summary=dict(models=len(models),new_models=sum(r['status']=='created' for r in migration.values()),reused_models=sum(r['status']=='existing' for r in migration.values()),text_models=sum(r['sizing_kind']=='text' for r in models.values()),validation=dict(counts),profile_links=len(json.loads((data/'icon-profile-links.json').read_text())['links']))
    ((target or gallery)/'sub-profiles-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    template='''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Linked sub profiles</title><style>body{font:15px system-ui;margin:32px;color:#203028;background:#f6f8f4}header{max-width:1050px}input,select{padding:10px;margin:6px}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(360px,1fr));gap:16px}article{background:white;border:1px solid #ddd;border-radius:12px;padding:20px;min-width:0}h2{font-size:16px;overflow-wrap:anywhere}.compare{display:grid;grid-template-columns:1fr 1fr}figure{margin:8px;min-width:0}.art{height:80px;overflow:auto;display:flex;align-items:center}.art img{height:32px;width:auto;max-width:none}figure:first-child img{height:48px}.pass{color:#187343}.review{color:#935700}li{overflow-wrap:anywhere;margin:6px 0}a{color:#25633d}details{margin-top:12px}article[hidden]{display:none}</style></head><body><header><h1>Linked sub profiles</h1><p>__SUMMARY__</p><p>Each model is independently editable. Source links preserve the 48px-to-32px relationship and shared references. Text keeps 32px ink height, natural width, and grid-snapped geometry.</p><p>Conversion preserves existing artwork; it does not approve it. Failed and review models are available here as drafts and remain outside the validated release.</p><input id="q" placeholder="Find an icon or source"><select id="status"><option value="">All validation states</option><option value="pass">Passed</option><option value="review">Needs repair or review</option></select><select id="kind"><option value="">All drawings</option><option value="true">Text only</option><option value="false">Symbols and objects</option></select><p id="count"></p></header><main>__CARDS__</main><script>const cards=[...document.querySelectorAll('article')];function filter(){let n=0;for(const c of cards){c.hidden=!(c.textContent.toLowerCase().includes(q.value.toLowerCase())&&(!status.value||c.dataset.status===status.value)&&(!kind.value||c.dataset.text===kind.value));if(!c.hidden)n++;}document.getElementById('count').textContent=n+' models';}const q=document.getElementById('q'),status=document.getElementById('status'),kind=document.getElementById('kind');for(const x of [q,status,kind])x.addEventListener('input',filter);filter();</script></body></html>'''
    headline=f'{summary["models"]:,} sub models: {summary["new_models"]:,} created, {summary["reused_models"]} reused. {summary["text_models"]} text models. {counts["pass"]} pass validation; {len(models)-counts["pass"]} need repair or review.'
    ((target or gallery)/'sub-profiles.html').write_text(template.replace('__SUMMARY__',headline).replace('__CARDS__',''.join(cards)))
    return summary

def stage(target, root=ROOT):
    import shutil
    source=root/'icon_set/assets/sub-profiles'
    required = ('icon_set/data/sub-profile-migration.json', 'icon_set/data/canonical-sub32.json',
                'icon_set/data/icon-profile-links.json', 'icon_set/work/sub-profile-migration/qa.json')
    if not source.is_dir() or not all((root / name).is_file() for name in required):
        return  # Historical reports are optional in a clean release checkout.
    shutil.copytree(source,target/'sub-profiles',dirs_exist_ok=True)
    build(root,target)

if __name__=='__main__':print(build())

"""Build a read-only gallery of current failed/review SUB32 models."""
import csv,hashlib,html,io,json,shutil,xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

if __package__:
    from .workspace import development_dist
else:
    from workspace import development_dist

ROOT=Path(__file__).resolve().parents[2]
def stage(target):
    required = (ROOT/'icon_set/data/canonical-sub32.json',
                ROOT/'icon_set/work/sub-profile-migration/qa.json')
    if not all(path.is_file() for path in required):
        target.mkdir(parents=True, exist_ok=True)
        (target/'index.html').write_text(
            '<!doctype html><meta charset="utf-8"><title>Historical sub review</title>'
            '<p>Historical sub review is unavailable in this checkout. '
            'See the gallery Failed build view for current validation findings.</p>')
        print('[reports] Historical sub repair review skipped: optional inputs unavailable', flush=True)
        return None
    target.mkdir(parents=True,exist_ok=True);assets=target/'svg';assets.mkdir(exist_ok=True)
    models=json.loads((ROOT/'icon_set/data/canonical-sub32.json').read_text());qa=json.loads((ROOT/'icon_set/work/sub-profile-migration/qa.json').read_text());rows=[];cards=[]
    for uid,m in sorted(models.items()):
        if m['model_validation'] not in ('fail','review'):continue
        document=(ROOT/m['svg']).read_text();digest=hashlib.sha256(document.encode()).hexdigest();q=qa[uid];assert digest==m['sha256']==q['svg_sha256'],uid
        findings=q.get('errors',[])+q.get('warnings',[]);assert findings,uid
        categories=[]
        for token,label in [('canvas','Bounds'),('keyshape','Bounds'),('spacing','Spacing'),('mic [','Spacing'),('grid','Grid'),('symmetr','Symmetry'),('stroke','Stroke'),('contour','Contours')]:
            if any(token in f.lower() for f in findings) and label not in categories:categories.append(label)
        if not categories:categories=['Other']
        source=ET.fromstring(document);w=float(source.get('width',m.get('canvas_width',32)));h=float(source.get('height',32));(assets/(uid+'.svg')).write_text(document)
        source.set('stroke','#c6d1d5')
        for e in list(source):
            if e.tag.rsplit('}',1)[-1] in ('path','circle','ellipse','line','polyline','polygon','rect'):
                c=ET.fromstring(ET.tostring(e));c.set('stroke','#0075c9');c.set('stroke-width','.24');c.set('fill','none');source.append(c)
        (assets/(uid+'.centerline.svg')).write_bytes(ET.tostring(source))
        r={'number':len(rows)+1,'icon':uid,'status':m['model_validation'],'kind':m['sizing_kind'],'categories':categories,'findings':findings,'python_source':m['python_source'],'profile_sources':m.get('profile_sources',[]),'sha256':digest};rows.append(r)
        def pic(suffix,label,dark=False,native=False):
            return f'<figure class="{"dark" if dark else ""}"><figcaption>{label}</figcaption><div class="image"><img loading="lazy" src="svg/{uid}{suffix}.svg" style="height:{32 if native else 128}px;width:{w if native else w*4:g}px" alt="{html.escape(uid)}"></div></figure>'
        cards.append(f'<article id="icon-{r["number"]}" data-status="{r["status"]}" data-kind="{r["kind"]}" data-categories="{" ".join(categories)}"><h2>{r["number"]}. {html.escape(uid)}</h2><p class="badge {r["status"]}">{"Failed checks" if r["status"]=="fail" else "Needs review"} · {r["kind"]} · {" / ".join(categories)}</p><div class="previews">'+pic('','Artwork')+pic('.centerline','Centerline')+pic('','Actual size · 32px',native=True)+pic('','Actual size · dark',dark=True,native=True)+'</div><button class="inspect">Enlarge</button><details><summary>Findings ('+str(len(findings))+')</summary><ul>'+''.join('<li>'+html.escape(f)+'</li>' for f in findings)+'</ul><p class="source">'+html.escape(m['python_source'])+'</p></details></article>')
    counts=Counter(r['status'] for r in rows);(target/'report.json').write_text(json.dumps({'total':len(rows),'counts':dict(counts),'icons':rows},indent=2))
    with (target/'report.csv').open('w') as f:
        writer=csv.writer(f);writer.writerow(['Number','Icon','Status','Kind','Categories','Findings','Python source'])
        for r in rows:writer.writerow([r['number'],r['icon'],r['status'],r['kind'],'; '.join(r['categories']),'\n'.join(r['findings']),r['python_source']])
    header=f'<h1>{len(rows)} sub icons · repair / review</h1><p><strong>{counts["fail"]} failed checks · {counts["review"]} need review.</strong> Current drawings and recorded findings; this report does not change artwork or approval.</p>'
    (target/'index.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sub icons · repair / review</title><style>*{box-sizing:border-box}body{margin:0;font:14px system-ui;background:#f3f5f1;color:#21342d}header{padding:20px}h1{font-size:24px;margin:0 0 8px}p{line-height:1.5}.controls{display:flex;gap:8px;flex-wrap:wrap}input,select,button{padding:8px;font:inherit;border:1px solid #bbc9c2;background:white;border-radius:6px}input{width:300px}main{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(420px,100%),1fr));gap:16px;padding:0 20px 20px}article{background:white;border-radius:10px;padding:16px;min-width:0}article[hidden]{display:none}h2{font-size:14px;overflow-wrap:anywhere}.badge{font-size:12px;padding:7px;border-radius:5px;background:#fff0ce}.badge.fail{background:#fee7e2}.previews{display:grid;grid-template-columns:1fr 1fr;gap:8px}figure{margin:0;background:#f6f8f6;padding:10px;border-radius:7px;min-width:0}figcaption{font-size:11px;color:#65736b;margin-bottom:10px}.image{overflow:auto;display:flex;min-height:42px;align-items:center}img{flex-shrink:0;margin:auto}.dark{background:#17252a}.dark img{filter:brightness(0) invert(1)}.dark figcaption{color:#c5d5ce}details{margin-top:12px}li,.source{font-size:12px;line-height:1.6;overflow-wrap:anywhere}li{margin-bottom:8px}button{cursor:pointer}.inspect{margin-top:10px}dialog{width:min(1000px,95vw);max-height:94vh;overflow:auto;border:1px solid #9fb3a7;border-radius:12px}dialog::backdrop{background:#15251dbb}dialog .image{min-height:80px}dialog .inspect{display:none}dialog .close{float:right;position:sticky;top:0}dialog .previews img{max-width:none}a{color:#266c55}</style><header>'''+header+'''<div class="controls"><input id="q" type="search" placeholder="Search name or finding" aria-label="Search"><select id="status" aria-label="Status"><option value="">All statuses</option><option value="fail">Failed checks</option><option value="review">Needs review</option></select><select id="kind" aria-label="Kind"><option value="">Symbols and text</option><option value="symbol">Symbols</option><option value="text">Text</option></select><select id="issue" aria-label="Finding"><option value="">All findings</option>'''+''.join('<option>'+x+'</option>' for x in ['Bounds','Spacing','Grid','Symmetry','Stroke','Contours','Other'])+'''</select><a href="report.csv" download>CSV report</a><a href="report.json" download>Full report</a></div><p id="count"></p></header><main>'''+''.join(cards)+'''</main><dialog id="inspect"><button class="close">Close</button><div class="content"></div></dialog><script>const cards=[...document.querySelectorAll('article')],q=document.getElementById('q'),statusFilter=document.getElementById('status'),kind=document.getElementById('kind'),issue=document.getElementById('issue'),modal=document.getElementById('inspect');function filter(){let n=0;for(const c of cards){c.hidden=!((!statusFilter.value||c.dataset.status===statusFilter.value)&&(!kind.value||c.dataset.kind===kind.value)&&(!issue.value||c.dataset.categories.split(' ').includes(issue.value))&&c.textContent.toLowerCase().includes(q.value.toLowerCase()));if(!c.hidden)n++;}document.getElementById('count').textContent=n+' of '+cards.length+' icons';}for(const e of [q,statusFilter,kind,issue])e.addEventListener('input',filter);for(const c of cards)c.querySelector('button').onclick=()=>{const copy=c.cloneNode(true);for(const image of copy.querySelectorAll('figure:nth-child(-n+2) img')){image.style.width=parseFloat(image.style.width)*2+'px';image.style.height='256px';}copy.querySelector('details').open=true;modal.querySelector('.content').replaceChildren(copy);modal.showModal();};modal.querySelector('.close').onclick=()=>modal.close();filter();</script></html>''')
    return dict(total=len(rows),counts=dict(counts))
if __name__=='__main__':
    dest=ROOT/'icon_set/work/sub-repair-review-638';print(stage(dest));shutil.copytree(dest,development_dist(ROOT) / 'gallery/sub-repair-review',dirs_exist_ok=True)

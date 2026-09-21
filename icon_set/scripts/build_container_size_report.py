"""Audit full 32/48-unit icon footprints: python3 -m icon_set.scripts.build_container_size_report."""
from pathlib import Path
from collections import Counter
import hashlib
import html
import json
import xml.etree.ElementTree as ET
from shapely.geometry import shape
from icon_set.scripts.container_square_fit import assess_square

if __package__:
    from .workspace import build_dist
else:
    from workspace import build_dist


BASE=Path(__file__).resolve().parents[1]
OUT=BASE/'work/container-size-report'
LABEL={'fits':'Fits','too-small':'Too small','borderline':'Borderline','review':'Boundary needed','overlay':'Overlay exception','stale':'Source changed'}


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    source=BASE/'work/container-vector-report/results.json'
    audit=json.loads(source.read_text())
    legacy=json.loads((BASE/'data/container-content-areas.json').read_text())['areas']
    records=[]
    for c in audit['containers']:
        ident=c['container']
        svg=build_dist(BASE.parent) / 'container64'/f'{ident}.svg'
        fresh=hashlib.sha256(svg.read_bytes()).hexdigest()==c['source_sha256']
        r={'container':ident,'source_sha256':c['source_sha256'],'zone_status':c['status'],'sizes':{}}
        for size in (32,48):
            if not fresh:
                fit={'status':'stale','size_units':size}
            elif c['status']=='vector':
                fit=assess_square(shape(c['safe_zone_inner']),shape(c['safe_zone_outer']),size,c['center_units'])
            else:
                fit={'status':c['status'] if c['status'] in ('review','overlay') else 'review','size_units':size}
            r['sizes'][str(size)]=fit
            preview=BASE/'work/container-vector-report'/c.get('preview','')
            if preview.is_file():
                root=ET.fromstring(preview.read_text())
                center=fit.get('placement_center_units') or c.get('center_units') or legacy.get(ident,{}).get('center') or [32,32]
                color='#176bb0' if fit['status']=='fits' else ('#d14747' if fit['status']=='too-small' else '#94661b')
                x,y=center
                ET.SubElement(root,'{http://www.w3.org/2000/svg}rect',{'x':str(x-size/2),'y':str(y-size/2),'width':str(size),'height':str(size),'fill':color,'fill-opacity':'.12','stroke':color,'stroke-width':'.4','stroke-dasharray':'1 .6'})
                fit['preview_center_units']=center
                fit['preview']=f'{ident}-{size}.svg'
                (OUT/fit['preview']).write_text(ET.tostring(root,encoding='unicode'))
        records.append(r)
    counts={str(s):dict(Counter(r['sizes'][str(s)]['status'] for r in records)) for s in (32,48)}
    output={'units':'SVG units','sizes':[32,48],'padding_units':2,'footprint':'Full axis-aligned square including all icon ink; translation allowed, no rotation or scaling.',
            'method':'Polygon configuration space: subtract square sweeps of every exterior and hole boundary segment. Test bounded inner and outer vector zones; borderline contacts remain review.',
            'source_audit_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'counts':counts,'containers':records}
    (OUT/'results.json').write_text(json.dumps(output,indent=2)+'\n')
    cards=[]
    order={'too-small':0,'borderline':1,'fits':2,'review':3,'overlay':4,'stale':5}
    for r in sorted(records,key=lambda r:(order[r['sizes']['32']['status']],r['container'])):
        ident=r['container'];f32=r['sizes']['32'];f48=r['sizes']['48']
        panels=[]
        for s,f in ((32,f32),(48,f48)):
            center=f.get('placement_center_units')
            note=(f'Placement center: ({center[0]:.4f}, {center[1]:.4f}) u.' if center else 'Shown square is illustrative; no verified placement.')
            if center and not f['fits_at_preferred_center']:note+=' Shifted from the area center to fit.'
            panels.append(f'<div class="size size{s}"><b class="badge {f["status"]}">{LABEL[f["status"]]} · {s} × {s}</b>'
                          +(f'<a href="{f["preview"]}"><img loading="lazy" src="{f["preview"]}" alt="{s}-unit square in {html.escape(ident)}"></a>' if 'preview' in f else '')
                          +f'<p>{note}</p></div>')
        cards.append(f'<article data-name="{ident}" data-s32="{f32["status"]}" data-s48="{f48["status"]}"><h2>{html.escape(ident)}</h2>{"".join(panels)}<p class="other">32: {LABEL[f32["status"]]} · 48: {LABEL[f48["status"]]}</p></article>')
    table='<table><tr><th>Full footprint</th><th>Fits</th><th>Too small</th><th>Borderline</th><th>Boundary needed</th><th>Overlay</th></tr>'+''.join(f'<tr><th>{s} × {s}</th>'+''.join(f'<td>{counts[str(s)].get(k,0)}</td>' for k in ('fits','too-small','borderline','review','overlay'))+'</tr>' for s in (32,48))+'</table>'
    page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Container 32 and 48 unit fit</title><style>
body{font:15px system-ui;margin:32px;background:#f5f7fa;color:#202630}header{max-width:1000px}h1{font-size:30px}p{line-height:1.55}a{color:#235da6}table{border-collapse:collapse;width:100%;margin:20px 0}th,td{text-align:left;border-bottom:1px solid #d9e0e8;padding:12px}nav{position:sticky;top:0;background:#f5f7fa;display:flex;gap:12px;flex-wrap:wrap;align-items:center;padding:15px 0;z-index:1}input,select{font:inherit;padding:10px;border:1px solid #cbd3dd;border-radius:8px;background:white}main{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:18px}article{padding:22px;border:1px solid #dde2ea;border-radius:12px;background:white}h2{font-size:16px;overflow-wrap:anywhere}img{display:block;width:100%;margin:18px auto}article p{font-size:13px}.badge{display:inline-block;padding:5px 9px;background:#edf0f5;border-radius:5px}.too-small{color:#a02727;background:#fff0ef}.fits{color:#175584;background:#eaf5ff}.other{color:#657184}article[hidden],body[data-size="32"] .size48,body[data-size="48"] .size32{display:none}</style><body data-size="32"><header><h1>Will a 32 × 32 icon fit?</h1><p><a href="../container-sub-preview/index.html"><b>Preview actual 32 × 32 sub-icons inside the containers</b></a></p>
<p>Check a <b>full square footprint</b> at native size inside each container, keeping <b>2 SVG units clear of the container ink</b>. Choose 48 × 48 to inspect larger-icon exceptions. Translation is allowed; no scaling or rotation. The footprint includes the icon’s own strokes.</p>
<p><b>Too small</b> means no full square of that size fits anywhere in the selected interior. A particular icon with empty margins or corners may still fit and needs its actual vector paths checked. Bounding-box width and height alone do not establish fit.</p>'''+table+'''
<p><b>Blue:</b> verified placement in the conservative vector interior. <b>Red:</b> too large; the displayed square illustrates the conflict. <b>Brown:</b> unresolved. Green is the usable vector area; orange is the existing clearance buffer. Borderline cases straddle the vector tolerance. Open boundaries and overlays have no automatic fit claim.</p>
<p><a href="results.json">Download fit results and placement coordinates</a> · <a href="../container-vector-report/index.html">Vector measurements</a></p></header>
<nav><select id="size" aria-label="Icon footprint"><option value="32">32 × 32 icon</option><option value="48">48 × 48 icon</option></select><select id="status" aria-label="Fit status"><option value="all">All containers</option><option value="too-small">Too small</option><option value="fits">Fits</option><option value="borderline">Borderline</option><option value="review">Boundary needed</option><option value="overlay">Overlay exceptions</option></select><input id="search" aria-label="Find container" placeholder="Find container…"><span id="count"></span></nav><main>'''+''.join(cards)+'''</main><script>const cards=[...document.querySelectorAll('article')],size=document.querySelector('#size'),status=document.querySelector('#status'),q=document.querySelector('#search');function filter(){document.body.dataset.size=size.value;let n=0;for(const c of cards){c.hidden=!(c.dataset.name.includes(q.value.toLowerCase())&&(status.value==='all'||c.dataset['s'+size.value]===status.value));if(!c.hidden)n++}document.querySelector('#count').textContent=n+' containers shown'}size.onchange=filter;status.onchange=filter;q.oninput=filter;filter()</script></body></html>'''
    (OUT/'index.html').write_text(page)
    print(json.dumps({'counts':counts,'report':str(OUT/'index.html'),
                      'fits48':[r['container'] for r in records if r['sizes']['48']['status']=='fits'],
                      'too_small32':[r['container'] for r in records if r['sizes']['32']['status']=='too-small']},indent=2))

if __name__=='__main__':main()

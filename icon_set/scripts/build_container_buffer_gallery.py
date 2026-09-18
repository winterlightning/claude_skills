#!/usr/bin/env python3
"""Render every container's ink buffer and existing pair buffers for review."""
from pathlib import Path
import copy
import hashlib
import html
import io
import json
import xml.etree.ElementTree as ET
from collections import Counter
import cairosvg
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage

if __package__:
    from .workspace import development_dist
else:
    from workspace import development_dist


ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'icon_set'
OUT=BASE/'work/container-buffer-preview'
SCALE=4
PADDING=2


def mask(svg):
    png=cairosvg.svg2png(bytestring=svg.encode(),output_width=256,output_height=256)
    return np.array(Image.open(io.BytesIO(png)).convert('RGBA'))[:,:,3]>100


def expanded(ink):
    return ndimage.distance_transform_edt(~np.pad(ink,16))[16:-16,16:-16]/SCALE<=PADDING


def paint(filename, ink, buffer, safe=None, collision=None, center=None):
    pixels=np.full((256,256,3),255,dtype=np.uint8)
    if safe is not None:pixels[safe]=[221,245,229]
    pixels[buffer]=[255,220,155]
    if collision is not None:pixels[collision]=[239,100,100]
    pixels[ink]=[24,28,34]
    image=Image.fromarray(pixels)
    if center:
        x,y=[round(v*SCALE) for v in center];draw=ImageDraw.Draw(image)
        draw.ellipse((x-4,y-4,x+4,y+4),fill='#2563eb',outline='white',width=1)
        draw.line((x-9,y,x+9,y),fill='#2563eb',width=2);draw.line((x,y-9,x,y+9),fill='#2563eb',width=2)
    image.save(OUT/filename)


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    rows=json.loads((development_dist(BASE.parent) / 'gallery/combinations.json').read_text())['rows']
    mapped={g['key'].split('/',1)[1] for r in rows if r['kind']=='container' for g in r.get('main_generated',[]) if g['key'].startswith('container/')}
    trials=json.loads((BASE/'data/container-solo-trials.json').read_text())['results']
    grouped={}
    for record in trials.values():
        grouped.setdefault(record['main_key'].split('/',1)[1],{})[record['svg_file']]=record
    zones=json.loads((BASE/'data/container-content-areas.json').read_text())['areas']
    cards=[];results=[];pair_count=0
    for source in sorted((development_dist(BASE.parent) / 'container64').glob('*.svg'),key=lambda p:(p.stem not in mapped,p.stem)):
        ident=source.stem;document=source.read_text();ink=mask(document);buffer=expanded(ink)
        enclosed=ndimage.binary_fill_holes(ink)&~ink
        zone=zones[ident]
        if zone['source_sha256']!=hashlib.sha256(source.read_bytes()).hexdigest():raise ValueError('Stale safe zone: '+ident)
        safe=np.zeros((256,256),dtype=bool)
        if zone['kind']=='safe-zone':
            canvas=Image.new('1',(256,256));ImageDraw.Draw(canvas).polygon([(x*4,y*4) for x,y in zone['polygon']],fill=1);safe=np.array(canvas,dtype=bool)
        image=f'{ident}-buffer.png';paint(image,ink,buffer,safe,center=zone['center'])
        pairs=[];pair_cards=[]
        for file,record in grouped.get(ident,{}).items():
            asset=BASE/'assets/container-solo-trials'/file
            sub=development_dist(BASE.parent) / 'solo48'/f"{record['sub_key'].split('/',1)[1]}.svg"
            stale=(hashlib.sha256(source.read_bytes()).hexdigest()!=record['main_sha256'] or not sub.exists() or hashlib.sha256(sub.read_bytes()).hexdigest()!=record['sub_sha256'] or not asset.exists() or hashlib.sha256(asset.read_bytes()).hexdigest()!=record['svg_sha256'])
            if stale:
                pair_cards.append('<p>Source changed — rebuild '+html.escape(record['sub_key'])+'</p>')
                pairs.append({'sub_key':record['sub_key'],'status':'stale'});continue
            root=ET.fromstring(asset.read_text());content=copy.deepcopy(root)
            for child in list(content):
                if child.get('id')!='content':content.remove(child)
            host=copy.deepcopy(root)
            for child in list(host):
                if child.get('id')!='container':host.remove(child)
            si=mask(ET.tostring(content,encoding='unicode'));hi=mask(ET.tostring(host,encoding='unicode'))
            halo=expanded(si);collision=halo&hi
            target=Path(file).stem+'-buffer.png'
            paint(target,hi|si,halo,collision=ndimage.binary_dilation(collision,iterations=2))
            status='Review spacing' if collision.any() else 'Buffer clear (raster estimate)'
            pair_cards.append(f'<figure><img loading="lazy" src="{target}" alt="Sub icon buffer"><figcaption>{html.escape(record["sub_key"].split("/",1)[1])}<br>{status}</figcaption></figure>')
            pairs.append({'sub_key':record['sub_key'],'preview':target,'buffer_overlap_estimate':bool(collision.any()),'original_trial_status':record['status']});pair_count+=1
        audit=zone.get('center_audit',{})
        evidence=''
        if audit:
            evidence=f'<p><b>{audit["confidence_level"]} confidence · {audit["confidence_score"]}/100</b></p><p>{html.escape(audit["method"])}</p><p>Center moved {audit["movement"]:g} units. <a href="../container-center-audit/index.html#{ident}">View measurements and before/after</a></p>'
        status='Chosen safe zone' if zone['kind']=='safe-zone' else 'Center only — no safe zone'
        result={'container':ident,'main_on_page':ident in mapped,'source_path':str(source),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'preview':image,'area_status':status,'area':zone,'pairs':pairs}
        results.append(result)
        detail=f'<details><summary>{len(pairs)} paired previews</summary><div class="pairs">'+''.join(pair_cards)+'</div></details>' if pairs else '<p class="muted">No solo trial pair yet</p>'
        cards.append(f'<article data-main="{str(ident in mapped).lower()}" data-name="{html.escape(ident)}"><h2>{html.escape(ident)}</h2><img loading="lazy" class="host" src="{image}" alt="Container ink and 2-unit buffer"><p>{status} · center {zone["center"][0]:g}, {zone["center"][1]:g}</p><p class="muted">{html.escape(zone["reason"])}</p>{evidence}{detail}</article>')
    (OUT/'results.json').write_text(json.dumps({'padding':PADDING,'raster_pixels_per_unit':SCALE,'containers':results},indent=2)+'\n')
    (OUT/'index.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>All container buffers</title><style>
body{font:14px system-ui;background:#f6f7f9;color:#202630;margin:28px}header{max-width:1000px}h1{font-size:28px}h2{font-size:14px;overflow-wrap:anywhere}p{line-height:1.5}nav{display:flex;gap:12px;flex-wrap:wrap;align-items:center;margin:22px 0}input,select,button{font:inherit;padding:10px;border:1px solid #ccd1d8;border-radius:8px;background:white}main{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:16px}article{padding:20px;background:white;border:1px solid #e0e3e8;border-radius:12px}.host{width:192px;height:192px;display:block;margin:16px auto}summary{cursor:pointer;padding:10px 0;color:#28624c}.pairs{display:flex;flex-wrap:wrap;gap:12px}figure{margin:0;width:128px}figure img{width:128px;height:128px}figcaption{font-size:12px;overflow-wrap:anywhere}.muted{color:#78818d}article[hidden]{display:none}</style><header><h1>Container buffer preview</h1><p><a href="../container-vector-report/index.html"><b>Open the vector report — measurements in SVG units</b></a></p>'''
        +f'<p><b>{len(mapped)} main containers · {len(results)} total containers · {pair_count} paired previews · 2-unit padding</b></p>'
        +'''<p><a href="../container-center-audit/index.html">Full center audit and confidence rubric</a>. Confidence is an evidence score, not a probability. Centers balance the chosen safe zone; the best position for a particular sub icon may differ.</p><p><b>Orange:</b> 2-unit exclusion buffer around visible ink. <b>Green:</b> chosen safe zone for sub-icon ink, excluding decorative compartments and hardware. <b>Blue:</b> preferred placement center. Brain and prohibition containers have a center only, with no safe-zone claim. Zones include a conservative raster margin; final combinations still need vector clearance checks.</p><p>Expand a container to see its existing trial pairs with a buffer around the sub icon. Red marks estimated collisions. Paired previews below still show the earlier trial placements; they have not been recomposed into these newly chosen zones.</p></header><nav><input id="search" placeholder="Find container…" aria-label="Find container"><select id="scope" aria-label="Container scope"><option value="main">Main containers on page</option><option value="all">All container-family icons</option></select><button id="expand">Expand paired previews</button><span id="count"></span></nav><main>'''+''.join(cards)+'''</main><script>
const cards=[...document.querySelectorAll('article')],search=document.querySelector('#search'),scope=document.querySelector('#scope');function filter(){let n=0;for(const c of cards){c.hidden=!(c.dataset.name.includes(search.value.toLowerCase())&&(scope.value==='all'||c.dataset.main==='true'));if(!c.hidden)n++}document.querySelector('#count').textContent=n+' containers shown'}search.oninput=filter;scope.onchange=filter;document.querySelector('#expand').onclick=()=>{const open=[...document.querySelectorAll('article:not([hidden]) details')].some(d=>!d.open);document.querySelectorAll('article:not([hidden]) details').forEach(d=>d.open=open)};filter();</script></html>''')
    print(json.dumps({'containers':len(results),'main_containers':len(mapped),'paired_previews':pair_count,'statuses':dict(Counter(r['area_status'] for r in results)),'preview':str(OUT/'index.html')},indent=2))

if __name__=='__main__':main()

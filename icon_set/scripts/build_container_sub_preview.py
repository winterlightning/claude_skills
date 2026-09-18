"""Build a local comparison gallery of untouched containers and native SUB32 SVGs."""
from pathlib import Path
import base64
import hashlib
import json
import xml.etree.ElementTree as ET

BASE=Path(__file__).resolve().parents[1]
OUT=BASE/'work/container-sub-preview'


def uri(path):
    return 'data:image/svg+xml;base64,'+base64.b64encode(path.read_bytes()).decode()


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    areas=json.loads((BASE/'data/container-content-areas.json').read_text())['areas']
    vector={r['container']:r for r in json.loads((BASE/'work/container-vector-report/results.json').read_text())['containers']}
    sizes={r['container']:r for r in json.loads((BASE/'work/container-size-report/results.json').read_text())['containers']}
    subs=[]
    for path in sorted((BASE/'dist/sub32').glob('*.svg')):
        root=ET.fromstring(path.read_text())
        if [float(v) for v in root.get('viewBox','').replace(',',' ').split()] != [0,0,32,32]:
            raise ValueError('Unexpected SUB32 canvas: '+path.name)
        subs.append({'name':path.stem,'uri':uri(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    hosts=[]
    for path in sorted((BASE/'dist/container64').glob('*.svg')):
        name=path.stem;area=areas.get(name,{});v=vector.get(name,{})
        sha=hashlib.sha256(path.read_bytes()).hexdigest()
        fresh=area.get('source_sha256')==sha and v.get('source_sha256')==sha
        center=(v.get('center_units') or area.get('center')) if fresh else None
        guide=BASE/'work/container-vector-report'/v.get('preview','')
        hosts.append({'name':name,'uri':uri(path),'sha256':sha,'center':center or [32,32],
                      'placement':('saved content center' if fresh and center else 'canvas center — needs placement review'),
                      'guide':uri(guide) if fresh and guide.is_file() else uri(path),
                      'square_status':sizes.get(name,{}).get('sizes',{}).get('32',{}).get('status','review') if fresh else 'review',
                      'boundary':v.get('status','review') if fresh else 'review'})
    data={'hosts':hosts,'subs':subs}
    template='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Actual sub-icons inside containers</title><style>
*{box-sizing:border-box}body{font:15px system-ui;background:#f5f7fa;color:#202630;margin:28px}header{max-width:1050px}h1{font-size:30px}p{line-height:1.6}a{color:#245f9a}nav{background:#f5f7fa;position:sticky;top:0;padding:12px 0;z-index:1;border-bottom:1px solid #dce2e9}label{display:inline-flex;gap:7px;align-items:center;margin:5px 10px 5px 0}select,input{font:inherit;border:1px solid #cbd3dd;border-radius:7px;padding:8px;background:white}select.sub{max-width:245px}main{display:grid;grid-template-columns:repeat(auto-fill,minmax(440px,1fr));gap:18px;margin-top:20px}article{background:white;border:1px solid #dce2e9;border-radius:12px;padding:20px;overflow:hidden}h2{font-size:16px;margin:0 0 8px;overflow-wrap:anywhere}.note{font-size:12px;color:#687585}.badge{display:inline-block;background:#edf1f6;padding:4px 7px;font-size:12px;border-radius:4px}.examples{display:flex;gap:12px;flex-wrap:wrap;margin-top:16px}figure{margin:0;flex:1;min-width:110px;text-align:center}figure svg{width:var(--preview-size,128px);height:var(--preview-size,128px);max-width:100%;background:white;display:block;margin:auto}figcaption{font-size:11px;overflow-wrap:anywhere;margin:8px 0;line-height:1.4}button{font:inherit;cursor:pointer;background:white;border:1px solid #cbd3dd;border-radius:6px;padding:5px 9px;font-size:12px}article[hidden]{display:none}#count{margin-left:10px;font-size:13px}@media(max-width:500px){body{margin:16px}main{grid-template-columns:1fr}}
</style><header><h1>Actual sub-icons inside containers</h1><p><a href="../container-pair-combinations/index.html"><b>Browse the defined container/sub-icon pairs on a 64 × 64 grid</b></a></p><p><a href="../container-fit-repair/index.html"><b>Review revised containers and corrected placements — before / after</b></a></p><p><b>Native 32 × 32 sub-icons, placed inside the 64 × 64 containers.</b> Compare three real shapes side by side. Change any selector to try another of the 266 existing sub-icons.</p><p>These are preview compositions at the saved content center. Sub-icons keep their original paths, size and strokes; the display zoom enlarges the entire composition equally. Overlaps remain visible for your review. No container or sub-icon artwork has been modified, and these previews are not automatic fit approvals.</p><p>The earlier full-square result is shown only as context. An actual glyph can fit differently because its corners and margins may be empty. Containers needing a boundary decision use their previous content center for this visual trial.</p><p><a href="../container-size-report/index.html">Square-footprint report</a> · <a href="../container-vector-report/index.html">Vector measurements</a></p></header>
<nav><div id="choices"></div><div><input id="search" placeholder="Find container…" aria-label="Find container"><label>Show <select id="scope"><option value="all">All containers</option><option value="too-small">Previously too small for square</option><option value="fits">Square fits</option><option value="borderline">Square borderline</option><option value="review">Boundary needed</option><option value="overlay">Overlay exceptions</option></select></label><label>Display <select id="zoom"><option value="128">2×</option><option value="64">Native 64 units</option><option value="192">3×</option></select></label><label><input type="checkbox" id="guides">Show clearance guides</label><span id="count"></span></div></nav><main></main>
<script id="data" type="application/json">__DATA__</script><script>
const data=JSON.parse(document.querySelector('#data').textContent),ns='http://www.w3.org/2000/svg',defaults=['check-mark','add-sub32','heart-state-63'];
const choices=document.querySelector('#choices'),main=document.querySelector('main'),q=document.querySelector('#search'),scope=document.querySelector('#scope'),guides=document.querySelector('#guides');
const selectors=defaults.map((name,i)=>{const l=document.createElement('label');l.textContent='Sub '+String.fromCharCode(65+i);const s=document.createElement('select');s.className='sub';s.setAttribute('aria-label','Sub icon '+String.fromCharCode(65+i));data.subs.forEach((sub,j)=>{const o=document.createElement('option');o.value=j;o.textContent=sub.name;s.append(o)});s.value=Math.max(0,data.subs.findIndex(x=>x.name===name));l.append(s);choices.append(l);s.onchange=()=>drawColumn(i);return s});
const labels={'too-small':'Full square: too small',fits:'Full square: fits',borderline:'Full square: borderline',review:'Boundary needs review',overlay:'Overlay exception'};
function svgElement(tag,attrs){const n=document.createElementNS(ns,tag);for(const [k,v] of Object.entries(attrs))n.setAttribute(k,v);return n}
function compose(h,sub){const svg=svgElement('svg',{xmlns:ns,viewBox:'0 0 64 64',width:64,height:64,role:'img','aria-label':h.name+' with '+sub.name});svg.append(svgElement('image',{href:guides.checked?h.guide:h.uri,x:0,y:0,width:64,height:64}));svg.append(svgElement('image',{href:sub.uri,x:h.center[0]-16,y:h.center[1]-16,width:32,height:32}));return svg}
const cards=data.hosts.map(h=>{const c=document.createElement('article');c.dataset.name=h.name;c.dataset.status=h.square_status;const title=document.createElement('h2');title.textContent=h.name;c.append(title);const b=document.createElement('span');b.className='badge';b.textContent=labels[h.square_status]||h.square_status;c.append(b);const p=document.createElement('p');p.className='note';p.textContent=h.placement+' · ('+h.center.map(x=>x.toFixed(2)).join(', ')+')';c.append(p);const row=document.createElement('div');row.className='examples';c.append(row);const figures=selectors.map((s,i)=>{const f=document.createElement('figure');row.append(f);return f});main.append(c);return {h,c,figures}});
function drawColumn(i){const sub=data.subs[Number(selectors[i].value)];for(const {h,figures} of cards){const f=figures[i],svg=compose(h,sub);f.replaceChildren(svg);const caption=document.createElement('figcaption');caption.textContent=sub.name;f.append(caption);const button=document.createElement('button');button.textContent='Save SVG';button.onclick=()=>{const clean=compose(h,sub);const blob=new Blob([new XMLSerializer().serializeToString(clean)],{type:'image/svg+xml'}),url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download=h.name+'--'+sub.name+'-preview.svg';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000)};f.append(button)}}
function filter(){let count=0;for(const {c,h} of cards){c.hidden=!(h.name.includes(q.value.toLowerCase())&&(scope.value==='all'||h.square_status===scope.value));if(!c.hidden)count++}document.querySelector('#count').textContent=count+' containers · '+(count*3)+' previews'}
selectors.forEach((_,i)=>drawColumn(i));filter();q.oninput=filter;scope.onchange=filter;guides.onchange=()=>selectors.forEach((_,i)=>drawColumn(i));document.querySelector('#zoom').onchange=e=>document.body.style.setProperty('--preview-size',e.target.value+'px');
</script></html>'''
    (OUT/'index.html').write_text(template.replace('__DATA__',json.dumps(data,separators=(',',':')).replace('<','\\u003c')))
    # Save standalone SVG compositions for the default comparison too.
    default_names=['check-mark','add-sub32','heart-state-63']
    selected=[next(s for s in subs if s['name']==name) for name in default_names]
    ET.register_namespace('','http://www.w3.org/2000/svg')
    for h in hosts:
        for sub in selected:
            root=ET.Element('{http://www.w3.org/2000/svg}svg',{'viewBox':'0 0 64 64','width':'64','height':'64'})
            for image,x,y,size in [(h['uri'],0,0,64),(sub['uri'],h['center'][0]-16,h['center'][1]-16,32)]:
                ET.SubElement(root,'{http://www.w3.org/2000/svg}image',{'href':image,'x':str(x),'y':str(y),'width':str(size),'height':str(size)})
            (OUT/f'{h["name"]}--{sub["name"]}.svg').write_text(ET.tostring(root,encoding='unicode'))
    manifest={'hosts':len(hosts),'native_sub32_options':len(subs),'default_subs':default_names,'default_combinations':len(hosts)*3,'placements':[{k:v for k,v in h.items() if k not in ('uri','guide')} for h in hosts]}
    (OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({k:v for k,v in manifest.items() if k!='placements'},indent=2))
    print(OUT/'index.html')

if __name__=='__main__':main()

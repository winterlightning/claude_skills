"""Compose the 23 newly generated text references with their recorded containers."""
from pathlib import Path
import sys,json,re,hashlib,html,copy,xml.etree.ElementTree as ET

if __package__:
    from .workspace import development_dist
else:
    from workspace import development_dist

ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
from svgpathtools import parse_path
from icon_set.scripts.container_placement import Artwork,place,digest
BASE=ROOT/'icon_set';OUT=BASE/'work/container-text-pair-trials'


def text_art(document):
    root=ET.fromstring(document);paths=[]
    def walk(node,scale=1,dx=0,dy=0,style=None):
        style={**(style or {}),**node.attrib}
        transform=node.get('transform','')
        rest=re.sub(r'(translate|scale)\s*\([^)]*\)','',transform).strip()
        if rest:raise ValueError('Unsupported text transform')
        for op,params in re.findall(r'(translate|scale)\s*\(([^)]*)\)',transform):
            ns=[float(v) for v in re.split(r'[ ,]+',params.strip())]
            if op=='translate':dx+=ns[0]*scale;dy+=(ns[1] if len(ns)>1 else 0)*scale
            else:
                if len(ns)>1 and ns[0]!=ns[1]:raise ValueError('Nonuniform text scale')
                scale*=ns[0]
        tag=node.tag.split('}')[-1]
        if tag=='path':
            if abs(float(style.get('stroke-width',0))*scale-4)>1e-6:raise ValueError('Text stroke must be 4')
            path=parse_path(node.get('d')).scaled(scale).translated(complex(dx,dy));paths.append((f'text-{len(paths)}',path.d(),path))
        elif tag not in ('svg','g','title','desc'):raise ValueError('Unsupported text geometry '+tag)
        for child in node:walk(child,scale,dx,dy,style)
    walk(root)
    b=[p.bbox() for _,_,p in paths]
    return Artwork(document,paths,(min(x[0] for x in b),min(x[2] for x in b),max(x[1] for x in b),max(x[3] for x in b)),digest(document),28)


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    items=json.loads((BASE/'work/container-unbriefed-subs/generated-items.json').read_text());by_source={r['source_id']:r for r in items}
    catalog=json.loads((development_dist(BASE.parent) / 'gallery/combinations.json').read_text());areas=json.loads((BASE/'data/container-content-areas.json').read_text())['areas'];records={r['key']:r for r in json.loads((development_dist(BASE.parent) / 'gallery/icons.json').read_text())['icons']}
    records.update({'container/'+r['icon_id']:r for r in json.loads((development_dist(BASE.parent) / 'container64/manifest.json').read_text())['icons']})
    main_map=json.loads((BASE/'data/container-main-icons.json').read_text())['mappings']
    records.update({'text/'+r['icon_id']:r for r in json.loads((development_dist(BASE.parent) / 'text28/manifest.json').read_text())['icons']})
    pairs=[r for r in catalog['rows'] if r['kind']=='container' and r['sub_id'] in by_source];results=[];cache={};cards=[]
    for pair in pairs:
        sub=by_source[pair['sub_id']];hosts=[r for r in pair.get('main_generated',[]) if r['key'].startswith('container/')]
        if not hosts and pair['main_id'] in main_map:
            mapped=main_map[pair['main_id']]['icon_id'];hosts=[{'icon_id':mapped,'key':'container/'+mapped}]
        if not hosts:raise ValueError('Missing container for '+pair['concept'])
        host=hosts[0];main_id=host['icon_id'];key=main_id+'--'+sub['icon_id']
        if key not in cache:
            host_path=development_dist(BASE.parent) / 'container64'/f'{main_id}.svg';sub_path=development_dist(BASE.parent) / 'text28'/f'{sub["icon_id"]}.svg'
            main=Artwork.read(host_path.read_text(),64);content=text_art(sub_path.read_text());extent=max(content.bounds[2]-content.bounds[0],content.bounds[3]-content.bounds[1])+4
            sizes=sorted(set([min(extent,x) for x in [48,44,40,36,32,28,24]]),reverse=True)
            result=place(main,content,padding=2,sizes=sizes,area=areas.get(main_id))
            (OUT/f'{key}.svg').write_text(result.pop('svg'));(OUT/f'{key}-buffer.svg').write_text(result.pop('debug_svg'))
            result.update(svg_file=key+'.svg',buffer_file=key+'-buffer.svg',main_key=host['key'],sub_key='text/'+sub['icon_id'],main_sha256=records[host['key']]['svg_sha256'],sub_sha256=records['text/'+sub['icon_id']]['svg_sha256'],source_file_hashes={'main':main.sha256,'sub':content.sha256},svg_sha256=hashlib.sha256((OUT/f'{key}.svg').read_bytes()).hexdigest(),native_sub32=False)
            cache[key]=result
            cards.append(f'<article><h2>{html.escape(sub["name"])}</h2><p>{html.escape(main_id)}</p><div><img src="{key}.svg"><img src="{key}-buffer.svg"></div><p>{result["status"]} · 2-unit minimum gap</p><p>Ink gap: {result["validation"].get("measured_ink_padding",0):.2f} units</p></article>')
            print(f'{len(cache)}: {main_id} + {sub["name"]}: {result["status"]}',flush=True)
        results.append({**cache[key],'pair_id':pair['id'],'concept':pair['concept'],'main_source_id':pair['main_id'],'sub_source_id':pair['sub_id']})
    (OUT/'results.json').write_text(json.dumps({'results':results},indent=2,default=lambda v:v.item())+'\n')
    (OUT/'index.html').write_text('<!doctype html><meta charset="utf-8"><title>Container + text pairs</title><style>body{font:14px system-ui;background:#f4f6f8;margin:28px;color:#17212d}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(330px,1fr));gap:16px}article{background:white;border:1px solid #ddd;border-radius:12px;padding:18px}h2{font-size:16px}img{width:128px;height:128px;margin:10px}p{color:#657080}</style><h1>Container + text pairs</h1><p>'+str(len(results))+' recorded pairs · '+str(len(cache))+' distinct combinations. Left: combination. Right: 2-unit buffer. Text source artwork remains unchanged; the fitted content keeps stroke width 4. These are trial compositions; clearance does not certify small-text legibility.</p><main>'+''.join(cards)+'</main>')

if __name__=='__main__':main()

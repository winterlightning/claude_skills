"""Materialize independent SUB32 Python models from reviewed reuse artwork.

Geometry is copied into ordinary editable primitive calls, never evaluated from
or scaled from a solo model at runtime. Validation remains the normal build gate.
"""
from __future__ import annotations
import argparse
import hashlib
import inspect
import io
import json
import re
import sys
from pathlib import Path
import xml.etree.ElementTree as ET
from svgpathtools import Document, Line, Arc, CubicBezier, QuadraticBezier
from icon_set.model.icons.registry import factories
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile

if __package__:
    from .workspace import development_dist
else:
    from workspace import development_dist


ROOT = Path(__file__).resolve().parents[2]
AUTHOR = 'gpt-6'


def point(z):
    return tuple(int(v) if float(v).is_integer() else float(v) for v in (z.real, z.imag))


def dot_text_layout(document):
    """Scale point-only text proportionally; a fixed 4px cap cannot reach height 32."""
    segments = [segment for path in Document(io.StringIO(document)).paths() for segment in path]
    if not segments or not all(isinstance(p, Line) and p.start == p.end for p in segments):
        return None
    if len({p.start.imag for p in segments}) != 1:
        return None
    xs = [p.start.real for p in segments]
    return min(xs), int(round((max(xs) - min(xs) + 4) * 8))


def primitive_calls(document, *, text=False):
    root = ET.fromstring(document)
    box=list(map(float, root.attrib['viewBox'].split()))
    if box[:2] != [0,0] or box[3] != 32 or (not text and box[2] != 32):
        raise ValueError('Requires an existing square 32px export')
    if float(root.get('stroke-width', 4)) != 4:
        raise ValueError('Requires a four-unit stroke')
    paths, elements = [], []
    for element in root:
        if element.tag.rsplit('}',1)[-1] not in ('path','circle'):
            continue
        single = ET.Element(root.tag, root.attrib)
        single.append(element)
        for path in Document(io.StringIO(ET.tostring(single,encoding='unicode'))).paths():
            paths.append(path)
            elements.append(element)
    dot_layout = dot_text_layout(document) if text else None
    calls, endpoints = [], {}
    for pi, path in enumerate(paths):
        element = elements[pi]
        number = r"[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?"
        authored_arcs = iter(re.findall(r"[Aa]\s*("+number+r")[,\s]+("+number+r")[,\s]+("+number+r")", element.get('d','')))

        subpath_texts=re.findall(r'[Mm][^Mm]*',element.get('d',''))
        for si, run in enumerate(path.continuous_subpaths()):
            explicitly_closed = element.tag.rsplit('}',1)[-1]=='circle' or (si < len(subpath_texts) and bool(re.search('[Zz]',subpath_texts[si])))
            members=[]
            for ni, segment in enumerate(run):
                name=f'p{pi+1}-r{si+1}-{ni+1}'
                members.append(name)
                start,end=point(segment.start),point(segment.end)
                if dot_layout:
                    start = end = (round((segment.start.real - dot_layout[0]) * 8 + 16), 16)
                endpoints[name]=(start,end)
                if isinstance(segment,Line):
                    calls.append(f'self.add_line({name!r}, {start!r}, {end!r})')
                elif isinstance(segment,Arc):
                    if segment.rotation % 90:
                        raise ValueError('Non-cardinal elliptical arc needs explicit model conversion')
                    if element.tag.rsplit('}',1)[-1] == 'circle':
                        rx = ry = float(element.get('r'))
                    else:
                        rx, ry, rotation = map(float, next(authored_arcs))
                    if segment.rotation % 180:
                        rx, ry = ry, rx
                    rx = int(rx) if float(rx).is_integer() else rx
                    ry = int(ry) if float(ry).is_integer() else ry
                    calls.append(f'self.add_arc({name!r}, {start!r}, {end!r}, radius_x={rx!r}, radius_y={ry!r}, large_arc={bool(segment.large_arc)!r}, sweep={bool(segment.sweep)!r})')
                else:
                    if isinstance(segment,QuadraticBezier):
                        c1=segment.start+2/3*(segment.control-segment.start)
                        c2=segment.end+2/3*(segment.control-segment.end)
                    elif isinstance(segment,CubicBezier):c1,c2=segment.control1,segment.control2
                    else:raise ValueError(type(segment).__name__)
                    calls.append(f'self.add_bezier({name!r}, {start!r}, {(point(c1),point(c2),end)!r})')
            if members:
                calls.append(f'self.add_contour({f"path-{pi+1}-{si+1}"!r}, '+', '.join(repr(n) for n in members)+f', closed={explicitly_closed!r})')
    # Declare only actual endpoint contacts between different primitive runs.
    names=list(endpoints)
    for i,a in enumerate(names):
        for b in names[i+1:]:
            if a.rsplit('-',1)[0] != b.rsplit('-',1)[0] and set(endpoints[a]) & set(endpoints[b]):
                calls.append(f'self.relate("connect", {a!r}, {b!r})')
    if not calls:raise ValueError('Empty drawing')
    return calls


def shape_for(record):
    bounds=record['ink32']['ink_bounds']
    shapes=[s for s in Keyshape if s not in (Keyshape.FREE,Keyshape.CIRCLE)]
    return min(shapes,key=lambda s:sum(abs(a-b) for a,b in zip(bounds,s.bounds_for(Profile.SUB32)))).name


def run(root=ROOT, *, rewrite=False):
    data=root/'icon_set/data'
    input_path=data/'sub-profile-inputs.json'
    canonical=json.loads((input_path if input_path.exists() else data/'canonical-sub32.json').read_text())
    if not input_path.exists():input_path.write_text(json.dumps(canonical,indent=2)+'\n')
    manifest=json.loads((data/'combination-sub32.json').read_text())
    aliases=json.loads((data/'sub-deduplication.json').read_text())['aliases']
    registered=factories()
    previous_path=data/'sub-profile-migration.json'
    previous=json.loads(previous_path.read_text()) if previous_path.exists() else {'icons':{}}
    text_path=development_dist(root) / 'text32/manifest.json'
    text_records={r['icon_id']:r for r in json.loads(text_path.read_text())['icons']} if text_path.exists() else {}
    rows={}; links=[]; pending=[]
    for uid, record in sorted(canonical.items()):
        family=record['family']
        members=[uid]+sorted(a for a,target in aliases.items() if target==uid)
        sources=[];originals=[]
        for member in members:
            origin=manifest[member];factory=registered.get(member)
            if origin['family']!='sub':
                sources.append(dict(key=origin['family']+'/'+member,profile='SOLO48' if origin['family']=='solo' else 'CONTAINER64' if origin['family']=='container' else 'TEXT32',
                                    source_svg=origin['source_svg'],svg_sha256=hashlib.sha256((root/origin['source_svg']).read_bytes()).hexdigest(),
                                    relationship='derived_from' if member==uid else 'canonical_reuse'))
            if factory:
                module=sys.modules[factory.__module__]
                solo=getattr(module,'SOLO_SOURCE_ICON_ID',None)
                if solo and solo in registered and not any(s['key']=='solo/'+solo for s in sources):
                    f=development_dist(root) / 'solo48'/f'{solo}.svg'
                    sources.append(dict(key='solo/'+solo,profile='SOLO48',source_svg=str(f.relative_to(root)),svg_sha256=hashlib.sha256(f.read_bytes()).hexdigest() if f.exists() else None,relationship='derived_from'))
                originals.extend([(getattr(module,'SOURCE_ICON_ID',None),getattr(module,'SOURCE_PATH',None))])
                for ref in getattr(module,'SOURCE_REFERENCES',()):
                    if isinstance(ref,(tuple,list)) and len(ref)==2:originals.append(tuple(ref))
        text_record=text_records.get(uid,{})
        for ref in text_record.get('original_sources',[]):
            originals.append((ref.get('source_id'),ref.get('source_path')))
        if not any(u for u,p in originals):
            match=re.search(r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}',record['source_svg'])
            if match:originals.append((match[0],record['source_svg']))
        sources=list({s['key']:s for s in sources}.values())
        document=(root/record['svg']).read_text()
        prior = previous['icons'].get(uid,{})
        if family=='sub' and uid in registered and prior.get('status') != 'created':
            target=uid
            if target not in registered:raise ValueError('Missing native model: '+target)
            path=Path(inspect.getsourcefile(registered[target])).resolve()
            state='existing'
        else:
            old=previous['icons'].get(uid,{})
            target=old.get('model_key','').removeprefix('sub/') or (uid if family=='sub' else uid.removesuffix('-solo')+'-sub32')
            if not old and target in registered:
                target=uid+'-profile32'
            if not old and target in registered:raise ValueError('Model collision: '+target)
            source_id=next((u for u,p in originals if u),None)
            source_path=next((p for u,p in originals if p),record['source_svg'])
            suffix='_'+re.sub('[^a-zA-Z0-9_]', '_',source_id) if source_id else ''
            path=(root/old['python_source']) if old else root/'icon_set/model/icons/sub'/(target.replace('-','_')+suffix+'.py')
            state='created'
            if path.exists():
                if not old or old.get('python_source')!=str(path.relative_to(root)):
                    raise ValueError('Refusing to overwrite '+str(path))
            if rewrite and prior.get("previous_model_keys"):
                raise ValueError("Refusing to regenerate a repaired variant: " + target)
            if not path.exists() or rewrite:
                calls=primitive_calls(document, text=family=='text')
                primary=registered.get(uid)
                category=getattr(primary,'category','primitives/mark')
                keys=tuple(s['key'] for s in sources)
                refs=list(dict.fromkeys((u,p) for u,p in originals if u or p))
                content='"""Independent 32px profile of '+uid+'.\nSnapshot of the reviewed reuse drawing; validate before publication.\nEdit these primitives independently of the linked source models.\n"""\n'
                base = 'TextSub32' if family=='text' else 'Sub32'
                content+='from ...keyshapes import Keyshape\nfrom '+('._text_base import TextSub32' if family=='text' else '._base import Sub32')+'\n\n'
                content+=f'SOURCE_ICON_ID = {source_id!r}\nSOURCE_PATH = {source_path!r}\nAUTHOR = {AUTHOR!r}\nSOURCE_REFERENCES = {tuple(refs)!r}\n'
                content+=f'PROFILE_SOURCE_KEYS = {keys!r}\nSOLO_SOURCE_ICON_IDS = {tuple(k.split("/",1)[1] for k in keys if k.startswith("solo/"))!r}\n'
                content+=f'TYPEFACE_GLYPH_IDS = {tuple(text_record.get("glyph_ids",[]))!r}\n'
                content+=f'REFERENCE_EXPORT_SHA256 = {hashlib.sha256(document.encode()).hexdigest()!r}\n\n'
                content+=f'class Drawing({base}):\n    icon_id = {target!r}\n    keyshape = Keyshape.{shape_for(record)}\n    semantic_role = "SUB"\n    semantic_kind = "modifier"\n    category = {category!r}\n    profile_source_keys = PROFILE_SOURCE_KEYS\n\n    def build(self):\n'
                if family=='text':
                    dots = dot_text_layout(document)
                    width = dots[1] if dots else int(ET.fromstring(document).get("width"))
                    ink = (0, 0, width, 32) if dots else tuple(record["ink32"]["ink_bounds"])
                    style = '    STROKE_WIDTH = 32  # Proportional dot-only text.\n' if dots else ''
                    content=content.replace('    def build(self):', style + f'    text_canvas_width = {width}\n    text_ink_bounds = {ink!r}\n\n    def build(self):')
                content+=''.join('        '+call+'\n' for call in calls)
                pending.append((path,content))
        key='sub/'+target
        rows[uid]=dict(canonical=uid,model_key=key,python_source=str(path.relative_to(root)),status=state,sources=sources,
                       reference_export=record['svg'],reference_export_sha256=hashlib.sha256(document.encode()).hexdigest())
        if prior.get("previous_model_keys"):
            rows[uid]["previous_model_keys"] = prior["previous_model_keys"]
        for source in sources:links.append(dict(source=source['key'],target=key,relationship=source['relationship'],source_svg_sha256=source['svg_sha256']))
    # Parse every generated module before any write.
    import ast
    for path,content in pending:ast.parse(content,filename=str(path))
    for path,content in pending:path.write_text(content)
    result=dict(schema='pictographic.sub-profile-migration.v1',icons=rows)
    (data/'sub-profile-migration.json').write_text(json.dumps(result,indent=2)+'\n')
    (data/'icon-profile-links.json').write_text(json.dumps(dict(schema='pictographic.icon-profile-links.v1',links=links),indent=2)+'\n')
    print('Created',len(pending),'models;',sum(r['status']=='existing' for r in rows.values()),'existing;',sum(r['status']=='text-kept-separate' for r in rows.values()),'text entries separate;',len(links),'profile links',flush=True)
    return result

if __name__=='__main__':run(rewrite='--rewrite-generated' in sys.argv)

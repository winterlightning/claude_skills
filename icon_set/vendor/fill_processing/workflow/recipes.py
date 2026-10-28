"""Freeze Normal region roles; replay roles on each source without smart-fill AI.

WKT is matching evidence only. Styled paint always comes from the styled source.
Ambiguous hierarchy/element correspondence is a hold, never a guessed decision.
"""
import copy
import hashlib
import importlib.metadata
import json
import math
import heapq
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import numpy as np
from scipy.optimize import linear_sum_assignment
from shapely import wkt
from shapely.geometry import Polygon, box, Point, LineString
from shapely.affinity import affine_transform
from shapely.ops import unary_union
from svgpathtools import parse_path, Line, Path as SvgPath

from ..treatments import geometry as g
from ..treatments.compiler import compile_recipe, engine_hash as object_engine_hash
from ..treatments.corners import round_export

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'vendor'))
from step_2_fill_refactor_enhance import process_svg

STYLES = ('normal', 'round', 'sharp')


def dump(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')


def engine_hash():
    files = [Path(__file__), Path(__file__).with_name('program.py'), Path(__file__).with_name('source_derivations.py'), Path(__file__).resolve().parents[1]/'vendor/step_2_fill_refactor_enhance.py']
    deps = {n: importlib.metadata.version(n) for n in ('shapely','scipy','numpy','svgpathtools','skia-pathops','fonttools')}
    return hashlib.sha256(object_engine_hash().encode()+json.dumps(deps,sort_keys=True).encode()+b''.join(p.read_bytes() for p in files)).hexdigest()


def raw_sources(root, name):
    return {s: {'file': f'{s}/{name}.svg', 'sha256': g.sha(root/s/(name+'.svg'))}
            for s in STYLES if (root/s/(name+'.svg')).is_file()}


def sources(root, name):
    from .source_derivations import apply_derivations
    return apply_derivations(root,name,raw_sources(root,name))


def source(recipe, root, style):
    record = recipe['sources'].get(style)
    if not record:
        raise ValueError('source: missing '+style)
    p = root/record['file']
    if p.resolve().is_relative_to((root/'derived-candidates').resolve()):
        if sources(root,recipe['name']).get(style)!=record:
            raise ValueError('source: private derived source lacks current accepted provenance')
    if g.sha(p) != record['sha256']:
        raise ValueError('source: stale '+style)
    document = ET.parse(p).getroot()
    if recipe.get('schema') == 'normal-region-decisions/v1' and recipe.get('mode') == 'retain':
        # Retention is an exact byte copy, not geometry compilation. Preserve
        # original canvases and paint (including backgrounds) without forcing
        # them through the fill compiler's 48-unit/monochrome restrictions.
        if document.tag not in ('svg', '{http://www.w3.org/2000/svg}svg'):
            raise ValueError('source: retained source is not an SVG document')
        if record != raw_sources(root, recipe['name']).get(style):
            raise ValueError('source: retention requires this style original SVG')
    else:
        g.validate_source(document)
    return p


def parent(value):
    return None if value is None or math.isnan(value) else int(value)


def freeze(df):
    return [{'id':int(r.region_id), 'parent':parent(r.parent_id), 'level':int(r.level),
             'ring':r.ring, 'decision':r.fill, 'geometry_wkt':r.geometry.wkt}
            for _,r in df.iterrows()]


def iou(a, b):
    return a.intersection(b).area/max(a.union(b).area, 1e-12)


def assignment(a, b, threshold=.45, margin=.05):
    if len(a) != len(b):
        raise ValueError('style_mapping: changed region/element count')
    if not a:
        return []
    scores = np.array([[iou(x,y) for y in b] for x in a])
    rows, cols = linear_sum_assignment(-scores)
    pairs = []
    for i,j in zip(rows,cols):
        alternatives = [scores[i,k] for k in range(len(b)) if k != j]
        column_alternatives = [scores[k,j] for k in range(len(a)) if k != i]
        if scores[i,j] < threshold or any(scores[i,j]-v < margin for v in alternatives+column_alternatives):
            raise ValueError(f'style_mapping: ambiguous correspondence (IoU {scores[i,j]:.4f})')
        pairs.append((int(i),int(j),float(scores[i,j])))
    return pairs


def transfer(definitions, df):
    styled = freeze(df.assign(fill='keep'))
    if len(definitions) != len(styled):
        raise ValueError('style_mapping: changed region topology')
    audit = []
    def visit(np_, sp):
        a = [r for r in definitions if r['parent']==np_]
        b = [r for r in styled if r['parent']==sp]
        pairs = assignment([Polygon(wkt.loads(r['geometry_wkt']).exterior) for r in a],
                           [Polygon(wkt.loads(r['geometry_wkt']).exterior) for r in b])
        for i,j,score in pairs:
            x,y=a[i],b[j]
            if (x['ring'],x['level']) != (y['ring'],y['level']):
                raise ValueError('style_mapping: incompatible hierarchy')
            df.loc[df.region_id == y['id'],'fill'] = x['decision']
            audit.append({'normal':x['id'],'styled':y['id'],'iou':score,'decision':x['decision']})
            visit(x['id'],y['id'])
    visit(None,None)
    if len(audit) != len(definitions):
        raise ValueError('style_mapping: incomplete hierarchy')
    return audit


def propose_baseline(item, root):
    bindings = sources(root,item['name'])
    row, geometry, df, distance = process_svg(root/bindings['normal']['file'], edge_close=item['close_bottom'])
    native_cuts=[]
    for evidence in row['small_detail_cutouts']:
        if evidence['rule'].startswith('native_solid'):
            matches=[p for s in row['filled_shapes'] for p in g.fu.to_polys(s['geometry'])
                     if s['source_id']==evidence['source_id'] and max(abs(a-b) for a,b in zip(p.bounds,evidence['bounds']))<.0001]
            if len(matches)!=1:
                raise ValueError('normal_semantics: ambiguous native dot')
            native_cuts.append({'geometry_wkt':matches[0].wkt,'source_id':evidence['source_id']})
    return {'schema':'normal-region-decisions/v1','name':item['name'],'sources':bindings,
            'mode':'regions','regions':freeze(df),'adjacency_distance':distance,
            'closure_requested':item['close_bottom'],'closures':row['closures'],
            'native_cuts':native_cuts,'small_detail_evidence':row['small_detail_cutouts'],
            'corner_policy':{'round':{'operation':'round_convex_black','radius':2}},
            'proposal':'Normal smart_fill only; per-region decisions frozen for review',
            'objects':[{'id':'source-assembly','name':item['name'],'scope':'entire source assembly',
                        'treatment':'explicit region roles; preserve unselected native paint'}]}


def retain(item, root, rationale):
    return {'schema':'normal-region-decisions/v1','name':item['name'],'sources':sources(root,item['name']),
            'mode':'retain','reason':rationale,
            'objects':[{'id':'original','name':item['name'],'treatment':'keep_original_paint'}]}


def paint_data(path, work, solids=False):
    root = ET.parse(path).getroot(); g.validate_source(root)
    ink = g.paint(root,work/'source-paint.svg')
    # Historical global faces are plain interior contours sorted spatially.
    faces = [Polygon(h) for p in g.fu.to_polys(ink) for h in p.interiors]
    faces.sort(key=lambda p:(round(p.centroid.y,4),round(p.centroid.x,4),p.area))
    paint=[]
    for n in range(len(g.leaves(root))):
        paint.append(g.paint(g.subset(root,[f'leaf:{n}']),work/f'leaf-{n}.svg'))
    return {'root':root,'ink':ink,'faces':faces,'paint':paint}


def _leaf_context(root, index):
    element=g.leaves(root)[index]; parents=g.fu._build_parent_map(root)
    if g.fu._local_tag(element.tag)!='path':
        raise ValueError('geometry_execution: structural cut requires an original path')
    chain=[]; node=element
    while node is not None:
        chain.append(node);node=parents.get(node)
    transform=g.fu._IDENTITY
    for node in reversed(chain):
        transform=g.fu._compose(transform,g.fu._parse_transform(node.get('transform','')))
    a,b,c,d,e,f=transform; matrix=np.array([[a,c,e],[b,d,f],[0,0,1.]])
    if g.fu._resolve_attr(element,'vector-effect',parents,'none')=='non-scaling-stroke':
        raise ValueError('geometry_execution: structural cut needs explicit non-scaling width mapping')
    width=g.fu._svg_length(g.fu._resolve_attr(element,'stroke-width',parents,'1'))
    if width<=0:raise ValueError('geometry_execution: structural cut requires positive stroke width')
    return element,matrix,width


def _terminal_direction(path,end):
    meaningful=[segment for segment in path if segment.length()>0]
    if not meaningful:
        raise ValueError('geometry_execution: structural cut has no directional segment')
    if end=='start':return path.start,-meaningful[0].unit_tangent(0)
    if end=='end':return path.end,meaningful[-1].unit_tangent(1)
    raise ValueError('geometry_execution: invalid structural cut terminal')


def _terminals(root,index):
    element,matrix,width=_leaf_context(root,index); records=[]
    for si,path in enumerate(parse_path(element.get('d')).continuous_subpaths()):
        if path.isclosed():continue
        for end in ('start','end'):
            z,v=_terminal_direction(path,end)
            point=matrix@np.array([z.real,z.imag,1.]); tangent=matrix[:2,:2]@np.array([v.real,v.imag])
            tangent=tangent/np.linalg.norm(tangent)
            records.append({'subpath':si,'end':end,'point':point[:2].tolist(),
                            'outward':tangent.tolist(),'world_width_limit':width*np.linalg.norm(matrix[:2,:2],2)})
    return records


def _map_terminals(root,index,definitions):
    available=_terminals(root,index); chosen=[]
    for definition in definitions:
        candidates=[]
        for row in available:
            distance=float(np.linalg.norm(np.array(row['point'])-definition['point']))
            agreement=float(np.dot(row['outward'],definition['outward']))
            if agreement>.5 and distance<=2*max(row['world_width_limit'],definition['world_width_limit'])+.02:
                candidates.append((distance,row))
        candidates.sort(key=lambda pair:pair[0])
        if not candidates or len(candidates)>1 and candidates[1][0]-candidates[0][0]<.05:
            raise ValueError('style_mapping: ambiguous structural-cut terminal')
        row=candidates[0][1]
        if any((r['subpath'],r['end'])==(row['subpath'],row['end']) for r in chosen):
            raise ValueError('style_mapping: two structural cuts map to one terminal')
        chosen.append(dict(row,normal_terminal={'subpath':definition['subpath'],'end':definition['end']},
                           endpoint_distance=candidates[0][0]))
    return chosen


def _solid_leaf(data,index,work,label):
    tree=g.subset(data['root'],[f'leaf:{index}']);g.leaves(tree)[index].set('fill','currentColor')
    return g.paint(tree,work/(label+'.svg'))


def _cut_to_outline(data,index,owner,endpoints,work,label,solid=False):
    """Port of the historical owner-clipped, full-width structural seam exit."""
    tree=g.subset(data['root'],[f'leaf:{index}']);element,matrix,width=_leaf_context(tree,index)
    inverse=np.linalg.inv(matrix)
    local=affine_transform(owner,(inverse[0,0],inverse[0,1],inverse[1,0],inverse[1,1],inverse[0,2],inverse[1,2]))
    paths=parse_path(element.get('d')).continuous_subpaths();records=[]
    for rule in endpoints:
        si,end=rule['subpath'],rule['end'];path=paths[si]
        if path.isclosed() or end not in ('start','end'):
            raise ValueError('geometry_execution: structural cut needs an authorized open terminal')
        z,v=_terminal_direction(path,end);point=Point(z.real,z.imag)
        distance=point.distance(local.boundary)
        if distance>width*2+.02:raise ValueError('style_mapping: structural terminal no longer near owning outline')
        length=width*4;outside=z+v*length
        if local.buffer(width).covers(Point(outside.real,outside.imag)):
            raise ValueError('geometry_execution: terminal direction does not exit owner')
        if not LineString([(z.real,z.imag),(outside.real,outside.imag)]).intersects(local.boundary):
            raise ValueError('geometry_execution: terminal extension misses owner')
        extension=Line(outside,z) if end=='start' else Line(z,outside)
        paths[si]=SvgPath(extension,*path) if end=='start' else SvgPath(*path,extension)
        records.append({'subpath':si,'end':end,'source_width_local':width,
                        'distance_to_outline':distance,'extension_length_local':length,'full_width_exit':True})
    element.set('d',' '.join(path.d() for path in paths))
    if solid:element.set('fill','currentColor')
    cutter=g.paint(tree,work/(label+'.svg'))
    return g.clean(cutter.intersection(owner.buffer(.01))),{
        'owner_clipped':True,'owner_clip_tolerance':.01,'endpoints':records,'solid_after_extension':solid}


def _close_between(data,left,right,work,label):
    """Join two bound sides with their existing source connector and one base."""
    root=copy.deepcopy(data['root']);elements=g.leaves(root)
    if any(element.get('transform') for element in root.iter()):
        raise ValueError('geometry_execution: stitched closure needs transform normalization')
    if any(g.fu._local_tag(elements[index].tag)!='path' for index in (left,right)):
        raise ValueError('geometry_execution: stitched closure needs original path sides')
    a=parse_path(elements[left].get('d'));b=parse_path(elements[right].get('d'))
    if not a.iscontinuous() or not b.iscontinuous() or a.isclosed() or b.isclosed():
        raise ValueError('geometry_execution: closure sides must be continuous open paths')
    key=lambda z:(round(z.real,5),round(z.imag,5));graph={}
    for index,element in enumerate(elements):
        if index in (left,right) or g.fu._local_tag(element.tag)!='path':continue
        for segment in parse_path(element.get('d')):
            if abs(segment.end-segment.start)<1e-8:continue
            graph.setdefault(key(segment.start),[]).append((key(segment.end),segment.length(),segment,index))
            graph.setdefault(key(segment.end),[]).append((key(segment.start),segment.length(),segment.reversed(),index))
    target=key(b[-1].end);pending=[(0,0,key(a[-1].end),[])];seen=set();serial=0;connector=None
    while pending:
        distance,_,node,route=heapq.heappop(pending)
        if node in seen:continue
        seen.add(node)
        if node==target:connector=route;break
        for nxt,cost,segment,index in graph.get(node,[]):
            if nxt not in seen:
                serial+=1;heapq.heappush(pending,(distance+cost,serial,nxt,route+[(segment,index)]))
    if connector is None:raise ValueError('style_mapping: no source-linked connector between closure sides')
    segments=[*a,*[segment for segment,_ in connector],*b.reversed(),Line(b[0].start,a[0].start)]
    if any(abs(p.end-q.start)>1e-5 for p,q in zip(segments,segments[1:])):
        raise ValueError('style_mapping: disconnected source closure boundary')
    elements[left].set('d',SvgPath(*segments).d()+' Z')
    tree=g.subset(root,[f'leaf:{left}']);g.leaves(tree)[left].set('fill','currentColor')
    material=g.clean(g.paint(tree,work/(label+'.svg')).intersection(box(*data['ink'].bounds)))
    return material,{'left_leaf':left,'right_leaf':right,
        'connector_leaves':sorted({index for _,index in connector}),
        'connector':'shortest_existing_centerline','new_edge':'between_open_bottom_terminals',
        'bounds_limit':list(data['ink'].bounds)}


def _mapped_operand(reference,available,kind):
    scores=sorted([(iou(wkt.loads(reference),paint),index) for index,paint in enumerate(available)],reverse=True)
    if not scores or scores[0][0]<.45 or len(scores)>1 and scores[0][0]-scores[1][0]<.05:
        raise ValueError('style_mapping: ambiguous operation '+kind)
    return scores[0][1],available[scores[0][1]],scores[0][0]


def recover_operations(item, old, root, work):
    if old.get('source_sha256') != g.sha(root/'normal'/(item['name']+'.svg')):
        raise ValueError('source: historical recipe source hash differs')
    if old.get('strategy')=='keep_script':
        recipe=propose_baseline(item,root)
        if old.get('script',{}).get('regions'):
            regions=old['script']['regions']
            recipe['regions']=[{'id':r.get('id',r.get('region_id')),'parent':r.get('parent',r.get('parent_id')),'level':r['level'],'ring':r['ring'],
                                'decision':r['decision'],'geometry_wkt':r['geometry_wkt']} for r in regions]
        recipe['historical_recipe']=old
        return recipe
    supported={'fill_face','cut_face','solidify_leaf','cut_leaf','cut_solid_leaf','close_fill_leaf','cut_extended_leaf',
               'cut_to_outline','close_between_leaves'}
    unsupported={o['operation'] for o in old.get('operations',[])}-supported
    if unsupported:
        raise ValueError('geometry_execution: unported historical operations '+','.join(sorted(unsupported)))
    data=paint_data(root/'normal'/(item['name']+'.svg'),work)
    ops=copy.deepcopy(old.get('operations',[]))
    for op in ops:
        if 'face' in op:
            face=data['faces'][op['face']]
            if 'anchor' in op:
                from shapely.geometry import Point
                if not face.buffer(.001).covers(Point(op['anchor'])):
                    raise ValueError('normal_semantics: historical face anchor mismatch')
            op['normal_geometry_wkt']=face.wkt
        if 'leaf' in op:
            op['normal_geometry_wkt']=data['paint'][op['leaf']].wkt
        if op['operation']=='cut_to_outline':
            terminals=_terminals(data['root'],op['leaf']);definitions=[]
            for endpoint in op['endpoints']:
                matches=[t for t in terminals if (t['subpath'],t['end'])==(endpoint['subpath'],endpoint['end'])]
                if len(matches)!=1:raise ValueError('normal_semantics: invalid historical structural-cut endpoint')
                definitions.append(matches[0])
            op['normal_endpoints']=definitions
            if 'owner_leaf' in op:op['normal_owner_geometry_wkt']=data['paint'][op['owner_leaf']].wkt
        if op['operation']=='close_between_leaves':
            op['normal_left_geometry_wkt']=data['paint'][op['left_leaf']].wkt
            op['normal_right_geometry_wkt']=data['paint'][op['right_leaf']].wkt
    return {'schema':'normal-region-decisions/v1','name':item['name'],'sources':sources(root,item['name']),
            'mode':'source_operations','operations':ops,'historical_recipe':old,
            'objects':old.get('objects',[]),
            'closure_policy':old.get('closure_policy',{}),
            'corner_policy':{'round':{'operation':'round_convex_black','radius':2}},
            'reason':old.get('historical_reason','Source-linked historical recipe; new review required')}


def replay(recipe_path, root, work, style):
    recipe=json.loads(recipe_path.read_text()); work.mkdir(parents=True,exist_ok=False)
    if recipe['schema']=='source-object-treatments/v1':
        receipt=compile_recipe(recipe_path,root,work/'compiled',styles=[style])
        result=receipt['styles'][style]
        if result['status']=='held': raise ValueError('geometry_execution: '+result['error'])
        (work/'fill.svg').write_bytes((work/'compiled'/style/'fill.svg').read_bytes())
        dump(work/'receipt.json',result)
        return result
    path=source(recipe,root,style); audit=[]
    if recipe['mode']=='retain':
        (work/'fill.svg').write_bytes(path.read_bytes())
        result={'status':'generated','source_sha256':g.sha(path),'output_sha256':g.sha(work/'fill.svg'),
                'mode':'retain','mapping':[]}
        dump(work/'receipt.json',result); return result
    if recipe['mode']=='source_program':
        from .program import execute
        geometry,audit=execute(recipe,path,work,style)
    elif recipe['mode']=='regions':
        # No smart_fill call here: only the Normal proposal selects region roles.
        closure_audit = None
        region_source = path
        if 'native_closures' in recipe:
            if recipe.get('closure_requested') is not False or recipe.get('closures') != []:
                raise ValueError('source: native binding cannot combine with implicit closure detection')
            from ..treatments.native_closures import apply
            closed, closure_audit = apply(ET.parse(path).getroot(), recipe, root, style)
            region_source = work/'native-closed-source.svg'
            ET.ElementTree(closed).write(region_source, encoding='unicode')
            closure_audit = dict(closure_audit, derived_source_sha256=g.sha(region_source))
        row=g.fu.load_one(region_source,edge_close=recipe['closure_requested'])
        if recipe['closures']:
            if style!='normal':
                raise ValueError('style_mapping: bottom closure needs explicit per-style endpoint binding')
            if row['closures']!=recipe['closures']:
                raise ValueError('source: closure proposal changed')
        elif row['closures']:
            raise ValueError('style_mapping: unexpected closure')
        df=g.fu.build_region_dataframe(row['stroke_polygon'],recipe['adjacency_distance'])
        if not df.empty: df['fill']='keep'
        audit=transfer(recipe['regions'],df)
        if closure_audit is not None: audit.append({'native_closures':closure_audit})
        assembled=g.fu.assemble_polygon(df) if not df.empty else row['stroke_polygon']
        geometry=unary_union([p for p in (assembled,row['filled_polygon']) if p is not None])
        for cut in recipe.get('native_cuts',[]):
            available=[p for s in row['filled_shapes'] for p in g.fu.to_polys(s['geometry'])]
            scores=sorted([(iou(wkt.loads(cut['geometry_wkt']),p),i) for i,p in enumerate(available)],reverse=True)
            if not scores or scores[0][0]<.45 or len(scores)>1 and scores[0][0]-scores[1][0]<.05:
                raise ValueError('style_mapping: native dot correspondence is ambiguous')
            geometry=geometry.difference(available[scores[0][1]])
            audit.append({'native_cut':cut['source_id'],'styled_component':scores[0][1],'iou':scores[0][0]})
    elif recipe['mode']=='source_operations':
        data=paint_data(path,work); geometry=data['ink'];owners={}
        for op in recipe['operations']:
            kind=op['operation']
            if kind=='close_between_leaves':
                left,_,left_score=_mapped_operand(op['normal_left_geometry_wkt'],data['paint'],'closure left side')
                right,_,right_score=_mapped_operand(op['normal_right_geometry_wkt'],data['paint'],'closure right side')
                if left==right:raise ValueError('style_mapping: closure sides map to one leaf')
                operand,closure=_close_between(data,left,right,work,f'closure-{len(audit)}')
                owners[op['id']]=operand;geometry=geometry.union(operand)
                audit.append({'operation':kind,'id':op['id'],'left_iou':left_score,'right_iou':right_score,**closure})
                continue
            available=data['faces'] if 'face' in op else data['paint']
            n,operand,score=_mapped_operand(op['normal_geometry_wkt'],available,kind)
            audit.append({'operation':kind,'styled_operand':n,'iou':score})
            if kind=='cut_to_outline':
                if op.get('owner_operation'):
                    if op['owner_operation'] not in owners:raise ValueError('geometry_execution: missing earlier material owner')
                    owner=owners[op['owner_operation']]
                    audit[-1]['owner_operation']=op['owner_operation']
                else:
                    owner_index,_,owner_score=_mapped_operand(op['normal_owner_geometry_wkt'],data['paint'],'structural-cut owner')
                    owner=_solid_leaf(data,owner_index,work,f'owner-{len(audit)}')
                    audit[-1].update(styled_owner_leaf=owner_index,owner_iou=owner_score)
                endpoints=_map_terminals(data['root'],n,op['normal_endpoints'])
                operand,extension=_cut_to_outline(data,n,owner,endpoints,work,f'cut-to-outline-{len(audit)}',solid=op.get('solid',False))
                audit[-1].update(extension=extension,terminal_mapping=endpoints)
            elif 'leaf' in op and kind!='cut_leaf':
                tree=g.subset(data['root'],[f'leaf:{n}']); element=g.leaves(tree)[n]
                if kind in {'solidify_leaf','cut_solid_leaf','close_fill_leaf'}:
                    element.set('fill','currentColor')
                if kind in {'close_fill_leaf','cut_extended_leaf'}:
                    if g.fu._local_tag(element.tag)!='path':
                        raise ValueError('geometry_execution: closure/extension requires a path')
                    paths=parse_path(element.get('d')).continuous_subpaths()
                    if kind=='close_fill_leaf':
                        element.set('d',' '.join(p.d()+' Z' for p in paths))
                    else:
                        segs=[]
                        for p in paths:
                            if p.isclosed(): segs.extend(p); continue
                            # Explicit historical both-terminal tangent extension (8 source units).
                            segs.extend([Line(p[0].start-8*p[0].unit_tangent(0),p[0].start),*p,
                                         Line(p[-1].end,p[-1].end+8*p[-1].unit_tangent(1))])
                        element.set('d',SvgPath(*segs).d())
                operand=g.paint(tree,work/f'operation-{len(audit)}.svg')
            if op.get('include_boundary_stroke'):
                # Historical decision explicitly subtracts the face's source-width
                # boundary band, including its recorded junction clearance ratio.
                if 'face' not in op:raise ValueError('geometry_execution: boundary band requires a source face')
                width=g.fu._svg_length(data['root'].get('stroke-width','4'))
                join={'round':'round','miter':'mitre','bevel':'bevel'}[data['root'].get('stroke-linejoin','miter')]
                distance=width*(1+op.get('junction_clearance_stroke_ratio',0))
                operand=operand.buffer(distance,join_style=join,quad_segs=32)
                audit[-1]['boundary_band']={'source_width':width,'distance':distance,'join':join}
            if kind=='close_fill_leaf' and style in recipe.get('closure_policy',{}).get('source_bounds_styles',[]):
                operand=operand.intersection(box(*data['ink'].bounds))
                audit[-1]['closure_bounds']=list(data['ink'].bounds)
            geometry=geometry.difference(operand) if kind.startswith('cut_') else geometry.union(operand)
            if op.get('id') and kind in ('solidify_leaf','close_fill_leaf'):owners[op['id']]=operand
    else:
        raise ValueError('geometry_execution: unsupported recipe mode')
    geometry=g.clean(geometry)
    if geometry.is_empty or not geometry.is_valid:
        raise ValueError('geometry_execution: invalid or empty output')
    before=geometry; corners=None
    if style=='round' and recipe.get('corner_policy',{}).get('round'):
        geometry,corners=round_export(geometry,work/'fill.svg',radius=2)
    else:
        (work/'fill.svg').write_text(g.serialize(geometry)); geometry=g.read_export(work/'fill.svg')
    if style=='normal' and recipe.get('preserve_normal_reference'):
        reference=recipe['reference'];reference_path=Path(reference['file'])
        if g.sha(reference_path)!=reference['sha256']:
            raise ValueError('normal_semantics: preferred previous fill changed')
        preferred=g.read_export(reference_path)
        score=iou(preferred,geometry)
        if score<recipe['preserve_normal_reference']['minimum_iou'] or g.topology(preferred)!=g.topology(geometry):
            raise ValueError('normal_semantics: recovered recipe does not reproduce preferred previous fill')
        (work/'fill.svg').write_bytes(reference_path.read_bytes());geometry=preferred
        audit.append({'preserved_normal_reference':reference,'recovered_recipe_iou':score})
    if not box(-.001,-.001,48.001,48.001).covers(geometry) or g.topology(geometry)!=g.topology(before):
        raise ValueError('geometry_execution: final bounds or topology invalid')
    if g.sha(path)!=recipe['sources'][style]['sha256']:
        raise ValueError('source: source changed during replay')
    result={'status':'generated','source_sha256':g.sha(path),'output_sha256':g.sha(work/'fill.svg'),
            'mode':recipe['mode'],'mapping':audit,'bounds':geometry.bounds,'topology':g.topology(geometry),
            'corner_pass':corners,'source_geometry_only':not(style=='normal' and recipe.get('preserve_normal_reference'))}
    dump(work/'receipt.json',result)
    return result

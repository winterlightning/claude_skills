"""Explicit source-bound material construction and detail subtraction.

Programs bind original drawing leaves for every style. Constructed closures are
endpoint rules; no flattened fill coordinates enter this executor.
"""
import copy
import math
import xml.etree.ElementTree as ET
from shapely.geometry import Polygon, box
from shapely.ops import unary_union
from shapely import affinity, set_precision
from svgpathtools import parse_path, Path, Line, CubicBezier
from ..treatments import geometry as g


def element(root, binding, style):
    selector=binding[style]
    if not selector.startswith('leaf:'):raise ValueError('Explicit drawing leaf required')
    return g.leaves(root)[int(selector.split(':')[1])],selector


def subpath(root,binding,style):
    e,_=element(root,binding,style)
    if g.fu._local_tag(e.tag)!='path':raise ValueError('Boundary requires an original SVG path')
    # Construction in a transformed local frame needs an explicit coordinate map.
    parents=g.fu._build_parent_map(root)
    node=e
    while node is not None:
        if node.get('transform'):raise ValueError('Endpoint construction requires untransformed source paths')
        node=parents.get(node)
    paths=parse_path(e.get('d')).continuous_subpaths()
    if len(paths)>1 and 'subpath' not in binding:
        if any(abs(a.end-b.start)>1e-7 for a,b in zip(paths,paths[1:])):
            raise ValueError('Disconnected path needs explicit subpath binding')
        paths=[Path(*[segment for p in paths for segment in p])]
    index=binding.get('subpath',{}).get(style,0)
    result=paths[index]
    segment_range=binding.get('segments',{}).get(style)
    if segment_range is not None:result=Path(*result[segment_range[0]:segment_range[1]])
    if binding.get('reverse'):result=result.reversed()
    return result


def leaf_paint(root,binding,style,work,label,solid=False,extension=None):
    e,selector=element(root,binding,style);tree=g.subset(root,[selector]);target=g.leaves(tree)[int(selector.split(':')[1])]
    if solid:target.set('fill','currentColor')
    # A fragment selector applies to ordinary cuts/keeps as well as extensions.
    # Ignoring it can cut a whole mixed outline when only its inner seam is owned.
    if extension or any(k in binding for k in ('segments','subpath','reverse')):
        p=subpath(root,binding,style);segments=list(p)
        if not segments:raise ValueError('Empty source fragment')
        target.set('d',p.d())
    if extension:
        # The rule is in source stroke widths, independent of Normal coordinates.
        parents=g.fu._build_parent_map(root);width=float(g.fu._resolve_attr(e,'stroke-width',parents,'4'))
        length=width*extension.get('stroke_widths',2)
        if not math.isfinite(length) or length<0:raise ValueError('Extension needs a finite nonnegative length')
        ends=extension.get('ends_by_style',{}).get(style,extension.get('ends',[]))
        if set(ends)-{'start','end'}:raise ValueError('Unknown extension terminal')
        if ends and p.isclosed():raise ValueError('Cannot extend a closed source contour')
        if 'start' in ends:
            segments.insert(0,Line(p.start-length*p[0].unit_tangent(0),p.start))
        if 'end' in ends:
            segments.append(Line(p.end,p.end+length*p[-1].unit_tangent(1)))
        target.set('d',Path(*segments).d())
    return g.paint(tree,work/(label+'.svg'))


def boundary(root,op,style,work,label,solid=True):
    bindings=op.get('parts_by_style',{}).get(style,op.get('parts',[]))
    fragments=[subpath(root,b,style) for b in bindings]
    segments=[]
    for p in fragments:
        if segments and abs(segments[-1].end-p.start)>1e-9:
            segments.append(Line(segments[-1].end,p.start))
        segments.extend(p)
    start,end=segments[0].start,segments[-1].end
    if op.get('closure')=='vertical_then_horizontal':
        corner=complex(end.real,start.imag)
        if abs(end-corner)>1e-9:segments.append(Line(end,corner))
        end=corner
    if abs(end-start)>1e-9:segments.append(Line(end,start))
    _,selector=element(root,bindings[0],style)
    tree=g.subset(root,[selector]);e=g.leaves(tree)[int(selector.split(':')[1])]
    e.set('d',Path(*segments).d()+' Z');e.set('fill','currentColor' if solid else 'none')
    result=g.paint(tree,work/(label+'.svg'))
    if op.get('clip_to_parts_painted_bounds'):
        selectors=list(dict.fromkeys(element(root,b,style)[1] for b in bindings))
        paint=g.paint(g.subset(root,selectors),work/(label+'-original.svg'))
        result=result.intersection(box(*paint.bounds))
    return result


def accordion_panels(root,op,style,work):
    """Reference-informed panel/bellows layout, bound to source extents.

    The previous approved treatment has four keyboard cutouts, while the line
    source has three key strokes. Count=4 is an explicit saved semantic decision.
    Preserve each styled panel's outer curves and scale only its horizontal extent.
    """
    panels=[]
    for side,binding in zip(('left','right'),op['panels']):
        p=subpath(root,binding,style)
        # Some Sharp leaves combine one panel and an attached bellows line;
        # the recipe explicitly selects the original panel segments only.
        parts=list(p)
        if abs(p.start-p.end)>1e-9:parts.append(Line(p.end,p.start))
        _,selector=element(root,binding,style);tree=g.subset(root,[selector]);e=g.leaves(tree)[int(selector.split(':')[1])]
        e.set('d',Path(*parts).d()+' Z');e.set('fill','currentColor')
        paint=g.paint(tree,work/f'{side}-panel.svg');bounds=paint.bounds
        anchor=(bounds[0] if side=='left' else bounds[2],0)
        paint=affinity.scale(paint,xfact=op['panel_width_ratio'],yfact=1,origin=anchor)
        panels.append(paint)
    left,right=panels; lx,top,li,bottom=left.bounds;ri,_,rx,_=right.bounds
    fold=subpath(root,op['fold'],style);center=(fold.start.real+fold.end.real)/2
    width=op['gap'];half=width/2; inset=op['attachment_inset_strokes']*width
    # The same material graph is fitted to this style's source panel extents.
    bellows=[Polygon([(li,top+inset),(center-half,top),(center-half,bottom),(li,bottom-inset)]),
             Polygon([(ri,top+inset),(center+half,top),(center+half,bottom),(ri,bottom-inset)])]
    result=unary_union([*panels,*bellows])
    count=op['keyboard_count'];size=op['keyboard_size_strokes']*width
    margin=op.get('keyboard_margin_strokes',1)*width
    step=(bottom-top-2*margin-size)/(count-1)
    x=(lx+li)/2
    cuts=[box(x-size/2,top+margin+i*step,x+size/2,top+margin+i*step+size) for i in range(count)]
    return result.difference(unary_union(cuts))


def adjusted_cut(root,op,style,work,label,body):
    """Recover declared source-relative edits from a previous Normal decision."""
    tree=copy.deepcopy(root);e,_=element(tree,op['source'],style)
    p=subpath(tree,op['source'],style)
    parents=g.fu._build_parent_map(tree)
    width=float(g.fu._resolve_attr(e,'stroke-width',parents,'4'))
    edit=op['adjustment']
    if edit['kind']=='translate':
        p=p.translated(complex(*edit['stroke_offset'])*width)
    elif edit['kind']=='move_start':
        segments=list(p);first=segments[0]
        if not isinstance(first,Line):raise ValueError('Start adjustment needs a straight source segment')
        segments[0]=Line(first.start+complex(*edit['stroke_offset'])*width,first.end)
        p=Path(*segments)
    elif edit['kind']=='inset_cubic_seam':
        a,b=p.start,p.end
        offsets=edit['stroke_offsets']
        p=Path(CubicBezier(a+complex(*offsets[0])*width,a+complex(*offsets[1])*width,
                          b+complex(*offsets[2])*width,b+complex(*offsets[3])*width))
    else:raise ValueError('Unknown source-relative detail adjustment')
    if op.get('outer_clearance_strokes') is not None:
        # Clip the centerline before expanding its own native styled caps.
        limit=body.buffer(-width*(op['outer_clearance_strokes']+.5))
        if op.get('fit_below_owner_inset'):
            ymax=p.bbox()[3]
            p=p.translated(complex(0,min(0,limit.bounds[3]-ymax-.00001)))
        lines=[line.intersection(limit) for line in g.fu.path_to_linestrings(p.d())]
        segments=[]
        for line in lines:
            parts=[line] if line.geom_type=='LineString' else list(getattr(line,'geoms',[]))
            for part in parts:
                if part.geom_type!='LineString' or part.length<.001:continue
                points=[complex(x,y) for x,y in part.coords]
                segments.extend(Line(a,b) for a,b in zip(points,points[1:]))
        p=Path(*segments)
    e.set('d',p.d())
    return leaf_paint(tree,op['source'],style,work,label)


def execute(recipe,source,work,style):
    root=ET.parse(source).getroot();g.validate_source(root)
    result=g.paint(root,work/'original-paint.svg') if recipe.get('base')=='source_paint' else Polygon()
    owners={};audit=[]
    for i,op in enumerate(recipe['operations']):
        kind=op['operation'];label=f'program-{i}'
        if kind in ('material_boundary','cut_boundary'):operand=boundary(root,op,style,work,label)
        elif kind=='accordion_panels':operand=accordion_panels(root,op,style,work)
        elif kind in ('solidify','keep','cut','cut_solid'):
            operand=(adjusted_cut(root,op,style,work,label,owners[op['inset_owner']]['material'] if op.get('inset_owner') else result) if kind=='cut' and op.get('adjustment') else
                     leaf_paint(root,op['source'],style,work,label,solid=kind in ('solidify','cut_solid'),extension=op.get('extension')))
        else:raise ValueError('Unknown material program operation: '+kind)
        if kind in ('cut','cut_solid','cut_boundary'):
            if op.get('clearance_strokes') is not None:
                clearance=float(op['clearance_strokes'])
                if not math.isfinite(clearance) or clearance<0:raise ValueError('Clearance needs finite nonnegative stroke widths')
                binding=op.get('source') or op.get('parts_by_style',{}).get(style,op.get('parts',[]))[0]
                e,_=element(root,binding,style)
                parents=g.fu._build_parent_map(root)
                width=float(g.fu._resolve_attr(e,'stroke-width',parents,'4'))
                # Offset this style's complete material. Never scale/trace Normal
                # paint or widen its internal counters independently.
                join=op.get('clearance_join') or g.fu._resolve_attr(e,'stroke-linejoin',parents,'miter')
                if join not in ('round','miter','bevel'):raise ValueError('Unsupported clearance join: '+join)
                operand=operand.buffer(clearance*width,quad_segs=64,join_style={'round':1,'miter':2,'bevel':3}[join])
            if op.get('clip_to_owner_interior'):
                owner=owners[op['clip_to_owner_interior']]
                operand=operand.intersection(unary_union(g.faces(owner['outline'])))
            if op.get('clip_to_owner_material'):
                operand=operand.intersection(owners[op['clip_to_owner_material']]['material'])
            result=result.difference(operand)
        else:
            result=result.union(operand)
            if op.get('id'):
                outline=(leaf_paint(root,op['source'],style,work,label+'-outline') if 'source' in op else
                         boundary(root,op,style,work,label+'-outline',solid=False) if kind=='material_boundary' else operand)
                owners[op['id']]={'material':operand,'outline':outline}
        audit.append({'operation':kind,'id':op.get('id'),'source':op.get('source'),
                      'parts':op.get('parts'),'parts_by_style':op.get('parts_by_style'),
                      'clearance_strokes':op.get('clearance_strokes'),
                      'clip_to_owner_material':op.get('clip_to_owner_material'),
                      'bounds':operand.bounds,'area':operand.area})
    # Resolve sub-micro-unit boolean seams before topology validation at the
    # same precision used by the six-decimal SVG serializer.
    result=g.clean(set_precision(result,.000001))
    # Skia exports float32 coordinates. Sub-1e-10-unit-area holes at joined
    # source terminals are below that precision and cannot survive serialization.
    # Remove only these numerical voids, never components or visible details.
    polygons=[];removed=0
    for polygon in g.fu.to_polys(result):
        holes=[]
        for ring in polygon.interiors:
            if Polygon(ring).area<1e-10:removed+=1
            else:holes.append(ring)
        polygons.append(Polygon(polygon.exterior,holes))
    if removed:audit.append({'numerical_voids_removed':removed,'maximum_area':1e-10})
    return g.clean(unary_union(polygons)),audit

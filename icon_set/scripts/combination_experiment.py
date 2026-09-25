"""64px main/sub experiments using the vendored box-combination engine."""
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import re
import xml.etree.ElementTree as ET
from .icon_artwork import safe_svg

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data/combination-pairs.json'
POSITIONS = {'br': (1,1), 'bl': (0,1), 'tr': (1,0), 'tl': (0,0),
             'ri': (1,.5), 'le': (0,.5), 'bo': (.5,1), 'to': (.5,0)}


def number(value, default=0):
    if value in (None, ''):
        return default
    try:
        n = float(value)
    except (TypeError, ValueError):
        raise ValueError('Offsets must be numbers.')
    if not math.isfinite(n) or abs(n) > 64:
        raise ValueError('Offsets must be between -64 and 64.')
    return n


def placement(item, size, anchor, offset, padding=2, size_lock="none", bound_size=None, canvas=64):
    x0,y0,x1,y1 = item['bounds']
    if item.get('sizing_mode') == 'typeface-native':
        if size_lock not in ('none', 'auto') or bound_size not in (None, ''):
            raise ValueError('Native typeface keeps its original size.')
        w,h=x1-x0+4,y1-y0+4
        if max(w,h)>canvas-2*padding+1e-8:
            raise ValueError('Native text needs a larger combination canvas.')
        x=padding+(canvas-2*padding-w)*anchor[0]+offset[0]
        y=padding+(canvas-2*padding-h)*anchor[1]+offset[1]
        return {'size_lock':'none','locked_axis':None,'rounded_box':False,'locked_size':None,
                'canvas_box':dict(x=x,y=y,w=w,h=h),'painted_box':dict(x=x,y=y,w=w,h=h),
                'box':dict(x=(x+2)*24/canvas,y=(y+2)*24/canvas,w=(w-4)*24/canvas,h=(h-4)*24/canvas)}
    if item.get('sizing_mode') == 'container-content-resize':
        cw, ch = item.get('canvas_width'), item.get('canvas_height')
        if size != 32 or any(type(v) is not int or not 4 <= v <= 60 for v in (cw, ch)):
            raise ValueError('Container resize artwork requires its declared integer dimensions.')
        if size_lock not in ('none', 'auto') or bound_size not in (None, ''):
            raise ValueError('Resize variants keep their authored dimensions; select another model to change size.')
        w, h = x1-x0+4, y1-y0+4
        if abs(w-cw) > 1e-8 or abs(h-ch) > 1e-8:
            raise ValueError('Resize artwork does not match its declared ink dimensions.')
        x = round(padding+(canvas-2*padding-cw)*anchor[0]+offset[0])
        y = round(padding+(canvas-2*padding-ch)*anchor[1]+offset[1])
        return {'size_lock':'none', 'locked_axis':None, 'rounded_box':False,
                'locked_size':None, 'canvas_box':dict(x=x,y=y,w=cw,h=ch),
                'painted_box':dict(x=x,y=y,w=w,h=h),
                'box':dict(x=(x+2)*24/canvas,y=(y+2)*24/canvas,w=(w-4)*24/canvas,h=(h-4)*24/canvas)}
    if item.get('sizing_mode') in ('side-32x48', 'side-one-axis32', 'side-source-fit'):
        cw,ch = item.get('canvas_width'),item.get('canvas_height')
        if size != 32 or type(cw) is not int or type(ch) is not int or min(cw,ch) < 32 or (item.get('sizing_mode') != 'side-source-fit' and 32 not in (cw,ch)):
            raise ValueError('Side artwork requires one 32px canvas dimension.')
        if size_lock not in ('none', 'auto') or bound_size not in (None, ''):
            raise ValueError('Side artwork keeps its original 32×48 or declared exception size.')
        if cw > canvas-2*padding or ch > canvas-2*padding:
            raise ValueError('Source-faithful artwork needs a larger combination canvas; it cannot be shrunk to fit.')
        w,h = x1-x0+4,y1-y0+4
        if w > cw or h > ch:
            raise ValueError('Tall side artwork exceeds its 32×48 canvas.')
        ax,ay = anchor
        bx,by = padding+(canvas-2*padding-cw)*ax,padding+(canvas-2*padding-ch)*ay
        x,y = bx+(cw-w)*ax+offset[0],by+(ch-h)*ay+offset[1]
        return {'size_lock':'none', 'locked_axis':None, 'rounded_box':False,
                'locked_size':None, 'canvas_box':dict(x=bx,y=by,w=cw,h=ch),
                'painted_box':dict(x=x,y=y,w=w,h=h),
                'box':dict(x=(x+2)*24/canvas,y=(y+2)*24/canvas,w=(w-4)*24/canvas,h=(h-4)*24/canvas)}
    scale = size / item['canvas']
    w,h = (x1-x0)*scale, (y1-y0)*scale
    if size_lock not in ('none', 'auto', 'width', 'height'):
        raise ValueError('Choose automatic, width, height, or original sub sizing.')
    locked_axis = None
    rounded_auto = size == 32 and size_lock == 'auto' and bound_size in (None, '')
    if rounded_auto:
        width,height = x1-x0,y1-y0
        longest = max(width,height)
        if longest <= 0:
            raise ValueError('Cannot normalize empty sub geometry.')
        # User-defined reuse envelope: longest painted axis is exactly 32.
        # Preserve proportions; never snap each axis independently.
        scale = (size-4)/longest
        w,h = width*scale,height*scale
        locked_axis = 'width' if w>=h else 'height'
    elif size_lock != 'none':
        locked_axis = ('width' if w >= h else 'height') if size_lock == 'auto' else size_lock
        extent = (x1-x0) if locked_axis == 'width' else (y1-y0)
        if extent <= 0:
            raise ValueError('Cannot lock an empty dimension; choose the other axis.')
        max_target = 4 + (size-4)*extent/max(x1-x0, y1-y0)
        current = (w if locked_axis == 'width' else h) + 4
        if bound_size in (None, ''):
            target = min(math.floor(current+.5), math.floor(max_target+1e-9))
            target = max(5, target)
        else:
            target = number(bound_size)
            if target != int(target) or not 5 <= target <= size:
                raise ValueError(f'Locked visible size must be a whole number from 5 to {size}.')
        scale = (target-4)/extent
        w,h = (x1-x0)*scale, (y1-y0)*scale
    if max(w,h)+4 > size+.01:
        raise ValueError(f'Artwork exceeds its {size}×{size} component canvas.')
    ax,ay = anchor
    bx,by = padding+(canvas-2*padding-size)*ax, padding+(canvas-2*padding-size)*ay
    x,y = bx+(size-w-4)*ax+offset[0], by+(size-h-4)*ay+offset[1]
    return {'size_lock': size_lock, 'locked_axis': locked_axis,
            'rounded_box': False,
            'locked_size': (w+4 if locked_axis == 'width' else h+4) if locked_axis else None,
            'canvas_box': dict(x=bx,y=by,w=size,h=size),
            'painted_box': dict(x=x,y=y,w=w+4,h=h+4),
            'box': dict(x=(x+2)*24/canvas,y=(y+2)*24/canvas,w=w*24/canvas,h=h*24/canvas)}


def custom_item(value, role):
    if not isinstance(value,dict) or not isinstance(value.get('document'),str):
        raise ValueError('Choose an SVG for '+role+'.')
    text=value['document']
    if len(text.encode())>1024*1024 or re.search(r'<!(DOCTYPE|ENTITY)',text,re.I):
        raise ValueError('Upload a plain SVG up to 1 MB without entity declarations.')
    try:
        root=ET.fromstring(text)
        view=[float(n) for n in re.split(r'[\s,]+',root.get('viewBox','').strip())]
    except (ET.ParseError,ValueError):
        raise ValueError('Upload an SVG with a square viewBox starting at 0,0.')
    if len(view)!=4 or view[:2]!=[0,0] or view[2]!=view[3] or not 0<view[2]<=4096:
        raise ValueError('Upload an SVG with a square viewBox starting at 0,0 (up to 4096 units).')
    text=safe_svg(text,view[2])
    with tempfile.TemporaryDirectory(prefix='pair-measure-') as temp:
        file=Path(temp)/'icon.svg';file.write_text(text)
        try:
            proc=subprocess.run([os.environ.get('PICTOGRAPHIC_COMBINE_PYTHON') or sys.executable,
                str(ROOT/'scripts/measure_combination_svg.py'),str(file)],capture_output=True,text=True,timeout=60)
            measured=json.loads(proc.stdout.strip().splitlines()[-1])
        except (ValueError,IndexError,subprocess.TimeoutExpired):
            raise ValueError('Could not measure this SVG. Try simpler stroked artwork.')
        if proc.returncode or measured.get('error'):
            raise ValueError(measured.get('error') or 'Could not measure SVG.')
    bounds=measured['bounds'];size=48 if role=='main' else 32
    # Keep source scale where it fits; uniformly shrink oversized custom art.
    extent=max(bounds[2]-bounds[0],bounds[3]-bounds[1])
    canvas=max(view[2],extent*size/(size-4))
    return {'icon':'custom-'+role,'document':text,'canvas':canvas,'bounds':bounds}


def restore_original_sub(svg, item, placed):
    """Keep the engine's clipped main, but publish the original sub curves.

    Sampling is only used to compute clearance. It must not become sub artwork.
    One affine placement keeps every path command/control point unchanged.
    """
    import copy
    ns = 'http://www.w3.org/2000/svg'
    ET.register_namespace('', ns)
    target = ET.fromstring(svg)
    source = ET.fromstring(item['document'])
    old = next(e for e in target if e.get('id') == 'state-icon')
    index = list(target).index(old)
    target.remove(old)
    x0,y0,x1,y1 = item['bounds']
    box = placed['painted_box']
    scale = (box['w'] - 4) / (x1-x0) if x1 != x0 else (box['h'] - 4) / (y1-y0)
    tx,ty = box['x']+2-x0*scale, box['y']+2-y0*scale
    attrs = {k:v for k,v in source.attrib.items() if k not in ('width','height','viewBox','id','transform')}
    attrs.setdefault('stroke-width', '4')
    attrs.update(id='state-icon', transform=f'translate({tx:.12g} {ty:.12g}) scale({scale:.12g})')
    group = ET.Element('{'+ns+'}g', attrs)
    content = ET.SubElement(group, '{'+ns+'}g', {'transform':source.get('transform')}) if source.get('transform') else group
    for child in source:
        if child.tag.rsplit('}',1)[-1] not in ('title','desc'):
            content.append(copy.deepcopy(child))
    ids = {e.get('id'): 'sub-source-'+e.get('id') for e in group.iter() if e is not group and e.get('id')}
    for element in group.iter():
        for key,value in list(element.attrib.items()):
            if key=='id' and value in ids:element.set(key,ids[value])
            else:
                for old_id,new_id in ids.items():
                    value=value.replace('url(#'+old_id+')','url(#'+new_id+')')
                    if value=='#'+old_id:value='#'+new_id
                element.set(key,value)
        # Compensate placement scale only; viewBox zoom must scale both strokes equally.
        element.attrib.pop('vector-effect', None)
        if 'stroke-width' in element.attrib:
            element.set('stroke-width', str(float(element.get('stroke-width')) / scale))
    target.insert(index, group)
    return ET.tostring(target, encoding='unicode')


def layout_placement(bounds, canvas=64):
    """A baked layout document is already in canvas coordinates: place it at scale 1."""
    x0,y0,x1,y1 = bounds
    return {'size_lock':'none','locked_axis':None,'rounded_box':False,'locked_size':None,
            'canvas_box':dict(x=0,y=0,w=canvas,h=canvas),
            'painted_box':dict(x=x0-2,y=y0-2,w=x1-x0+4,h=y1-y0+4),
            'box':dict(x=x0*24/canvas,y=y0*24/canvas,w=(x1-x0)*24/canvas,h=(y1-y0)*24/canvas)}


def check_layout(layout):
    """{main: [{paths, x, y, w, h}], sub: [...]}; each role optional; whole grid units only.

    (x, y, w, h) is a group's centerline box on the canvas; width and height scale independently.
    """
    if layout is None:
        return None
    if not isinstance(layout,dict) or not set(layout) <= {'main','sub'}:
        raise ValueError('A layout lists groups for the main and/or the sub.')
    clean={}
    for role,groups in layout.items():
        if groups is None:
            continue
        if not isinstance(groups,list) or not groups or len(groups)>64:
            raise ValueError(f'List the {role} element groups.')
        clean[role]=[]
        for g in groups:
            if not isinstance(g,dict) or not isinstance(g.get('paths'),list) or not g['paths'] \
                    or any(type(i) is not int or i<0 for i in g['paths']):
                raise ValueError(f'Each {role} group needs its element numbers.')
            values={}
            for key in ('x','y','w','h'):
                v=g.get(key)
                if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v) or v!=int(v):
                    raise ValueError(f'{role} {key} must snap to a whole grid unit.')
                values[key]=int(v)
            # Native text can need a canvas larger than 64.
            if not -64<=values['x']<=256 or not -64<=values['y']<=256 or not 0<=values['w']<=256 or not 0<=values['h']<=256:
                raise ValueError(f'The {role} layout is outside the canvas.')
            clean[role].append({'paths':list(g['paths']),**values})
    return clean or None


def layout_components(components, canvas):
    """Connected element groups (and baked layouts) from the isolated engine helper."""
    python=os.environ.get('PICTOGRAPHIC_COMBINE_PYTHON') or sys.executable
    try:
        proc=subprocess.run([python,str(ROOT/'scripts/combination_layout_svg.py')],
                            input=json.dumps({'canvas':canvas,'components':components}),
                            capture_output=True,text=True,timeout=60,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
        out=json.loads(proc.stdout.strip().splitlines()[-1])
    except (ValueError,IndexError,subprocess.TimeoutExpired):
        raise ValueError('Could not measure the connected elements.')
    if proc.returncode or out.get('error'):
        raise ValueError(out.get('error') or 'Could not measure the connected elements.')
    return {c['role']:c for c in out['components']}


def solo48_keyshapes():
    """SOLO48 keyshape centerline bounds from the locked keyshape contract."""
    contract=json.loads((ROOT/'model/contracts/keyshapes.v1.json').read_text())
    return {name:k['centerline_bounds'] for name,k in contract['resolved']['SOLO48'].items()}


def placement_transform(item, placed):
    """Component coordinates -> canvas: (scale, tx, ty) of a default placement."""
    x0,y0,x1,y1 = item['bounds']
    box = placed['painted_box']
    scale = (box['w']-4)/(x1-x0) if x1-x0>1e-9 else (box['h']-4)/(y1-y0) if y1-y0>1e-9 else 1
    return scale, box['x']+2-x0*scale, box['y']+2-y0*scale


def pair_canvas(row, sub=None, padding=2):
    """64, or larger when the pair's native text sub needs it."""
    native_sub=next((s for s in row['subs'] if s['icon']==(sub or row['subs'][0]['icon'])),None)
    if native_sub and native_sub.get('sizing_mode')=='typeface-native':
        return max(64,math.ceil(max(native_sub['canvas_width'],native_sub['canvas_height'])+2*padding-1e-8))
    return 64


def default_groups(row, main=None, sub=None, padding=2):
    """The automatic placement's connected element groups, without running the combine engine.

    Returns (canvas, {role: [{paths, source, box}]}) for applying one pair's layout to another.
    """
    ax,ay=POSITIONS[row['position']]
    canvas=pair_canvas(row,sub,padding)
    requests=[]
    for role,group,size,anchor,icon in [('main','mains',48,(1-ax,1-ay),main),('sub','subs',32,(ax,ay),sub)]:
        item=next((i for i in row[group] if i['icon']==(icon or row[group][0]['icon'])),None)
        if item is None:
            raise ValueError(f'The {role} does not belong to this pair.')
        p=placement(item,size,anchor,(0,0),padding,size_lock='auto' if role=='sub' else 'none',canvas=canvas)
        scale,tx,ty=placement_transform(item,p)
        requests.append({'role':role,'document':item.get('engine_document',item['document']),'scale':scale,'tx':tx,'ty':ty,'layout':None})
    return canvas,{role:c['elements'] for role,c in layout_components(requests,canvas).items()}


def render(data, row=None):
    if row is None:
        rows = json.loads(DATA.read_text())['rows']
        row = next((r for r in rows if r['id']==data.get('id')),None)
    if row is None:
        raise ValueError('Choose an available icon pair.')
    position = data.get('position') or row['position']
    if position not in POSITIONS:
        raise ValueError('Choose one of the eight positions.')
    ax,ay = POSITIONS[position]
    margin = number(data.get('margin'),8)
    padding = number(data.get('padding'),2)
    if not 0 <= padding <= 8:
        raise ValueError('Canvas padding must be between 0 and 8.')
    if margin < 0:
        raise ValueError('Erasure margin must be between 0 and 64.')
    canvas=pair_canvas(row,data.get('sub'),padding)
    layout=check_layout(data.get('layout'))
    chosen=[]
    for role,group,size,anchor in [('main','mains',48,(1-ax,1-ay)),('sub','subs',32,(ax,ay))]:
        choices=row[group]; wanted=data.get(role) or choices[0]['icon']
        item=next((i for i in choices if i['icon']==wanted),None)
        if data.get(role+'Upload') is not None:
            item=custom_item(data[role+'Upload'],role)
        if item is None:
            raise ValueError('The selected component does not belong to this pair.')
        p=placement(item,size,anchor,(number(data.get(role+'X')),number(data.get(role+'Y'))),padding,
                    size_lock=data.get('subSizeLock', 'auto') if role=='sub' else 'none',
                    bound_size=data.get('subBoundSize') if role=='sub' else None,canvas=canvas)
        chosen.append([role,size,item,p])
    # Connected elements for the layout editor; a saved layout bakes them onto the grid.
    elements=None; elements_error=''
    if layout or data.get('elements'):
        requests=[]
        for role,_size,item,p in chosen:
            scale,tx,ty=placement_transform(item,p)
            # Native text positions its glyphs with transforms; its engine copy has them baked in.
            requests.append({'role':role,'document':item.get('engine_document',item['document']),'scale':scale,'tx':tx,'ty':ty,
                             'layout':(layout or {}).get(role)})
        try:
            measured=layout_components(requests,canvas)
        except ValueError as error:
            if layout:
                raise
            measured={}; elements_error=str(error)
        for entry in chosen:
            role,_size,item,_p=entry
            baked=measured.get(role,{})
            if 'document' in baked:
                item={'icon':item['icon'],'document':baked['document'],'canvas':canvas,'bounds':baked['bounds']}
                p=layout_placement(baked['bounds'],canvas)
                b=p['painted_box']
                if b['x']<-1e-6 or b['y']<-1e-6 or b['x']+b['w']>canvas+1e-6 or b['y']+b['h']>canvas+1e-6:
                    raise ValueError(f'The adjusted {role} extends beyond the {canvas}×{canvas} canvas.')
                entry[2:]=[item,p]
        if measured:
            elements={role:{'markup':c['markup'],'names':c['names'],'sources':c['sources'],'groups':c['elements']} for role,c in measured.items()}
    placements=[]; selected_sub=None
    with tempfile.TemporaryDirectory(prefix='pictographic-combination-') as temp:
        out = Path(temp); items=[]
        for n,(role,size,item,p) in enumerate(chosen):
            if role=='sub':selected_sub=item
            placements.append(dict(p,role=role,icon=item['icon']))
            file=out/(role+'.svg');file.write_text(item.get('engine_document',item['document']))
            items.append({'sid':item['icon'],'file':str(file),'box':p['box'],
                          'natural_box':p['box'],'manual_combined':True,
                          'preserve_geometry':True,'rounded_box':p['rounded_box'],'area':size*size,'ink':0,'z':n+1})
        spec={'id':row['id'],'name':row['concept'],'out_dir':str(out/'result'),
              'canvas':canvas,'stroke':4,'buffer_px':margin,'symbols':items}
        (out/'spec.json').write_text(json.dumps(spec))
        python=os.environ.get('PICTOGRAPHIC_COMBINE_PYTHON') or sys.executable
        try:
            proc=subprocess.run([python,str(ROOT/'vendor/combination/run_combine.py'),
                                 '--spec',str(out/'spec.json')],capture_output=True,text=True,
                                timeout=120,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
        except subprocess.TimeoutExpired:
            raise ValueError('This combination took too long. Try again.')
        try:
            result=json.loads(proc.stdout.strip().splitlines()[-1])
        except (ValueError,IndexError):
            raise ValueError('The combination engine could not start. Check its Python dependencies.')
        if not result.get('ok'):
            raise ValueError(result.get('error') or 'Could not combine these components.')
        file=(out/'result'/result['file']).resolve()
        if not file.is_relative_to(out.resolve()):
            raise ValueError('Unexpected combination output path.')
        svg=restore_original_sub(file.read_text(), selected_sub, placements[1])
    warnings=[]
    for p in placements:
        b=p['painted_box']
        if b['x']<0 or b['y']<0 or b['x']+b['w']>canvas+.01 or b['y']+b['h']>canvas+.01:
            warnings.append(f'Adjusted artwork extends beyond the {canvas}×{canvas} canvas and may be clipped.');break
    result={'svg':svg,'placements':placements,'position':position,'canvas':canvas,
            'filename':row['id']+'.svg','warnings':warnings,'margin':margin,'padding':padding,'subSizeLock':data.get('subSizeLock','auto'),'subBoundSize':data.get('subBoundSize','')}
    if layout:
        result['layout']=layout
    if elements is not None and data.get('elements'):
        result['elements']=elements
        # The editor's main size presets grow the main's SOLO48 keyshape onto a larger canvas.
        result['keyshapes']=solo48_keyshapes()
    if elements_error:
        result['elements_error']=elements_error
    return result

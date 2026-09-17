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


def placement(item, size, anchor, offset, padding=2):
    x0,y0,x1,y1 = item['bounds']
    scale = size / item['canvas']
    w,h = (x1-x0)*scale, (y1-y0)*scale
    if max(w,h)+4 > size+.01:
        raise ValueError(f'Artwork exceeds its {size}×{size} component canvas.')
    ax,ay = anchor
    bx,by = padding+(64-2*padding-size)*ax, padding+(64-2*padding-size)*ay
    x,y = bx+(size-w-4)*ax+offset[0], by+(size-h-4)*ay+offset[1]
    return {'canvas_box': dict(x=bx,y=by,w=size,h=size),
            'painted_box': dict(x=x,y=y,w=w+4,h=h+4),
            'box': dict(x=(x+2)*24/64,y=(y+2)*24/64,w=w*24/64,h=h*24/64)}


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
    placements=[]
    with tempfile.TemporaryDirectory(prefix='pictographic-combination-') as temp:
        out = Path(temp); items=[]
        for n,(role,group,size,anchor) in enumerate([
                ('main','mains',48,(1-ax,1-ay)),('sub','subs',32,(ax,ay))]):
            choices=row[group]; wanted=data.get(role) or choices[0]['icon']
            item=next((i for i in choices if i['icon']==wanted),None)
            if data.get(role+'Upload') is not None:
                item=custom_item(data[role+'Upload'],role)
            if item is None:
                raise ValueError('The selected component does not belong to this pair.')
            p=placement(item,size,anchor,(number(data.get(role+'X')),number(data.get(role+'Y'))),padding)
            placements.append(dict(p,role=role,icon=item['icon']))
            file=out/(role+'.svg');file.write_text(item['document'])
            items.append({'sid':item['icon'],'file':str(file),'box':p['box'],
                          'natural_box':p['box'],'manual_combined':True,
                          'preserve_geometry':True,'area':size*size,'ink':0,'z':n+1})
        spec={'id':row['id'],'name':row['concept'],'out_dir':str(out/'result'),
              'canvas':64,'stroke':4,'buffer_px':margin,'symbols':items}
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
        svg=file.read_text()
    warnings=[]
    for p in placements:
        b=p['painted_box']
        if b['x']<0 or b['y']<0 or b['x']+b['w']>64.01 or b['y']+b['h']>64.01:
            warnings.append('Adjusted artwork extends beyond the 64×64 canvas and may be clipped.');break
    return {'svg':svg,'placements':placements,'position':position,'canvas':64,
            'filename':row['id']+'.svg','warnings':warnings,'margin':margin,'padding':padding}

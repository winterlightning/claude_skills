"""Content-area proposals and measured placement for 64px container trials.

AI chooses a semantic area; geometry decides clearance. No primitive family or
profile is changed. Inputs must be uniform round 4-unit stroked path artwork.
"""
from __future__ import annotations
import copy
import hashlib
import io
import math
import xml.etree.ElementTree as ET
from dataclasses import dataclass

import cairosvg
from cairosvg.parser import Tree
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage, signal
from svgpathtools import parse_path, Line, CubicBezier, QuadraticBezier, Arc
from icon_set.validation.path_commands import Command
from icon_set.validation.stroke_distance import analyze_paths

NS='http://www.w3.org/2000/svg'
ET.register_namespace('',NS)
RESOLUTION=4
STROKE=4


def digest(document):
    return hashlib.sha256(document.encode()).hexdigest()


@dataclass
class Artwork:
    document: str
    paths: list
    bounds: tuple
    sha256: str
    canvas: int | tuple[int, int]

    @classmethod
    def read(cls, document, canvas):
        root=ET.fromstring(document)
        width, height = canvas if isinstance(canvas, tuple) else (canvas, canvas)
        if any(type(v) is not int or v < 4 for v in (width, height)):
            raise ValueError('Artwork canvas requires positive integer dimensions of at least 4.')
        if [float(x) for x in root.get('viewBox','').replace(',',' ').split()] != [0,0,width,height]:
            raise ValueError(f'Artwork must have viewBox 0 0 {width} {height}.')
        if any(any(k in n.attrib for k in ('transform','clip-path','mask','filter')) for n in root.iter()):
            raise ValueError('Flatten transforms, clipping and effects before measured placement.')
        paths=[]
        def walk(node):
            if node.tag in ('defs','style','title','desc','metadata'):return
            if node.tag in ('svg','g'):
                for child in node.children:walk(child)
                return
            if node.tag!='path':raise ValueError(f'Unsupported geometry: {node.tag}; use stroked paths.')
            width=float(str(node.get('stroke-width','0')).removesuffix('px'))
            if (width!=4 or node.get('fill','black')!='none' or node.get('stroke','none')=='none'
                or node.get('stroke-linecap')!='round' or node.get('stroke-linejoin')!='round'):
                raise ValueError('Measured placement requires unfilled paths with round 4-unit strokes.')
            if any(float(node.get(k,1))!=1 for k in ('opacity','stroke-opacity')):
                raise ValueError('Transparent source strokes require separate review.')
            path=parse_path(node['d'])
            if path:paths.append((node.get('id',f'path-{len(paths)}'),node['d'],path))
        walk(Tree(bytestring=document.encode()))
        if not paths:raise ValueError('No supported painted paths.')
        boxes=[p.bbox() for _,_,p in paths]
        bounds=(min(b[0] for b in boxes),min(b[2] for b in boxes),max(b[1] for b in boxes),max(b[3] for b in boxes))
        return cls(document,paths,bounds,digest(document),canvas)


def root_svg():
    return ET.Element('{'+NS+'}svg',{'width':'64','height':'64','viewBox':'0 0 64 64'})


def artwork_group(art,prefix,scale=1,dx=0,dy=0,stroke=4,color='currentColor',opacity=1):
    group=ET.Element('{'+NS+'}g',{'id':prefix,'fill':'none','stroke':color,'stroke-width':str(stroke/scale),
        'stroke-linecap':'round','stroke-linejoin':'round','opacity':str(opacity),
        'transform':f'translate({dx:.10f} {dy:.10f}) scale({scale:.10f})'})
    for i,(_,data,_) in enumerate(art.paths):
        ET.SubElement(group,'{'+NS+'}path',{'id':f'{prefix}-{i}','d':data})
    return group


def transform_for(art,scale,center):
    x0,y0,x1,y1=art.bounds
    return scale,center[0]-scale*(x0+x1)/2,center[1]-scale*(y0+y1)/2


def render(host,sub,transform,*,padding=None,area=None):
    root=root_svg()
    if area is not None:
        ET.SubElement(root,'{'+NS+'}polygon',{'points':' '.join(f'{x},{y}' for x,y in area),
            'fill':'#86efac','fill-opacity':'.18','stroke':'#16a34a','stroke-width':'.5'})
    if host:root.append(artwork_group(host,'container'))
    if padding is not None:root.append(artwork_group(sub,'buffer',*transform,stroke=4+2*padding,color='#f59e0b',opacity=.35))
    root.append(artwork_group(sub,'content',*transform))
    return ET.tostring(root,encoding='unicode')


def raster(document):
    data=cairosvg.svg2png(bytestring=document.encode(),output_width=256,output_height=256)
    return np.array(Image.open(io.BytesIO(data)).convert('RGBA'))[:,:,3]>100


def polygon_mask(points):
    image=Image.new('1',(256,256));ImageDraw.Draw(image).polygon([(x*4,y*4) for x,y in points],fill=1)
    return np.array(image,dtype=bool)


def validate_area(area,sha):
    if area.get('source_sha256')!=sha:raise ValueError('Saved content area is stale: container SVG changed.')
    points=area.get('polygon');center=area.get('center')
    def point(p):return isinstance(p,(list,tuple)) and len(p)==2 and all(type(n) in (int,float) and math.isfinite(n) and 0<=n<=64 for n in p)
    if area.get('kind')=='center-only':
        if not point(center) or area.get('composition_mode')!='overlay' or area.get('status') not in ('proposed','reviewed'):
            raise ValueError('Center-only needs a valid center, review status, and overlay mode.')
        if points:raise ValueError('Center-only cannot claim a safe polygon.')
        return area
    if not isinstance(points,list) or len(points)<3 or not all(point(p) for p in points):raise ValueError('Area polygon needs at least three finite points inside 0–64.')
    if not point(center):raise ValueError('Area center must be a finite point inside 0–64.')
    from shapely.geometry import Polygon,Point
    poly=Polygon(points)
    if not poly.is_valid or poly.area<=0 or not poly.covers(Point(center)):raise ValueError('Area must be a simple polygon containing its center.')
    if area.get('status') not in ('proposed','reviewed'):raise ValueError('Area status must be proposed or reviewed.')
    if area.get('composition_mode','contain') not in ('contain','overlay'):raise ValueError('Choose contain or overlay composition mode.')
    return area


def detect_area(host):
    root=root_svg();root.append(artwork_group(host,'host'));ink=raster(ET.tostring(root,encoding='unicode'))
    labels,count=ndimage.label(ndimage.binary_fill_holes(ink)&~ink)
    areas=np.bincount(labels.ravel());areas[0]=0
    enclosed=bool(count and areas.max()>16*100)
    if enclosed:region=labels==areas.argmax()
    else:
        x0,y0,x1,y1=host.bounds
        region=polygon_mask([[x0+4,y0+4],[x1-4,y0+4],[x1-4,y1-4],[x0+4,y1-4]])
    yy,xx=np.where(region)
    if not len(xx):raise ValueError('No usable content area; supply an area proposal.')
    return ink,region,[float(xx.mean()/4),float(yy.mean()/4)],enclosed


def paths_as_commands(art,prefix,transform):
    scale,dx,dy=transform
    def point(z):return (z.real*scale+dx,z.imag*scale+dy)
    result=[]
    for _,_,path in art.paths:
        for piece in path.continuous_subpaths():
            commands=[Command('M',[point(piece[0].start)])]
            for segment in piece:
                if isinstance(segment,Line):commands.append(Command('L',[point(segment.end)]))
                elif isinstance(segment,CubicBezier):commands.append(Command('C',[point(segment.control1),point(segment.control2),point(segment.end)]))
                elif isinstance(segment,QuadraticBezier):commands.append(Command('Q',[point(segment.control),point(segment.end)]))
                elif isinstance(segment,Arc):commands.append(Command('A',[point(segment.end)],(segment.radius.real*scale,segment.radius.imag*scale,float(segment.rotation),int(segment.large_arc),int(segment.sweep))))
                else:raise ValueError('Unsupported path segment.')
            result.append({'id':f'{prefix}-{len(result)}','commands':commands})
    return result


def validate_padding(host,sub,transform,padding):
    """Check every cross-component contour pair; contacts never waive padding."""
    host_paths=paths_as_commands(host,'host',(1,0,0));sub_paths=paths_as_commands(sub,'sub',transform)
    findings=[]
    for a in host_paths:
        for b in sub_paths:
            report=analyze_paths([a,b],minimum_distance=STROKE+padding,stroke_width=STROKE,tolerance=.001)
            if report['connectedPairs']:
                findings.append({'status':'fail','inkClearance':0,'inkClearanceLowerBound':0,'inkClearanceUpperBound':0,'reason':'Sub and container centerlines touch or cross.'})
            elif report['pairs']:findings.extend(report['pairs'])
            else:findings.append({'status':'review','reason':str(report.get('errors') or 'Could not certify distance.')})
    status='fail' if any(f['status']=='fail' for f in findings) else ('review' if any(f['status']!='pass' for f in findings) else 'pass')
    nearest=min((f for f in findings if 'inkClearance' in f),key=lambda f:f['inkClearance'],default={})
    return {'status':status,'required_ink_padding':padding,'required_centerline_distance':4+padding,
            'measured_ink_padding':nearest.get('inkClearance'),'lower_bound':min((f.get('inkClearanceLowerBound',0) for f in findings),default=0),
            'nearest':nearest,'issues':[f for f in findings if f['status']!='pass'],
            'method':'continuous vector distance with adaptive curve error bounds'}


def place(host,sub,*,padding=2,sizes=(32,28,24),area=None,max_shift=10):
    if not math.isfinite(padding) or padding<0 or padding>32:raise ValueError('Padding must be between 0 and 32 units.')
    if not sizes or any(not math.isfinite(s) or s<=4 or s>60 for s in sizes):raise ValueError('Content ink sizes must be greater than 4 and at most 60.')
    if not math.isfinite(max_shift) or max_shift<0 or max_shift>64:raise ValueError('Maximum shift must be between 0 and 64.')
    if area and area.get('kind')=='center-only':
        validate_area(area,host.sha256)
        extent=max(sub.bounds[2]-sub.bounds[0],sub.bounds[3]-sub.bounds[1])
        if extent<=0:raise ValueError('Cannot fit empty artwork.')
        size=sizes[min(1,len(sizes)-1)]
        transform=transform_for(sub,(size-4)/extent,area['center'])
        check=validate_padding(host,sub,transform,padding)
        return {'status':'review-overlay','placement':{'center':area['center'],'content_ink_size':size,'scale':transform[0],'stroke':4,'padding':padding},
                'validation':{**check,'inside_content_area_estimate':None,'safe_zone_claimed':False},'area':area,
                'svg':render(host,sub,transform),'debug_svg':render(host,sub,transform,padding=padding)}
    ink,region,center,enclosed=detect_area(host)
    if area:
        validate_area(area,host.sha256);region=polygon_mask(area['polygon']);center=area['center']
    distance=ndimage.distance_transform_edt(~ink)/4
    allowed=region&(distance>=padding+.25)
    extent=max(sub.bounds[2]-sub.bounds[0],sub.bounds[3]-sub.bounds[1])
    if extent<=0:raise ValueError('Cannot fit empty or point-only artwork.')
    candidates=[]
    for size in sizes:
        scale=(size-4)/extent
        mask=raster(render(None,sub,transform_for(sub,scale,(32,32))));ys,xs=np.where(mask)
        top,left=ys.min(),xs.min();bottom,right=ys.max()+1,xs.max()+1;crop=mask[top:bottom,left:right]
        bad=signal.fftconvolve((~allowed).astype(float),crop[::-1,::-1].astype(float),mode='valid')
        yy,xx=np.indices(bad.shape);cx=32+(xx-left)/4;cy=32+(yy-top)/4
        cost=(cx-center[0])**2+(cy-center[1])**2
        # Center grid belongs to the final placement, not the cropped bitmap.
        valid=(bad<.1)&(cost<=max_shift**2)&np.isclose(cx,np.round(cx))&np.isclose(cy,np.round(cy))
        score=np.where(valid,cost,np.inf)
        # Try near-center alternatives if raster approximation misses a tight curve.
        for _ in range(4):
            y,x=np.unravel_index(score.argmin(),score.shape)
            if not np.isfinite(score[y,x]):break
            transform=transform_for(sub,scale,(float(cx[y,x]),float(cy[y,x])))
            check=validate_padding(host,sub,transform,padding)
            candidates.append((size,[float(cx[y,x]),float(cy[y,x])],transform,check))
            score[y,x]=np.inf
            if check['status']=='pass':break
        if candidates and candidates[-1][3]['status']=='pass':break
    if candidates:chosen=next((c for c in candidates if c[3]['status']=='pass'),candidates[-1])
    else:
        size=sizes[min(1,len(sizes)-1)];transform=transform_for(sub,(size-4)/extent,center)
        chosen=(size,center,transform,validate_padding(host,sub,transform,padding))
    size,center,transform,check=chosen
    mask=raster(render(None,sub,transform));inside=not bool((mask&~region).any())
    x0,y0,x1,y1=sub.bounds;s,dx,dy=transform
    canvas_fit=min(x0*s+dx-2,y0*s+dy-2)>=0 and max(x1*s+dx+2,y1*s+dy+2)<=64
    area_review=bool(area and area['status']=='reviewed' and area.get('composition_mode','contain')=='contain')
    status='clearance-pass' if check['status']=='pass' and inside and canvas_fit else 'review-fit'
    if status=='clearance-pass' and not area_review:status='review-area'
    if area and area.get('composition_mode')=='overlay':status='review-overlay'
    return {'status':status,'placement':{'center':center,'content_ink_size':size,'scale':s,'stroke':4,'padding':padding},
            'validation':{**check,'inside_content_area_estimate':inside,'inside_canvas':canvas_fit},
            'area':area or {'method':'largest enclosed region' if enclosed else 'inset bounds fallback','status':'proposed','center':center},
            'svg':render(host,sub,transform),'debug_svg':render(host,sub,transform,padding=padding,area=area.get('polygon') if area else None)}

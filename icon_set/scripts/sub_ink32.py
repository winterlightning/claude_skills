"""Derived combination exports: integer-grid icons and height-locked text."""
from __future__ import annotations
import io
import xml.etree.ElementTree as ET
import numpy as np
from svgpathtools import Document, Path, Line, CubicBezier, QuadraticBezier, Arc


def _bounds(paths):
    boxes=[p.bbox() for p in paths]
    return min(b[0] for b in boxes),min(b[2] for b in boxes),max(b[1] for b in boxes),max(b[3] for b in boxes)


def _snap(paths, preserve_arcs=True, width=32, stroke=4):
    # Split at curve extrema so boundary points become explicit grid anchors.
    # Keep the control polygon inside the ink-safe centerline box.
    def point(z):
        return complex(max(stroke/2,min(width-stroke/2,round(z.real))),max(stroke/2,min(32-stroke/2,round(z.imag))))
    result=[]
    for path in paths:
        segments=[]
        for original in path:
            if preserve_arcs and isinstance(original,Arc):
                start,end=point(original.start),point(original.end)
                if start==end:
                    segments.append(Line(start,end));continue
                radius=complex(max(1,round(original.radius.real)),max(1,round(original.radius.imag)))
                snapped=Arc(start,radius,original.rotation,original.large_arc,original.sweep,end)
                box=snapped.bbox()
                if box[0]>=stroke/2-1e-7 and box[1]<=width-stroke/2+1e-7 and box[2]>=stroke/2-1e-7 and box[3]<=32-stroke/2+1e-7:
                    segments.append(snapped);continue
            curves=list(original.as_cubic_curves(2)) if isinstance(original,Arc) else [original]
            for segment in curves:
                cuts=[0.,1.]
                if isinstance(segment,(CubicBezier,QuadraticBezier)):
                    derivative=segment.poly().deriv()
                    for coeff in (np.real(derivative.coeffs),np.imag(derivative.coeffs)):
                        for root in np.roots(np.trim_zeros(coeff,'f')):
                            if abs(root.imag)<1e-9 and 1e-8<root.real<1-1e-8:cuts.append(float(root.real))
                cuts=sorted(set(cuts))
                for lo,hi in zip(cuts,cuts[1:]):
                    part=segment.cropped(lo,hi) if lo or hi!=1 else segment
                    if isinstance(part,Line):out=Line(point(part.start),point(part.end))
                    elif isinstance(part,CubicBezier):out=CubicBezier(*(point(z) for z in (part.start,part.control1,part.control2,part.end)))
                    else:out=QuadraticBezier(*(point(z) for z in (part.start,part.control,part.end)))
                    segments.append(out)
        result.append(Path(*segments))
    return result


def normalize_ink32(document: str, *, text: bool=False) -> tuple[str, dict]:
    paths=[p for p in Document(io.StringIO(document)).paths() if len(p)]
    if not paths:raise ValueError('No supported paths in artwork')
    left,top,right,bottom=_bounds(paths)
    extent=bottom-top if text else max(right-left,bottom-top)
    stroke=4
    if extent<=1e-12:
        if not text:raise ValueError('Artwork has no finite fitting extent')
        # A dots-only label has no centerline height: fit its actual round ink.
        stroke=32
        scale=8
    else:scale=28/extent
    width=(right-left)*scale+stroke if text else 32
    dx,dy=width/2-(left+right)*scale/2,16-(top+bottom)*scale/2
    fitted=[p.scaled(scale).translated(complex(dx,dy)) for p in paths]
    width=round(width) if text else width
    unsnapped=fitted
    fitted=_snap(fitted,width=width,stroke=stroke)
    l,t,r,b=_bounds(fitted)
    extent=b-t if text else max(r-l,b-t)
    if abs(extent+stroke-32)>1e-6:
        fitted=_snap(unsnapped,preserve_arcs=False,width=width,stroke=stroke)
    l,t,r,b=_bounds(fitted);ink=[l-stroke/2,t-stroke/2,r+stroke/2,b+stroke/2]
    if text:
        assert abs(b-t+stroke-32)<1e-6
        assert ink[0]>=-1e-7 and ink[2]<=width+1e-7
    if not text:
        assert min(ink)>=-1e-7 and max(ink)<=32+1e-7
        assert abs(max(r-l,b-t)+4-32)<1e-6
    root=ET.Element('svg',xmlns='http://www.w3.org/2000/svg',width=str(width),height='32',viewBox=f'0 0 {width} 32',fill='none',stroke='currentColor',**{'stroke-width':str(stroke),'stroke-linecap':'round','stroke-linejoin':'round'})
    for i,p in enumerate(fitted):ET.SubElement(root,'path',id=f'part-{i+1}',d=p.d())
    return ET.tostring(root,encoding='unicode'),dict(ink_bounds=ink,ink_width=r-l+stroke,ink_height=b-t+stroke,geometry_scale=scale,stroke=stroke,canvas=32,canvas_width=width,bounds=[l,t,r,b],grid=1)

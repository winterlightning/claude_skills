"""Diagnostic centerlines from saved review SVGs; never changes icon artwork."""
from pathlib import Path
from copy import deepcopy
import json, math
import xml.etree.ElementTree as ET
import cairosvg
from svgpathtools import parse_path

NS='http://www.w3.org/2000/svg'
ET.register_namespace('',NS)
def node(tag,attrs=None):return ET.Element('{'+NS+'}'+tag,attrs or {})
def diagnostic(document,canvas):
    source=ET.fromstring(document)
    root=node('svg',{'viewBox':f'-4 -4 {canvas+8} {canvas+8}','width':'672','height':'672'})
    root.append(node('rect',{'x':'-4','y':'-4','width':str(canvas+8),'height':str(canvas+8),'fill':'white'}))
    for v in range(canvas+1):
        style={'stroke':'#d9e1ea' if v%4==0 else '#edf1f5','stroke-width':'.09' if v%4==0 else '.05'}
        root.append(node('line',dict(style,x1=str(v),y1='0',x2=str(v),y2=str(canvas))))
        root.append(node('line',dict(style,x1='0',y1=str(v),x2=str(canvas),y2=str(v))))
        if v%8==0:
            for x,y in [(v,-1.3),(-2,v+.5)]:
                label=node('text',{'x':str(x),'y':str(y),'font-size':'1.2','font-family':'sans-serif','fill':'#64748b','text-anchor':'middle'});label.text=str(v);root.append(label)
    # Saved selected paths are reused exactly, with rendering styles only changed.
    for color,width,opacity in [('#cbd5e1','4','.65'),('#1764c0','.24','1')]:
        layer=node('g',{'fill':'none','stroke':color,'stroke-width':width,'stroke-linecap':'round','stroke-linejoin':'round','opacity':opacity})
        for child in source:
            if child.tag.rsplit('}',1)[-1] in ('title','desc'):continue
            c=deepcopy(child)
            for part in c.iter():
                for a in ['stroke','stroke-width','fill','color','style']:part.attrib.pop(a,None)
            layer.append(c)
        root.append(layer)
    points=set()
    for part in source.iter():
        if part.tag.rsplit('}',1)[-1]=='path':
            for segment in parse_path(part.get('d','')):
                for z in [segment.start,segment.end]:points.add((round(z.real,6),round(z.imag,6)))
    for x,y in sorted(points):root.append(node('circle',{'cx':str(x),'cy':str(y),'r':'.31','fill':'#bc2564','stroke':'white','stroke-width':'.09'}))
    return ET.tostring(root,encoding='unicode')

def generate(folder):
    folder=Path(folder);data=json.loads((folder/'review.json').read_text())
    for r in data['icons']:
        target=folder/r['icon_id'];document=(target/'selected.svg').read_text()
        svg=diagnostic(document,r['native_size'])
        (target/'centerline.svg').write_text(svg)
        cairosvg.svg2png(bytestring=svg.encode(),write_to=str(target/'centerline.png'))
    # The commandline frame has explicit, measurable non-tangent corner joins.
    r=next((r for r in data['icons'] if r['icon_id']=='commandline'),None)
    if r is None:
        print(f"Rendered {len(data['icons'])} centerline diagrams from the exact selected artwork.")
        return
    target=folder/'commandline'
    doc=ET.parse(target/'selected.svg');path=parse_path(next(p.get('d') for p in doc.getroot() if p.get('id')=='c2'))
    measurements=[]
    for i in range(len(path)):
        prev=path[i-1];current=path[i]
        if abs(prev.end-current.start)>1e-7:continue
        p=current.start
        if (round(p.real),round(p.imag)) not in [(4,11),(6,8),(4,38),(6,40)]:continue
        a=prev.unit_tangent(1);b=current.unit_tangent(0)
        angle=math.degrees(math.acos(max(-1,min(1,(a.conjugate()*b).real))))
        measurements.append({'position':[p.real,p.imag],'path':'c2','tangent_change_degrees':round(angle,2),'interpretation':'Optional polish; not a symmetry requirement or a native-size rejection.'})
    (target/'centerline-measurements.json').write_text(json.dumps({'source_svg_sha256':r['svg_sha256'],'method':'Angle between outgoing and incoming unit tangent vectors at consecutive c2 segments. Zero means tangent-continuous. Purposeful corners are not defects.','junctions':measurements},indent=2))
    print('Rendered 50 centerline diagrams from the exact selected artwork.')
    print(json.dumps(measurements))
if __name__=='__main__':
    import sys
    generate(sys.argv[1])

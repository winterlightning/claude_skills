"""Reconstruct existing cohort models, preserving original source IDs and paths."""
import json,re,textwrap
from pathlib import Path
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/intersection-review-977/cohort.json'
AUTHOR='gpt-6'
HERE=Path(__file__).parent
rows=json.loads(Path(SOURCE_PATH).read_text());byid={r['icon_id']:r for r in rows}
changes=[]
def patch(id,body,plan,reference,keyshape=None):
 p=Path(byid[id]['python_source']['path']);s=(HERE/'before'/p.name).read_text();s=s[:s.index('    def build(')]
 s=re.sub(r'REVIEW_ACTION = .*',"REVIEW_ACTION = 'geometry-reconstructed'",s)
 s=re.sub(r'AUTHOR = [^\n]+',"AUTHOR = 'gpt-6'",s,count=1)
 if keyshape:s=re.sub(r'keyshape = Keyshape.\w+','keyshape = Keyshape.'+keyshape,s)
 s='"""'+id+': geometric reconstruction on SOLO48."""\n'+s[s.index('from ...'):]
 s+='    def build(self):\n'+textwrap.indent('# Plan: '+plan+'\n# Reference: '+reference+'\n'+textwrap.dedent(body).strip()+'\n','        ')
 p.write_text(s);changes.append(dict(id=id,source=str(p),plan=plan,reference=reference))

def main():
 patch('panoramic','''
# A shared parabola owns both bowed rails and the panel attachments.
axis = 24
panel_x = (14, 34)
knots = (4, *panel_x, 44)
for name, reflection in [('top', False), ('bottom', True)]:
    def point(x, y): return (x, 48-y if reflection else y)
    for i, (a, b) in enumerate(zip(knots, knots[1:])):
        ya = 12-(a-axis)**2/100
        yb = 12-(b-axis)**2/100
        step = (b-a)/3
        self.add_bezier(f'{name}-{i}', point(a,round(ya)),
            (point(a+step,ya-step*(a-axis)/50),
             point(b-step,yb+step*(b-axis)/50),point(b,round(yb))))
self.add_line('left',(4,8),(4,40))
self.add_line('right',(44,8),(44,40))
# Reverse lower rail and left wall for one coherent perimeter.
from dataclasses import replace
from ...primitives import Bezier
for i,p in enumerate(self.primitives):
    if p.element_id.startswith('bottom'):
        c1,c2,end=p.segments[0]
        self.primitives[i]=Bezier(p.element_id,p.end,p.start,((c2,c1,p.start.as_tuple()),))
    elif p.element_id=='left':self.primitives[i]=replace(p,start=p.end,end=p.start)
self.add_contour('outline','top-0','top-1','top-2','right','bottom-2','bottom-1','bottom-0','left',closed=True)
for i,x in enumerate(panel_x):
    self.add_line(f'panel-{i}',(x,11),(x,37))
    self.relate('connect',f'panel-{i}','outline')
''','HRECT_L (4,8)-(44,40); exact horizontal and vertical symmetry, identical parabolic rails, shared panel nodes.','No close panorama match; shared-axis geometric construction.')
 patch('pen-4d7410cc','''
# The cap and the barrel mirror across the diagonal x+y=48.
self.add_line('upper-barrel',(12,28),(30,10))
self.add_bezier('cap-upper',(30,10),((32,8),(33,6),(36,6)))
self.add_arc('cap-round',(36,6),(42,12),radius_x=6)
self.add_bezier('cap-lower',(42,12),((42,15),(40,16),(38,18)))
self.add_line('lower-barrel',(38,18),(20,36))
self.add_line('tip-lower',(20,36),(6,42))
self.add_line('tip-upper',(6,42),(12,28))
self.add_contour('outline','upper-barrel','cap-upper','cap-round','cap-lower','lower-barrel','tip-lower','tip-upper',closed=True)
self.add_line('cap-seam',(26,14),(34,22))
self.relate('connect','cap-seam','outline')
''','SQUARE (6,6)-(42,42); tangent rounded cap, parallel diagonal barrel and seam ending exactly on its sides.','Lucide pencil: coherent rounded cap and one shared seam.')
 patch('amazon-elastic-kubernetes-service','''
axis = 24
left, right = axis-16, axis+16
self.add_polyline('hexagon',(axis,4),(right,14),(right,34),(axis,44),(left,34),(left,14),closed=True)
self.add_polyline('stem',(20,16),(20,24),(20,32))
self.add_polyline('arms',(29,16),(20,24),(29,32))
self.relate('connect','stem','arms')
''','VRECT_L (8,4)-(40,44); six clean sides mirrored around both axes; K arms share one stem node.','Lucide hexagon: common vertices and equal opposite sides.')
 patch('amazon-web-service-game-tech','''
axis = 24
# Mirrored shoulders and grips are generated from the same left-side definition.
for side,mirror in [('left',False),('right',True)]:
    def p(x,y):return (2*axis-x,y) if mirror else (x,y)
    self.add_arc(side+'-shoulder',p(4,18),p(12,8),radius_x=8,radius_y=10,sweep=not mirror)
    self.add_bezier(side+'-top',p(12,8),(p(16,8),p(16,12),p(20,12)))
    self.add_line(side+'-wall',p(4,34),p(4,18))
    self.add_arc(side+'-heel',p(10,40),p(4,34),radius_x=6,sweep=not mirror)
    self.add_bezier(side+'-grip',p(18,30),(p(14,30),p(14,40),p(10,40)))
# Orient right side in the reverse direction to close the contour.
from dataclasses import replace
from ...primitives import Arc,Bezier
for i,q in enumerate(self.primitives):
    if q.element_id.startswith('right'):
        if isinstance(q,Bezier):
            c1,c2,end=q.segments[0]
            self.primitives[i]=Bezier(q.element_id,q.end,q.start,((c2,c1,q.start.as_tuple()),))
        elif isinstance(q,Arc):self.primitives[i]=replace(q,start=q.end,end=q.start,sweep=not q.sweep)
        else:self.primitives[i]=replace(q,start=q.end,end=q.start)
self.add_line('top',(20,12),(28,12))
self.add_line('underside',(30,30),(18,30))
self.add_contour('outline','left-shoulder','left-top','top','right-top','right-shoulder','right-wall','right-heel','right-grip','underside','left-grip','left-heel','left-wall',closed=True)
''','HRECT_L (4,8)-(44,40); mirrored shoulders and grips; smooth tangent joins throughout.','Lucide gamepad-2: flowing controller silhouette and paired grips.')
 (HERE/'changes.json').write_text(json.dumps(changes,indent=2))
if __name__=='__main__':main()

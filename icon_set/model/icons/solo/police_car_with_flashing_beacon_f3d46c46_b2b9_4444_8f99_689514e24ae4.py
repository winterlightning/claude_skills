"""police car. Revision: Round the car body and roof, use two complete wheels and a rounded beacon with two flashes. Omit center window divider.
Construction: Lucide car: coherent roof and body with full circular wheels. Preserve source-facing direction and arrangement.
Keyshape SQUARE; exact contract extremes, stroke four. No validation exceptions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f3d46c46-b2b9-4444-8f99-689514e24ae4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/police car_f3d46c46-b2b9-4444-8f99-689514e24ae4.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='police-car-with-flashing-beacon'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('police', 'car')

    def build(self):
        # Each contour owns its shape. Repeated parts share dimensions and axes.
        def path(n,start,steps,closed=False):
            p=start; members=[]
            for j,s in enumerate(steps):
                k=f'{n}-{j}';kind,q,*v=s
                if kind=='L': self.add_line(k,p,q)
                elif kind=='A': self.add_arc(k,p,q,radius_x=v[0],radius_y=v[1],sweep=v[2])
                elif kind=='C': self.add_bezier(k,p,(v[0],v[1],q))
                members.append(k);p=q
            self.add_contour(n,*members,closed=closed)
        def line(n,a,b):self.add_line(n,a,b)
        def poly(n,*p):self.add_polyline(n,*p)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def join(a,b):self.relate('connect',a,b)

        circle('left-wheel',12,36,6);circle('right-wheel',36,36,6)
        path('body',(6,36),[('L',(6,29)),('A',(10,25),4,4,True),('L',(12,25)),('L',(18,17)),('L',(20,17)),('L',(28,17)),('L',(30,17)),('L',(36,25)),('L',(38,25)),('A',(42,29),4,4,True),('L',(42,36))])
        line('sill',(18,36),(30,36))
        path('beacon',(20,17),[('L',(20,10)),('A',(24,6),4,4,True),('A',(28,10),4,4,True),('L',(28,17))])
        line('flash-left',(6,6),(9,9));line('flash-right',(39,9),(42,6))

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)

"""dragster. Revision: Connect pointed racing body to two equal wheels and restore a rectangular raised rear wing. Omit tiny suspension detail.
Construction: Lucide car: round wheels and a coherent body with shared chassis junctions. Preserve source-facing direction and arrangement.
Keyshape HRECT_L; exact contract extremes, stroke four. No validation exceptions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9f803b66-a6f0-4bdf-b4c8-49f7ac21db0e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/dragster_9f803b66-a6f0-4bdf-b4c8-49f7ac21db0e.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='low-racing-car-with-raised-rear-wing'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('dragster',)

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

        circle('front-wheel',12,34,6);circle('rear-wheel',36,34,6)
        path('shell',(6,34),[('L',(4,30)),('L',(6,28)),('L',(20,24)),('L',(24,17)),('L',(28,17)),('L',(36,24)),('L',(44,29)),('L',(42,34))])
        line('sill',(18,34),(30,34))
        poly('wing',(36,24),(36,8),(44,8),(44,16),(36,16))
        join('wing','shell')

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)

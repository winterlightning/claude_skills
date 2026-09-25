"""car side. Revision: Smooth hood and roof transitions and enlarge two equal wheels; preserve blank side body. No extra window added.
Construction: Lucide car: complete wheels and flowing body contour. Preserve source-facing direction and arrangement.
Keyshape HRECT_M; exact contract extremes, stroke four. No validation exceptions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '66a7bddb-97e8-4a0e-854b-1b3a855bbd18'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/car side_66a7bddb-97e8-4a0e-854b-1b3a855bbd18.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='plain-compact-hatchback'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('car', 'side')

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

        circle('rear-wheel',12,32,6);circle('front-wheel',36,32,6)
        path('body',(6,32),[('L',(4,29)),('L',(4,24)),('C',(13,20),(4,21),(9,21)),('L',(20,12)),('A',(24,10),5,5,True),('L',(29,10)),('C',(44,24),(35,10),(44,18)),('L',(44,29)),('L',(42,32))])
        line('sill',(18,32),(30,32))

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)

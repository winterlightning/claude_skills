"""car truck. Revision: Restore full circular wheels and rounded bed corners; retain open pickup bed and raised sloped cab. Omit no defining part.
Construction: Lucide truck: round wheels, shared chassis contacts, rounded corners. Preserve source-facing direction and arrangement.
Keyshape HRECT_L; exact contract extremes, stroke four. No validation exceptions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1dcbab5c-09f3-41b2-be1b-b176d7fcb178'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/car truck_1dcbab5c-09f3-41b2-be1b-b176d7fcb178.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='plain-pickup-truck-profile'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('car', 'truck')

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

        circle('rear-wheel',12,34,6);circle('front-wheel',36,34,6)
        path('body',(6,34),[('L',(4,34)),('L',(4,24)),('A',(8,20),4,4,True),('L',(24,20)),('L',(40,20)),('A',(44,24),4,4,True),('L',(44,34)),('L',(42,34))])
        path('cab',(24,20),[('L',(24,12)),('A',(28,8),4,4,True),('L',(31,8)),('C',(35,10),(33,8),(34,8)),('L',(40,20))]);join('cab','body')
        line('chassis',(18,34),(30,34))

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)

"""camper. Revision: Smooth overcab roof and front cab, enlarge round wheels and use a single window mark. Omit tight door and second window.
Construction: Lucide truck: body arcs, shared chassis and circular wheels. Preserve source-facing direction and arrangement.
Keyshape HRECT_L; exact contract extremes, stroke four. No validation exceptions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd86d46d5-367a-4ef9-b622-6b5791529dc1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/camper_d86d46d5-367a-4ef9-b622-6b5791529dc1.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='motorhome-with-overcab-roof-d86d46d5'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/reference'
    aliases=()
    keywords=('camper',)

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

        circle('rear-wheel',11,34,6);circle('front-wheel',37,34,6)
        path('body',(5,34),[('L',(4,14)),('A',(10,8),6,6,True),('L',(34,8)),('A',(40,16),6,8,True),('L',(32,16)),('L',(44,26)),('L',(44,32)),('L',(43,34))])
        line('sill',(17,34),(31,34))
        line('window',(13,18),(22,18))

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)

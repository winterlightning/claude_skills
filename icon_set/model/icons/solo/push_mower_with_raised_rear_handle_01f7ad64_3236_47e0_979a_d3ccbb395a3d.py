"""mower. Revision: Restore full wheels beneath low deck, rounded motor housing and long rear handle. Omit wheel hubs.
Construction: Lucide car: complete circular wheels and shared chassis attachments. Preserve source-facing direction and arrangement.
Keyshape HRECT_L; exact contract extremes, stroke four. No validation exceptions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '01f7ad64-3236-47e0-979a-d3ccbb395a3d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/mower_01f7ad64-3236-47e0-979a-d3ccbb395a3d.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='push-mower-with-raised-rear-handle'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('mower',)

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

        circle('front-wheel',10,34,6);circle('rear-wheel',34,33,7)
        path('deck',(4,34),[('L',(4,28)),('A',(10,22),6,6,True),('L',(13,22)),('L',(25,22)),('L',(32,22)),('A',(41,31),9,9,True),('L',(41,33))])
        line('chassis',(16,34),(27,33))
        path('motor',(13,22),[('L',(14,16)),('A',(18,13),4,4,True),('L',(25,13)),('L',(25,22))])
        poly('handle',(32,22),(40,8),(44,8))

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)

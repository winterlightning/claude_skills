"""alligator. Revision: Low curved snout and curled tail, restrained back ridges, two bent legs. Omit eye dot and mouth line to keep the snout open.
Construction: No useful direct Lucide match; supplied source silhouette. Preserve source-facing direction and arrangement.
Keyshape HRECT_M; exact contract extremes, stroke four. No validation exceptions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '033c9d4f-a0ab-42dc-80b5-4f148935d09a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/alligator_033c9d4f-a0ab-42dc-80b5-4f148935d09a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='low-alligator-in-profile'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('alligator',)

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

        path('animal',(14,38),[('C',(4,26),(7,38),(4,33)),('C',(12,16),(4,20),(7,16)),('L',(16,14)),('L',(20,16)),('L',(24,14)),('L',(28,16)),('A',(36,16),4,6,True),('L',(40,16)),('A',(44,20),4,4,True),('A',(40,26),4,6,True),('L',(32,26)),('L',(34,34)),('L',(26,34)),('L',(22,26))])

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)

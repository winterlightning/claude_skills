"""maintenance tool. Revision: Restore upright diagonal wrench with parallel handle sides and a rounded heel; round the internal jaw. Omit no defining feature.
Construction: Lucide wrench: round jaw, parallel shaft and semicircular heel. Preserve source-facing direction and arrangement.
Keyshape VRECT_L; exact contract extremes, stroke four. No validation exceptions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ee54ecd1-dacb-44d6-bb14-618638eed18c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/maintenance tool_ee54ecd1-dacb-44d6-bb14-618638eed18c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='open-end-wrench-with-rounded-handle'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/reference'
    aliases=()
    keywords=('maintenance', 'tool')

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

        path('wrench',(10,34),[('L',(20,21)),('C',(16,14),(17,19),(16,17)),('C',(29,4),(16,7),(22,4)),('L',(24,12)),('A',(25,16),3,3,False),('L',(29,19)),('A',(33,18),3,3,False),('L',(39,9)),('C',(40,17),(40,11),(40,14)),('C',(35,27),(40,21),(39,24)),('C',(29,29),(33,29),(31,29)),('L',(20,42)),('C',(14,44),(18,44),(16,44)),('A',(8,38),6,6,True),('C',(10,34),(8,36),(9,35))],True)

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)

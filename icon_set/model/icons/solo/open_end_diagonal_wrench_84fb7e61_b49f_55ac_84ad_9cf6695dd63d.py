"""tools wrench. Revision: Rebuild straight parallel handle sides with a semicircular heel and smooth jaw; preserve open diagonal mouth. Omit no defining feature.
Construction: Lucide wrench: parallel shaft, round heel, and rounded inner jaw. Preserve source-facing direction and arrangement.
Keyshape SQUARE; exact contract extremes, stroke four. No validation exceptions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '84fb7e61-b49f-55ac-84ad-9cf6695dd63d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/tools/tools wrench_84fb7e61-b49f-55ac-84ad-9cf6695dd63d.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='open-end-diagonal-wrench'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'tools'
    aliases=()
    keywords=('tools', 'wrench')

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

        path('wrench',(8,30),[('L',(17,20)),('C',(16,14),(16,18),(16,16)),('C',(30,6),(16,8),(23,6)),('L',(23,13)),('A',(23,17),3,3,False),('L',(27,21)),('A',(31,21),3,3,False),('L',(42,10)),('C',(39,27),(42,18),(42,23)),('C',(29,29),(36,30),(32,30)),('L',(18,40)),('C',(12,42),(16,42),(14,42)),('A',(6,36),6,6,True),('C',(8,30),(6,34),(6,32))],True)

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)

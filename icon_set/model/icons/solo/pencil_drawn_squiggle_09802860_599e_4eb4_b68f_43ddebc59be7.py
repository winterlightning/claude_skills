"""pen draw 2. Revision: Straighten parallel pencil edges, use a true rounded end, and make the loose drawn line flow smoothly. Omit cap seam.
Construction: Lucide pencil: parallel barrel, rounded cap and open triangular tip. Preserve source-facing direction and arrangement.
Keyshape SQUARE; exact contract extremes, stroke four. No validation exceptions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '09802860-599e-4eb4-b68f-43ddebc59be7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pen draw 2_09802860-599e-4eb4-b68f-43ddebc59be7.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='pencil-drawn-squiggle'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/reference'
    aliases=()
    keywords=('pen', 'draw', '2')

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

        path('pencil',(21,34),[('L',(24,23)),('L',(35,12)),('C',(42,18),(39,10),(42,14)),('L',(29,30)),('L',(21,34))],True)
        path('squiggle',(14,6),[('C',(6,19),(10,10),(6,14)),('C',(12,23),(6,23),(10,21)),('C',(6,36),(16,27),(6,32)),('C',(12,42),(6,40),(8,42))])

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)

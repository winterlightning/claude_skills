"""message bottle. Revision: Round bottle shoulders and draw paper as a distinct diagonal stroke; replace jagged wave with smooth wave crests. Omit cork seam and scroll curl.
Construction: Lucide milk: a continuous bottle silhouette with distinct shoulders. Preserve source-facing direction and arrangement.
Keyshape SQUARE; exact contract extremes, stroke four. No validation exceptions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8c6e78dd-8392-422f-8f4b-d2a4ec2762f7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/message bottle_8c6e78dd-8392-422f-8f4b-d2a4ec2762f7.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='message-in-a-bottle-batch-025-01'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases=()
    keywords=('message', 'bottle')

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

        path('bottle',(9,30),[('L',(14,20)),('C',(23,15),(16,17),(21,18)),('L',(29,6)),('L',(39,12)),('L',(34,21)),('C',(34,30),(32,24),(34,27))])
        line('message',(21,31),(23,27))
        path('wave',(6,42),[('C',(16,38),(10,42),(12,42)),('C',(26,38),(20,42),(22,42)),('C',(36,38),(30,42),(32,42)),('C',(42,42),(38,42),(40,42))])

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)

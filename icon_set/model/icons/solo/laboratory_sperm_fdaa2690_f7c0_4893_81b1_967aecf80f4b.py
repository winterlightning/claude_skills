"""laboratory sperm: fresh spacing repair.
Plan: Two offset repeated sperm cells inside the circular field. Heads expose actual lower tail attachment; organic diagonal arrangement preserved. No useful Lucide match.
Keyshape CIRCLE: extrema derived from the profile's standard envelope.
Omissions: Detached third cell omitted; sperm heads simplified to small circular outlines.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='fdaa2690-f7c0-4893-81b1-967aecf80f4b'
SOURCE_PATH='pictographic-primitives/health/laboratory sperm_fdaa2690-f7c0-4893-81b1-967aecf80f4b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='laboratory-sperm'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'health'
    aliases=()
    keywords=('laboratory', 'sperm')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def path(self,n,start,segments,closed=False):
        at=start; members=[]
        for i,s in enumerate(segments):
            eid=f'{n}-{i}'; kind,end,*args=s
            if end==at: continue
            if kind=='L': self.add_line(eid,at,end)
            else: self.add_arc(eid,at,end,radius_x=args[0],sweep=args[1] if len(args)>1 else True)
            at=end; members.append(eid)
        self.add_contour(n,*members,closed=closed)
    def cross(self,n,x,y,r):
        for i,(dx,dy) in enumerate([(-r,0),(r,0),(0,-r),(0,r)]):
            self.add_line(f'{n}-{i}',(x,y),(x+dx,y+dy))
        for i in range(4):
            for j in range(i): self.relate('connect',f'{n}-{i}',f'{n}-{j}')

    def build(self):
        self.circle('field',24,24,20)
        for n,x,y in [('left',18,18),('right',30,22)]:
            self.path(n+'-head',(x,y-2),[('A',(x+2,y),2),('A',(x,y+2),2),('A',(x-2,y),2),('A',(x,y-2),2)],True)
            self.add_bezier(n+'-tail',(x,y+2),((x-3,y+5),(x,y+7),(x-3,y+9)))
            self.relate('connect',n+'-head',n+'-tail')

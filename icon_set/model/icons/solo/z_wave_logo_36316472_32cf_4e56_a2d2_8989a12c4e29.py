"""z wave logo: fresh spacing repair.
Plan: Circular Z badge lower right and detached quarter-circle broadcast arc upper left; intentional diagonal asymmetry. No useful Lucide logo match.
Keyshape SQUARE: extrema derived from the profile's standard envelope.
Omissions: Three broadcast arcs reduced to one to preserve legible enclosed Z.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='36316472-32cf-4e56-a2d2-8989a12c4e29'
SOURCE_PATH='pictographic-primitives/_uncategorized_40/z wave logo_36316472-32cf-4e56-a2d2-8989a12c4e29.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='z-wave-logo'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('z', 'wave', 'logo')

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
        self.add_arc('wave',(6,18),(18,6),radius_x=12)
        self.circle('badge',28,28,14)
        self.add_polyline('z',(25,24),(31,24),(25,32),(31,32))

"""kanda matsuri: fresh spacing repair.
Plan: Circular festival crest with one coherent three-lobed heart knot. Shared center owns all lobes, mirrored lower pair. No useful Lucide match.
Keyshape CIRCLE: extrema derived from the profile's standard envelope.
Omissions: Three inward heart tips merged into one continuous central knot; outside tassels and radial stems omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='89d827d8-1f4b-40fc-aad1-858c1f8fb087'
SOURCE_PATH='pictographic-primitives/holidays/kanda matsuri_89d827d8-1f4b-40fc-aad1-858c1f8fb087.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='kanda-matsuri'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'holidays'
    aliases=()
    keywords=('kanda', 'matsuri')

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
        self.circle('medallion',24,24,20)
        # One continuous three-lobed knot, with a shared central junction.
        self.add_bezier('crest',(24,24),((32,20),(32,10),(24,16)),((16,10),(16,20),(24,24)),((18,18),(10,22),(18,28)),((14,36),(24,34),(24,24)),((24,34),(34,36),(30,28)),((38,22),(30,18),(24,24)))

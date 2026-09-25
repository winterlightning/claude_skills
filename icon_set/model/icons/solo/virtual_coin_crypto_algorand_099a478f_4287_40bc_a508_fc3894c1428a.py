"""virtual coin crypto algorand: fresh spacing repair.
Plan: Circular coin with angular Algorand apex and parallel inner diagonal; true shared node at (30,25). No useful Lucide logo match.
Keyshape CIRCLE: extrema derived from the profile's standard envelope.
Omissions: Inner diagonal extended to a true junction on the right leg.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='099a478f-4287-40bc-a508-fc3894c1428a'
SOURCE_PATH='pictographic-primitives/finance/virtual coin crypto algorand_099a478f-4287-40bc-a508-fc3894c1428a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='virtual-coin-crypto-algorand'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'finance'
    aliases=()
    keywords=('virtual', 'coin', 'crypto', 'algorand')

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
        self.circle('coin',24,24,20)
        self.add_polyline('logo',(15,31),(24,13),(30,25),(33,31))
        self.add_line('inner-stroke',(26,33),(30,25))
        self.relate('connect','logo','inner-stroke')

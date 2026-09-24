"""circle bluetooth: fresh spacing repair.
Plan: Circle encloses the Lucide-style continuous angular Bluetooth rune. Opposing diagonals and upright stem retain logo identity.
Keyshape CIRCLE: extrema derived from the profile's standard envelope.
Omissions: None; reconstructed directly on SOLO48.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='809bf53d-f979-4aa8-bf75-748eb9b9dacd'
SOURCE_PATH='pictographic-primitives/other/circle bluetooth_809bf53d-f979-4aa8-bf75-748eb9b9dacd.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='bluetooth-wireless-connectivity-symbol-solo'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('circle', 'bluetooth')

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
        self.circle('frame',24,24,20)
        self.add_polyline('bluetooth',(14,18),(32,30),(23,35),(23,13),(32,18),(14,30))

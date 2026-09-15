"""Broadcast Antenna with Signal Waves — authored for the current SOLO48 contract."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '77eb85cc-0e8c-543c-b156-fbfb85464273'
SOURCE_PATH = 'pictographic-primitives/tv/wifi signal_77eb85cc-0e8c-543c-b156-fbfb85464273.svg'
AUTHOR = 'gpt-6'

class BroadcastAntennaSignal(Solo48):
    icon_id = 'broadcast-antenna-signal'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('antenna', 'signal', 'broadcast', 'wireless', 'radio', 'transmitter', 'wifi', 'hotspot')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-a', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-b', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)

    def box(self, name, x, y, right, bottom, r=3, attachments=()):
        points=[(x+r,y),(right-r,y),(right,y+r),(right,bottom-r),(right-r,bottom),(x+r,bottom),(x,bottom-r),(x,y+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; k=f'{name}-{i}'; members.append(k)
            if i%2: self.add_arc(k,a,b,radius_x=r)
            else:
                nodes=[p for p in attachments if (a[0]==b[0]==p[0] and min(a[1],b[1])<p[1]<max(a[1],b[1])) or (a[1]==b[1]==p[1] and min(a[0],b[0])<p[0]<max(a[0],b[0]))]
                if nodes:
                    members.pop()
                    nodes.sort(key=lambda p:(p[0]-a[0])**2+(p[1]-a[1])**2)
                    chain=[a]+nodes+[b]
                    for j,(u,v) in enumerate(zip(chain,chain[1:])):
                        part=f'{k}-{j}'; members.append(part); self.add_line(part,u,v)
                else: self.add_line(k,a,b)
        self.add_contour(name,*members,closed=True)

    def build(self):

        # Mirrored nested waves; centerline extremes (6,8)-(42,40).
        for side in (-1,1):
            x=lambda d:24+side*d
            self.add_arc(f'outer-{side}',(x(12),8),(x(12),40),radius_x=8,radius_y=16,sweep=side>0)
            self.add_arc(f'inner-{side}',(x(9),16),(x(9),32),radius_x=2,radius_y=8,sweep=side>0)
        self.circle('head',24,24,2)
        self.add_line('mast',(24,26),(24,40))
        self.relate('connect','head','mast')

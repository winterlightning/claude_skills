"""Electrical Wall Power Socket.

Symbol plan: Wall outlet with one circular opening and two upright slots. The outer plate owns a horizontal rounded rectangle; omit redundant recessed border for clearance.
Keyshape HRECT_L; exact visible bounds (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '008837a7-eeba-4296-91b4-e7fef98dd8d1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/devices/renewable energy power socket_008837a7-eeba-4296-91b4-e7fef98dd8d1.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'rectangular-wall-socket-with-round-and-slot-openings'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/devices'
    aliases = ()
    keywords = ('electrical', 'wall', 'power', 'socket')

    def build(self):
        self.rect('plate',4,8,40,32,3)
        self.circle('round-opening',16,24,3)
        for i,x in enumerate((27,35)):self.add_line(f'slot-{i}',(x,20),(x,28))

    def circle(self,name,cx,cy,r):
        points=[(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
        names=[]
        for i,start in enumerate(points):
            part=f'{name}-{i}';self.add_arc(part,start,points[(i+1)%4],radius_x=r);names.append(part)
        self.add_contour(name,*names,closed=True)

    def rect(self,name,x,y,w,h,r=2):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for i,start in enumerate(points):
            end=points[(i+1)%8];part=f'{name}-{i}'
            if start==end: continue
            if i%2:self.add_arc(part,start,end,radius_x=r)
            else:self.add_line(part,start,end)
            names.append(part)
        self.add_contour(name,*names,closed=True)

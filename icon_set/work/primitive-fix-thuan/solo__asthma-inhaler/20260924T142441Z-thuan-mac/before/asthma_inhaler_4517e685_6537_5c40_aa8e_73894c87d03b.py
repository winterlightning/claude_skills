from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4517e685-6537-5c40-aa8e-73894c87d03b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/inhaler_4517e685-6537-5c40-aa8e-73894c87d03b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'asthma-inhaler'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/health"
    aliases = ()
    keywords = ('asthma', 'inhaler')

    def build(self):
        # Plan: L-shaped canister and mouthpiece; SQUARE (6,6)-(42,42). Lucide heater rounded housing construction; no exact inhaler match. Upright canister simplifies slight reference tilt; cap seams retained.
        self.path('body',(6,14),[(14,14),(22,14),(22,28),(32,28),(36,28),((40,28),(42,30),(42,34)),(42,36),((42,40),(40,42),(36,42)),(32,42),(14,42),((9,42),(6,39),(6,34)),(6,14)],True)
        self.add_polyline('canister',(6,14),(6,6),(22,6),(22,14));self.relate('connect','canister','body')
        self.add_line('cap-seam',(32,28),(32,42));self.relate('connect','cap-seam','body')

    def path(self, name, start, commands, closed=False):
        members=[]
        for i, command in enumerate(commands):
            tag=f"{name}-{i}"
            if len(command)==2:
                self.add_line(tag,start,command); start=command
            else:
                self.add_bezier(tag,start,command); start=command[2]
            members.append(tag)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)

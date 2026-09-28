from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5faf9360-04f6-45b9-a0d4-f000e5846bb1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/massage stick ball_5faf9360-04f6-45b9-a0d4-f000e5846bb1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'double-ball-massage-hammer'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ()
    keywords = ('double', 'ball', 'massage', 'hammer')

    def build(self):
        # Plan: Two equal ball heads and central grip; bounds (6,6)-(42,42). Shared axis24 and radius7 heads. No exact Lucide match; omit grip band.
        self.circle('left',13,13,7)
        self.circle('right',35,13,7)
        self.add_line('bridge',(20,13),(28,13));self.relate('connect','bridge','left');self.relate('connect','bridge','right')
        self.path('handle',(20,13),[(20,38),((20,42),(22,42),(24,42)),((26,42),(28,42),(28,38)),(28,13)])
        self.relate('connect','handle','bridge');self.relate('connect','handle','left');self.relate('connect','handle','right')

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

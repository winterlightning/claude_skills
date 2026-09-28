from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ab3bbc9-6273-405c-bf4d-ba06eaf3b3e5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/massage stick double_4ab3bbc9-6273-405c-bf4d-ba06eaf3b3e5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dual-head-massager'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ()
    keywords = ('dual', 'head', 'massager')

    def build(self):
        # Plan: Two outward round pads and a forked handle; bounds (6,6)-(42,42). Equal pads mirrored about24; simplify oval pads into circular outlines. No useful exact Lucide match.
        self.circle('left',13,13,7)
        self.circle('right',35,13,7)
        self.add_polyline('fork',(13,20),(24,30),(35,20));self.relate('connect','fork','left');self.relate('connect','fork','right')
        self.add_line('grip',(24,30),(24,42));self.relate('connect','grip','fork')

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
        points=[(x-r,y),(x,y-r),(x+r,y),(x,y+r)]
        for i,start in enumerate(points):
            self.add_arc(f'{name}-{i}',start,points[(i+1)%4],radius_x=r)
        self.add_contour(name,*(f'{name}-{i}' for i in range(4)),closed=True)

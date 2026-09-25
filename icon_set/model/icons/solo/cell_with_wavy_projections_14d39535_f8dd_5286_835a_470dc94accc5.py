from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14d39535-f8dd-5286-835a-470dc94accc5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/cancer cell_14d39535-f8dd-5286-835a-470dc94accc5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cell-with-wavy-projections'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ()
    keywords = ('cell', 'with', 'wavy', 'projections')

    def build(self):
        # Plan: Circular cell with six curved projections and a nucleus; bounds (6,6)-(42,42). Radial organic asymmetry from source, omit one crowded projection. No useful exact Lucide match.
        points=[(24,14),(34,24),(32,30),(24,34),(14,24),(16,18)]
        for i,start in enumerate(points):
            self.add_arc(f'cell-{i}',start,points[(i+1)%len(points)],radius_x=10)
        self.add_contour('cell',*(f'cell-{i}' for i in range(len(points))),closed=True)
        self.add_dot('nucleus',(24,24))
        for name,start,curve in [('n',(24,14),((30,10),(20,10),(24,6))),('s',(24,34),((18,38),(28,38),(24,42))),('w',(14,24),((8,28),(10,20),(6,24))),('e',(34,24),((40,20),(38,28),(42,24))),('nw',(16,18),((9,17),(13,10),(8,8))),('se',(32,30),((39,31),(35,38),(40,40)))]:
            self.add_bezier(name,start,curve);self.relate('connect',name,'cell')

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

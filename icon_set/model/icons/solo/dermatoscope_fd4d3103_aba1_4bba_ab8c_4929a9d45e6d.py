from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd4d3103-aba1-4bba-ab8c-4929a9d45e6d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/dermatoscope_fd4d3103-aba1-4bba-ab8c-4929a9d45e6d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dermatoscope'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ()
    keywords = ('dermatoscope',)

    def build(self):
        # Plan: Broad horizontal inspection head and tilted grip; bounds (6,6)-(42,42). Source owns angled handle; Lucide ear demonstrates broad coherent curves. Omit narrow handle bands.
        self.path('head',(10,6),[(32,6),(42,12),(42,18),(32,24),(26,24),(16,24),(10,24),((6,24),(6,22),(6,20)),(6,10),((6,6),(8,6),(10,6))],True)
        self.path('grip',(16,24),[(10,38),((9,41),(12,42),(16,42)),((18,42),(20,42),(21,39)),(26,24)])
        self.relate('connect','grip','head')

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

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6cb102ae-38d0-4d2c-a4ad-c70db66b2436'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/pill_6cb102ae-38d0-4d2c-a4ad-c70db66b2436.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'capsule-pill-6cb102ae'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/health"
    aliases = ()
    keywords = ('capsule', 'pill')

    def build(self):
        # Plan: Diagonal capsule with a single center seam. SQUARE centerlines (6,6)-(42,42). Lucide pill informs a coherent rounded capsule and transverse seam. Matched paired cubic shoulders preserve smooth integer-grid tangents. The source UUID distinguishes this brief from the other capsule sources.
        self.path('shell',(24,10),[((28,6),(30,6),(34,6)),((40,6),(42,10),(42,16)),((42,20),(40,22),(38,24)),(31,31),(24,38),((20,42),(18,42),(14,42)),((8,42),(6,38),(6,32)),((6,28),(8,26),(10,24)),(17,17),(24,10)],True)
        self.add_line('seam',(17,17),(31,31))
        self.relate('connect','seam','shell')

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

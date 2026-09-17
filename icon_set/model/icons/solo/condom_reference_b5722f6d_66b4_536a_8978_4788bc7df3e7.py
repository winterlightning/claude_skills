from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b5722f6d-66b4-536a-8978-4788bc7df3e7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/condom_b5722f6d-66b4-536a-8978-4788bc7df3e7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'condom-reference'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/health"
    aliases = ()
    keywords = ('condom',)

    def build(self):
        # Plan: Reservoir tip, rounded shoulders, rolled base; bounds (8,4)-(40,44). Mirror about24. Omit extra collar seam; no useful exact Lucide match.
        self.path('body',(12,36),[(12,20),((12,14),(16,12),(20,10)),((20,6),(21,4),(24,4)),((27,4),(28,6),(28,10)),((32,12),(36,14),(36,20)),(36,36)])
        self.path('rim',(12,36),[(36,36),((40,36),(40,38),(40,40)),((40,42),(40,44),(36,44)),(12,44),((8,44),(8,42),(8,40)),((8,38),(8,36),(12,36))],True)
        self.relate('connect','rim','body')

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

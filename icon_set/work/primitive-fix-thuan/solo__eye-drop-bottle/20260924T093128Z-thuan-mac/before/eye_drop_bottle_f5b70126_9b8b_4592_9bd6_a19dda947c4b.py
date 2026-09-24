from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f5b70126-9b8b-4592-9bd6-a19dda947c4b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/eye drop medicine_f5b70126-9b8b-4592-9bd6-a19dda947c4b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'eye-drop-bottle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/health"
    aliases = ()
    keywords = ('eye', 'drop', 'bottle')

    def build(self):
        # Plan: Diagonal bottle with integral nozzle and a separated pointed drop; bounds (6,6)-(42,42). Lucide pill smooth diagonal housing. Drop kept broad, remove narrow double collar.
        self.path('bottle',(20,14),[(32,6),((34,6),(35,6),(36,8)),(42,20),((42,22),(42,23),(40,24)),(28,30),(14,24),(20,14)],True)
        self.add_line('collar',(20,14),(28,30));self.relate('connect','collar','bottle')
        self.path('drop',(11,32),[((9,34),(6,36),(6,38)),((6,41),(8,42),(11,42)),((14,42),(16,41),(16,38)),((16,36),(13,34),(11,32))],True)

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

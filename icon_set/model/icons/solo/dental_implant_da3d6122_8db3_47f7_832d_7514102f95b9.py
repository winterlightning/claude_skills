from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'da3d6122-8db3-47f7-832d-7514102f95b9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/dental implant_da3d6122-8db3-47f7-832d-7514102f95b9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dental-implant'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ()
    keywords = ('dental', 'implant')

    def build(self):
        # Plan: Two-lobed crown and tapered screw with one diagonal thread stroke; bounds (8,4)-(40,44). Mirrored crown and shaft; omit separate collar to open spacing. No useful exact Lucide match.
        self.path('crown',(8,12),[((8,6),(12,4),(16,4)),((20,4),(22,8),(24,8)),((26,8),(28,4),(32,4)),((36,4),(40,6),(40,12)),((40,18),(38,22),(34,22)),(30,22),(18,22),(14,22),((10,22),(8,18),(8,12))],True)
        self.path('shaft',(18,22),[(18,32),(18,40),(24,44),(30,40),(30,32),(30,22)])
        self.relate('connect','shaft','crown')
        self.add_line('thread',(18,34),(30,30));self.relate('connect','thread','shaft')

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

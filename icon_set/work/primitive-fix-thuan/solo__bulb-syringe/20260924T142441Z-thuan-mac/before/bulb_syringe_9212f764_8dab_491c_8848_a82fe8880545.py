from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9212f764-8dab-491c-8848-a82fe8880545'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/enema_9212f764-8dab-491c-8848-a82fe8880545.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bulb-syringe'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/health"
    aliases = ()
    keywords = ('bulb', 'syringe')

    def build(self):
        # Plan: Rounded squeeze bulb with integral diagonal nozzle; SQUARE (6,6)-(42,42). Lucide syringe informs diagonal narrow nozzle and coherent silhouette. Omit neck ridges; continuous tangent curves define bulb.
        self.path('outline',(6,28),[((6,20),(12,14),(20,14)),((23,14),(24,16),(26,14)),(34,6),((36,6),(38,6),(40,8)),((42,10),(42,10),(42,11)),((42,12),(41,13),(40,14)),(32,22),((30,24),(34,26),(34,30)),((34,37),(28,42),(20,42)),((12,42),(6,36),(6,28))],True)

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

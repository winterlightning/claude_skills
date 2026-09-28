from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '78c52f14-f83d-547b-9f4f-1bc5a23d537d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/specialty knee_78c52f14-f83d-547b-9f4f-1bc5a23d537d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bent-knee-joint'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/health"
    aliases = ()
    keywords = ('bent', 'knee', 'joint')

    def build(self):
        # Plan: Femur angled into separated upright tibia; VRECT_L (8,4)-(40,44). Source anatomy retained as two broad bone contours; no useful exact Lucide match. Deliberate anatomical bend and open cropped shafts; no decorative marks.
        self.path('femur',(8,4),[(20,16),((20,20),(18,24),(24,24)),((28,24),(28,19),(32,20)),((36,25),(40,23),(40,19)),((40,15),(35,15),(32,12)),(24,4)])
        self.path('tibia',(22,44),[(22,38),((20,32),(24,33),(28,35)),((32,37),(34,33),(38,33)),((40,33),(36,39),(36,44))])

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

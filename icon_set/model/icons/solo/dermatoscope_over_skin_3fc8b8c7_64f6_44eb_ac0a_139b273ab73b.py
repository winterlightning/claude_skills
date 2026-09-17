from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3fc8b8c7-64f6-44eb-ac0a-139b273ab73b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/dermatoscope skin_3fc8b8c7-64f6-44eb-ac0a-139b273ab73b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dermatoscope-over-skin'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/health"
    aliases = ()
    keywords = ('dermatoscope', 'over', 'skin')

    def build(self):
        # Plan: Angled handle joins a rounded upright probe over one undulating skin line; bounds (4,8)-(44,40). Omit second skin contour and grip seams. No exact Lucide match.
        self.path('probe',(32,8),[(40,8),((44,8),(44,10),(44,12)),(44,22),((44,27),(40,30),(36,30)),((32,30),(28,27),(28,22)),(28,20),(28,12),((28,8),(30,8),(32,8))],True)
        self.path('handle',(28,12),[(8,8),((5,8),(4,9),(4,12)),((4,15),(4,16),(7,17)),(28,22)])
        self.relate('connect','handle','probe')
        self.path('skin',(4,40),[((12,40),(12,38),(20,38)),((28,38),(28,40),(36,40)),((40,40),(42,39),(44,39))])

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

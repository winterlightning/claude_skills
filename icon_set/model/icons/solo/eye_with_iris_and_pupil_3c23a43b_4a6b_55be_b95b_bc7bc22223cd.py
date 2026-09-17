from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3c23a43b-4a6b-55be-b95b-bc7bc22223cd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/specialty eye_3c23a43b-4a6b-55be-b95b-bc7bc22223cd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'eye-with-iris-and-pupil'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/health"
    aliases = ()
    keywords = ('eye', 'with', 'iris', 'and', 'pupil')

    def build(self):
        # Plan: Almond eye with one central circular iris; bounds (4,8)-(44,40). Lucide eye paired smooth eyelids and central ring. Omit separate inner pupil ring to preserve open negative space.
        self.path('lids',(4,24),[((8,14),(16,8),(24,8)),((32,8),(40,14),(44,24)),((40,34),(32,40),(24,40)),((16,40),(8,34),(4,24))],True)
        self.circle('iris',24,24,6)

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

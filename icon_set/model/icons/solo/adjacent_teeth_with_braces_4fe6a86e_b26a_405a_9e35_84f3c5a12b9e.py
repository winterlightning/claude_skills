from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4fe6a86e-b26a-405a-9e35-84f3c5a12b9e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/dental brace_4fe6a86e-b26a-405a-9e35-84f3c5a12b9e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'adjacent-teeth-with-braces'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ()
    keywords = ('adjacent', 'teeth', 'with', 'braces')

    def build(self):
        # Plan: Two joined molar silhouettes and continuous brace wire. HRECT_L (4,8)-(44,40); common center seam and mirrored crowns. Brackets reduced to short uprights, root detail simplified. No useful exact Lucide match; source owns paired teeth.
        self.path('teeth',(4,20),[((4,12),(8,8),(14,8)),((18,8),(21,10),(24,12)),((27,10),(30,8),(34,8)),((40,8),(44,12),(44,20)),(44,30),((44,36),(44,40),(40,40)),((36,40),(38,30),(34,30)),((30,30),(32,40),(28,40)),(24,40),(20,40),((16,40),(18,30),(14,30)),((10,30),(12,40),(8,40)),((4,40),(4,36),(4,30)),(4,20)],True)
        self.add_line('divider',(24,12),(24,20));self.relate('connect','divider','teeth')
        self.add_polyline('wire',(4,20),(14,20),(24,20),(34,20),(44,20));self.relate('connect','wire','teeth');self.relate('connect','wire','divider')
        for name,x in [('left',14),('right',34)]:
            self.add_polyline('bracket-'+name,(x,16),(x,20),(x,24));self.relate('connect','bracket-'+name,'wire')

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

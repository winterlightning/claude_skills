from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a3e9b51-1d2b-5969-ac5c-503d8629e1bb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/hearing aid ear_6a3e9b51-1d2b-5969-ac5c-503d8629e1bb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ear-with-hearing-aid-reference'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/health"
    aliases = ()
    keywords = ('ear', 'with', 'hearing', 'aid')

    def build(self):
        # Plan: Ear contour with inner arch and visible behind-ear hearing aid; bounds (8,4)-(40,44). Lucide ear smooth upper bowl to lobe; omit tiny canal loop.
        self.path('ear',(8,18),[((8,10),(13,4),(22,4)),((30,4),(34,10),(34,18)),((34,28),(24,30),(24,36)),((24,40),(21,44),(16,44)),((10,44),(8,40),(8,36))])
        self.path('fold',(17,22),[((14,14),(24,12),(25,19)),((26,21),(23,23),(20,24))])
        self.path('aid',(34,18),[((40,18),(40,22),(40,26)),((40,31),(38,34),(34,34)),(28,34)])
        self.relate('connect','aid','ear')

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

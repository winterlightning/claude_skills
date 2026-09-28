from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7e4163be-eaca-4061-a449-298bdb7d7f9a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/head dizziness_7e4163be-eaca-4061-a449-298bdb7d7f9a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dizzy-head-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/health"
    aliases = ()
    keywords = ('dizzy', 'head', 'profile')

    def build(self):
        # Plan: Left-facing head with orbit across crown; bounds (6,6)-(42,42). Drop crowded stars and retain circular motion cue. Human reference for simplified contour; source profile intentional asymmetry.
        self.path('head',(14,16),[(6,28),(14,28),(14,32),((14,36),(16,38),(20,38)),(22,38),(22,42)])
        self.path('back',(32,42),[(32,34),((38,30),(40,24),(34,16))])
        self.path('orbit',(14,6),[((6,6),(6,8),(6,11)),((6,14),(10,16),(14,16)),(34,16),((40,16),(42,14),(42,11)),((42,8),(40,6),(34,6)),(26,6)])
        self.relate('connect','orbit','head');self.relate('connect','orbit','back')

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

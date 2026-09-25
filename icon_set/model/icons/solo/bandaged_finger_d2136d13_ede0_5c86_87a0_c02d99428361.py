from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd2136d13-ede0-5c86-87a0-c02d99428361'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/bandage finger_d2136d13-ede0-5c86-87a0-c02d99428361.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bandaged-finger'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ()
    keywords = ('bandaged', 'finger')

    def build(self):
        # Plan: Extended bandaged finger and bent neighbor; SQUARE (6,6)-(42,42). Shared human-reference vocabulary for simple body contours; Lucide pill rounded diagonal construction. Two band edges attach to split finger sides; finger positions intentionally asymmetric.
        self.path('hand',(6,42),[(6,32),((6,29),(8,26),(10,24)),(14,20),(22,12),(26,8),((28,6),(31,6),(34,6)),((39,6),(42,10),(42,14)),((42,17),(40,20),(38,22)),(34,26),(30,30),(28,32),(22,38)])
        self.path('neighbor',(34,26),[((40,20),(42,24),(42,28)),((42,32),(38,36),(32,42))])
        self.relate('connect','hand','neighbor')
        self.add_line('band-upper',(22,12),(38,22));self.relate('connect','band-upper','hand')
        self.add_line('band-lower',(14,20),(30,30));self.relate('connect','band-lower','hand')

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

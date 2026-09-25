"""Right triangle and outlined terminal bar, horizontally directional; Lucide skip-forward spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ce0c35d-f4cb-526e-93da-1cd93ff0c33d'
SOURCE_PATH = 'pictographic-primitives/video/controls next_8ce0c35d-f4cb-526e-93da-1cd93ff0c33d.svg'
AUTHOR = 'gpt-6'

class SkipForwardSolo(Solo48):
    icon_id = 'skip-forward-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video"
    categories = ("video", "primitives")
    aliases = ()
    keywords = ('skip', 'next', 'forward', 'media', 'playback', 'control', 'track')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def rounded(self, name, x, y, w, h, r):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i,a in enumerate(pts):
            b=pts[(i+1)%8]; ident=name+'-'+str(i);ids.append(ident)
            if i%2:self.add_arc(ident,a,b,radius_x=r)
            else:self.add_line(ident,a,b)
        self.add_contour(name,*ids,closed=True)

    def build(self):
        # Right triangle and outlined terminal bar, horizontally directional; Lucide skip-forward spacing.
        self.add_polyline('play',(4,8),(28,24),(4,40),closed=True)
        self.add_polyline('bar',(36,8),(44,8),(44,40),(36,40),closed=True)

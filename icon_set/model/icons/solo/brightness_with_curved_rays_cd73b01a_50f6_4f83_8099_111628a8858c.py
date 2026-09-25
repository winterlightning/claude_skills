"""Right disc and two nested circular waves; concentric construction with intentional right weighting."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd73b01a-50f6-4f83-8099-111628a8858c'
SOURCE_PATH = 'pictographic-primitives/video/video edit brightness_cd73b01a-50f6-4f83-8099-111628a8858c.svg'
AUTHOR = 'gpt-6'

class BrightnessWithCurvedRays(Solo48):
    icon_id = 'brightness-with-curved-rays'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video"
    aliases = ()
    keywords = ('brightness', 'light', 'circle', 'arcs', 'exposure', 'video', 'adjustment')

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
        # Right disc and two nested circular waves; concentric construction with intentional right weighting.
        self.circle('disc',35,24,9)
        self.add_arc('outer-ray',(12,8),(12,40),radius_x=20,sweep=False)
        self.add_arc('inner-ray',(21,12),(21,36),radius_x=13,sweep=False)

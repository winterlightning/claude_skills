"""Right disc with three left rays; directional asymmetry preserves source."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c296425d-8a02-4c54-9617-c19889ea6244'
SOURCE_PATH = 'pictographic-primitives/video/video edit brightness_c296425d-8a02-4c54-9617-c19889ea6244.svg'
AUTHOR = 'gpt-6'

class BrightnessWithStraightRays(Solo48):
    icon_id = 'brightness-with-straight-rays'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('brightness', 'light', 'circle', 'rays', 'exposure', 'video', 'adjustment')

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
        # Right disc with three left rays; directional asymmetry preserves source.
        self.circle('disc',32,24,12)
        for i,(x,y,end) in enumerate([(8,8,14),(4,24,11),(8,40,14)]):
            self.add_line(f'ray-{i}',(x,y),(end,y))

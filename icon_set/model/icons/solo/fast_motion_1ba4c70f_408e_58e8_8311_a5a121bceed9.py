"""Circular leading edge and three trails; horizontal motion intentionally asymmetric; tiny extra dashes omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1ba4c70f-408e-58e8-8311-a5a121bceed9'
SOURCE_PATH = 'pictographic-primitives/video/fast motion_1ba4c70f-408e-58e8-8311-a5a121bceed9.svg'
AUTHOR = 'gpt-6'

class FastMotion(Solo48):
    icon_id = 'fast-motion'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video"
    categories = ("video", "primitives")
    aliases = ()
    keywords = ('motion', 'fast', 'speed', 'trail', 'movement', 'circle', 'velocity')

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
        # Circular leading edge and three trails; horizontal motion intentionally asymmetric; tiny extra dashes omitted.
        self.add_line('upper-trail',(15,8),(28,8))
        self.add_arc('head',(28,8),(28,40),radius_x=16)
        self.add_line('lower-trail',(28,40),(15,40))
        self.add_contour('moving-head','upper-trail','head','lower-trail')
        self.add_line('middle-trail',(4,24),(25,24))
        self.add_line('upper-dash',(4,8),(4,8))
        self.add_line('lower-dash',(4,40),(4,40))

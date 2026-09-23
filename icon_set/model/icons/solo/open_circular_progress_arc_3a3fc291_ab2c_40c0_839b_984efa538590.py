from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3a3fc291-ab2c-40c0-839b-984efa538590'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_07/blizzards 1_3a3fc291-ab2c-40c0-839b-984efa538590.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-circular-progress-arc'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('open', 'circular', 'progress', 'arc')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def box(self, name, x, y, w, h, r=0):
        if not r:
            self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            return
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i in range(8):
            part=f'{name}-{i}'; ids.append(part)
            if i%2: self.add_arc(part,pts[i],pts[(i+1)%8],radius_x=r)
            else: self.add_line(part,pts[i],pts[(i+1)%8])
        self.add_contour(name,*ids,closed=True)

    def build(self):
        # Plan: CIRCLE radius20 about24,24; exact 12-16-20 endpoints retain broad lower-left opening.
        self.add_arc('progress',(8,12),(36,40),radius_x=20,large_arc=True)

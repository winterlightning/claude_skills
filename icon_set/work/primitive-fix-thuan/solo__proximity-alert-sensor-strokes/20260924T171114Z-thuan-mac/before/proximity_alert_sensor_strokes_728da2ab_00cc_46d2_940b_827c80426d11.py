from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '728da2ab-00cc-46d2-940b-827c80426d11'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/audi pre sense warning_728da2ab-00cc-46d2-940b-827c80426d11.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'proximity-alert-sensor-strokes'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('proximity', 'alert', 'sensor', 'strokes')

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
        # Plan: HRECT_M extremes 4,10 to 44,38; three separate strokes preserve the visible left, upper-middle and right arrangement.
        self.add_line('left-sensor',(4,16),(4,38))
        self.add_line('upper-signal',(20,10),(26,10))
        self.add_line('right-signal',(38,22),(44,27))

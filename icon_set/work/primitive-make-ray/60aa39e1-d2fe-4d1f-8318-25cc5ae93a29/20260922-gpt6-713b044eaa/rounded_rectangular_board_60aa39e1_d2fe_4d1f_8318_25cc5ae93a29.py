from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '60aa39e1-d2fe-4d1f-8318-25cc5ae93a29'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_07/board_60aa39e1-d2fe-4d1f-8318-25cc5ae93a29.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-rectangular-board'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('rounded', 'rectangular', 'board')

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
        # Plan: HRECT_M extremes4,10 to44,38; wide empty board with four shared radius3 corners.
        self.box('board',4,10,40,28,3)

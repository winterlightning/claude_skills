from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd3179da3-e2e2-4329-8932-7b3c8044a535'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/astronomy planet saturn 1_d3179da3-e2e2-4329-8932-7b3c8044a535.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'planet-with-diagonal-ring'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('planet', 'with', 'diagonal', 'ring')

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
        # Plan: SQUARE extremes 6,6 to 42,42; concentric circular planet and rising diagonal ring preserve source arrangement.
        self.circle('planet',24,24,18)
        self.add_line('edge-on-ring',(6,42),(42,6))

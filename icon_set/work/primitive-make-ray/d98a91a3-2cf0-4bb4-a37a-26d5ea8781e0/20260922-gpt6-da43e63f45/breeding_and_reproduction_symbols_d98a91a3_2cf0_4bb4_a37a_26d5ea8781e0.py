from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd98a91a3-2cf0-4bb4-a37a-26d5ea8781e0'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_08/breeding gender symbols_d98a91a3-2cf0-4bb4-a37a-26d5ea8781e0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'breeding-and-reproduction-symbols'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('breeding', 'and', 'reproduction', 'symbols')

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
        # Plan: SQUARE extremes6,6 to42,42; open male-symbol arc, upward-right arrow, unequal detached circles and lower-left triangle.
        self.add_arc('ring-upper',(14,20),(32,14),radius_x=10)
        self.add_arc('ring-lower',(32,14),(24,30),radius_x=10)
        self.add_contour('open-ring','ring-upper','ring-lower')
        self.add_line('arrow-shaft',(32,14),(42,6))
        self.add_polyline('arrowhead',(34,6),(42,6),(42,14))
        self.relate('connect','open-ring','arrow-shaft')
        self.relate('connect','arrow-shaft','arrowhead')
        self.circle('small-circle',9,25,3)
        self.circle('larger-circle',20,22,4)
        self.add_polyline('triangle',(17,34),(25,42),(9,42),closed=True)

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '57a71ef9-0c30-4a25-a290-84a6666d4f6e'
SOURCE_PATH = 'pictographic-primitives/other/money bill_57a71ef9-0c30-4a25-a290-84a6666d4f6e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'banknote-currency-bill'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('money', 'cash', 'banknote')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def rounded_rect(self, name, x0, y0, x1, y1, r):
        pts=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
        ids=[]
        for i in range(8):
            eid=f'{name}-{i}'
            a,b=pts[i],pts[(i+1)%8]
            if i%2: self.add_arc(eid,a,b,radius_x=r)
            else: self.add_line(eid,a,b)
            ids.append(eid)
        self.add_contour(name,*ids,closed=True)

    def build(self):
        # Plan: landscape rectangle with four mirrored quarter-circle corner panels and central seal.
        # HRECT_M centerlines (4,10)-(44,38); corner radius 8 and seal radius 4.
        x0,y0,x1,y1,r=4,10,44,38,8
        self.add_polyline('bill',(x0,y0),(x0+r,y0),(x1-r,y0),(x1,y0),
                          (x1,y0+r),(x1,y1-r),(x1,y1),(x1-r,y1),
                          (x0+r,y1),(x0,y1),(x0,y1-r),(x0,y0+r),closed=True)
        corners=[((x0+r,y0),(x0,y0+r)),((x1,y0+r),(x1-r,y0)),
                 ((x0,y1-r),(x0+r,y1)),((x1-r,y1),(x1,y1-r))]
        for i,(a,b) in enumerate(corners):
            self.add_arc(f'corner-{i}',a,b,radius_x=r)
            self.relate('connect','bill',f'corner-{i}')
        self.circle('seal',24,24,4)

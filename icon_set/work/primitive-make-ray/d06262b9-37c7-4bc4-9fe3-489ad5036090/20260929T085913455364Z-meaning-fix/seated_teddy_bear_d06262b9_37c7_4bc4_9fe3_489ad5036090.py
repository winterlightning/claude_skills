"""Separate two round seated paws, add rounded arms and a small central nose under the domed bear head."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd06262b9-37c7-4bc4-9fe3-489ad5036090'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-teddy-bear/20260929T085457Z-thuan-mac/reference/teddy bear_d06262b9-37c7-4bc4-9fe3-489ad5036090.svg'
AUTHOR = "gpt-6"

class RevisedIcon(Solo48):
    icon_id = 'seated-teddy-bear'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/people" 
    aliases = ()
    keywords = ('teddy bear',)
    # Symbol plan: Separate two round seated paws, add rounded arms and a small central nose under the domed bear head.
    # Construction: No useful Lucide teddy match; original reference controls the ears, belly and paws.

    def path(self, name, start, *segments, closed=False):
        ids = []
        point = start
        for j, segment in enumerate(segments):
            eid = f"{name}-{j}"
            if len(segment) == 2:
                self.add_line(eid, point, segment)
                end = segment
            else:
                end, rx, ry, sweep, large = segment
                self.add_arc(eid, point, end, radius_x=rx, radius_y=ry,
                             sweep=sweep, large_arc=large)
            ids.append(eid)
            point = end
        self.add_contour(name, *ids, closed=closed)

    def circle(self, name, x, y, r):
        self.path(name, (x-r,y), ((x+r,y),r,r,True,False),
                  ((x-r,y),r,r,True,False), closed=True)

    def oval(self, name, x, y, rx, ry):
        self.path(name, (x-rx,y), ((x+rx,y),rx,ry,True,False),
                  ((x-rx,y),rx,ry,True,False), closed=True)

    def box(self, name, x1,y1,x2,y2,r=3):
        self.path(name, (x1+r,y1), (x2-r,y1),
                  ((x2,y1+r),r,r,True,False), (x2,y2-r),
                  ((x2-r,y2),r,r,True,False), (x1+r,y2),
                  ((x1,y2-r),r,r,True,False), (x1,y1+r),
                  ((x1+r,y1),r,r,True,False), closed=True)

    def build(self):

        # Bilateral head, ears and paws use shared dimensions.
        self.oval('head',24,16,11,10)
        self.path('left-ear',(14,12),((20,7),5,5,True,True))
        self.path('right-ear',(28,7),((34,12),5,5,True,True))
        self.add_dot('nose',(24,19))
        self.oval('left-paw',13,37,6,7)
        self.oval('right-paw',35,37,6,7)
        self.path('left-arm',(16,25),((7,32),10,10,False,False),(8,34))
        self.path('right-arm',(32,25),((41,32),10,10,True,False),(40,34))
        self.path('belly',(19,41),((29,41),12,4,False,False))
     

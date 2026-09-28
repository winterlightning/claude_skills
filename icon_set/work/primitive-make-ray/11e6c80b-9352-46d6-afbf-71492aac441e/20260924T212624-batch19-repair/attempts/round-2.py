"""Game controller above an open package.
SOLO48 SQUARE; geometry authored independently from the rendered reference.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '11e6c80b-9352-46d6-afbf-71492aac441e'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-04/game bundle package 2 game game bundle package_11e6c80b-9352-46d6-afbf-71492aac441e.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'game-bundle-package-2-game-game-bundle-package'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/gaming'
    aliases = ()
    keywords = ('game', 'bundle', 'package', '2', 'game', 'game', 'bundle', 'package')

    def line(self, n, a, b):
        self.add_line(n,a,b)

    def arc(self,n,a,b,rx,ry=None,sweep=True):
        self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)

    def rect(self,n,x,y,w,h,r):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for i in range(8):
            a,b=pts[i],pts[(i+1)%8]
            if i%2:self.arc(f"{n}-{i}",a,b,r)
            else:self.line(f"{n}-{i}",a,b)
        self.add_contour(n,*(f"{n}-{i}" for i in range(8)),closed=True)

    def build(self):
        # Plan: controller silhouette and controls above two mirrored box flaps.
        self.add_polyline('controller',(16,6),(32,6),(35,18),(29,18),(27,16),(21,16),(19,18),(13,18),closed=True)
        # Tiny controller controls omitted: silhouette carries gaming identity.
        axis=24
        for side in (-1,1):
            p=lambda x,y:(axis+side*x,y)
            self.add_polyline('flap'+str(side),p(0,26),p(14,26),p(18,34),p(4,34),closed=True)
        self.add_polyline('box', (10,34),(10,42),(38,42),(38,34))
        self.line('seam',(24,36),(24,42))
        self.relate('connect','box','flap-1')
        self.relate('connect','box','flap1')
        self.relate('connect','seam','box')
        self.relate('connect','flap-1','flap1')

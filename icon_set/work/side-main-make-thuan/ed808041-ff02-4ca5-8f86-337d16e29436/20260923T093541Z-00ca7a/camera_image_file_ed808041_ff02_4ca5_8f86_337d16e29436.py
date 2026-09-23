from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ed808041-ff02-4ca5-8f86-337d16e29436'
SOURCE_PATH = 'pictographic-primitives/other/camera file_ed808041-ff02-4ca5-8f86-337d16e29436.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'camera-image-file'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('camera', 'file', 'image', 'photo')

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
        # Plan: rounded document with clipped top-right corner enclosing camera silhouette and central point.
        # SQUARE centerlines (6,6)-(42,42); widen source page to preserve internal clearances.
        self.add_line('page-top',(10,6),(32,6))
        self.add_line('page-cut',(32,6),(42,16))
        self.add_line('page-right',(42,16),(42,38))
        self.add_arc('page-br',(42,38),(38,42),radius_x=4)
        self.add_line('page-bottom',(38,42),(10,42))
        self.add_arc('page-bl',(10,42),(6,38),radius_x=4)
        self.add_line('page-left',(6,38),(6,10))
        self.add_arc('page-tl',(6,10),(10,6),radius_x=4)
        self.add_contour('page','page-top','page-cut','page-right','page-br','page-bottom','page-bl','page-left','page-tl',closed=True)
        self.add_polyline('camera',(16,18),(19,18),(20,15),(28,15),(29,18),(32,18),(32,33),(16,33),closed=True)
        self.add_dot('lens',(24,25))

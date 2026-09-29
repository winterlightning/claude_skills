"""Restore a distinct lower-right speech tail, two horizontal text strokes, and an open yuan/yen glyph."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '16791ce0-2910-4e3b-82ee-8dcb1834e398'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__yen-currency-message-bubble-solo/20260929T085457Z-thuan-mac/reference/message yuan sign lines_16791ce0-2910-4e3b-82ee-8dcb1834e398.svg'
AUTHOR = "gpt-6"

class RevisedIcon(Solo48):
    icon_id = 'yen-currency-message-bubble-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/people" 
    aliases = ()
    keywords = ('message yuan sign lines',)
    # Symbol plan: Restore a distinct lower-right speech tail, two horizontal text strokes, and an open yuan/yen glyph.
    # Construction: Original reference: lower-right bubble tail, currency sign and two text lines; no additional Lucide match required.

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

        self.path('bubble',(10,6),(38,6),((43,11),5,5,True,False),(43,32),
                  ((38,37),5,5,True,False),(34,37),(34,44),(25,37),(10,37),
                  ((5,32),5,5,True,False),(5,11),((10,6),5,5,True,False),closed=True)
        self.path('currency',(12,15),(18,23),(24,15))
        self.add_line('currency-stem',(18,23),(18,30))
        self.add_line('currency-bar',(13,24),(23,24))
        self.add_line('message-one',(30,20),(36,20))
        self.add_line('message-two',(30,28),(36,28))
        self.relate('connect','currency','currency-stem')
        self.relate('connect','currency','currency-bar')
        self.relate('connect','currency-stem','currency-bar')
     

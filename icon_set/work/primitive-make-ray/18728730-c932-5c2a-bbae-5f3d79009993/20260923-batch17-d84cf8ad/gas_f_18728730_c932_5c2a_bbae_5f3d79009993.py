"""A semicircular fuel gauge with needle, ticks, and two F labels.
SOLO48 HRECT_L; geometry authored independently from the rendered reference.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '18728730-c932-5c2a-bbae-5f3d79009993'
SOURCE_PATH = 'icon_set/work/todo-references/gas f_18728730-c932-5c2a-bbae-5f3d79009993.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'gas-f'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/instruments'
    aliases = ()
    keywords = ('gas', 'f')

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
        # Plan: elliptical gauge arch with shared tick nodes, diagonal needle, two F glyphs.
        self.arc('arch-left',(4,22),(24,8),20,14)
        self.arc('arch-right',(24,8),(44,22),20,14)
        self.add_contour('arch','arch-left','arch-right')
        self.line('tick-top',(24,8),(24,12));self.relate('connect','arch','tick-top')
        for side in (-1,1):
            x=24+side*20
            self.line('tick'+str(side),(x,22),(x-side*4,22))
            self.relate('connect','arch','tick'+str(side))
        self.arc('hub-a',(22,24),(26,24),2)
        self.arc('hub-b',(26,24),(22,24),2)
        self.add_contour('hub','hub-a','hub-b',closed=True)
        self.line('needle',(26,24),(30,18));self.relate('connect','hub','needle')
        for x in (6,38):
            self.add_polyline('f'+str(x),(x,40),(x,30),(x+4,30))
            self.line('fbar'+str(x),(x,38),(x+3,38));self.relate('connect','f'+str(x),'fbar'+str(x))

"""explosive gas: reference reconstructed as a complete SOLO48 subject.
Plan: coherent contours and shared parameters; see build for symbol ownership.
Keyshape SQUARE; visible extremes (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '93f5c2d8-a034-5d90-a88b-7e453bb0f1b5'
SOURCE_PATH = 'icon_set/work/todo-references/explosive gas_93f5c2d8-a034-5d90-a88b-7e453bb0f1b5.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'explosive-gas'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    aliases = ()
    keywords = ('explosive gas',)

    def circle(self, name, x, y, r):
        self.add_arc(name+'-a', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-b', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-a', name+'-b', closed=True)

    def rounded(self, name, x, y, w, h, r):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for i in range(8):
            a,b=points[i],points[(i+1)%8]
            if i%2:self.add_arc(name+str(i),a,b,radius_x=r)
            else:self.add_line(name+str(i),a,b)
        self.add_contour(name,*(name+str(i) for i in range(8)),closed=True)

    def build(self):
        # Gas cylinder at lower left; an eight-ray burst overlaps its upper right.
        self.add_line('valve-top',(6,6),(18,6))
        self.add_line('valve-stem',(12,6),(12,14))
        self.relate('connect','valve-top','valve-stem')
        self.add_line('tank-top',(12,14),(18,14))
        self.add_arc('tank-tl',(6,20),(12,14),radius_x=6)
        self.add_line('tank-left',(6,36),(6,20))
        self.add_arc('tank-bl',(12,42),(6,36),radius_x=6)
        self.add_line('tank-bottom',(20,42),(12,42))
        self.add_arc('tank-br',(26,36),(20,42),radius_x=6)
        self.add_line('tank-right',(26,34),(26,36))
        self.add_contour('tank','tank-right','tank-br','tank-bottom','tank-bl','tank-left','tank-tl','tank-top')
        self.relate('connect','valve-stem','tank')
        self.add_polyline('burst',(32,6),(35,14),(41,11),(38,18),(42,22),(35,25),(37,32),(30,28),(26,34),(23,27),(16,28),(20,21),(17,16),(25,17),closed=True)
        self.relate('connect','burst','tank')

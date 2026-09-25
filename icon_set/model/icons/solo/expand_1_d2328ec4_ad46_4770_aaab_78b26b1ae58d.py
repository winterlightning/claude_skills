"""expand 1: reference reconstructed as a complete SOLO48 subject.
Plan: coherent contours and shared parameters; see build for symbol ownership.
Keyshape SQUARE; visible extremes (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd2328ec4-ad46-4770-aaab-78b26b1ae58d'
SOURCE_PATH = 'icon_set/work/todo-references/expand 1_d2328ec4-ad46-4770-aaab-78b26b1ae58d.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'expand-1'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('expand 1',)

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
        # Opposite frame corners surround a smaller rounded square at lower left.
        self.add_line('tl-top',(10,6),(18,6))
        self.add_arc('tl-turn',(6,10),(10,6),radius_x=4)
        self.add_line('tl-side',(6,18),(6,10))
        self.add_contour('top-left','tl-side','tl-turn','tl-top')
        self.add_line('tr-top',(30,6),(38,6))
        self.add_arc('tr-turn',(38,6),(42,10),radius_x=4)
        self.add_line('tr-side',(42,10),(42,18))
        self.add_contour('top-right','tr-top','tr-turn','tr-side')
        self.add_line('br-side',(42,30),(42,38))
        self.add_arc('br-turn',(42,38),(38,42),radius_x=4)
        self.add_line('br-bottom',(38,42),(30,42))
        self.add_contour('bottom-right','br-side','br-turn','br-bottom')
        self.rounded('small-square',6,26,16,16,3)

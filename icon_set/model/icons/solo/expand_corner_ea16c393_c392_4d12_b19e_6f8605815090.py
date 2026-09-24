"""expand corner: reference reconstructed as a complete SOLO48 subject.
Plan: coherent contours and shared parameters; see build for symbol ownership.
Keyshape SQUARE; visible extremes (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ea16c393-c392-4d12-b19e-6f8605815090'
SOURCE_PATH = 'icon_set/work/todo-references/expand corner_ea16c393-c392-4d12-b19e-6f8605815090.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'expand-corner'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('expand corner',)

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
        # Open square at lower left and a diagonal escaping to the upper right.
        self.add_polyline('open-box',(26,14),(6,14),(6,42),(34,42),(34,28))
        self.add_line('shaft',(26,22),(42,6))
        self.add_polyline('arrow',(30,6),(42,6),(42,18))
        self.relate('connect','shaft','arrow')

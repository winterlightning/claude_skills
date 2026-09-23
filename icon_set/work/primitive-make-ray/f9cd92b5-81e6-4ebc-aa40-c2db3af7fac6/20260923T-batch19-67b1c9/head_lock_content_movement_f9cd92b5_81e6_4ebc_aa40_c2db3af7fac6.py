"""head lock content movement, re-authored as one complete SOLO48 composition.
Symbol plan is recorded in build(); paired shapes share dimensions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f9cd92b5-81e6-4ebc-aa40-c2db3af7fac6'
SOURCE_PATH = 'icon_set/work/todo-references/head lock content movement_f9cd92b5-81e6-4ebc-aa40-c2db3af7fac6.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'head-lock-content-movement'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('head lock content movement',)

    def circle(self,n,x,y,r):
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'a',n+'b',closed=True)

    def rounded(self,n,x,y,w,h,r):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for i in range(8):
            a,b=points[i],points[(i+1)%8]
            if i%2:self.add_arc(n+str(i),a,b,radius_x=r)
            else:self.add_line(n+str(i),a,b)
        self.add_contour(n,*(n+str(i) for i in range(8)),closed=True)

    def heart(self):
        # Paired nine-unit lobes and mirrored lower shoulders.
        self.add_arc('left-lobe',(24,15),(6,15),radius_x=9,sweep=False)
        self.add_arc('left-shoulder',(6,15),(10,25),radius_x=14,sweep=False)
        self.add_line('point-1',(10,25),(24,42))
        self.add_line('point-2',(24,42),(38,25))
        self.add_arc('right-shoulder',(38,25),(42,15),radius_x=14,sweep=False)
        self.add_arc('right-lobe',(42,15),(24,15),radius_x=9,sweep=False)
        self.add_contour('heart','left-lobe','left-shoulder','point-1','point-2','right-shoulder','right-lobe',closed=True)

    def build(self):
        # Tilted content slab above a separate head, with curved turn arrow.
        self.add_polyline('content',(6,22),(22,6),(28,12),(12,28),(6,22))
        self.circle('head',34,34,8)
        self.add_line('ray-left',(6,6),(11,11))
        self.add_line('ray-right',(22,24),(25,27))
        self.add_arc('turn',(42,22),(30,10),radius_x=12,sweep=False)
        self.add_polyline('arrow',(34,6),(30,10),(34,14))
        self.relate('connect','turn','arrow')

# Declared visible keyshape extremes: (4, 4, 44, 44).

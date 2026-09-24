"""A tilted content panel near a head with a curved turning arrow.
Plan: SQUARE separates the upper-left panel, lower-right head and upper-right turn arrow.
Reduction: Removed the lower motion ray and shortened the upper ray; moved the turning arrow away from the panel and head.
Construction: Supplied reference governs the composition; human-reference guidance inspected for the isolated head.
Layout: Deliberate diagonal arrangement. There is no torso, so no detached head-to-body gap applies."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f9cd92b5-81e6-4ebc-aa40-c2db3af7fac6'
SOURCE_PATH = 'pictographic-primitives/technology/head lock content movement_f9cd92b5-81e6-4ebc-aa40-c2db3af7fac6.svg'
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
        self.add_polyline('content',(6,23),(20,9),(26,15),(12,29),closed=True)
        self.circle('head',34,34,8)
        self.add_line('ray-left',(6,6),(8,8))
        self.add_arc('turn',(42,18),(34,10),radius_x=8,sweep=False)
        self.add_polyline('arrow',(38,6),(34,10),(38,14))
        self.relate('connect','turn','arrow')



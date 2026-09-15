"""Dog Catching Disc.

Plan: Right-facing raised dog head holds an oval disc at an exact mouth node; bent foreleg below. Intentional side-view asymmetry.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '655b22db-42de-59f5-ad65-7c9cf706dfcd'
SOURCE_PATH = 'pictographic-primitives/pets/dog play bring disc_655b22db-42de-59f5-ad65-7c9cf706dfcd.svg'
AUTHOR = 'gpt-6'

class DogCatchingDisc(Solo48):
    icon_id = 'dog-catching-disc'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('dog', 'disc', 'frisbee', 'fetch', 'play', 'catch', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        self.add_polyline('head',(42,18),(38,6),(34,14),(28,14),(22,20),(18,22))
        arc('disc-top-left',(6,30),(18,22),12,8)
        arc('disc-top-right',(18,22),(30,30),12,8)
        arc('disc-bottom',(30,30),(6,30),12,8)
        contour('disc','disc-top-left','disc-top-right','disc-bottom',closed=True)
        self.add_polyline('leg',(30,30),(34,34),(38,42))
        self.relate('connect','leg','disc')
        self.relate('connect','head','disc')

"""Dog Catching Disc.

Plan: Right-facing raised dog head holds an oval disc at an exact mouth node; bent foreleg below. Intentional side-view asymmetry.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bf29416e-316c-548b-9cc0-8b851d979c09'
SOURCE_PATH = 'pictographic-primitives/pets/dog_bf29416e-316c-548b-9cc0-8b851d979c09.svg'
AUTHOR = 'gpt-6'

class DogCatchingDiscRaisedHead(Solo48):
    icon_id = 'dog-catching-disc-raised-head'
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
        self.add_polyline('head',(42,18),(40,6),(36,14),(28,14),(22,20),(18,22))
        arc('disc-top-left',(6,30),(18,22),12,8)
        arc('disc-top-right',(18,22),(30,30),12,8)
        arc('disc-bottom',(30,30),(6,30),12,8)
        contour('disc','disc-top-left','disc-top-right','disc-bottom',closed=True)
        self.add_polyline('leg',(30,30),(34,34),(38,42))
        self.relate('connect','leg','disc')
        self.relate('connect','head','disc')
        self.relate('connect','head','disc')

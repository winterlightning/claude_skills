"""French Bulldog Head.

Plan: Large rounded upright bat ears and broad lower muzzle split by a center line; paired equal curves.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa674db0-c0e5-5143-91ef-ccf00700cb03'
SOURCE_PATH = 'pictographic-primitives/pets/french bulldog_aa674db0-c0e5-5143-91ef-ccf00700cb03.svg'
AUTHOR = 'gpt-6'

class FrenchBulldogHead(Solo48):
    icon_id = 'french-bulldog-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('dog', 'french-bulldog', 'frenchie', 'head', 'breed', 'bat-ears', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(p): return (2 * axis - p[0], p[1])
        arc('ear-left',(6,12),(18,12),6)
        line('ear-left-inner',(18,12),(18,20))
        line('forehead',(18,20),mirror((18,20)))
        line('ear-right-inner',mirror((18,20)),mirror((18,12)))
        arc('ear-right',mirror((18,12)),mirror((6,12)),6)
        line('ear-right-side',mirror((6,12)),mirror((6,24)))
        arc('jaw-right',mirror((6,24)),(24,42),18)
        arc('jaw-left',(24,42),(6,24),18)
        line('ear-left-side',(6,24),(6,12))
        contour('head','ear-left','ear-left-inner','forehead','ear-right-inner','ear-right','ear-right-side','jaw-right','jaw-left','ear-left-side',closed=True)
        line('muzzle',(24,32),(24,42))
        self.relate('connect','muzzle','head')

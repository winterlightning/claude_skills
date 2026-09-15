"""Scottish Fold Cat Face.

Plan: Round face with flat folded ears, two forehead stripes and one pair of attached whiskers; symmetric.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd294ce66-fca9-4ed0-b3fa-35f8ef9b43f3'
SOURCE_PATH = 'pictographic-primitives/pets/scottish fold_d294ce66-fca9-4ed0-b3fa-35f8ef9b43f3.svg'
AUTHOR = 'gpt-6'

class ScottishFoldCatFace(Solo48):
    icon_id = 'scottish-fold-cat-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('cat', 'scottish-fold', 'face', 'breed', 'folded-ears', 'whiskers', 'feline')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(p): return (2 * axis - p[0], p[1])
        self.add_polyline('upper',(6,24),(6,6),(14,6),(18,10),mirror((18,10)),mirror((14,6)),mirror((6,6)),mirror((6,24)))
        arc('right-jaw',mirror((6,24)),(24,42),18)
        arc('left-jaw',(24,42),(6,24),18)
        contour('jaw','right-jaw','left-jaw')
        self.relate('connect','upper','jaw')
        for i,x in enumerate((20,28)):line(f'stripe-{i}',(x,10),(x,18));self.relate('connect','upper',f'stripe-{i}')
        line('whisker-left',(6,24),(14,24))
        line('whisker-right',mirror((14,24)),mirror((6,24)))
        for w in ('whisker-left','whisker-right'):
         self.relate('connect','upper',w);self.relate('connect','jaw',w)

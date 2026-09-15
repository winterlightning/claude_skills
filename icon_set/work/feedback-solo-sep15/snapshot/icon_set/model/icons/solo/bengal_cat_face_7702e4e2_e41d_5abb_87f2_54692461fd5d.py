"""Bengal Cat Face.

Plan: Wide pointed ears and tapering cheek contour mirror around 24; low nose stays separate.
Keyshape centerline extremes: (6,6)-(42,42)
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7702e4e2-e41d-5abb-87f2-54692461fd5d'
SOURCE_PATH = 'pictographic-primitives/pets/bengal_7702e4e2-e41d-5abb-87f2-54692461fd5d.svg'
AUTHOR = 'gpt-6'

class BengalCatFace(Solo48):
    icon_id = 'bengal-cat-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('cat', 'bengal', 'face', 'breed', 'feline', 'pet', 'ears')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(point): return (2 * axis - point[0], point[1])
        self.add_polyline('upper',(6,24),(6,6),(18,14),mirror((18,14)),mirror((6,6)),mirror((6,24)))
        arc('cheek-right',mirror((6,24)),(24,42),18)
        arc('cheek-left',(24,42),(6,24),18)
        self.relate('connect','upper','cheek-right')
        self.relate('connect','upper','cheek-left')
        self.relate('connect','cheek-left','cheek-right')
        self.add_polyline('nose',(21,29),(24,32),mirror((21,29)))

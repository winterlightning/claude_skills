"""Chihuahua Head.

Plan: Mirror pair of very large pointed ears, narrow lower face and squared muzzle; no added facial features.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9582a217-8eaa-54f5-9d7b-c99178704cd9'
SOURCE_PATH = 'pictographic-primitives/pets/chihuahua_9582a217-8eaa-54f5-9d7b-c99178704cd9.svg'
AUTHOR = 'gpt-6'

class ChihuahuaHead(Solo48):
    icon_id = 'chihuahua-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('dog', 'chihuahua', 'head', 'breed', 'small-dog', 'ears', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis = 24
        def mirror(p): return (2 * axis - p[0], p[1])
        self.add_polyline('head',(6,6),(18,18),mirror((18,18)),mirror((6,6)),mirror((6,24)),mirror((14,30)),mirror((18,42)),(18,42),(14,30),(6,24),closed=True)

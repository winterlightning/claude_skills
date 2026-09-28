"""Corgi Head Silhouette.

Plan: Mirrored broad upright ears and widening neck; open lower outline preserves reference silhouette without added facial marks.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c75020d7-8516-4fa5-af3e-737a8f244554'
SOURCE_PATH = 'pictographic-primitives/pets/corgi_c75020d7-8516-4fa5-af3e-737a8f244554.svg'
AUTHOR = 'gpt-6'

class CorgiHeadSilhouette(Solo48):
    icon_id = 'corgi-head-silhouette'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    categories = ("pets", "primitives")
    aliases = ()
    keywords = ('dog', 'corgi', 'head', 'silhouette', 'breed', 'ears', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis = 24
        def mirror(p): return (2 * axis - p[0], p[1])
        line('neck-left',(6,42),(10,24))
        arc('ear-left',(10,24),(6,6),4,18)
        self.add_polyline('crown',(6,6),(18,14),mirror((18,14)),mirror((6,6)))
        arc('ear-right',mirror((6,6)),mirror((10,24)),4,18)
        line('neck-right',mirror((10,24)),mirror((6,42)))
        self.relate('connect','neck-left','ear-left')
        self.relate('connect','ear-left','crown')
        self.relate('connect','crown','ear-right')
        self.relate('connect','ear-right','neck-right')

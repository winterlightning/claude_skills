"""Rottweiler Head Outline.

Plan: Broad flat crown, hanging folded corner ears and long open cheek lines. Symmetric outline without facial detail.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6ea8228d-0d5b-43b9-b5b1-530b48dcdcfa'
SOURCE_PATH = 'pictographic-primitives/pets/rottweiller_6ea8228d-0d5b-43b9-b5b1-530b48dcdcfa.svg'
AUTHOR = 'gpt-6'

class RottweilerHeadOutline(Solo48):
    icon_id = 'rottweiler-head-outline'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('dog', 'rottweiler', 'head', 'breed', 'outline', 'ears', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(p): return (2 * axis - p[0], p[1])
        self.add_polyline('crown',(6,18),(10,6),mirror((10,6)),mirror((6,18)))
        arc('ear-right',mirror((6,18)),mirror((16,18)),5,6)
        arc('ear-left',(16,18),(6,18),5,6)
        self.relate('connect','crown','ear-left')
        self.relate('connect','crown','ear-right')
        self.add_polyline('cheek-left',(16,18),(10,32),(6,42))
        self.add_polyline('cheek-right',mirror((16,18)),mirror((10,32)),mirror((6,42)))
        self.relate('connect','ear-left','cheek-left')
        self.relate('connect','ear-right','cheek-right')

"""Bulldog Face.

Plan: Wide squarish head with folded ears and heavy paired jowls; centered nose, mirrored outline.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b82a8e4c-4496-539d-b448-cb99ae868dd5'
SOURCE_PATH = 'pictographic-primitives/pets/dog_b82a8e4c-4496-539d-b448-cb99ae868dd5.svg'
AUTHOR = 'gpt-6'

class BulldogFace(Solo48):
    icon_id = 'bulldog-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('dog', 'bulldog', 'face', 'breed', 'jowls', 'pet', 'english-bulldog')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(p): return (2 * axis - p[0], p[1])
        self.add_polyline('crown',(6,18),(10,6),(18,6),(22,10),mirror((22,10)),mirror((18,6)),mirror((10,6)),mirror((6,18)))
        arc('ear-right',mirror((6,18)),mirror((16,18)),5,4)
        arc('ear-left',(16,18),(6,18),5,4)
        self.relate('connect','crown','ear-left')
        self.relate('connect','crown','ear-right')
        line('cheek-left',(6,18),(6,30))
        line('cheek-right',mirror((6,30)),mirror((6,18)))
        arc('jowl-left',(6,30),(24,30),9,12,False)
        arc('jowl-right',(24,30),mirror((6,30)),9,12,False)
        contour('lower','cheek-left','jowl-left','jowl-right','cheek-right')
        for ear in ('ear-left','ear-right'):
            self.relate('connect','lower',ear)
        self.relate('connect','lower','crown')
        line('nose',(22,23),mirror((22,23)))
        line('stem',(24,23),(24,30))
        self.relate('connect','nose','stem')
        self.relate('connect','stem','lower')

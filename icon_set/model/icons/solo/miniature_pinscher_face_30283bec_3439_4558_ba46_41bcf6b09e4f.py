"""Miniature Pinscher Face.

Plan: Large rounded ears above a tapering narrow muzzle; symmetric forehead, dot eyes and minimal nose.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30283bec-3439-4558-ba46-41bcf6b09e4f'
SOURCE_PATH = 'pictographic-primitives/pets/miniature pinscher_30283bec-3439-4558-ba46-41bcf6b09e4f.svg'
AUTHOR = 'gpt-6'

class MiniaturePinscherFace(Solo48):
    icon_id = 'miniature-pinscher-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    categories = ("pets", "primitives")
    aliases = ()
    keywords = ('dog', 'miniature-pinscher', 'pinscher', 'face', 'breed', 'ears', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(p): return (2 * axis - p[0], p[1])
        arc('ear-left',(6,6),(10,22),4,16,False)
        self.add_polyline('forehead',(6,6),(18,14),mirror((18,14)),mirror((6,6)))
        arc('ear-right',mirror((10,22)),mirror((6,6)),4,16,False)
        self.add_polyline('jaw',(10,22),(10,30),(20,42),mirror((20,42)),mirror((10,30)),mirror((10,22)))
        for ear in ('ear-left','ear-right'):
         self.relate('connect',ear,'forehead')
         self.relate('connect',ear,'jaw')
        for i,x in enumerate((20,28)):self.add_dot(f'eye-{i}',(x,24))
        self.add_dot('nose',(24,33))

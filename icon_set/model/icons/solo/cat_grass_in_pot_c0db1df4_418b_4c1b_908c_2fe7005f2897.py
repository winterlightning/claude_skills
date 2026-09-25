"""Cat Grass in Pot.

Plan: Tapered pot owns three upright grass blades, mirrored fan and central blade; rim rendered as one line.
Keyshape centerline extremes: (8,4)-(40,44)
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c0db1df4-418b-4c1b-908c-2fe7005f2897'
SOURCE_PATH = 'pictographic-primitives/pets/cat grass 1_c0db1df4-418b-4c1b-908c-2fe7005f2897.svg'
AUTHOR = 'gpt-6'

class CatGrassInPot(Solo48):
    icon_id = 'cat-grass-in-pot'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('cat-grass', 'grass', 'pot', 'plant', 'cat', 'pet', 'greens')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(point): return (2 * axis - point[0], point[1])
        self.add_polyline('pot',(8,28),(14,44),mirror((14,44)),mirror((8,28)),mirror((16,28)),(24,28),(16,28),(8,28))
        for i,(x,top) in enumerate(((16,(12,6)),(24,(24,4)),(32,mirror((12,6))))):
         line(f'grass-{i}',top,(x,28))
         self.relate('connect','pot',f'grass-{i}')

"""Pet Carrier with Straps.

Plan: Body owns handle attachment and symmetric repeated straps.
Keyshape centerline extremes: (6,6)-(42,42)
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3a808f8d-c6c4-5793-9412-be443ff8dd99'
SOURCE_PATH = 'pictographic-primitives/pets/cat carrier_3a808f8d-c6c4-5793-9412-be443ff8dd99.svg'
AUTHOR = 'gpt-6'

class PetCarrierWithStraps(Solo48):
    icon_id = 'pet-carrier-with-straps'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('pet-carrier', 'carrier', 'crate', 'travel', 'cat', 'basket', 'transport')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(point): return (2 * axis - point[0], point[1])
        arc('handle',(16,14),mirror((16,14)),8)
        self.add_polyline('body',(16,14),(10,14),(6,42),mirror((6,42)),mirror((10,14)),mirror((16,14)),(16,14))
        self.relate('connect','handle','body')

        for i,x in enumerate((axis-8,axis+8)):
         line(f'strap-{i}',(x,14),(x,42))
         self.relate('connect','body',f'strap-{i}')

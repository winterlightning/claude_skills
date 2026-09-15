"""Dog Placing Paw on Hand.

Plan: Upper-right floppy dog head with offered forepaw resting on a broad open palm; finger detail reduced to one contour.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '511ea518-3b8b-552d-b9df-827c71ed2c6b'
SOURCE_PATH = 'pictographic-primitives/pets/dog training giving hand paw_511ea518-3b8b-552d-b9df-827c71ed2c6b.svg'
AUTHOR = 'gpt-6'

class DogPawOnHand(Solo48):
    icon_id = 'dog-paw-on-hand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('dog', 'paw', 'hand', 'shake', 'training', 'trick', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        arc('head',(26,18),(42,18),8,12)
        self.add_polyline('muzzle',(26,18),(18,20),(18,26),(28,28),(28,34),(20,34))
        line('back',(42,18),(42,34))
        self.relate('connect','head','muzzle')
        self.relate('connect','head','back')
        self.add_polyline('hand',(6,30),(12,30),(20,34),(32,34),(36,38),(32,42),(18,42),(6,36))
        self.relate('connect','muzzle','hand')

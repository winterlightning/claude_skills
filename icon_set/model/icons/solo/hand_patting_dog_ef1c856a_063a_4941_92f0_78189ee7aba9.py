"""Hand Patting Dog.

Plan: Left-facing pointed-ear dog with a simplified hand resting against the back of its head; two broad fingers.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef1c856a-063a-4941-92f0-78189ee7aba9'
SOURCE_PATH = 'pictographic-primitives/pets/dog side patting good_ef1c856a-063a-4941-92f0-78189ee7aba9.svg'
AUTHOR = 'gpt-6'

class HandPattingDog(Solo48):
    icon_id = 'hand-patting-dog'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    categories = ("pets", "primitives")
    aliases = ()
    keywords = ('dog', 'pat', 'hand', 'good-dog', 'praise', 'petting', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        self.add_polyline('head',(18,42),(16,26),(6,22),(6,16),(18,14),(24,6),(28,18),(34,22))
        self.add_polyline('hand',(42,18),(34,22),(26,30),(34,36),(42,28))
        self.add_polyline('fingers',(34,36),(34,42),(42,42))
        self.relate('connect','head','hand')
        self.relate('connect','hand','fingers')

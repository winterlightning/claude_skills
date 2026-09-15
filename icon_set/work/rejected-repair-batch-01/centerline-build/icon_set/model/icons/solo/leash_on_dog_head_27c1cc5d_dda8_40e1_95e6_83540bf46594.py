"""Leash on Dog Head.

Plan: Triangular handle at upper-left; long curved leash attaches to right-facing dog neck. Profile retains pointed ear and snout.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '27c1cc5d-dda8-40e1-95e6-83540bf46594'
SOURCE_PATH = 'pictographic-primitives/pets/dog leash_27c1cc5d-dda8-40e1-95e6-83540bf46594.svg'
AUTHOR = 'gpt-6'

class LeashOnDogHead(Solo48):
    icon_id = 'leash-on-dog-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('leash', 'dog', 'lead', 'walk', 'collar', 'handle', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        self.add_polyline('handle',(6,6),(22,6),(14,16),(6,6))
        line('lead',(14,16),(14,30))
        arc('lead-curve',(14,30),(26,42),12,sweep=False)
        line('lead-end',(26,42),(34,42))
        contour('leash','lead','lead-curve','lead-end')
        self.relate('connect','handle','leash')
        self.add_polyline('dog',(34,42),(34,32),(26,32),(26,24),(32,20),(32,14),(38,20),(42,30),(34,34))
        self.relate('connect','leash','dog')

"""Dog Wearing Muzzle.

Plan: Left-facing pointed-ear head with basket muzzle, one structural strap and leash below-right. Muzzle owns a wide opening.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c0f8a347-2fb8-5f5a-a745-e0b0e6b8be68'
SOURCE_PATH = 'pictographic-primitives/pets/dog mouth protection_c0f8a347-2fb8-5f5a-a745-e0b0e6b8be68.svg'
AUTHOR = 'gpt-6'

class DogWearingMuzzle(Solo48):
    icon_id = 'dog-wearing-muzzle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('dog', 'muzzle', 'safety', 'protection', 'leash', 'head', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        self.add_polyline('head',(42,34),(34,20),(32,6),(26,16),(18,6),(20,20),(14,24),(6,24))
        self.add_polyline('basket',(6,24),(8,36),(24,36),(28,24),(6,24))
        self.add_polyline('strap',(16,24),(16,36))
        self.relate('connect','basket','head')
        self.relate('connect','strap','basket')
        line('lead',(24,36),(28,42))
        self.relate('connect','lead','basket')

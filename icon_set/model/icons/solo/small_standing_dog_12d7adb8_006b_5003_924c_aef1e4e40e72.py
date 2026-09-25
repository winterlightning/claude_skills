"""Small Standing Dog.

Plan: Low standing dog, pointed ear, short tail and two readable legs; paired rear/front leg gaps.
Centerline extremes: (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '12d7adb8-006b-5003-924c-aef1e4e40e72'
SOURCE_PATH = 'pictographic-primitives/pets/dog small_12d7adb8-006b-5003-924c-aef1e4e40e72.svg'
AUTHOR = 'gpt-6'

class SmallStandingDog(Solo48):
    icon_id = 'small-standing-dog'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('dog', 'small-dog', 'standing', 'profile', 'puppy', 'pet', 'silhouette')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        self.add_polyline('outline',(4,30),(8,24),(26,24),(26,16),(32,8),(36,16),(44,20),(44,26),(36,28),(34,40),(26,40),(26,32),(16,32),(16,40),(8,40),(8,32),(4,30))

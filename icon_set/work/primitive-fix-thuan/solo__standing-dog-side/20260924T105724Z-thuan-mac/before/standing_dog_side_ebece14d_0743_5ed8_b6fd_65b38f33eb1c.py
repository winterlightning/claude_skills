"""Standing Dog.

Plan: Right-facing standing dog with rounded skull, projecting muzzle, raised tail and broad front/rear legs; reduce far legs.
Centerline extremes: (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ebece14d-0743-5ed8-b6fd-65b38f33eb1c'
SOURCE_PATH = 'pictographic-primitives/pets/dog_ebece14d-0743-5ed8-b6fd-65b38f33eb1c.svg'
AUTHOR = 'gpt-6'

class StandingDogSide(Solo48):
    icon_id = 'standing-dog-side'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('dog', 'standing', 'profile', 'pet', 'puppy', 'silhouette', 'canine')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        line('back',(10,20),(28,20))
        arc('head',(28,20),(40,20),6,12)
        self.add_polyline('front',(40,20),(44,20),(44,28),(36,28),(36,40),(28,40),(28,30),(18,30),(18,40),(10,40),(10,20))
        self.relate('connect','head','front')
        self.relate('connect','back','head')
        self.relate('connect','back','front')
        arc('tail',(10,20),(4,8),6,12)
        self.relate('connect','tail','back')
        self.relate('connect','tail','front')

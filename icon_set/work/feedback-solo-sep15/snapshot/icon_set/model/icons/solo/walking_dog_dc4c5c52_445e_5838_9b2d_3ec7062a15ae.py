"""Walking Dog.

Plan: Level back, floppy head, raised tail and one lifted front leg; legs reduced to three clear strokes.
Centerline extremes: (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dc4c5c52-445e-5838-9b2d-3ec7062a15ae'
SOURCE_PATH = 'pictographic-primitives/pets/dog walk_dc4c5c52-445e-5838-9b2d-3ec7062a15ae.svg'
AUTHOR = 'gpt-6'

class WalkingDog(Solo48):
    icon_id = 'walking-dog'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('dog', 'walk', 'walking', 'profile', 'pet', 'stride', 'exercise')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        line('back',(10,20),(28,20))
        arc('head',(28,20),(40,20),6,12)
        line('snout',(40,20),(44,20))
        arc('chin',(44,20),(36,28),8)
        line('front-leg',(36,28),(34,40))
        line('paw',(34,40),(42,40))
        contour('dog','back','head','snout','chin','front-leg','paw')
        arc('tail',(10,20),(4,8),6,12)
        self.relate('connect','tail','dog')
        self.add_polyline('rear-leg',(10,20),(10,32),(6,40),(14,40))
        self.relate('connect','rear-leg','dog')
        self.relate('connect','rear-leg','tail')
        self.add_polyline('stride',(24,29),(20,34),(24,40))

"""Sitting Dog Profile.

Plan: Right-facing upright dog, pointed ear, straight chest, round haunch and raised tail; shared tail attachment.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a440cb03-a795-5a15-9bc2-11c255685591'
SOURCE_PATH = 'pictographic-primitives/pets/dog sit_a440cb03-a795-5a15-9bc2-11c255685591.svg'
AUTHOR = 'gpt-6'

class SittingDogProfile(Solo48):
    icon_id = 'sitting-dog-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('dog', 'sit', 'sitting', 'profile', 'training', 'pet', 'obedient')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        self.add_polyline('head',(24,22),(28,14),(28,6),(34,14),(42,18),(42,24),(34,26),(34,42))
        arc('haunch-top',(24,22),(16,32),8,10,False)
        arc('haunch-bottom',(16,32),(24,42),8,10,False)
        line('base',(24,42),(34,42))
        contour('body','haunch-top','haunch-bottom','base')
        self.relate('connect','head','body')
        arc('tail',(16,32),(6,16),10,16)
        self.relate('connect','tail','body')

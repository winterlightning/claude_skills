"""Sitting Dog with Tucked Paw.

Plan: Seated dog with a small angular tucked paw in the base; raised tail meets haunch.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd0aa2ec-ca07-513d-88f0-0566b2c9e3a4'
SOURCE_PATH = 'pictographic-primitives/pets/dog_cd0aa2ec-ca07-513d-88f0-0566b2c9e3a4.svg'
AUTHOR = 'gpt-6'

class SittingDogTuckedPaw(Solo48):
    icon_id = 'sitting-dog-tucked-paw'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('dog', 'sitting', 'profile', 'silhouette', 'pet', 'paw', 'obedient')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        self.add_polyline('head',(24,22),(28,14),(28,6),(34,14),(42,18),(42,24),(34,26),(34,42))
        arc('haunch-top',(24,22),(16,32),8,10,False)
        arc('haunch-bottom',(16,32),(24,42),8,10,False)
        line('base',(24,42),(30,36))
        line('paw',(30,36),(34,42))
        contour('body','haunch-top','haunch-bottom','base','paw')
        self.relate('connect','head','body')
        arc('tail',(16,32),(6,16),10,16)
        self.relate('connect','tail','body')

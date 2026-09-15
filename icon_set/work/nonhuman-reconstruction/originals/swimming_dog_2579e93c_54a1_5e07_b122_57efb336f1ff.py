"""Swimming Dog.

Plan: Left-facing floppy head and level back above a repeated wave line; no submerged legs.
Centerline extremes: (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2579e93c-54a1-5e07-b122-57efb336f1ff'
SOURCE_PATH = 'pictographic-primitives/pets/dog swimming_2579e93c-54a1-5e07-b122-57efb336f1ff.svg'
AUTHOR = 'gpt-6'

class SwimmingDog(Solo48):
    icon_id = 'swimming-dog'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('dog', 'swimming', 'water', 'waves', 'pet', 'summer', 'paddle')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        arc('head',(12,20),(28,20),8,12)
        self.add_polyline('muzzle',(12,20),(4,20),(4,26),(14,27))
        line('back',(28,20),(38,20))
        arc('rump',(38,20),(44,26),6)
        self.relate('connect','head','muzzle')
        self.relate('connect','head','back')
        self.relate('connect','back','rump')
        for i in range(4):arc(f'wave-{i}',(4+10*i,36),(14+10*i,36),5,4,False)
        contour('water',*(f'wave-{i}' for i in range(4)))

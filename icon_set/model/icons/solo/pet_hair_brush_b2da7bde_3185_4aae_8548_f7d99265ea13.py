"""Pet Hair Brush.

Plan: Diagonal rounded brush body with a lower handle and three equally spaced projecting bristles; repeated attachment nodes.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b2da7bde-3185-4aae-8548-f7d99265ea13'
SOURCE_PATH = 'pictographic-primitives/pets/pets hair brush_b2da7bde-3185-4aae-8548-f7d99265ea13.svg'
AUTHOR = 'gpt-6'

class PetHairBrush(Solo48):
    icon_id = 'pet-hair-brush'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    categories = ("pets", "primitives")
    aliases = ()
    keywords = ('brush', 'hair-brush', 'grooming', 'comb', 'fur', 'pet', 'bristles')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        self.add_polyline('spine',(6,36),(18,24),(24,18),(30,12),(36,6))
        arc('head-end',(36,6),(42,12),6)
        line('lower-edge',(42,12),(12,42))
        arc('handle-end',(12,42),(6,36),6)
        self.relate('connect','spine','head-end')
        self.relate('connect','head-end','lower-edge')
        self.relate('connect','lower-edge','handle-end')
        self.relate('connect','handle-end','spine')
        for i in range(3):
         x,y=18+6*i,24-6*i;line(f'bristle-{i}',(x-6,y-6),(x,y));self.relate('connect','spine',f'bristle-{i}')

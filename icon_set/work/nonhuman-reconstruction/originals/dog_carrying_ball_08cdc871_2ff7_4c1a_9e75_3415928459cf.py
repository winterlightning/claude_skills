"""Dog Carrying Ball.

Plan: Left-facing carrying dog head at upper-right, large ball at left and bent front leg below. Ball held at an exact mouth attachment.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '08cdc871-2ff7-4c1a-9e75-3415928459cf'
SOURCE_PATH = 'pictographic-primitives/pets/dog carrying bring play ball_08cdc871-2ff7-4c1a-9e75-3415928459cf.svg'
AUTHOR = 'gpt-6'

class DogCarryingBall(Solo48):
    icon_id = 'dog-carrying-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('dog', 'ball', 'fetch', 'play', 'carrying', 'training', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        self.add_polyline('head',(42,18),(40,6),(34,14),(28,14),(22,18),(22,24))
        arc('ball-top',(6,24),(22,24),8)
        arc('ball-bottom',(22,24),(6,24),8)
        contour('ball','ball-top','ball-bottom',closed=True)
        self.add_polyline('mouth-leg',(22,24),(30,24),(30,32),(22,38),(30,42),(36,36),(42,42))
        self.relate('connect','ball','mouth-leg')
        self.relate('connect','head','ball')
        self.relate('connect','head','mouth-leg')

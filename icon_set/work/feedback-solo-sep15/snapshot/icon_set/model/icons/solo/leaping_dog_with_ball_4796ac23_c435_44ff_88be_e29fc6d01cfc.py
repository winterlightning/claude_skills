"""Leaping Dog with Ball.

Plan: Diagonal leaping dog gesture, pointed ear and projecting snout; detached ball below muzzle and trailing legs at left.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4796ac23-c435-44ff-88be-e29fc6d01cfc'
SOURCE_PATH = 'pictographic-primitives/pets/dog bring ball training_4796ac23-c435-44ff-88be-e29fc6d01cfc.svg'
AUTHOR = 'gpt-6'

class LeapingDogWithBall(Solo48):
    icon_id = 'leaping-dog-with-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('dog', 'fetch', 'ball', 'training', 'leaping', 'play', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(p): return (2 * axis - p[0], p[1])
        self.add_polyline('dog',(6,34),(18,30),(28,16),(30,6),(36,12),(42,12),(42,20),(32,24),(32,42))
        self.add_polyline('hindleg',(18,30),(20,38),(12,42))
        self.relate('connect','dog','hindleg')
        arc('ball-right',(12,8),(12,20),6)
        arc('ball-left',(12,20),(12,8),6)
        contour('ball','ball-right','ball-left',closed=True)

"""Dog Reaching for Ball.

Plan: Dog rises toward a detached ball above-left, floppy head lifted and foreleg raised; long sloped right edge.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f5e7c3d9-93a4-51aa-af25-f4dfca60a44e'
SOURCE_PATH = 'pictographic-primitives/pets/dog playing ball_f5e7c3d9-93a4-51aa-af25-f4dfca60a44e.svg'
AUTHOR = 'gpt-6'

class DogReachingForBall(Solo48):
    icon_id = 'dog-reaching-for-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    categories = ("pets", "primitives")
    aliases = ()
    keywords = ('dog', 'ball', 'play', 'jump', 'fetch', 'training', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        arc('ball-right',(10,6),(10,14),4)
        arc('ball-left',(10,14),(10,6),4)
        contour('ball','ball-right','ball-left',closed=True)
        self.add_polyline('muzzle',(24,26),(20,20),(28,18))
        arc('head',(28,18),(40,18),6,8)
        line('back',(40,18),(42,42))
        self.relate('connect','head','muzzle')
        self.relate('connect','head','back')
        self.add_polyline('paw',(6,26),(16,34),(26,36),(28,42))

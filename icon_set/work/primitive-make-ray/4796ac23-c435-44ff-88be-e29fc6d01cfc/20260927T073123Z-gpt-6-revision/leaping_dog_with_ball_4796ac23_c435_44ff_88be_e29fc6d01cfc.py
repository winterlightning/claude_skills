"""Leaping Dog with Ball.

Plan: Diagonal leaping dog gesture, pointed ear and projecting snout; detached ball below muzzle and trailing legs at left.
Centerline extremes: (6,6)-(42,42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4796ac23-c435-44ff-88be-e29fc6d01cfc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__leaping-dog-with-ball/20260927T072903Z-thuan-mac-1/reference/dog bring ball training_4796ac23-c435-44ff-88be-e29fc6d01cfc.svg'
AUTHOR = "gpt-6"

class LeapingDogWithBall(Solo48):
    icon_id = 'leaping-dog-with-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    categories = ("pets", "primitives")
    aliases = ()
    keywords = ('dog', 'fetch', 'ball', 'training', 'leaping', 'play', 'pet')

    def build(self):
        # Dog facing the ball: extended muzzle, pointed ear, bounding body and legs.
        self.add_polyline('dog-top',(6,18),(17,18),(22,15),(29,15),(34,6),(40,14),(39,25),(42,34),(42,42))
        self.add_polyline('dog-low',(6,18),(8,27),(17,27),(22,29),(29,27),(34,34),(25,40))
        self.add_line('rear-leg',(34,34),(25,42))
        self.relate('connect','dog-top','dog-low')
        self.relate('connect','dog-low','rear-leg')
        self.add_arc('ball-top',(9,39),(15,39),radius_x=3)
        self.add_arc('ball-bottom',(15,39),(9,39),radius_x=3)
        self.add_contour('ball','ball-top','ball-bottom',closed=True)

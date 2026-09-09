# Variant of penguin-looking-down; parent file remains unchanged.
'A left-facing penguin looking down, with a rounded belly, compact downward bill and single curved flipper. VRECT_L extremes (8,2)-(40,46) retain upright proportions. The narrow parent neck-like body is replaced by a full torso. Lucide bird informs the coherent contour and dot eye. Side-view asymmetry is intentional.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9ca363f4-f61f-5da3-a3be-41fa52d1fa3a'
SOURCE_PATH = 'pictographic-primitives/animals/penguin mother_9ca363f4-f61f-5da3-a3be-41fa52d1fa3a.svg'
AUTHOR = 'gpt-6'

class PenguinLookingDownVariant2(Solo48):
    icon_id = 'penguin-looking-down-v2'
    variant_of = 'penguin-looking-down'
    variant_label = 'Clear left-facing penguin'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('penguin', 'bending', 'looking', 'down', 'bird', 'antarctic', 'nurture', 'care')

    def build(self) -> None:
        # VRECT_L centerlines (8,2)-(40,46); head bows to the left.
        self.add_arc('crown', (12, 15), (24, 2), radius_x=12, radius_y=13, sweep=True)
        self.add_arc('head-back', (24, 2), (36, 14), radius_x=12, sweep=True)
        self.add_arc('back', (36, 14), (40, 34), radius_x=52, sweep=True)
        self.add_arc('rump', (40, 34), (28, 46), radius_x=12, sweep=True)
        self.add_line('base', (28, 46), (18, 46))
        self.add_arc('belly', (18, 46), (15, 24), radius_x=12, radius_y=26, sweep=True)
        self.add_line('beak-under', (15, 24), (8, 25))
        self.add_line('beak-top', (8, 25), (12, 15))
        self.add_contour('outline', 'crown', 'head-back', 'back', 'rump', 'base', 'belly', 'beak-under', 'beak-top', closed=True)
        self.add_dot('eye', (22, 13))
        self.add_arc('flipper', (29, 23), (26, 36), radius_x=20, sweep=True)

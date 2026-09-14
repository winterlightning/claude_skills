"""Wide face with two eyes, three-point crown and long hair. Rounded cheeks replace the narrow featureless oval. Bilateral symmetry.
SQUARE centerline extremes (6,6)-(42,42); stroke 4 on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '00eb0d5d-7557-4801-bb6f-304ff4b914ce'
SOURCE_PATH = 'pictographic-primitives/work/workflow manager female crown_00eb0d5d-7557-4801-bb6f-304ff4b914ce.svg'
AUTHOR = 'gpt-6'

class WomanWearingCrownVariant3(Solo48):
    icon_id = 'woman-wearing-crown-v3'
    variant_of = 'woman-wearing-crown-v2'
    variant_label = 'Recognizable hands, seated laptop user and crowned face'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/work'
    aliases = ()
    keywords = ('woman', 'crown', 'queen', 'leader', 'head', 'royalty')

    def build(self) -> None:
        self.add_polyline('crown', (9, 20), (8, 6), (18, 12), (24, 6), (30, 12), (40, 6), (39, 20), closed=True)
        self.add_arc('face', (39, 20), (9, 20), radius_x=15, radius_y=20, sweep=True, large_arc=False)
        self.relate("connect", 'face', 'crown')
        self.add_arc('hair-left-top', (9, 20), (6, 23), radius_x=3, radius_y=3, sweep=False, large_arc=False)
        self.add_line('hair-left', (6, 23), (6, 42))
        self.relate("connect", 'hair-left-top', 'hair-left')
        self.add_arc('hair-right-top', (39, 20), (42, 23), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('hair-right', (42, 23), (42, 42))
        self.relate("connect", 'hair-right-top', 'hair-right')
        self.relate("connect", 'hair-left-top', 'crown')
        self.relate("connect", 'hair-left-top', 'face')
        self.relate("connect", 'hair-right-top', 'crown')
        self.relate("connect", 'hair-right-top', 'face')
        self.add_dot('eye-left', (20, 29))
        self.add_dot('eye-right', (28, 29))

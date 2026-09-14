# Independent revision; parent models preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9c25c01a-0cb7-5bcc-be3b-bc55d5411b62'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird owl_9c25c01a-0cb7-5bcc-be3b-bc55d5411b62.svg'
AUTHOR = 'gpt-6'

class OwlHeadVariant3(Solo48):
    icon_id = 'owl-head-v3'
    variant_of = 'owl-head'
    variant_label = 'Exact keyshape envelope and clear spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/birds'
    aliases = ()
    keywords = ('owl', 'head', 'horned', 'ears', 'beak', 'night', 'bird', 'minimal')

    def build(self) -> None:
        self.add_line('ear-left', (6, 6), (14, 13))
        self.add_arc('crown', (14, 13), (34, 13), radius_x=22, radius_y=12, sweep=True)
        self.add_line('ear-right', (34, 13), (42, 6))
        self.add_arc('brow-right', (42, 6), (34, 23), radius_x=24, radius_y=24, sweep=True)
        self.add_arc('cheek-right', (34, 23), (24, 31), radius_x=20, radius_y=20, sweep=False)
        self.add_arc('cheek-left', (24, 31), (14, 23), radius_x=20, radius_y=20, sweep=False)
        self.add_arc('brow-left', (14, 23), (6, 6), radius_x=24, radius_y=24, sweep=True)
        self.add_contour('brows', 'ear-left', 'crown', 'ear-right', 'brow-right', 'cheek-right', 'cheek-left', 'brow-left', closed=True)
        self.add_arc('face-left', (14, 23), (8, 38), radius_x=14, radius_y=14, sweep=False)
        self.add_arc('face-right', (34, 23), (40, 38), radius_x=14, radius_y=14, sweep=True)
        self.add_line('beak-a', (24, 31), (28, 37))
        self.add_line('beak-b', (28, 37), (24, 42))
        self.add_line('beak-c', (24, 42), (20, 37))
        self.add_line('beak-d', (20, 37), (24, 31))
        self.add_contour('beak', 'beak-a', 'beak-b', 'beak-c', 'beak-d', closed=True)
        self.relate('connect', 'brows', 'face-left')
        self.relate('connect', 'brows', 'face-right')
        self.relate('connect', 'brows', 'beak')

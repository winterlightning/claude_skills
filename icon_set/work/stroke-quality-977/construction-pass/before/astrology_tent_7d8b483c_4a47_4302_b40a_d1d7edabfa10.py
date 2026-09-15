"""Astrology tent (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7d8b483c-4a47-4302-b40a-d1d7edabfa10'
SOURCE_PATH = 'pictographic-primitives/arrows/astrology tent_7d8b483c-4a47-4302-b40a-d1d7edabfa10.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class AstrologyTent(Solo48):
    icon_id = 'astrology-tent'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('astrology', 'tent', 'arrows')

    def build(self):
        self.add_line('e0', (4, 40), (44, 40))
        self.add_line('e1', (44, 40), (24, 8))
        self.add_line('e2', (24, 8), (4, 40))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)

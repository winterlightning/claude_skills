"""three-dots: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '12eb4663-24d4-4740-956a-57124928664f'
SOURCE_PATH = 'pictographic-primitives/state/three dots_12eb4663-24d4-4740-956a-57124928664f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class ThreeDots(Solo48):
    icon_id = 'three-dots'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('three', 'dots', 'state')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('frame-0', (8, 4), (40, 4))
        self.add_line('frame-2', (40, 4), (40, 44))
        self.add_line('frame-4', (40, 44), (8, 44))
        self.add_line('frame-6', (8, 44), (8, 4))
        self.add_line('dot-13', (24, 13), (24, 13))
        self.add_line('dot-24', (24, 24), (24, 24))
        self.add_line('dot-35', (24, 35), (24, 35))
        self.add_contour('frame', 'frame-0', 'frame-2', 'frame-4', 'frame-6', closed=True)

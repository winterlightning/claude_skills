"""ranking ribbon: repaired SOLO48 composition.
Plan: Mirrored alternating star points.
Keyshape: HRECT_L reserves ribbon width and room above it for the star.
Reduction: Fold seams removed; ribbon is a single notched band, separated from the star to avoid crowded crossings.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3792f25a-9089-4cd6-9389-b22b47f0380b'
SOURCE_PATH = 'pictographic-primitives/rewards/ranking ribbon_3792f25a-9089-4cd6-9389-b22b47f0380b.svg'
AUTHOR = "gpt-6"
CONSTRUCTION_REFERENCES = 'star'

class Drawing(Solo48):
    icon_id = 'ranking-ribbon'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('ranking', 'ribbon')

    def build(self):
        axis = 24
        self.add_polyline('star', (axis, 8), (27, 13), (34, 14), (29, 18), (30, 24), (axis, 21), (18, 24), (19, 18), (14, 14), (21, 13), closed=True)
        self.add_polyline('ribbon', (4, 32), (44, 32), (40, 36), (44, 40), (4, 40), (8, 36), closed=True)

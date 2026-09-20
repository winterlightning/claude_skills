# Independent container symbol; edit separately from linked side sub-icon.
"""Smiling Face: A round face contains two short vertical eyes above a broad upward-curving smile. The features are centred within the circular head and form a balanced, open expression.

Construction: Circular face, paired short eyes and shallow elliptical smile centred on x16.
Keyshape: CIRCLE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '26f40b93-a3b7-419f-a55b-3b6e5693c80a'
SOURCE_PATH = 'pictographic-primitives/state/circle smiley face_26f40b93-a3b7-419f-a55b-3b6e5693c80a.svg'
AUTHOR = 'gpt-6'

class SmilingFaceSubContainerSymbol(Sub32):
    icon_id = 'smiling-face-sub-symbol'
    variant_of = 'smiling-face-sub'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/smiling-face-sub'
    counterpart_icon_id = 'smiling-face-sub'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('smiling', 'face', 'round', 'contains', 'short', 'vertical', 'eyes', 'broad')

    def build(self):

        def circle(name, cx, cy, radius):
            self.add_arc(name + '-top', (cx - radius, cy), (cx + radius, cy), radius_x=radius)
            self.add_arc(name + '-bottom', (cx + radius, cy), (cx - radius, cy), radius_x=radius)
            self.add_contour(name, name + '-top', name + '-bottom', closed=True)
        circle('face', 16, 16, 14)
        for x in (10, 22):
            self.add_line(f'eye-{x}', (x, 11), (x, 13))
        self.add_arc('smile', (11, 20), (21, 20), radius_x=5, radius_y=3, sweep=False)

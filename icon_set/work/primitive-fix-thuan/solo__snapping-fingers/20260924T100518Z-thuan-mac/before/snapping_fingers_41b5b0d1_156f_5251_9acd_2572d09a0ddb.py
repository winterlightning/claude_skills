# Repair: Widen the folded thumb within the snapping gesture.
"""An angled hand extends a long finger toward the upper-right while the thumb rises at the left. The remaining fingers curl into the palm beneath three short snapping accent strokes.

Construction: A long diagonal finger extends from a curled fist with two emphasis rays. Bounds (6,6)-(42,42).
Lucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '41b5b0d1-156f-5251-9acd-2572d09a0ddb'
SOURCE_PATH = 'pictographic-primitives/wayfinding/hand snapping finger_41b5b0d1-156f-5251-9acd-2572d09a0ddb.svg'
AUTHOR = 'gpt-6'

class SnappingFingers(Solo48):
    icon_id = 'snapping-fingers'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('hand', 'snap', 'fingers', 'gesture', 'motion', 'thumb')

    def build(self):
        self.add_line('hand-1', (8, 32), (12, 20))
        self.add_line('hand-2', (12, 20), (21, 22))
        self.add_line('hand-3', (21, 22), (19, 30))
        self.add_line('hand-4', (19, 30), (34, 12))
        self.add_line('hand-5', (34, 12), (42, 12))
        self.add_line('hand-6', (42, 12), (42, 18))
        self.add_line('hand-7', (42, 18), (30, 30))
        self.add_line('hand-8', (30, 30), (34, 34))
        self.add_line('hand-9', (34, 34), (26, 42))
        self.add_line('hand-10', (26, 42), (16, 42))
        self.add_line('hand-11', (16, 42), (8, 32))
        self.add_line('hand-12', (8, 32), (8, 32))
        self.add_line('ray-one', (18, 6), (18, 10))
        self.add_line('ray-two', (6, 6), (8, 8))
        self.add_contour('hand', 'hand-1', 'hand-2', 'hand-3', 'hand-4', 'hand-5', 'hand-6', 'hand-7', 'hand-8', 'hand-9', 'hand-10', 'hand-11', 'hand-12', closed=True)

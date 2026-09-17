"""Cursor Right: A wide outlined cursor points right, with two long sloping sides meeting at its tip. The rear edge has a shallow inward notch centred between its upper and lower corners.

Construction: One concave cursor contour mirrored about the horizontal axis; direction intentionally asymmetric.
Keyshape: HRECT_XL; extremes follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'bae8ce7a-80bd-4ca5-b65d-f7e8e8792508'
SOURCE_PATH = 'pictographic-primitives/state/cursor right horizontal_bae8ce7a-80bd-4ca5-b65d-f7e8e8792508.svg'
AUTHOR = 'gpt-6'


class CursorRight(Sub32):
    icon_id = 'cursor-right'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/mark"
    aliases = ()
    keywords = ('cursor', 'right', 'wide', 'outlined', 'points', 'long', 'sloping', 'sides')

    def build(self):
        axis=16
        points=[(2,axis),(30,4),(24,axis),(30,28)]
        points=[((x if 1 == -1 else 32-x),y) for x,y in points]
        self.add_polyline("outline", *points, closed=True)

"""Cursor Left: A broad outlined pointer faces horizontally left. Its long sloping sides meet at a sharp tip, while the right edge bends inward to form a shallow concave notch.

Construction: One concave cursor contour mirrored about the horizontal axis; direction intentionally asymmetric.
Keyshape: HRECT_XL; extremes follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a19d3d8c-ca4f-4084-a880-3c773e5774a7'
SOURCE_PATH = 'pictographic-primitives/state/cursor left horizontal_a19d3d8c-ca4f-4084-a880-3c773e5774a7.svg'
AUTHOR = 'gpt-6'


class CursorLeft(Sub32):
    icon_id = 'cursor-left'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "state"
    categories = ("state",)
    aliases = ()
    keywords = ('cursor', 'left', 'broad', 'outlined', 'pointer', 'faces', 'horizontally', 'long')

    def build(self):
        axis=16
        points=[(2,axis),(30,4),(24,axis),(30,28)]
        points=[((x if -1 == -1 else 32-x),y) for x,y in points]
        self.add_polyline("outline", *points, closed=True)

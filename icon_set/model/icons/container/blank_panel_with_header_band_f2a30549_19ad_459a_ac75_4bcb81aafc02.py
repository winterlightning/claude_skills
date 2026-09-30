"""An empty upright application panel with one shallow header band.
VRECT_XL gives exact centerline extremes (6,2)-(58,62).
Owner: mirrored rounded enclosure, radius 6, with a horizontal header at y=18.
The side rails split at the two true divider attachments. No source details omitted.
Lucide panels-top-left original and atoms inform quarter-circle corners and divider.
Preserves the source's recorded user choice of container family.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (blank-panel-with-header-band VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = 'f2a30549-19ad-459a-ac75-4bcb81aafc02'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/remnant_f2a30549-19ad-459a-ac75-4bcb81aafc02.svg'
AUTHOR = 'claude-opus-5-5'


class Drawing(Container64):
    icon_id = 'blank-panel-with-header-band'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('Application Window with Top Header',)
    keywords = ('panel', 'header', 'card', 'frame', 'blank', 'layout')

    def build(self) -> None:
        self.add_line('frame-0', (16, 4), (48, 4))
        self.add_arc('frame-1', (48, 4), (54, 10), radius_x=6)
        self.add_line('frame-2', (54, 10), (54, 19))
        self.add_line('frame-3', (54, 19), (54, 54))
        self.add_arc('frame-4', (54, 54), (48, 60), radius_x=6)
        self.add_line('frame-5', (48, 60), (16, 60))
        self.add_arc('frame-6', (16, 60), (10, 54), radius_x=6)
        self.add_line('frame-7', (10, 54), (10, 19))
        self.add_line('frame-8', (10, 19), (10, 10))
        self.add_arc('frame-9', (10, 10), (16, 4), radius_x=6)
        self.add_line('header', (10, 19), (54, 19))
        self.add_contour('frame', 'frame-0', 'frame-1', 'frame-2', 'frame-3', 'frame-4', 'frame-5', 'frame-6', 'frame-7', 'frame-8', 'frame-9', closed=True)
        self.relate('connect', 'header', 'frame')

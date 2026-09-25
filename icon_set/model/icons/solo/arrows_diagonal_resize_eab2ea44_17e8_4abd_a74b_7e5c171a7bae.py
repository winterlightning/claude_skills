"""Diagonal Resize Arrows. Preserves two parallel opposing shafts with enough lateral separation; a single shared arrow was not substituted.

VRECT_L visible extremes (6, 2, 42, 46); centerlines (8, 4, 40, 44).
Lucide rotate-cw and undo-2: coherent arcs, open arrowheads and explicit shaft joins.
Mirrored subjects use paired coordinates; directional parts preserve their
intentional asymmetry. Geometry is authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'eab2ea44-17e8-4abd-a74b-7e5c171a7bae'
SOURCE_PATH = 'pictographic-primitives/symbol/arrows left right 1_eab2ea44-17e8-4abd-a74b-7e5c171a7bae.svg'
AUTHOR = 'gpt-6'

class ArrowsDiagonalResize(Solo48):
    icon_id = 'arrows-diagonal-resize'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('resize', 'expand', 'diagonal', 'arrows', 'scale', 'fullscreen', 'stretch', 'direction')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_line('ne-shaft', (8, 28), (32, 4))
        self.add_polyline('ne-head', (20, 4), (32, 4), (32, 16))
        self.relate('connect', 'ne-shaft', 'ne-head')
        self.add_line('sw-shaft', (40, 20), (16, 44))
        self.add_polyline('sw-head', (16, 32), (16, 44), (28, 44))
        self.relate('connect', 'sw-shaft', 'sw-head')

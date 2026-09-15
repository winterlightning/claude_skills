"""Arrows Pointing to Centre. Retains all identifying parts, reconstructed on the integer grid.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Lucide rotate-cw and undo-2: coherent arcs, open arrowheads and explicit shaft joins.
Mirrored subjects use paired coordinates; directional parts preserve their
intentional asymmetry. Geometry is authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fcb9a9f7-cbcc-4a2d-a0b4-8129e68d2831'
SOURCE_PATH = 'pictographic-primitives/symbol/arrows pointing to center_fcb9a9f7-cbcc-4a2d-a0b4-8129e68d2831.svg'
AUTHOR = 'gpt-6'


class ArrowsPointingToCenter(Solo48):
    icon_id = 'arrows-pointing-to-center'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('collapse', 'minimize', 'shrink', 'arrows', 'center', 'compress', 'exit-fullscreen', 'inward')

    def build(self) -> None:
        self.add_line('shaft-0', (6, 6), (18, 18))
        self.add_polyline('head-0', (10, 18), (18, 18), (18, 10))
        self.relate("connect", 'shaft-0', 'head-0')
        self.add_line('shaft-1', (42, 6), (30, 18))
        self.add_polyline('head-1', (38, 18), (30, 18), (30, 10))
        self.relate("connect", 'shaft-1', 'head-1')
        self.add_line('shaft-2', (6, 42), (18, 30))
        self.add_polyline('head-2', (10, 30), (18, 30), (18, 38))
        self.relate("connect", 'shaft-2', 'head-2')
        self.add_line('shaft-3', (42, 42), (30, 30))
        self.add_polyline('head-3', (38, 30), (30, 30), (30, 38))
        self.relate("connect", 'shaft-3', 'head-3')

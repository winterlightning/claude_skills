"""Diagonal notched RAM board; square extremes (2,2)-(46,46). Lucide memory-stick informs minimal chips. Middle circuit bracket omitted for clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6f237c30-c7db-4dfc-91c5-5d21fb166711'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/computer ram_6f237c30-c7db-4dfc-91c5-5d21fb166711.svg'
AUTHOR = 'astra-chatgpt'

class MemoryModuleWithNotch(Solo48):
    icon_id = 'memory-module-with-notch'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('ram', 'memory', 'module', 'dimm', 'chip', 'hardware', 'computer', 'upgrade')

    def build(self) -> None:
        self.add_line('board-start', (2, 32), (14, 20))
        self.add_arc('notch', (14, 20), (20, 14), radius_x=5, radius_y=5, sweep=False)
        self.add_line('board-rest-1', (20, 14), (32, 2))
        self.add_line('board-rest-2', (32, 2), (46, 16))
        self.add_line('board-rest-3', (46, 16), (16, 46))
        self.add_line('board-rest-4', (16, 46), (2, 32))
        self.add_contour('board', 'board-start', 'notch', 'board-rest-1', 'board-rest-2', 'board-rest-3', 'board-rest-4', closed=True)
        self.add_polyline('chip-low', (11, 32), (16, 27), (21, 32), (16, 37), closed=True)
        self.add_polyline('chip-high', (27, 16), (32, 11), (37, 16), (32, 21), closed=True)

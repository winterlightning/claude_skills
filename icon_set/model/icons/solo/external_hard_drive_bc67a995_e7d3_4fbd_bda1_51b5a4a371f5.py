"""Perspective hard drive with seam and front slot. Extremes (2,8)-(46,40); Lucide hard-drive trapezoid and rounded front."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc67a995-e7d3-4fbd-bda1-51b5a4a371f5'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/hard drive 1_bc67a995-e7d3-4fbd-bda1-51b5a4a371f5.svg'
AUTHOR = 'astra-chatgpt'

class ExternalHardDrive(Solo48):
    icon_id = 'external-hard-drive'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('hard drive', 'hdd', 'storage', 'external', 'disk', 'backup', 'hardware', 'computer')

    def build(self) -> None:
        self.add_line('top-1', (2, 24), (9, 8))
        self.add_line('top-2', (9, 8), (39, 8))
        self.add_line('top-3', (39, 8), (46, 24))
        self.add_line('right', (46, 24), (46, 36))
        self.add_arc('se', (46, 36), (42, 40), radius_x=4, radius_y=4, sweep=True)
        self.add_line('bottom', (42, 40), (6, 40))
        self.add_arc('sw', (6, 40), (2, 36), radius_x=4, radius_y=4, sweep=True)
        self.add_line('left', (2, 36), (2, 24))
        self.add_contour('case', 'top-1', 'top-2', 'top-3', 'right', 'se', 'bottom', 'sw', 'left', closed=True)
        self.add_line('seam', (2, 24), (46, 24))
        self.relate('connect', 'case', 'seam')
        self.add_line('slot', (12, 32), (36, 32))

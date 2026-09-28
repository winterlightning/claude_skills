'external-hard-drive: Narrowed the case and enlarged the front panel around the slot. Keyshape HRECT_L; SOLO48 stroke 4. Reviewed at 48 px in both themes.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bc67a995-e7d3-4fbd-bda1-51b5a4a371f5'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/hard drive 1_bc67a995-e7d3-4fbd-bda1-51b5a4a371f5.svg'
AUTHOR = 'gpt-6'

class ExternalHardDrive(Solo48):
    icon_id = 'external-hard-drive'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    categories = ('computers', 'primitives')
    aliases = ()
    keywords = ('hard drive', 'hdd', 'storage', 'external', 'disk', 'backup', 'hardware', 'computer')

    def build(self) -> None:
        self.add_line('top-1', (4, 22), (9, 8))
        self.add_line('top-2', (9, 8), (39, 8))
        self.add_line('top-3', (39, 8), (44, 22))
        self.add_line('right', (44, 22), (44, 36))
        self.add_arc('se', (44, 36), (40, 40), radius_x=4, radius_y=4, sweep=True)
        self.add_line('bottom', (40, 40), (8, 40))
        self.add_arc('sw', (8, 40), (4, 36), radius_x=4, radius_y=4, sweep=True)
        self.add_line('left', (4, 36), (4, 22))
        self.add_contour('case', 'top-1', 'top-2', 'top-3', 'right', 'se', 'bottom', 'sw', 'left', closed=True)
        self.add_line('seam', (4, 22), (44, 22))
        self.relate('connect', 'case', 'seam')
        self.add_line('slot', (13, 31), (35, 31))

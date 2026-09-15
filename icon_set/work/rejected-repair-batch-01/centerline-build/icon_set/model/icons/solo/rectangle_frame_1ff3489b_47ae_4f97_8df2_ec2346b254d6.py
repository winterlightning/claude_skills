"""Rectangle frame (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1ff3489b-47ae-4f97-8df2-ec2346b254d6'
SOURCE_PATH = 'pictographic-primitives/design/rectangle frame_1ff3489b-47ae-4f97-8df2-ec2346b254d6.svg'
AUTHOR = 'gpt-6'

class RectangleFrame(Solo48):
    icon_id = 'rectangle-frame'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('rectangle', 'frame', 'design')

    def build(self):
        self.add_line('sym-e0', (5, 8), (43, 8))
        self.add_line('sym-e2', (43, 8), (44, 9))
        self.add_line('sym-e4', (44, 9), (44, 39))
        self.add_line('sym-e7', (44, 39), (43, 40))
        self.add_line('sym-e8', (43, 40), (5, 40))
        self.add_arc('sym-e10', (5, 40), (4, 39), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('sym-e12', (4, 39), (4, 9))
        self.add_line('sym-e15', (4, 9), (5, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e4', 'sym-e7', 'sym-e8', 'sym-e10', 'sym-e12', 'sym-e15', closed=True)

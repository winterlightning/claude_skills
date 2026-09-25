'A paintbrush lies diagonally with its long rounded handle pointing upper-right. A short collar connects the handle to a broad curved tuft of bristles ending at lower-left.\n\nConstruction: Diagonal handle and broad brush tuft with a single collar seam. Bounds (6,6)-(42,42).\nLucide: paintbrush: clear handle/collar/bristle hierarchy.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '155f94d2-9337-4308-87e9-3df5169ddd1f'
SOURCE_PATH = 'pictographic-primitives/wayfinding/brush_155f94d2-9337-4308-87e9-3df5169ddd1f.svg'
AUTHOR = 'gpt-6'

class Paintbrush(Solo48):
    icon_id = 'paintbrush'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('brush', 'paintbrush', 'painting', 'bristles', 'handle', 'art')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('handle-cap', (32, 6), (42, 16), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('handle-right', (42, 16), (26, 30))
        self.add_line('collar-bottom', (26, 30), (18, 22))
        self.add_line('handle-left', (18, 22), (32, 6))
        self.add_arc('bristle-top', (18, 22), (10, 30), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('bristle-tip', (10, 30), (6, 42))
        self.add_arc('bristle-bottom', (6, 42), (26, 30), radius_x=20, radius_y=12, large_arc=False, sweep=False)
        self.add_contour('handle', 'handle-cap', 'handle-right', 'collar-bottom', 'handle-left', closed=True)
        self.add_contour('tuft', 'bristle-top', 'bristle-tip', 'bristle-bottom', closed=False)
        self.relate('connect', 'handle', 'tuft')

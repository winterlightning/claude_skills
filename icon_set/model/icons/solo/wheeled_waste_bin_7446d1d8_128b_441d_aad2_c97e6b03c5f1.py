'A waste bin has a broad overhanging lid and a body tapering toward its base. A single visible wheel overlaps the lower-left corner beneath the straight rear edge.\n\nConstruction: Tapered bin with wide lid and one visible transport wheel. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7446d1d8-128b-441d-aad2-c97e6b03c5f1'
SOURCE_PATH = 'pictographic-primitives/wayfinding/garbage bin_7446d1d8-128b-441d-aad2-c97e6b03c5f1.svg'
AUTHOR = 'gpt-6'

class WheeledWasteBin(Solo48):
    icon_id = 'wheeled-waste-bin'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('bin', 'waste', 'garbage', 'wheel', 'disposal', 'cleaning')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('lid-1', (8, 12), (8, 4))
        self.add_line('lid-2', (8, 4), (40, 4))
        self.add_line('lid-3', (40, 4), (40, 12))
        self.add_line('lid-4', (40, 12), (32, 12))
        self.add_line('lid-5', (32, 12), (16, 12))
        self.add_line('lid-6', (16, 12), (8, 12))
        self.add_line('lid-7', (8, 12), (8, 12))
        self.add_line('bin-left', (16, 12), (14, 32))
        self.add_line('bin-bottom-1', (20, 38), (32, 38))
        self.add_line('bin-bottom-2', (32, 38), (40, 12))
        self.add_arc('wheel-top-joint-1', (8, 38), (14, 32), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('wheel-top-joint-2', (14, 32), (20, 38), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('wheel-bottom', (20, 38), (8, 38), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('lid', 'lid-1', 'lid-2', 'lid-3', 'lid-4', 'lid-5', 'lid-6', 'lid-7', closed=True)
        self.add_contour('bin-bottom', 'bin-bottom-1', 'bin-bottom-2', closed=False)
        self.add_contour('wheel', 'wheel-top-joint-1', 'wheel-top-joint-2', 'wheel-bottom', closed=True)
        self.relate('connect', 'lid', 'bin-left')
        self.relate('connect', 'lid', 'bin-bottom')
        self.relate('connect', 'wheel', 'bin-left')
        self.relate('connect', 'wheel', 'bin-bottom')

'Six separate circular dots form a regular braille cell with two vertical columns of three. The circles share the same size and align in three evenly spaced horizontal rows.\n\nConstruction: Two columns of three circular raised dots; shared 26-unit column separation and 14-unit row step. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8bb203af-04f2-462c-9b42-170fa7c7a70f'
SOURCE_PATH = 'pictographic-primitives/wayfinding/disability braille_8bb203af-04f2-462c-9b42-170fa7c7a70f.svg'
AUTHOR = 'gpt-6'

class BrailleCell(Solo48):
    icon_id = 'braille-cell'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('braille', 'accessibility', 'dots', 'tactile', 'reading', 'cell')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('dot-11-7-top', (8, 7), (14, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('dot-11-7-bottom', (14, 7), (8, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('dot-11-24-top', (8, 24), (14, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('dot-11-24-bottom', (14, 24), (8, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('dot-11-41-top', (8, 41), (14, 41), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('dot-11-41-bottom', (14, 41), (8, 41), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('dot-37-7-top', (34, 7), (40, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('dot-37-7-bottom', (40, 7), (34, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('dot-37-24-top', (34, 24), (40, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('dot-37-24-bottom', (40, 24), (34, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('dot-37-41-top', (34, 41), (40, 41), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('dot-37-41-bottom', (40, 41), (34, 41), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('dot-11-7', 'dot-11-7-top', 'dot-11-7-bottom', closed=True)
        self.add_contour('dot-11-24', 'dot-11-24-top', 'dot-11-24-bottom', closed=True)
        self.add_contour('dot-11-41', 'dot-11-41-top', 'dot-11-41-bottom', closed=True)
        self.add_contour('dot-37-7', 'dot-37-7-top', 'dot-37-7-bottom', closed=True)
        self.add_contour('dot-37-24', 'dot-37-24-top', 'dot-37-24-bottom', closed=True)
        self.add_contour('dot-37-41', 'dot-37-41-top', 'dot-37-41-bottom', closed=True)

"""Photo bokeh (photography), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3274b84e-eb11-47ba-b5cb-24b415eafb0f'
SOURCE_PATH = 'pictographic-primitives/photography/photo bokeh_3274b84e-eb11-47ba-b5cb-24b415eafb0f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class PhotoBokeh(Solo48):
    icon_id = 'photo-bokeh'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    categories = ('photography', 'primitives')
    aliases = ()
    keywords = ('photo', 'bokeh', 'photography')

    def build(self):
        # Plan: open the smallest bokeh ring and lift the upper-left ring for clear spacing.
        # Reference: original circular bokeh arrangement; exact circles and their inner openings.
        self.add_arc('e0-top', (36, 9), (42, 9), radius_x=3)
        self.add_arc('e0-bottom', (42, 9), (36, 9), radius_x=3)
        self.add_arc('e1-top', (6, 11), (16, 11), radius_x=5)
        self.add_arc('e1-bottom', (16, 11), (6, 11), radius_x=5)
        self.add_arc('e2-top', (23, 17), (29, 17), radius_x=3)
        self.add_arc('e2-bottom', (29, 17), (23, 17), radius_x=3)
        self.add_arc('e3-top', (34, 27), (42, 27), radius_x=4)
        self.add_arc('e3-bottom', (42, 27), (34, 27), radius_x=4)
        self.add_arc('e4-top', (9, 34), (25, 34), radius_x=8)
        self.add_arc('e4-bottom', (25, 34), (9, 34), radius_x=8)
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)

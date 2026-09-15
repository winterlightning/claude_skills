'Two large outlined capital C letters sit side by side on the same baseline. Both open toward the right, with matching curved backs and short diagonal terminals.\n\nConstruction: Two matching open C contours. Elliptical arcs preserve the letter openings; no enclosing badge. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c6b43566-f4cb-4cb8-90e7-0c3b09e69bdd'
SOURCE_PATH = 'pictographic-primitives/wayfinding/disability cc_c6b43566-f4cb-4cb8-90e7-0c3b09e69bdd.svg'
AUTHOR = 'gpt-6'

class ClosedCaptionLetters(Solo48):
    icon_id = 'closed-caption-letters'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('captions', 'closed', 'cc', 'accessibility', 'text', 'hearing')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('left-top', (20, 8), (4, 24), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_arc('left-bottom', (4, 24), (20, 40), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_arc('right-top', (44, 8), (28, 24), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_arc('right-bottom', (28, 24), (44, 40), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_contour('left', 'left-top', 'left-bottom', closed=False)
        self.add_contour('right', 'right-top', 'right-bottom', closed=False)

"""Previous arrow (state), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '53227aaa-0ab2-4f90-8901-7c384959220c'
SOURCE_PATH = 'pictographic-primitives/state/previous arrow_53227aaa-0ab2-4f90-8901-7c384959220c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class PreviousArrow(Solo48):
    icon_id = 'previous-arrow'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('previous', 'arrow', 'state')

    def build(self):
        self.add_line('e0', (16, 4), (8, 12))
        self.add_line('e1', (17, 20), (8, 12))
        self.add_line('e2', (20, 44), (25, 44))
        self.add_line('e3', (25, 12), (8, 12))
        self.add_arc('e4-1', (25, 44), (40, 28), radius_x=17, sweep=False)
        self.add_arc('e4-2', (40, 28), (37, 19), radius_x=15, sweep=False)
        self.add_arc('e4-3', (37, 19), (25, 12), radius_x=17, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e4-1', 'e4-2', 'e4-3', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')

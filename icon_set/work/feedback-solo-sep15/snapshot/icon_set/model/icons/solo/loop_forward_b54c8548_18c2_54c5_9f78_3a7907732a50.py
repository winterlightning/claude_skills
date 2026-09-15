"""Loop forward (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b54c8548-18c2-54c5-9f78-3a7907732a50'
SOURCE_PATH = 'pictographic-primitives/interface-essential/loop forward_b54c8548-18c2-54c5-9f78-3a7907732a50.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class LoopForward(Solo48):
    icon_id = 'loop-forward'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('loop', 'forward', 'interface-essential')

    def build(self):
        self.add_line('e0', (31, 35), (13, 35))
        self.add_line('e1', (6, 26), (6, 13))
        self.add_line('e2', (15, 6), (35, 6))
        self.add_line('e3', (42, 12), (42, 17))
        self.add_line('e4', (31, 35), (24, 42))
        self.add_line('e5', (31, 35), (24, 27))
        self.add_bezier('e6', (13, 35), ((9.654, 35), (6.016, 31.822), (6.016, 28.402)), ((6.016, 28.173), (6, 27.952), (6, 27.723)), ((6, 27.305), (6, 26.425), (6, 26)))
        self.add_bezier('e7', (6, 13), ((6.008, 12.877), (6.008, 12.3), (6.016, 12.169)), ((6.016, 8.602), (9.526, 6.016), (12.856, 6.016)), ((13.315, 6.016), (13.781, 6), (14.247, 6)), ((14.501, 6), (14.746, 6), (15, 6)))
        self.add_bezier('e8', (35, 6), ((35.139, 6), (34.906, 6.008), (35.045, 6.008)), ((37.811, 6.008), (40.756, 8.021), (41.673, 10.631)), ((41.804, 10.983), (42, 11.615), (42, 12)))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e7', 'e2', 'e8', 'e3')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')

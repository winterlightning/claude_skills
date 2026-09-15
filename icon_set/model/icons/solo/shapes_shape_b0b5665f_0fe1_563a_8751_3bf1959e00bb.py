"""Shapes shape (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0b5665f-0fe1-563a-8751-3bf1959e00bb'
SOURCE_PATH = 'pictographic-primitives/design/shapes shape_b0b5665f-0fe1-563a-8751-3bf1959e00bb.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class ShapesShape(Solo48):
    icon_id = 'shapes-shape'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('shapes', 'shape', 'design')

    def build(self):
        # Plan: remove subpixel cubic detours while preserving real contour nodes.
        # Reference: supplied subject and its existing stroke graph.
        self.add_line('e0', (42, 20), (20, 20))
        self.add_line('e1', (20, 20), (20, 42))
        self.add_line('e2', (20, 42), (42, 42))
        self.add_line('e3', (42, 42), (42, 20))
        self.add_bezier('e4', (20, 31), ((18.061, 30.975), (16.039, 31.249), (14.215, 30.521)), ((9.641, 28.696), (6.008, 24.155), (6.008, 19.091)), ((6.008, 18.962), (6, 18.833), (6, 18.704)), ((6, 18.502), (6.008, 18.305), (6.008, 18.109)), ((6.008, 11.776), (11.695, 6.008), (18.027, 6.008)), ((18.108, 6.008), (18.18, 6), (18.261, 6)), ((18.404, 6), (18.543, 6.008), (18.682, 6.008)), ((23.427, 6.008), (27.976, 9.109), (29.67, 13.552)), ((30.447, 15.597), (31.082, 17.832), (31, 20)))
        self.add_contour('c0', 'e4', closed=False)
        self.add_contour('c1', 'e0', 'e1', 'e2', 'e3', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')

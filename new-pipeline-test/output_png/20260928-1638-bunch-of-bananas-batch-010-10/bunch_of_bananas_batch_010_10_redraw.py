"""bunch-of-bananas-batch-010-10 (redraw of the new-pipeline traced SVG).

Plan: draft.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "01dfab52-1214-532b-8f84-ea5dce7a2998"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1638-bunch-of-bananas-batch-010-10/"
    "bunch-of-bananas-batch-010-10_raw.svg"
)
AUTHOR = "claude-opus-5-5"

J = (12, 16)            # crown: every fruit leaves the stem here
STEM_TOP = (10, 8)
T_TIP = (44, 18)        # top fruit tip, rightmost
M_TIP = (44, 30)        # middle fruit tip, rightmost
A = (34, 25)            # top fruit's curl lands on the middle fruit
BP = (32, 36)           # bottom fruit's curl lands on the middle fruit
B_LEFT = (4, 24)
B_LOW = (24, 40)


class BunchOfBananasBatch01010Redraw(Solo48):
    icon_id = "bunch-of-bananas-batch-010-10-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/fruit"
    aliases = ("bananas", "banana bunch", "hand of bananas")
    keywords = ("banana", "bunch", "fruit", "food", "tropical", "yellow", "produce")

    def build(self) -> None:
        self.add_line("stem", J, STEM_TOP)

        # Middle fruit: closed, its edges are shared with the outer two.
        self.add_bezier("m-top-a", J, ((16, 22), (26, 25), A))
        self.add_bezier("m-top-b", A, ((40, 25), (44, 27), M_TIP))
        self.add_bezier("m-bot-a", M_TIP, ((44, 34), (38, 36), BP))
        self.add_bezier("m-bot-b", BP, ((22, 36), (14, 26), J))
        self.add_contour("middle", "m-top-a", "m-top-b", "m-bot-a", "m-bot-b", closed=True)

        # Top fruit: over the top, round the tip, curl back onto the middle.
        self.add_bezier("t-top", J, ((18, 21), (28, 19), (36, 15)))
        self.add_bezier("t-tip", (36, 15), ((40, 13), (44, 14), T_TIP))
        self.add_bezier("t-curl", T_TIP, ((44, 22), (38, 24), A))
        self.add_contour("top", "t-top", "t-tip", "t-curl")

        # Bottom fruit: round the left and underside, curl back onto the middle.
        self.add_bezier("b-left", J, ((8, 17), (4, 20), B_LEFT))
        self.add_bezier("b-under", B_LEFT, ((4, 32), (14, 40), B_LOW))
        self.add_bezier("b-tip", B_LOW, ((32, 40), (38, 40), (38, 38)))
        self.add_bezier("b-curl", (38, 38), ((38, 36), (35, 36), BP))
        self.add_contour("bottom", "b-left", "b-under", "b-tip", "b-curl")

        self.relate("connect", "stem", "middle")
        self.relate("connect", "stem", "top")
        self.relate("connect", "stem", "bottom")
        self.relate("connect", "top", "middle")
        self.relate("connect", "bottom", "middle")
        self.relate("connect", "top", "bottom")

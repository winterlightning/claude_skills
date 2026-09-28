"""Euro financial document: a page with a clipped top-right corner holding a euro sign.

Revision of the disapproved drawing, whose one-bar C read as a letter rather than a
euro. Plan (SQUARE, centerline (6,6)-(42,42)): rounded page (r4) with a chamfer from
(34,6) to (42,14); inside, a euro built from five cubics mirrored about y=24 (top 15,
bottom 33, left bulge to 15.25) whose left knots (16,19)/(16,29) carry the two bars to
x=23. The reference's two short text lines are omitted: they cannot keep 8 units from
both the sign and the wall. Lucide `euro` and `file` inform the construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "36b5ce8c-0ffe-4bbc-9abc-5d99e806b0d9"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__euro-financial-document-solo/20260927T150749Z-thuan-mac-1/reference/euro bill_36b5ce8c-0ffe-4bbc-9abc-5d99e806b0d9.svg"
AUTHOR = "claude-fable-5-1"


class EuroFinancialDocument(Solo48):
    icon_id = "euro-financial-document-solo"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "other"
    aliases = ("euro bill", "euro invoice")
    keywords = ("euro", "document", "bill", "invoice", "finance", "currency", "page")

    def build(self) -> None:
        r = 4
        self.add_line("page-top", (10, 6), (34, 6))
        self.add_line("page-chamfer", (34, 6), (42, 14))
        self.add_line("page-right", (42, 14), (42, 38))
        self.add_arc("page-br", (42, 38), (38, 42), radius_x=r)
        self.add_line("page-bottom", (38, 42), (10, 42))
        self.add_arc("page-bl", (10, 42), (6, 38), radius_x=r)
        self.add_line("page-left", (6, 38), (6, 10))
        self.add_arc("page-tl", (6, 10), (10, 6), radius_x=r)
        self.add_contour("page", "page-top", "page-chamfer", "page-right", "page-br",
                         "page-bottom", "page-bl", "page-left", "page-tl", closed=True)
        # euro C, mirrored about y=24
        self.add_bezier("euro-1", (30, 17), ((28, 15), (26, 15), (24, 15)))
        self.add_bezier("euro-2", (24, 15), ((20, 15), (17, 16), (16, 19)))
        self.add_bezier("euro-3", (16, 19), ((15, 22), (15, 26), (16, 29)))
        self.add_bezier("euro-4", (16, 29), ((17, 32), (20, 33), (24, 33)))
        self.add_bezier("euro-5", (24, 33), ((26, 33), (28, 33), (30, 31)))
        self.add_contour("euro", "euro-1", "euro-2", "euro-3", "euro-4", "euro-5")
        self.add_line("bar-top", (16, 19), (23, 19))
        self.add_line("bar-bottom", (16, 29), (23, 29))
        self.relate("connect", "bar-top", "euro")
        self.relate("connect", "bar-bottom", "euro")

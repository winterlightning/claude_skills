"""Two differently oriented samosas above a rounded bowl of dipping sauce.

Symbol plan: a triangular pastry, a turned pastry with folded curved tip, and
an elliptical-lipped bowl. Lucide ice-cream-bowl informed the bowl outline;
the source reference controls the pastry angles and arrangement.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "71feabef-8b20-4158-9c30-80cdbd5cbfc9"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__samosa-dipping-sauce/20260927T091420Z-thuan-mac-1/reference/exotic food samosa dip_71feabef-8b20-4158-9c30-80cdbd5cbfc9.svg"
AUTHOR = "gpt-6"


class SamosaDippingSauce(Solo48):
    icon_id = "samosa-dipping-sauce"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ("samosa", "dipping", "sauce", "bowl", "pastry")

    def build(self) -> None:
        self.add_polyline("samosa-left", (6,22), (14,7), (21,22), closed=True)
        self.add_line("fold-top", (29,15), (42,6))
        self.add_line("fold-side", (42,6), (42,20))
        self.add_arc("fold-tip", (42,20), (40,22), radius_x=2, sweep=True)
        self.add_line("fold-bottom", (40,22), (37,22))
        self.add_line("fold-crease", (37,22), (34,18))
        self.add_line("fold-back", (34,18), (29,15))
        self.add_contour("samosa-right", "fold-top", "fold-side", "fold-tip",
                         "fold-bottom", "fold-crease", "fold-back", closed=True)

        self.add_arc("rim", (20,32), (42,32), radius_x=11, radius_y=2, sweep=True)
        self.add_arc("bowl", (42,32), (20,32), radius_x=11, radius_y=10, sweep=True)
        self.add_contour("sauce-bowl", "rim", "bowl", closed=True)

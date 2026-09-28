"""Korean tteokbokki skewer with a sauce bowl.

Symbol plan: skewer on the diagonal y=x from (6,6) to (42,42). Three rice
cakes, one repeated definition: a square turned to the skewer (half-diagonal
6, sides 8.5) centred at (12,12), (24,24) and (36,36); consecutive cakes are
8.5 apart and the stick shows between them and at both ends, joining each
cake at the midpoints of its skewer-facing sides. The cakes' lower-left sides
all lie on y=x+6, so the sauce bowl sits in the lower-left corner with its
rim on y=x+18 (8.5 away): rim (6,24)-(18,36) and an r9 bowl belly.
Revision: the rejected drawing fused the cakes into one strip with seams and
drew the bowl as a flat "D"; the reference shows separate cakes on a visible
stick and a dipping bowl beside them.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "c5b185fc-2fac-4f46-9e95-acf2bd4b9e3d"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__korean-rice-cake-skewer-sauce/20260927T153253Z-thuan-mac-1/reference/korean tokboki_c5b185fc-2fac-4f46-9e95-acf2bd4b9e3d.svg"
AUTHOR = "claude-opus-5-5"


class KoreanRiceCakeSkewerSauce(Solo48):
    icon_id = "korean-rice-cake-skewer-sauce"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ("tteokbokki", "tokboki", "rice cake skewer")
    keywords = ("tteokbokki", "korean", "rice cake", "skewer", "sauce", "street food")

    def build(self) -> None:
        h = 6
        centres = (12, 24, 36)
        for i, c in enumerate(centres):
            m = h // 2
            self.add_polyline(f"cake-{i}", (c - m, c - m), (c, c - h), (c + h, c),
                              (c + m, c + m), (c, c + h), (c - h, c), closed=True)
        stick = [((6, 6), (9, 9)), ((15, 15), (21, 21)), ((27, 27), (33, 33)), ((39, 39), (42, 42))]
        for i, (p, q) in enumerate(stick):
            self.add_line(f"stick-{i}", p, q)
            if i > 0:
                self.relate("connect", f"stick-{i}", f"cake-{i - 1}")
            if i < 3:
                self.relate("connect", f"stick-{i}", f"cake-{i}")

        self.add_line("bowl-rim", (6, 24), (18, 36))
        self.add_arc("bowl-belly", (18, 36), (6, 24), radius_x=9, sweep=True)
        self.add_contour("bowl", "bowl-rim", "bowl-belly", closed=True)

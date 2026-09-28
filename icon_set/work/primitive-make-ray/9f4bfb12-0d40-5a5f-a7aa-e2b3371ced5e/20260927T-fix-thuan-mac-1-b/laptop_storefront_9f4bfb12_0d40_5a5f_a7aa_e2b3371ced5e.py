"""E-commerce shop: a storefront awning over a laptop base.

Symbol plan: awning = trapezoid top (12,6)-(36,6) splaying to (9,14)/(39,14)
with a valance of three r5 scallops hanging down (bottoms at y=19) and two
stripe dividers rising from the scallop cusps to the top edge (8 apart at the
top). Shop walls x=10/x=38 leave the outer scallops at their lattice points
(10,17)/(38,17) and stand on the laptop base. Base = wide deck (top y=32,
bottom y=42, r8 lower corners) with a shallow r10 trackpad notch in its top
edge. Mirror-symmetric about x=24.
Revision: the rejected drawing turned the scallops upward into bumps and drew
the base as a bowl without the notch; the reference has a hanging valance,
striped awning and a laptop deck.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "9f4bfb12-0d40-5a5f-a7aa-e2b3371ced5e"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__laptop-storefront/20260927T153253Z-thuan-mac-1/reference/e commerce shop_9f4bfb12-0d40-5a5f-a7aa-e2b3371ced5e.svg"
AUTHOR = "claude-opus-5-5"


class LaptopStorefront(Solo48):
    icon_id = "laptop-storefront"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "commerce"
    categories = ("primitives", "commerce")
    aliases = ("e-commerce shop", "online store")
    keywords = ("ecommerce", "shop", "store", "laptop", "online", "awning")

    def build(self) -> None:
        self.add_line("awning-top", (12, 6), (36, 6))
        self.add_line("awning-right", (36, 6), (39, 14))
        self.add_arc("scallop-3a", (39, 14), (38, 17), radius_x=5, sweep=True)
        self.add_arc("scallop-3b", (38, 17), (29, 14), radius_x=5, sweep=True)
        self.add_arc("scallop-2", (29, 14), (19, 14), radius_x=5, sweep=True)
        self.add_arc("scallop-1b", (19, 14), (10, 17), radius_x=5, sweep=True)
        self.add_arc("scallop-1a", (10, 17), (9, 14), radius_x=5, sweep=True)
        self.add_line("awning-left", (9, 14), (12, 6))
        self.add_contour("awning", "awning-top", "awning-right", "scallop-3a", "scallop-3b",
                         "scallop-2", "scallop-1b", "scallop-1a", "awning-left", closed=True)
        self.add_line("stripe-left", (19, 14), (20, 6))
        self.add_line("stripe-right", (29, 14), (28, 6))
        self.add_line("wall-left", (10, 17), (10, 32))
        self.add_line("wall-right", (38, 17), (38, 32))
        for part in ("stripe-left", "stripe-right", "wall-left", "wall-right"):
            self.relate("connect", "awning", part)

        self.add_line("deck-left", (6, 32), (10, 32))
        self.add_line("deck-mid-left", (10, 32), (18, 32))
        self.add_arc("deck-notch", (18, 32), (30, 32), radius_x=10, sweep=False)
        self.add_line("deck-mid-right", (30, 32), (38, 32))
        self.add_line("deck-right", (38, 32), (42, 32))
        self.add_line("deck-side-right", (42, 32), (42, 34))
        self.add_arc("deck-corner-right", (42, 34), (34, 42), radius_x=8, sweep=True)
        self.add_line("deck-bottom", (34, 42), (14, 42))
        self.add_arc("deck-corner-left", (14, 42), (6, 34), radius_x=8, sweep=True)
        self.add_line("deck-side-left", (6, 34), (6, 32))
        self.add_contour("deck", "deck-left", "deck-mid-left", "deck-notch", "deck-mid-right",
                         "deck-right", "deck-side-right", "deck-corner-right", "deck-bottom",
                         "deck-corner-left", "deck-side-left",
                         closed=True)
        self.relate("connect", "wall-left", "deck")
        self.relate("connect", "wall-right", "deck")

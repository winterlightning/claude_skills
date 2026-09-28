"""A beer mug: a straight-walled mug with a side handle under a billowing head of foam.

Symbol plan: the foam is one closed cloud: a round left cap (r4) and three bumps (r4,
a 6x4 half-ellipse crest, r6) over a straight base line that is also the mug's rim, with
a rounded r4 corner back to the base on the right, overhanging the walls on both sides
as in the reference. The mug body is an open U with r3 bottom corners hanging from the
foam base; the handle is a rounded rectangle (r4 outer corners) on the right wall,
placed 9 below the foam corner.
Lucide construction: 'beer' - straight mug body with a rectangular side handle and a
cloud of arcs for the foam.
Keyshape SQUARE: centerline x 6..42 (foam cap, handle), y 6..42 (foam crest, mug base).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5429b76f-075c-4738-87f2-f8390c36df79"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__beer-mug/20260926T030905Z-thuan-mac/reference/beer_5429b76f-075c-4738-87f2-f8390c36df79.svg"
AUTHOR = "claude-opus-5-5"


class BeerMug(Solo48):
    icon_id = "beer-mug"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/drink"
    aliases = ("beer", "tankard", "pint")
    keywords = ("beer", "mug", "tankard", "stein", "ale", "lager", "foam", "drink", "pub", "bar")

    def build(self) -> None:
        wl, wr, rim, base = 10, 31, 20, 42
        ht, hb = 29, 39
        # foam cloud
        self.add_arc("foam-cap", (wl, rim), (wl, 12), radius_x=4, sweep=True)
        self.add_arc("foam-bump-left", (wl, 12), (17, 10), radius_x=4, sweep=True)
        self.add_arc("foam-bump-crest", (17, 10), (29, 10), radius_x=6, radius_y=4, sweep=True)
        self.add_arc("foam-bump-right", (29, 10), (35, 16), radius_x=6, sweep=True)
        self.add_arc("foam-corner", (35, 16), (wr, rim), radius_x=4, sweep=True)
        self.add_line("foam-base", (wr, rim), (wl, rim))
        self.add_contour("foam", "foam-cap", "foam-bump-left", "foam-bump-crest",
                         "foam-bump-right", "foam-corner", "foam-base", closed=True)
        # mug body
        self.add_line("wall-left", (wl, rim), (wl, base - 3))
        self.add_arc("corner-left", (wl, base - 3), (wl + 3, base), radius_x=3, sweep=False)
        self.add_line("bottom", (wl + 3, base), (wr - 3, base))
        self.add_arc("corner-right", (wr - 3, base), (wr, base - 3), radius_x=3, sweep=False)
        self.add_line("wall-right-low", (wr, base - 3), (wr, hb))
        self.add_line("wall-right-mid", (wr, hb), (wr, ht))
        self.add_line("wall-right-top", (wr, ht), (wr, rim))
        self.add_contour("body", "wall-left", "corner-left", "bottom", "corner-right",
                         "wall-right-low", "wall-right-mid", "wall-right-top")
        # handle
        self.add_line("handle-top", (wr, ht), (38, ht))
        self.add_arc("handle-corner-top", (38, ht), (42, ht + 4), radius_x=4, sweep=True)
        self.add_line("handle-side", (42, ht + 4), (42, hb - 4))
        self.add_arc("handle-corner-bottom", (42, hb - 4), (38, hb), radius_x=4, sweep=True)
        self.add_line("handle-bottom", (38, hb), (wr, hb))
        self.add_contour("handle", "handle-top", "handle-corner-top", "handle-side",
                         "handle-corner-bottom", "handle-bottom")
        self.relate("connect", "foam", "body")
        self.relate("connect", "body", "handle")

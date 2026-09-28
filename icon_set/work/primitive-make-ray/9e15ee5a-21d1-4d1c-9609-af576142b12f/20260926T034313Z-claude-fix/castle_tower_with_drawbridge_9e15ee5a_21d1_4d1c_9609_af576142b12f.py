"""A castle gate: a crenellated tower with an arched window and a drawbridge hanging from its base on a chain.

Symbol plan: the tower is one open outline (no ground line, as in the reference): left
wall split where the chain attaches, a battlement of two 9-wide merlons around an
8-wide, 6-deep square notch, right wall. The window is a closed arch (r4 top, 8 wide),
9 from both walls and 10 below the notch. The drawbridge is a plank line hinged at the
tower's left foot and raised up-left; the chain runs from the tower wall to
the plank's free end, closing the triangle of the reference.
The reference's water wave is dropped: under the raised plank no wave keeps 8 units of
clearance inside the canvas. Its two scalloped notches become one square notch (three
8-wide merlons and two notches do not fit).
Lucide construction: 'castle' square battlements and arched window.
Keyshape SQUARE: centerline x 6..42 (plank end, tower right wall), y 6..42 (battlement, feet).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "9e15ee5a-21d1-4d1c-9609-af576142b12f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__castle-tower-with-drawbridge/20260926T034135Z-thuan-mac/reference/castle gate_9e15ee5a-21d1-4d1c-9609-af576142b12f.svg"
AUTHOR = "claude-opus-5-5"


class CastleTowerWithDrawbridge(Solo48):
    icon_id = "castle-tower-with-drawbridge"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/building"
    aliases = ("castle gate", "drawbridge", "castle tower")
    keywords = ("castle", "gate", "drawbridge", "tower", "fortress", "medieval", "chain", "moat")

    def build(self) -> None:
        tl, tr, top, foot = 16, 42, 6, 42
        notch_l, notch_r, notch_y = 25, 33, 12
        chain_y = 16
        plank_end = (6, 30)
        wx, wr, w_arch, w_bot = 29, 4, 26, 34  # window axis, arch radius, arch centre y, sill
        # tower
        self.add_line("wall-l-low", (tl, foot), (tl, chain_y))
        self.add_line("wall-l-high", (tl, chain_y), (tl, top))
        crest = [(tl, top), (notch_l, top), (notch_l, notch_y), (notch_r, notch_y), (notch_r, top), (tr, top)]
        for k in range(1, len(crest)):
            self.add_line(f"battlements-{k}", crest[k - 1], crest[k])
        self.add_line("wall-r", (tr, top), (tr, foot))
        self.add_contour("tower", "wall-l-low", "wall-l-high", *[f"battlements-{k}" for k in range(1, 6)],
                         "wall-r")
        # arched window
        self.add_line("window-l", (wx - wr, w_bot), (wx - wr, w_arch))
        self.add_arc("window-arch", (wx - wr, w_arch), (wx + wr, w_arch), radius_x=wr)
        self.add_line("window-r", (wx + wr, w_arch), (wx + wr, w_bot))
        self.add_line("window-sill", (wx + wr, w_bot), (wx - wr, w_bot))
        self.add_contour("window", "window-l", "window-arch", "window-r", "window-sill", closed=True)
        # drawbridge and chain
        self.add_line("plank", (tl, foot), plank_end)
        self.add_line("chain", plank_end, (tl, chain_y))
        self.add_contour("bridge", "plank", "chain")
        self.relate("connect", "tower", "bridge")

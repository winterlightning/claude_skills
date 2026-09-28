"""A cabin ship on the water: a bowl hull with a raised bow, a cabin with a funnel, and a wave below.

Symbol plan: the hull is one closed outline - a flat deck from the stern that steps up
at 45 degrees to a raised bow, then smooth bezier sides into a flat keel. The cabin is
an open outline standing on the deck (shared endpoints) with its funnel as a tab of the
same outline on the roof. The sea is one smooth wave of horizontal-tangent half waves,
10 below the keel. The reference's second wave line is dropped: two waves plus hull,
cabin and funnel cannot keep 8-unit gaps inside 36 units of height.
Lucide construction: 'ship' - hull outline, cabin block on deck, one wave line under it.
Keyshape SQUARE: centerline x 6..42 (stern, bow / wave ends), y 6..42 (funnel, wave trough).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a5ee704a-fe51-550f-977a-8fdb2e527282"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__cabin-boat-on-waves/20260926T034135Z-thuan-mac/reference/ship 1_a5ee704a-fe51-550f-977a-8fdb2e527282.svg"
AUTHOR = "claude-opus-5-5"


class CabinBoatOnWaves(Solo48):
    icon_id = "cabin-boat-on-waves"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/water"
    aliases = ("ship", "boat", "steamboat")
    keywords = ("ship", "boat", "cabin", "sea", "waves", "ferry", "cruise", "voyage", "marine")

    def build(self) -> None:
        deck, bow, keel = 20, 16, 29
        cab_l, cab_r, cab_top = 10, 24, 11
        fun_l, fun_r, fun_top = 13, 21, 6
        # hull
        self.add_line("deck-stern", (6, deck), (cab_l, deck))
        self.add_line("deck-mid", (cab_l, deck), (cab_r, deck))
        self.add_line("deck-fore", (cab_r, deck), (30, deck))
        self.add_line("bow-rise", (30, deck), (34, bow))
        self.add_line("bow-top", (34, bow), (42, bow))
        self.add_bezier("hull-fore", (42, bow), ((42, 23), (38, keel), (30, keel)))
        self.add_line("keel", (30, keel), (16, keel))
        self.add_bezier("hull-aft", (16, keel), ((11, keel), (7, 25), (6, deck)))
        self.add_contour("hull", "deck-stern", "deck-mid", "deck-fore", "bow-rise", "bow-top",
                         "hull-fore", "keel", "hull-aft", closed=True)
        # cabin with funnel
        self.add_polyline("cabin", (cab_l, deck), (cab_l, cab_top), (fun_l, cab_top), (fun_l, fun_top),
                          (fun_r, fun_top), (fun_r, cab_top), (cab_r, cab_top), (cab_r, deck))
        self.relate("connect", "hull", "cabin")
        # wave: half waves 9 wide between y 38 (crest) and 42 (trough)
        xs = list(range(6, 43, 9))
        ys = [38 if i % 2 == 0 else 42 for i in range(len(xs))]
        segs = []
        for i in range(1, len(xs)):
            mx = (xs[i - 1] + xs[i]) / 2
            segs.append(((mx, ys[i - 1]), (mx, ys[i]), (xs[i], ys[i])))
        self.add_bezier("wave", (xs[0], ys[0]), *segs)

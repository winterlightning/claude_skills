"""A rising side-view airplane with one swept lower wing above a ground line.

Construction: plane-takeoff: rounded nose and detached runway; plane: coherent wing silhouette.
Reduction: Windows omitted; fuselage and near wing widened for clear negative space. Deliberate side-view asymmetry.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '28bc625b-2596-540d-91c3-fb5e36336a56'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__airplane-rising-above-ground-line/20260926T064521Z-thuan-mac/reference/plane land_28bc625b-2596-540d-91c3-fb5e36336a56.svg'
AUTHOR = "claude-opus-5-5"


class AirplaneRisingAboveGroundLine(Solo48):
    icon_id = 'airplane-rising-above-ground-line'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "travel"
    categories = ("travel", "primitives")
    aliases = ()
    keywords = ('airplane', 'runway', 'flight', 'landing', 'aviation', 'plane', 'ground', 'travel')

    def build(self) -> None:
        # Revision per review: the tail ends in a short, nearly horizontal top (8, 12)-(16, 13) with a
        # smoothly curved cubic underside down to the wing root; the lower wing is narrower
        # (8 across), its tip is slanted (19, 31)-(29, 33), and its leading edge curves into the
        # belly (a cubic from the tip to (36, 18)). The trailing edge keeps a notch at (22, 25)
        # so the wing still reads separately. (A version whose trailing edge merged into the
        # underside read as a boot, attempts/v1-merged-wing.svg; a tall fin read as a bird,
        # attempts/v2-tall-fin.svg.)
        self.add_arc("nose", (34, 7), (40, 15), radius_x=5)
        self.add_line("belly-front", (40, 15), (36, 18))
        self.add_bezier("wing-leading", (36, 18), ((33, 21), (31, 27), (29, 33)))
        self.add_line("wing-tip", (29, 33), (19, 31))
        self.add_line("wing-trailing", (19, 31), (22, 25))
        self.add_bezier("tail-underside", (22, 25), ((14, 23), (8, 20), (8, 12)))
        self.add_line("tail-top", (8, 12), (16, 13))
        self.add_line("back", (16, 13), (34, 7))
        self.add_contour("airplane", "nose", "belly-front", "wing-leading", "wing-tip", "wing-trailing",
                         "tail-underside", "tail-top", "back", closed=True)
        self.add_line('ground', (6, 42), (42, 42))

"""AdBlue indicator: the letters "AD" over a fluid-level wave (partial -- see below).

Symbol plan: hand-authored cap letters on one 18-unit cap band (y 6..24): an arched A
(two stems, r6 arch, crossbar) and a D (stem, r9 half-round bowl), 9 apart; below them a
single fluid wave of three r6/4 half-ellipses joined with vertical tangents across the full
width. The second text line "BLUE" is omitted: four letters need at least 3 x 8 units of
letter gaps plus ~28 of letters, more than the 36-unit width, so it cannot be drawn at
SOLO48 clearance.
Lucide construction: 'waves' (half-ellipse wave) and the round-bowl D of Lucide lettering.
Keyshape SQUARE: centerline x 6..42 (A stem, D bowl / wave ends), y 6..42 (cap top, wave trough).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ddba64a9-7a33-401d-9571-bce55808907f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__adblue-fluid-level-wave/20260925T093141Z-thuan-mac/reference/adblue indicator 1_ddba64a9-7a33-401d-9571-bce55808907f.svg"
AUTHOR = "claude-opus-5-5"


class AdblueFluidLevelWave(Solo48):
    icon_id = "adblue-fluid-level-wave"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/indicator"
    aliases = ("adblue-indicator", "adblue", "def-fluid")
    keywords = ("adblue", "ad", "blue", "diesel", "exhaust", "fluid", "level", "indicator", "dashboard")

    def build(self) -> None:
        top, base = 6, 24
        # A: arched top between two stems, crossbar at y17
        self.add_line("a-left", (6, base), (6, 12))
        self.add_arc("a-arch", (6, 12), (18, 12), radius_x=6, sweep=True)
        self.add_line("a-right-upper", (18, 12), (18, 17))
        self.add_line("a-right-lower", (18, 17), (18, base))
        self.add_contour("a", "a-left", "a-arch", "a-right-upper", "a-right-lower")
        self.add_line("a-bar", (6, 17), (18, 17))
        self.relate("connect", "a", "a-bar")
        # D: stem and a half-round bowl of r9
        self.add_line("d-foot", (33, base), (27, base))
        self.add_line("d-stem", (27, base), (27, top))
        self.add_line("d-head", (27, top), (33, top))
        self.add_arc("d-bowl", (33, top), (33, base), radius_x=9, sweep=True)
        self.add_contour("d", "d-foot", "d-stem", "d-head", "d-bowl", closed=True)
        # fluid wave
        self.add_arc("wave-1", (6, 38), (18, 38), radius_x=6, radius_y=4, sweep=True)
        self.add_arc("wave-2", (18, 38), (30, 38), radius_x=6, radius_y=4, sweep=False)
        self.add_arc("wave-3", (30, 38), (42, 38), radius_x=6, radius_y=4, sweep=True)
        self.add_contour("wave", "wave-1", "wave-2", "wave-3")

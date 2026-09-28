"""The ancient theatre at Delphi: a curved band of tiered seating (cavea) wrapped around a
round stage (orchestra) in front of it.

Symbol plan: the cavea is a band between two concentric arcs about (24,33) -- outer r25,
inner r15 -- closed by radial end walls through the (4,3)-family integer points, so ends
and aisle all point at the stage. A radial aisle on the axis x=24 splits the tiers into two
mirrored wedges. The orchestra is a flat ellipse (rx8, ry5) centred under the same axis,
inside the arc's opening. Everything mirrors about x=24.
Lucide construction: no amphitheatre glyph; the concentric-arc band with radial ends
follows Lucide 'rainbow' / 'gauge' construction, the stage follows 'ellipse' discs in
'cylinder'/'database'.
Keyshape HRECT_L: centerline x 4..44 (outer arc ends), y 8..40 (outer apex, stage bottom).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8a4178c7-eedb-4a97-930f-a81a357d0119"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__amphitheater-seating-and-round-stage/20260925T093141Z-thuan-mac/reference/amfitheater in delphi_8a4178c7-eedb-4a97-930f-a81a357d0119.svg"
AUTHOR = "claude-opus-5-5"


class AmphitheaterSeatingAndRoundStage(Solo48):
    icon_id = "amphitheater-seating-and-round-stage"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmark"
    aliases = ("amphitheater-in-delphi", "ancient-theatre", "delphi-theater")
    keywords = ("amphitheater", "amphitheatre", "theatre", "theater", "delphi", "greece",
                "ancient", "stage", "orchestra", "seating", "arena", "landmark")

    def build(self) -> None:
        cx, cy = 24, 33
        outer, inner = 25, 15
        # (4,3) family: outer ends at (+-20,-15), inner ends at (+-12,-9); apex on the axis
        self.add_arc("outer-left", (cx - 20, cy - 15), (cx, cy - outer), radius_x=outer, sweep=True)
        self.add_arc("outer-right", (cx, cy - outer), (cx + 20, cy - 15), radius_x=outer, sweep=True)
        self.add_line("end-right", (cx + 20, cy - 15), (cx + 12, cy - 9))
        self.add_arc("inner-right", (cx + 12, cy - 9), (cx, cy - inner), radius_x=inner, sweep=False)
        self.add_arc("inner-left", (cx, cy - inner), (cx - 12, cy - 9), radius_x=inner, sweep=False)
        self.add_line("end-left", (cx - 12, cy - 9), (cx - 20, cy - 15))
        self.add_contour("cavea", "outer-left", "outer-right", "end-right", "inner-right",
                         "inner-left", "end-left", closed=True)
        self.add_line("aisle", (cx, cy - outer), (cx, cy - inner))
        self.relate("connect", "cavea", "aisle")

        # orchestra: flat round stage in front of the seating
        self.add_arc("stage-top", (16, 35), (32, 35), radius_x=8, radius_y=5, sweep=True)
        self.add_arc("stage-bottom", (32, 35), (16, 35), radius_x=8, radius_y=5, sweep=True)
        self.add_contour("stage", "stage-top", "stage-bottom", closed=True)

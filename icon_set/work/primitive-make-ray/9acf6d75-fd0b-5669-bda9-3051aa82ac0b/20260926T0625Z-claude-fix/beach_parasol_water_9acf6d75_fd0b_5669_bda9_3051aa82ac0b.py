"""Beach parasol and water: a tilted beach umbrella planted in the sand, with the sea
as a wave line below.

Symbol plan: the canopy is a true half disc - a radius-13 semicircle on a straight
hem from (7,26) to (31,16), a chord of direction (24,-10) (22.6 degrees of tilt)
centred on (19,21). The arc is split at its apex (14,9), the axis point, where a
short finial continues outward. The pole leaves the hem centre along the same axis
to the sand. The sand is one straight horizontal line (y=30) from beneath the
canopy to the right edge, kept 8.5+ from the hem; the sea is a smooth three-crest
wave line along the bottom, 9 below the sand.
Deliberate asymmetry: the tilted parasol, as in the reference.
Revision (reviewer: "Make the canopy more semicircular and the horizontal line
between the canopy and waves"): the flattened bezier canopy is now a semicircle,
and the short curved sand stub is a straight horizontal line.
Lucide construction: 'umbrella' - half-disc canopy with a pole; 'waves'.
Keyshape SQUARE: centerline x 6 (canopy) .. 42 (sand, waves), y 6 (finial) .. 42.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "9acf6d75-fd0b-5669-bda9-3051aa82ac0b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__beach-parasol-water/20260926T061914Z-thuan-mac/reference/beach parasol water_9acf6d75-fd0b-5669-bda9-3051aa82ac0b.svg"
AUTHOR = "claude-opus-5-5"


class BeachParasolWater(Solo48):
    icon_id = "beach-parasol-water"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "travel/beach"
    aliases = ("beach-umbrella", "parasol")
    keywords = ("beach", "parasol", "umbrella", "sea", "water", "waves", "summer", "vacation")

    def build(self) -> None:
        hem_a, hem_b, centre, apex = (7, 26), (31, 16), (19, 21), (14, 9)
        self.add_arc("canopy-left", hem_a, apex, radius_x=13, sweep=True)
        self.add_arc("canopy-right", apex, hem_b, radius_x=13, sweep=True)
        self.add_line("hem-right", hem_b, centre)
        self.add_line("hem-left", centre, hem_a)
        self.add_contour("canopy", "canopy-left", "canopy-right", "hem-right", "hem-left", closed=True)
        self.add_line("finial", apex, (13, 6))
        self.relate("connect", "finial", "canopy")
        self.add_line("pole", centre, (23, 30))
        self.relate("connect", "pole", "canopy")
        self.add_polyline("sand", (20, 30), (23, 30), (42, 30))
        self.relate("connect", "pole", "sand")
        self.add_bezier("water", (6, 42),
                        ((9, 42), (9, 39), (12, 39)), ((15, 39), (15, 42), (18, 42)),
                        ((21, 42), (21, 39), (24, 39)), ((27, 39), (27, 42), (30, 42)),
                        ((33, 42), (33, 39), (36, 39)), ((39, 39), (39, 42), (42, 42)))

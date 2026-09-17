"""A check stroke grows into one pointed leaf: a vegetarian leaf-check mark."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "dedaf74d-7497-5c2e-8916-fa8e21f2e9ed"
SOURCE_PATH = "/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/vegetarian check mark_dedaf74d-7497-5c2e-8916-fa8e21f2e9ed.svg"
AUTHOR = "gpt-6"


class LeafCheckMark(Solo48):
    icon_id = "leaf-check-mark"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/food"
    aliases = ("vegetarian-leaf-check",)
    keywords = ("leaf", "check", "vegetarian", "plant", "foliage")

    def build(self):
        # Plan: one pointed lens leaf and its attached check-shaped stem.
        # SQUARE centerline extremes: left 6, top 6, right 42, bottom 42.
        # Two matching quarter-circle shoulders own the leaf radius and join.
        # Lucide leaf informs the flowing outline and integral stem; the source
        # owns the check silhouette. Deliberate upper-right diagonal orientation.
        # Omit the internal vein to keep the pointed leaf's opening generous.
        tip = (42, 6)
        radius = 22
        base = (tip[0] - radius, tip[1] + radius)
        self.add_arc("leaf-upper", base, tip, radius_x=radius)
        self.add_arc("leaf-lower", tip, base, radius_x=radius)
        self.add_contour("leaf", "leaf-upper", "leaf-lower", closed=True)
        self.add_polyline("check-stem", (6, 28), (14, 42), base)
        self.relate("connect", "check-stem", "leaf")

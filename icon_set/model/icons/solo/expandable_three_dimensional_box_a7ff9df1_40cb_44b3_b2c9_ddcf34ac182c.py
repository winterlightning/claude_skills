"""A three-dimensional box expands toward two mirrored lower corners.

SQUARE: centerline extremes (6, 6)-(42, 42), owned by the cube apex
and arrow tips. The root owns the clearance between cube and arrows.
Cube: one closed hexagonal silhouette and three shared-node face seams;
its left/right vertices and both arrow instances mirror about x=24.
Reference: supplied SVG contributes the three visible faces and two detached
outward arrows. Lucide box contributes the hexagonal outline and Y seams;
retain purposeful straight corners, without its small corner arcs.
No identity-carrying features omitted; shorten the cube for arrow clearance.
"""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "a7ff9df1-40cb-44b3-b2c9-ddcf34ac182c"
SOURCE_PATH = "pictographic-primitives/_uncategorized_01/3 d box expand corners_a7ff9df1-40cb-44b3-b2c9-ddcf34ac182c.svg"
AUTHOR = "gpt-6"


class ExpandableThreeDimensionalBox(Solo48):
    icon_id = "expandable-three-dimensional-box"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/uncategorized"
    aliases = ("expandable 3D box", "expand cube")
    keywords = ("box", "cube", "3d", "expand", "resize", "corners", "outward")

    def build(self):
        axis = 24
        mirror = lambda p: (2 * axis - p[0], p[1])
        apex = (axis, 6)
        shoulder_left = (12, 13)
        base_left = (12, 23)
        shoulder_right = mirror(shoulder_left)
        base_right = mirror(base_left)
        base = (axis, 30)
        junction = (axis, 20)

        self.add_polyline("cube-outline", apex, shoulder_right, base_right,
                          base, base_left, shoulder_left, closed=True)
        self.add_polyline("top-seam", shoulder_left, junction, shoulder_right)
        self.add_line("vertical-seam", junction, base)
        self.relate("connect", "cube-outline", "top-seam")
        self.relate("connect", "cube-outline", "vertical-seam")
        self.relate("connect", "top-seam", "vertical-seam")

        for name, transform in (("left", lambda p: p), ("right", mirror)):
            tip = transform((6, 42))
            self.add_polyline(f"{name}-arrowhead", transform((6, 34)),
                              tip, transform((14, 42)))
            self.add_line(f"{name}-shaft", transform((14, 34)), tip)
            self.relate("connect", f"{name}-arrowhead", f"{name}-shaft")

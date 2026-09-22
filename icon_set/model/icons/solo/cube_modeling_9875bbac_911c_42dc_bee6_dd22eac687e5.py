"""A diagonal pencil draws an open three-dimensional cube.

SQUARE centerline envelope (6,6)-(42,42): the cube owns left/bottom
extremes; the pencil owns top/right. Root owns pencil-to-cube clearance.
Cube vertices share a lower junction and an upper-left attachment; its
face seam is one continuous bent run. The pencil
is one pointed closed contour, with parallel sides derived from a shared
diagonal vector. Deliberate asymmetry follows the drawing action.
Supplied reference contributes the open cube and upper-right
pencil. Lucide box informs shared face vertices; Lucide pencil informs the
diagonal body and pointed outline. Omit pencil cap/nib seams at this size.
The reference's circular modeling point was tried, then omitted because its
clearance required shortening cube seams until the cube resembled a die.
"""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "9875bbac-911c-42dc-bee6-dd22eac687e5"
SOURCE_PATH = "pictographic-primitives/_uncategorized_01/3 d pen draw box_9875bbac-911c-42dc-bee6-dd22eac687e5.svg"
AUTHOR = "gpt-6"


class CubeModeling(Solo48):
    icon_id = "cube-modeling"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/uncategorized"
    aliases = ("3D cube modeling", "draw cube", "3D design")
    keywords = ("cube", "box", "modeling", "3d", "pencil", "drawing", "design")

    def build(self):
        left = (6, 18)
        bottom = (18, 42)
        self.add_polyline("cube-outline", (20, 13), (18, 12), left,
                          (6, 34), bottom, (30, 34), (30, 30))
        self.add_polyline("face-seam", left, (18, 26), bottom)
        self.relate("connect", "cube-outline", "face-seam")

        nib_left = (28, 14)
        width = (6, 6)
        length = (8, -8)
        add = lambda a, b: (a[0]+b[0], a[1]+b[1])
        cap_left = add(nib_left, length)
        cap_right = add(cap_left, width)
        nib_right = add(nib_left, width)
        self.add_polyline("pencil", (26, 22), nib_left, cap_left,
                          cap_right, nib_right, closed=True)

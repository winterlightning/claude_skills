"""A three-face cube expands in four cardinal directions.

CIRCLE: arrow tips reach radius 20; the centered cube owns its shared seams.
Keep all three faces and four detached arrows; root owns cube/arrow clearance.
Mirror cube vertices about x=24 and rotate one compact arrow definition four times.
Source supplies composition; Lucide box supplies shared, continuous face junctions.
"""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "c0533ffd-a454-4b10-be0b-3f5c8c0be2bf"
SOURCE_PATH = "pictographic-primitives/_uncategorized_01/3 d box expand_c0533ffd-a454-4b10-be0b-3f5c8c0be2bf.svg"
AUTHOR = "gpt-6"


class Expanding3DCube(Solo48):
    icon_id = "expanding-3d-cube"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("expanding cube", "3D box expand")
    keywords = ("cube", "expand", "scale", "3d", "outward", "arrows")

    def build(self):
        axis = 24
        left, right = axis - 9, axis + 9
        top, bottom = (axis, 14), (axis, 34)
        shoulder_left, shoulder_right = (left, 19), (right, 19)
        center = (axis, 24)
        self.add_polyline("cube-outline", top, shoulder_right, (right, 29),
                          bottom, (left, 29), shoulder_left, closed=True)
        self.add_polyline("face-seams", shoulder_left, center, shoulder_right)
        self.add_line("front-seam", center, bottom)
        self.relate("connect", "cube-outline", "face-seams")
        self.relate("connect", "front-seam", "face-seams")
        self.relate("connect", "front-seam", "cube-outline")

        for index, direction in enumerate(("up", "right", "down", "left")):
            def rotate(point):
                x, y = point[0] - axis, point[1] - axis
                for _ in range(index):
                    x, y = -y, x
                return (axis + x, axis + y)
            tip = rotate((24, 4))
            self.add_polyline(direction + "-head", rotate((20, 6)), tip,
                              rotate((28, 6)))
            self.add_line(direction + "-shaft", tip, rotate((24, 6)))
            self.relate("connect", direction + "-head", direction + "-shaft")

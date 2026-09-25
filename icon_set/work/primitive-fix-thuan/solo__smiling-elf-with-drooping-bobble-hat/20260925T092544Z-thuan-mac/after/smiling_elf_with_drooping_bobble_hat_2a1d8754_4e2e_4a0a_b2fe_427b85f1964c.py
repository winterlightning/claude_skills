"""Smiling elf head: rounded face with pointed ears, two dot eyes and a smile,
under a bobble hat whose tip droops to the right onto a small pompom.

Symbol plan: face contour mirrored about x=24 (ears, straight cheeks, half-
ellipse jaw); the hat brim is the face's top edge and is shared by the hat
contour; the pompom circle shares the hat tip's two end points.
Keyshape VRECT_L: ear tips x=8/40, pompom top y=4, chin y=44.
Human reference: user.svg head proportions (face only, no body).
Lucide construction: smile (dot eyes + shallow smile arc) and a rounded cap.
Revision of the rejected drawing ("Bad stroke drawn"): the old drawing had a
filled blob mouth, no eyes and a spiral hat tip; here the features are clean
strokes with even spacing.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2a1d8754-4e2e-4a0a-b2fe-427b85f1964c"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__smiling-elf-with-drooping-bobble-hat/20260925T092544Z-thuan-mac/reference/elf_2a1d8754-4e2e-4a0a-b2fe-427b85f1964c.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
BRIM = 16
POM = (38, 6)
POM_R = 2


def m(point):
    return (2 * AXIS - point[0], point[1])


class SmilingElfWithDroopingBobbleHat(Solo48):
    icon_id = "smiling-elf-with-drooping-bobble-hat"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("elf",)
    keywords = ("elf", "christmas", "hat", "pointed ears", "fantasy", "character", "smile")

    def path(self, name, start, steps, closed=False):
        members = []
        for index, (kind, *args) in enumerate(steps):
            tag = f"{name}-{index + 1}"
            if kind == "L":
                end = args[0]
                self.add_line(tag, start, end)
            elif kind == "C":
                c1, c2, end = args
                self.add_bezier(tag, start, (c1, c2, end))
            else:
                end, rx, ry, sweep = args
                self.add_arc(tag, start, end, radius_x=rx, radius_y=ry, sweep=sweep)
            start = end
            members.append(tag)
        self.add_contour(name, *members, closed=closed)

    def build(self) -> None:
        # Face: right brim corner -> right ear -> jaw -> left ear -> left brim corner.
        self.path("face", m((12, BRIM)), [
            ("L", m((8, 16))),                                   # right ear top edge
            ("C", m((8.5, 21)), m((10, 25)), m((11, 27))),       # right ear lower edge
            ("L", m((11, 34))),                                  # right cheek
            ("A", (AXIS, 44), 13, 10, True),        # jaw to chin
            ("A", (11, 34), 13, 10, True),
            ("L", (11, 27)),                                     # left cheek
            ("C", (10, 25), (8.5, 21), (8, 16)),                 # left ear lower edge
            ("L", (12, BRIM)),                                   # left ear top edge
        ])
        px, py = POM
        self.path("hat", (px, py + POM_R), [
            ("C", (38, 10), (36, 13), m((12, BRIM))),            # drooping back of the hat
            ("L", (12, BRIM)),                                   # brim
            ("C", (12, 9), (17, 5), (AXIS, 5)),                 # front of the hat to the crown
            ("C", (30, 5), (34, 5.5), (px - POM_R, py)),         # tip drooping into the pompom
        ])
        self.path("pompom", (px - POM_R, py), [
            ("A", (px, py - POM_R), POM_R, POM_R, True),
            ("A", (px + POM_R, py), POM_R, POM_R, True),
            ("A", (px, py + POM_R), POM_R, POM_R, True),
            ("A", (px - POM_R, py), POM_R, POM_R, True),
        ], closed=True)
        self.relate("connect", "hat", "face")
        self.relate("connect", "hat", "pompom")
        self.add_dot("eye-left", (20, 25))
        self.add_dot("eye-right", m((20, 25)))
        self.add_arc("smile", (20, 34), m((20, 34)), radius_x=6, sweep=False)

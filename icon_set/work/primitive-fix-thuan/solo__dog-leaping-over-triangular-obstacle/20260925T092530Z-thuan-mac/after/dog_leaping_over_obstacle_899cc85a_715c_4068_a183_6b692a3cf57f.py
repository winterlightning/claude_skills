"""Dog race: a dog in mid-leap, facing right with legs stretched fore and
aft and tail raised, clearing a triangular jump obstacle beneath it.

Symbol plan: the dog's torso and head are one closed outline (back, neck,
head, snout, throat, chest, belly, rump) of integer nodes joined by lines
and tangent cubics. Stretched legs and the raised tail are single strokes
leaving outline nodes at wide angles so no wedges form. The obstacle is a
separate closed triangle whose apex sits more than 8 below the belly.
Deliberately asymmetric (motion to the right).
Keyshape SQUARE, centerline box (6,6)-(42,42).
Lucide construction: no leaping dog; rabbit/squirrel side-silhouette
construction (one body outline plus stroke limbs) informed the drawing.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "899cc85a-715c-4068-a183-6b692a3cf57f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__dog-leaping-over-triangular-obstacle/20260925T092530Z-thuan-mac/reference/dog race compettion 2_899cc85a-715c-4068-a183-6b692a3cf57f.svg"
AUTHOR = "claude-opus-5-5"


class DogLeapingOverObstacle(Solo48):
    icon_id = "dog-leaping-over-triangular-obstacle"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ("dog race", "dog agility", "dog competition")
    keywords = ("dog", "race", "competition", "agility", "jump", "obstacle")

    def build(self) -> None:
        rump = (14, 14)
        hip = (13, 20)
        chest = (32, 21)
        self.path("dog", rump, [
            ("L", (25, 13)),                                  # back
            ("C", (28, 13), (29, 6), (33, 6)),                # neck to crown
            ("C", (36, 6), (37, 9), (42, 11)),                # forehead to snout tip
            ("C", (42, 14), (38, 15), (35, 15)),              # muzzle underside
            ("C", (34, 17), (34, 20), chest),                 # throat to chest
            ("L", (18, 22)),                                  # belly
            ("C", (15, 22), (13, 22), hip),                   # rump underside
            ("C", (12, 17), (12, 15), rump),                  # rump back
        ], closed=True)
        self.path("tail", rump, [("C", (12, 10), (10, 7), (7, 6))])
        self.add_line("front-legs", chest, (41, 25))
        self.add_line("hind-legs", hip, (6, 26))
        for part in ("tail", "front-legs", "hind-legs"):
            self.relate("connect", "dog", part)
        self.add_polyline("obstacle", (24, 31), (33, 42), (15, 42), closed=True)

    def path(self, name, start, commands, closed=False):
        members = []
        here = start
        for index, (kind, *args) in enumerate(commands):
            member = f"{name}-{index + 1}"
            if kind == "L":
                self.add_line(member, here, args[0])
                here = args[0]
            else:
                self.add_bezier(member, here, (args[0], args[1], args[2]))
                here = args[2]
            members.append(member)
        self.add_contour(name, *members, closed=closed)

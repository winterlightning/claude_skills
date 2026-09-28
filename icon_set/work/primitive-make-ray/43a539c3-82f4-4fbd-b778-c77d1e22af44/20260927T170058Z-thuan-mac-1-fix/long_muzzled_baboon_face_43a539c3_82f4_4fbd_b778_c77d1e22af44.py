"""Long-muzzled baboon face, front view.

Plan: mirrored about x=24. One closed head outline: domed crown, round ear
bumps (r4) on both sides, then long cheeks tapering to a flat chin. Inside,
the baboon's long muzzle patch: a rounded brow over two straight sides that narrow to a rounded snout. Eye dots and the nose line do
not fit 8u inside the patch at 48 and are dropped. Keyshape SQUARE: ears
x=6/42, crown y=6, chin y=42.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "43a539c3-82f4-4fbd-b778-c77d1e22af44"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__long-muzzled-baboon-face/20260927T164623Z-thuan-mac-1/reference/baboon_43a539c3-82f4-4fbd-b778-c77d1e22af44.svg"
AUTHOR = "claude-opus-5-5"


class LongMuzzledBaboonFace(Solo48):
    icon_id = "long-muzzled-baboon-face"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('baboon', 'monkey face', 'mandrill')
    keywords = ('baboon', 'monkey', 'primate', 'ape', 'face', 'animal')

    def path(self, name, start, steps, closed=False):
        here, members = start, []
        for j, (kind, end, *args) in enumerate(steps):
            member = f"{name}-{j}"
            if kind == "L":
                self.add_line(member, here, end)
            elif kind == "A":
                self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2],
                             large_arc=args[3] if len(args) > 3 else False)
            else:
                self.add_bezier(member, here, (args[0], args[1], end))
            here = end
            members.append(member)
        self.add_contour(name, *members, closed=closed)

    def build(self) -> None:

        self.path("head", (24, 6), [
            ("C", (38, 12), (31, 6), (36, 8)),
            ("A", (38, 20), 4, 4, True),               # right ear
            ("C", (28, 42), (38, 32), (35, 41)),       # right cheek
            ("L", (20, 42)),                           # chin
            ("C", (10, 20), (13, 41), (10, 32)),       # left cheek
            ("A", (10, 12), 4, 4, True),               # left ear
            ("C", (24, 6), (12, 8), (17, 6)),
        ], closed=True)
        self.path("muzzle", (24, 15), [
            ("C", (30, 18), (27, 15), (30, 15.5)),     # right brow
            ("C", (28, 24), (30, 20), (28, 22)),
            ("L", (28, 29)),
            ("A", (20, 29), 4, 4, True),               # snout
            ("L", (20, 24)),
            ("C", (18, 18), (20, 22), (18, 20)),
            ("C", (24, 15), (18, 15.5), (21, 15)),     # left brow
        ], closed=True)

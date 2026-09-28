"""Manual typewriter, front view.

Plan: mirrored about x=24. A paper sheet with r4 top corners rises out of a
wide platen roller (capsule x 6-42, y 14-22) that overhangs the body; the
body is an open U hung from the roller at x=13/35 with r4 bottom corners, and
the typebar basket is a deep r12 arc hung from the
roller at the wall tops. Side knobs omitted (no 8u room beside the roller). Keyshape SQUARE:
roller x=6/42, paper y=6, base y=42.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "529f66ce-bbc1-4b10-b496-db11d5c10c2e"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__manual-typewriter-batch-078/20260927T164623Z-thuan-mac-1/reference/typing machine 1_529f66ce-bbc1-4b10-b496-db11d5c10c2e.svg"
AUTHOR = "claude-opus-5-5"


class ManualTypewriter(Solo48):
    icon_id = "manual-typewriter-batch-078"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('typing machine', 'typewriter')
    keywords = ('typewriter', 'typing', 'writer', 'vintage', 'keyboard', 'machine')

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

        self.path("paper", (14, 14), [
            ("L", (14, 10)),
            ("A", (18, 6), 4, 4, True),
            ("L", (30, 6)),
            ("A", (34, 10), 4, 4, True),
            ("L", (34, 14)),
        ])
        self.path("roller", (10, 14), [
            ("L", (14, 14)), ("L", (34, 14)), ("L", (38, 14)),
            ("A", (38, 22), 4, 4, True),
            ("L", (35, 22)), ("L", (13, 22)), ("L", (10, 22)),
            ("A", (10, 14), 4, 4, True),
        ], closed=True)
        self.relate("connect", "roller", "paper")
        self.path("body", (13, 22), [
            ("L", (13, 38)),
            ("A", (17, 42), 4, 4, False),
            ("L", (31, 42)),
            ("A", (35, 38), 4, 4, False),
            ("L", (35, 22)),
        ])
        self.relate("connect", "roller", "body")
        self.path("basket", (13, 22), [("A", (35, 22), 12, 12, False)])
        self.relate("connect", "roller", "basket")
        self.relate("connect", "body", "basket")

"""Megaphone (bullhorn) facing right.

Plan: mirrored about y=24 except the grip. A mouthpiece with r4 rounded back
(x 6-18, y 18-30) and a separator line at x=18; the horn flares from the
mouthpiece to a tall bell (x=42) with r4 bell corners; a slanted single-stroke
grip drops from under the mouthpiece to the bottom edge, as in the reference.
Keyshape SQUARE: back x=6, bell x=42, bell y=6/42.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "bac73377-8266-4be0-ab30-2c147588004d"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__megaphone-reference-bac73377/20260927T164623Z-thuan-mac-1/reference/ligula_bac73377-8266-4be0-ab30-2c147588004d.svg"
AUTHOR = "claude-opus-5-5"


class MegaphoneReference(Solo48):
    icon_id = "megaphone-reference-bac73377"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('ligula', 'bullhorn', 'loudspeaker')
    keywords = ('megaphone', 'bullhorn', 'announce', 'loud', 'marketing', 'speaker')

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

        self.path("body", (18, 18), [
            ("L", (38, 6)),                            # horn top
            ("A", (42, 10), 4, 4, True),
            ("L", (42, 38)),                           # bell
            ("A", (38, 42), 4, 4, True),
            ("L", (18, 30)),                           # horn bottom
            ("L", (13, 30)),
            ("L", (10, 30)),
            ("A", (6, 26), 4, 4, True),                # mouthpiece back
            ("L", (6, 22)),
            ("A", (10, 18), 4, 4, True),
            ("L", (18, 18)),
        ], closed=True)
        self.add_line("separator", (18, 18), (18, 30))
        self.add_line("grip", (13, 30), (10, 42))
        self.relate("connect", "body", "separator")
        self.relate("connect", "body", "grip")

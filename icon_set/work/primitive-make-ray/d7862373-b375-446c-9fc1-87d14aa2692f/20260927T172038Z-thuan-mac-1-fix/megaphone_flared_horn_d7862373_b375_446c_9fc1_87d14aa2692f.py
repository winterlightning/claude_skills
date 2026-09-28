"""Megaphone with a flared horn, tilted upward.

Plan: follows the reference's tilt: the horn's top edge climbs steeply to
the bell while the bottom edge stays almost level, so the bell edge
B1=(36,6)-B2=(42,38) leans like the mouth ring M1=(14,20)-M2=(16,30) (both
about 1:5). The mouthpiece runs back from the ring and closes with a round
back (two cubics through the leftmost vertex (6,26)). A separator marks the
mouth ring and a slanted grip drops from M2 to the bottom edge.
Keyshape SQUARE.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d7862373-b375-446c-9fc1-87d14aa2692f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__megaphone-flared-horn/20260927T164623Z-thuan-mac-1/reference/advertising megaphone_d7862373-b375-446c-9fc1-87d14aa2692f.svg"
AUTHOR = "claude-opus-5-5"


class MegaphoneFlaredHorn(Solo48):
    icon_id = "megaphone-flared-horn"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('advertising megaphone', 'bullhorn')
    keywords = ('megaphone', 'bullhorn', 'advertising', 'announce', 'marketing', 'loud')

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

        m1, m2, b1, b2 = (14, 20), (16, 30), (36, 6), (42, 38)
        self.path("body", m1, [
            ("L", b1),                                 # horn top
            ("L", b2),                                 # bell
            ("L", m2),                                 # horn bottom
            ("L", (11, 31)),                           # mouthpiece bottom
            ("C", (6, 26), (8, 32), (6, 29)),          # round back
            ("C", (9, 21), (6, 23), (7, 21.5)),
            ("L", m1),                                 # mouthpiece top
        ], closed=True)
        self.add_line("separator", m1, m2)
        self.add_line("grip", m2, (13, 42))
        self.relate("connect", "body", "separator")
        self.relate("connect", "body", "grip")

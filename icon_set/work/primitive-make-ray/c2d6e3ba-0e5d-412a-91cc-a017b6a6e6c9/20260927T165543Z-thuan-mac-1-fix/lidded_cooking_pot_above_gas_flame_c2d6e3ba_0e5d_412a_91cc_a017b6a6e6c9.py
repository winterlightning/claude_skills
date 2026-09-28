"""Lidded cooking pot above a gas flame.

Plan: mirrored about x=24. Domed knob (semicircle r6) on a lid line that
overhangs the pot walls; pot walls x=13/35 with r4 bottom corners; short side
handles at y=18 reach the keyshape sides; below an 8 gap, a three-tip gas
flame (tall centre tip, two shoulder tips) with a rounded base. Keyshape
VRECT_L: handles x=8/40, knob y=4, flame base y=44.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "c2d6e3ba-0e5d-412a-91cc-a017b6a6e6c9"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__lidded-cooking-pot-above-gas-flame/20260927T164623Z-thuan-mac-1/reference/stove steamer gas_c2d6e3ba-0e5d-412a-91cc-a017b6a6e6c9.svg"
AUTHOR = "claude-opus-5-5"


class LiddedCookingPotAboveGasFlame(Solo48):
    icon_id = "lidded-cooking-pot-above-gas-flame"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('stove steamer gas', 'pot on stove')
    keywords = ('pot', 'cooking', 'stove', 'gas', 'flame', 'kitchen', 'boil')

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

        self.path("lid", (10, 10), [("L", (13, 10)), ("L", (18, 10)), ("L", (30, 10)), ("L", (35, 10)), ("L", (38, 10))])
        self.path("knob", (18, 10), [("A", (30, 10), 6, 6, True)])
        self.path("pot", (13, 10), [
            ("L", (13, 18)),
            ("L", (13, 20)),
            ("A", (17, 24), 4, 4, False),
            ("L", (31, 24)),
            ("A", (35, 20), 4, 4, False),
            ("L", (35, 18)),
            ("L", (35, 10)),
        ])
        self.add_line("handle-l", (8, 18), (13, 18))
        self.add_line("handle-r", (35, 18), (40, 18))
        for part in ("knob", "pot"):
            self.relate("connect", "lid", part)
        self.relate("connect", "pot", "handle-l")
        self.relate("connect", "pot", "handle-r")
        self.path("flame", (24, 32), [
            ("L", (26, 38)),
            ("L", (31, 34)),                           # right shoulder tip
            ("C", (24, 44), (35, 39), (30, 44)),       # rounded flank and base
            ("C", (17, 34), (18, 44), (13, 39)),
            ("L", (22, 38)),                           # left shoulder tip
            ("L", (24, 32)),                           # centre tip
        ], closed=True)

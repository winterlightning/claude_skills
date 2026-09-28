"""Looping sewing thread.

Plan: one continuous thread. The top tail ends in a small hook at the upper
left, runs down into the crossing node C=(24,24) heading down-right, loops
round a large right lobe (quarter cubics through bottom, right and top
extremes) and passes back through C heading down-left, then sweeps down to a
turned-up end at the bottom. The crossing is a shared node, so the four
strands meet exactly. Keyshape SQUARE: hook x=6, lobe x=42, top y=6,
bottom y=42.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "44e88e9d-a0d5-432e-b08f-05a0b1522e97"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__looping-sewing-thread/20260927T164623Z-thuan-mac-1/reference/crafts sewing_44e88e9d-a0d5-432e-b08f-05a0b1522e97.svg"
AUTHOR = "claude-opus-5-5"


class LoopingSewingThread(Solo48):
    icon_id = "looping-sewing-thread"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('crafts sewing', 'loose thread')
    keywords = ('thread', 'sewing', 'craft', 'yarn', 'string', 'loop')

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

        k = 0.5523
        c = (24, 24)
        self.path("thread", (6, 12), [
            ("A", (12, 6), 6, 6, True),                # hook
            ("C", c, (18, 6), (20, 20)),               # top tail into the crossing
            ("C", (33, 34), (28, 28), (29, 34)),
            ("C", (42, 24), (33 + 9 * k, 34), (42, 24 + 10 * k)),
            ("C", (33, 14), (42, 24 - 10 * k), (33 + 9 * k, 14)),
            ("C", c, (29, 14), (28, 20)),              # back through the crossing
            ("C", (14, 38), (20, 28), (14, 32)),       # bottom tail
            ("C", (24, 42), (14, 42), (20, 42)),       # turned-up end
        ])

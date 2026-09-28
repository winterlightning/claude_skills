"""Low battery level.

Plan: a wide horizontal battery like the reference: one closed outline with
r4 body corners running straight into a centred r2-cornered terminal nub (no
inner wall), and a single low-charge bar at the left, 9 from the walls.
Mirrored about y=24. Keyshape HRECT_M: body x=4, terminal x=44, y=10/38.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "058db2e8-12db-48c2-b344-337f39e8f77d"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__low-battery-level/20260927T164623Z-thuan-mac-1/reference/charging battery low_058db2e8-12db-48c2-b344-337f39e8f77d.svg"
AUTHOR = "claude-opus-5-5"


class LowBatteryLevel(Solo48):
    icon_id = "low-battery-level"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('charging battery low', 'battery low')
    keywords = ('battery', 'low', 'power', 'charge', 'energy', 'status')

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

        self.path("battery", (8, 10), [
            ("L", (34, 10)),
            ("A", (38, 14), 4, 4, True),
            ("L", (38, 18)),
            ("L", (42, 18)),
            ("A", (44, 20), 2, 2, True),
            ("L", (44, 28)),
            ("A", (42, 30), 2, 2, True),
            ("L", (38, 30)),
            ("L", (38, 34)),
            ("A", (34, 38), 4, 4, True),
            ("L", (8, 38)),
            ("A", (4, 34), 4, 4, True),
            ("L", (4, 14)),
            ("A", (8, 10), 4, 4, True),
        ], closed=True)
        self.add_line("level", (13, 19), (13, 29))

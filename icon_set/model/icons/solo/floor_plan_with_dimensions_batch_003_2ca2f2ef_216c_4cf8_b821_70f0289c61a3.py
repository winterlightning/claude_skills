"""floor-plan-with-dimensions-batch-003: independent batch-003 SOLO48 result for brief 04.

Subject: A rounded square floor plan with two corner rooms, dimensioned by a width arrow above and a height arrow at the left.
Keyshape: SQUARE -- plan plus arrows form a square block.
Plan: Plan 20..42 with r=2 corners; rooms on an 8-unit pitch at opposite corners; arrow shafts span the plan exactly with 45-degree heads.
Reduction: The reference's two small lower-right rooms are merged into one 8x8 room; a 7-unit split would break the 8-unit spacing.
Construction reference: ruler-dimension-line / move-horizontal (double-headed dimension arrows).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ca2f2ef-216c-4cf8-b821-70f0289c61a3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/construction/real estate dimensions block_2ca2f2ef-216c-4cf8-b821-70f0289c61a3.svg'
AUTHOR = "claude-opus-5"
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/references/real estate dimensions block_2ca2f2ef-216c-4cf8-b821-70f0289c61a3.svg'
BRIEF = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/04-floor-plan-dimensions--2ca2f2ef-216c-4cf8-b821-70f0289c61a3.md'


class FloorPlanWithDimensionsBatch003(Solo48):
    icon_id = 'floor-plan-with-dimensions-batch-003'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('floor', 'plan', 'dimensions', 'architecture', 'room', 'measurement', 'real-estate')

    # -- local construction helpers ------------------------------------------
    def _run(self, name, start, commands, closed=False):
        """One stroke run: ('L', end) lines, ('A', end, rx, ry, sweep[, large]) arcs,
        ('C', end, c1, c2) cubics. Members are grouped into one contour."""
        here, members = start, []
        for index, (kind, end, *args) in enumerate(commands, 1):
            ident = f"{name}-{index}"
            if kind == "L":
                self.add_line(ident, here, end)
            elif kind == "A":
                rx, ry, sweep = args[:3]
                large = args[3] if len(args) > 3 else False
                self.add_arc(ident, here, end, radius_x=rx, radius_y=ry, sweep=sweep, large_arc=large)
            elif kind == "C":
                self.add_bezier(ident, here, (args[0], args[1], end))
            members.append(ident)
            here = end
        self.add_contour(name, *members, closed=closed)
        return members

    def _circle(self, name, cx, cy, r):
        self._run(name, (cx - r, cy), [("A", (cx + r, cy), r, r, True), ("A", (cx - r, cy), r, r, True)], closed=True)

    def build(self) -> None:
        # Plan block 20..42 (r=2); rooms on an 8-unit pitch at opposite corners.
        p0, p1, r = 20, 42, 2
        room, room2 = 28, 34
        self._run("plan", (p0 + r, p0), [
            ("L", (room, p0)), ("L", (p1 - r, p0)), ("A", (p1, p0 + r), r, r, True),
            ("L", (p1, room2)), ("L", (p1, p1 - r)), ("A", (p1 - r, p1), r, r, True),
            ("L", (room2, p1)), ("L", (p0 + r, p1)), ("A", (p0, p1 - r), r, r, True),
            ("L", (p0, room)), ("L", (p0, p0 + r)), ("A", (p0 + r, p0), r, r, True)], closed=True)
        self._run("room-top-left", (room, p0), [("L", (room, room)), ("L", (p0, room))])
        self._run("room-bottom-right", (p1, room2), [("L", (room2, room2)), ("L", (room2, p1))])
        self.relate("connect", "plan", "room-top-left")
        self.relate("connect", "plan", "room-bottom-right")
        # Dimension arrows: shafts span the plan exactly; 45-degree heads reaching 3.
        ay, ax, h = 9, 9, 3
        self.add_line("width-shaft", (p0, ay), (p1, ay))
        self.add_polyline("width-head-start", (p0 + h, ay - h), (p0, ay), (p0 + h, ay + h))
        self.add_polyline("width-head-end", (p1 - h, ay - h), (p1, ay), (p1 - h, ay + h))
        self.add_line("height-shaft", (ax, p0), (ax, p1))
        self.add_polyline("height-head-start", (ax - h, p0 + h), (ax, p0), (ax + h, p0 + h))
        self.add_polyline("height-head-end", (ax - h, p1 - h), (ax, p1), (ax + h, p1 - h))
        for axis in ("width", "height"):
            self.relate("connect", f"{axis}-shaft", f"{axis}-head-start")
            self.relate("connect", f"{axis}-shaft", f"{axis}-head-end")

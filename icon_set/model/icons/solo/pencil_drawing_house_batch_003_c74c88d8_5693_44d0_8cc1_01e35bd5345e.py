"""pencil-drawing-house-batch-003: independent batch-003 SOLO48 result for brief 05.

Subject: A diagonal pencil pointing down-left toward a broken drawing line above a small house with an arched door.
Keyshape: SQUARE -- the scene fills a square: house lower-left, pencil upper-right.
Plan: House axis x=17: walls 6..28, 45-degree roof apex (17,21), r=3 arched door notch in the floor; pencil on a (2,-1) axis with a 90-degree tip and a ferrule band; two dashes at y=13 end 8 short of the tip.
Reduction: Roof overhang omitted and dashes kept short: longer dashes or eaves would close gaps below the 8-unit minimum.
Construction reference: pencil (tip and body construction) and house (door in the floor line).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c74c88d8-5693-44d0-8cc1-01e35bd5345e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/construction/project plan pen_c74c88d8-5693-44d0-8cc1-01e35bd5345e.svg'
AUTHOR = "claude-opus-5"
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/references/project plan pen_c74c88d8-5693-44d0-8cc1-01e35bd5345e.svg'
BRIEF = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/05-pencil-drawing-house-plan--c74c88d8-5693-44d0-8cc1-01e35bd5345e.md'


class PencilDrawingHouseBatch003(Solo48):
    icon_id = 'pencil-drawing-house-batch-003'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('pencil', 'house', 'drawing', 'architecture', 'plan', 'design', 'project')

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
        # House: axis x=17, walls 6..28, eaves y=32, 45-degree roof, r=3 arched door notch in the floor.
        w0, w1, ax, eave, floor, door_r = 6, 28, 17, 32, 42, 3
        apex = (ax, eave - (ax - w0))
        self._run("house", (w0, eave), [
            ("L", apex), ("L", (w1, eave)), ("L", (w1, floor)), ("L", (ax + door_r, floor)),
            ("A", (ax - door_r, floor), door_r, door_r, False), ("L", (w0, floor)), ("L", (w0, eave))], closed=True)
        # Pencil on a (2,-1) axis with half-width offset (2,4): tip (26,17), end centre (40,10).
        # A 67-degree tip three steps long, then a body of four steps (8.94 x 8.94).
        tip = (26, 17)
        self._run("pencil", tip, [("L", (30, 10)), ("L", (38, 6)), ("L", (42, 14)), ("L", (34, 18)), ("L", tip)], closed=True)
        # Broken drawing line above the roof, ending 8 short of the pencil tip.
        self.add_line("dash-start", (6, 13), (8, 13))
        self.add_line("dash-end", (16, 13), (18, 13))

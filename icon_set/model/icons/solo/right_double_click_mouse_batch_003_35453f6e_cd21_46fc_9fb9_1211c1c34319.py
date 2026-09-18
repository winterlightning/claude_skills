"""right-double-click-mouse-batch-003: independent batch-003 SOLO48 result for brief 02.

Subject: An upright capsule mouse with its right button outlined and two click ripples at its upper right.
Keyshape: VRECT_L -- the mouse is taller than wide and the ripples reach the top-right corner.
Plan: Capsule body (axis x=16, r=8); seam drops from the top apex and turns right into the button boundary; ripples concentric with the top arc at r=17 and r=26.
Reduction: Ripples keep 9 units between mouse, inner and outer arc.
Construction reference: mouse-right (split seam and right-button boundary).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35453f6e-cd21-46fc-9fb9-1211c1c34319'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/computers/batch-06/right double click mouse_35453f6e-cd21-46fc-9fb9-1211c1c34319.svg'
AUTHOR = "claude-opus-5"
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/references/right double click mouse_35453f6e-cd21-46fc-9fb9-1211c1c34319.svg'
BRIEF = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/02-double-right-click-mouse--35453f6e-cd21-46fc-9fb9-1211c1c34319.md'


class RightDoubleClickMouseBatch003(Solo48):
    icon_id = 'right-double-click-mouse-batch-003'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'computers'
    aliases = ()
    keywords = ('mouse', 'click', 'double', 'right', 'computer', 'input')

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
        # Capsule mouse: axis x=16, r=8; top arc centre (16,28), bottom arc centre (16,36).
        cx, r, top_c, bot_c = 16, 8, 28, 36
        seam_y, seam_r = 30, 4
        self._run("body", (cx, top_c - r), [
            ("A", (cx + r, top_c), r, r, True),
            ("L", (cx + r, seam_y)), ("L", (cx + r, bot_c)),
            ("A", (cx, bot_c + r), r, r, True), ("A", (cx - r, bot_c), r, r, True),
            ("L", (cx - r, top_c)), ("A", (cx, top_c - r), r, r, True)], closed=True)
        # Seam: down from the apex, quarter-turn right into the right-button boundary.
        self._run("seam", (cx, top_c - r), [
            ("L", (cx, seam_y - seam_r)), ("A", (cx + seam_r, seam_y), seam_r, seam_r, False),
            ("L", (cx + r, seam_y))])
        self.relate("connect", "body", "seam")
        # Double-click ripples concentric with the top arc (r=8 -> 17 -> 26, 9 apart).
        self._run("click-inner", (cx + 8, top_c - 15), [("A", (cx + 15, top_c - 8), 17, 17, True)])
        self._run("click-outer", (cx + 10, top_c - 24), [("A", (cx + 24, top_c - 10), 26, 26, True)])

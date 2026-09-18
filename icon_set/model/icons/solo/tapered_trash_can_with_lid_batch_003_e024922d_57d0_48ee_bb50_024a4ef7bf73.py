"""tapered-trash-can-with-lid-batch-003: independent batch-003 SOLO48 result for brief 12.

Subject: A tapered trash bin with a wide lid line and a rounded handle on top.
Keyshape: VRECT_L -- an upright bin.
Plan: Lid line 8..40 at y=12; handle 18..30 by 8 tall; body tapers from 10/38 at the lid to 14/34 at the base.
Reduction: Base corners use round joins rather than small arcs on the sloped walls.
Construction reference: trash (lid, handle and body construction).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e024922d-57d0-48ee-bb50-024a4ef7bf73'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/container/trash 3_e024922d-57d0-48ee-bb50-024a4ef7bf73.svg'
AUTHOR = "claude-opus-5"
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/references/trash 3_e024922d-57d0-48ee-bb50-024a4ef7bf73.svg'
BRIEF = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/12-trash-can-with-lid--e024922d-57d0-48ee-bb50-024a4ef7bf73.md'


class TaperedTrashCanWithLidBatch003(Solo48):
    icon_id = 'tapered-trash-can-with-lid-batch-003'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'container'
    aliases = ()
    keywords = ('trash', 'bin', 'garbage', 'delete', 'waste', 'lid', 'tapered')

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
        # Lid line 8..40 at y=12; handle 18..30 x 4..12; body tapers 10/38 -> 14/34.
        lid_y, l0, l1 = 12, 8, 40
        h0, h1, ht, hr = 18, 30, 4, 2
        self.add_polyline("lid", (l0, lid_y), (10, lid_y), (h0, lid_y), (h1, lid_y), (38, lid_y), (l1, lid_y))
        self._run("handle", (h0, lid_y), [
            ("L", (h0, ht + hr)), ("A", (h0 + hr, ht), hr, hr, True), ("L", (h1 - hr, ht)),
            ("A", (h1, ht + hr), hr, hr, True), ("L", (h1, lid_y))])
        self.add_polyline("body", (38, lid_y), (34, 44), (14, 44), (10, lid_y))
        self.relate("connect", "lid", "handle")
        self.relate("connect", "lid", "body")

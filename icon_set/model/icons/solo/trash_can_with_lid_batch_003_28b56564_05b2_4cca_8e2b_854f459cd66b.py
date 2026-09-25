"""trash-can-with-lid-batch-003: independent batch-003 SOLO48 result for brief 11.

Subject: A straight-sided trash bin with a wide lid line and a rounded handle on top.
Keyshape: VRECT_L -- an upright bin.
Plan: Lid line 8..40 at y=12; handle 18..30 by 8 tall; body walls 11/37 with r=4 base corners; all joins share lid endpoints.
Reduction: As in the reference: no ribs.
Construction reference: trash (lid, handle and body construction).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '28b56564-05b2-4cca-8e2b-854f459cd66b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/container/trash 1_28b56564-05b2-4cca-8e2b-854f459cd66b.svg'
AUTHOR = "claude-opus-5"
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/references/trash 1_28b56564-05b2-4cca-8e2b-854f459cd66b.svg'
BRIEF = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/11-trash-can-with-lid--28b56564-05b2-4cca-8e2b-854f459cd66b.md'


class TrashCanWithLidBatch003(Solo48):
    icon_id = 'trash-can-with-lid-batch-003'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('trash', 'bin', 'garbage', 'delete', 'waste', 'lid')

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
        # Lid line 8..40 at y=12; handle 18..30 x 4..12; straight body walls at 11 and 37.
        lid_y, l0, l1 = 12, 8, 40
        h0, h1, ht, hr = 18, 30, 4, 2
        b0, b1, bb, br = 11, 37, 44, 4
        self.add_polyline("lid", (l0, lid_y), (b0, lid_y), (h0, lid_y), (h1, lid_y), (b1, lid_y), (l1, lid_y))
        self._run("handle", (h0, lid_y), [
            ("L", (h0, ht + hr)), ("A", (h0 + hr, ht), hr, hr, True), ("L", (h1 - hr, ht)),
            ("A", (h1, ht + hr), hr, hr, True), ("L", (h1, lid_y))])
        self._run("body", (b1, lid_y), [
            ("L", (b1, bb - br)), ("A", (b1 - br, bb), br, br, True), ("L", (b0 + br, bb)),
            ("A", (b0, bb - br), br, br, True), ("L", (b0, lid_y))])
        self.relate("connect", "lid", "handle")
        self.relate("connect", "lid", "body")

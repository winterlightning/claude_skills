"""captive-bead-ring-jewelry-batch-003: independent batch-003 SOLO48 result for brief 07.

Subject: A captive bead ring: an open hoop whose two ends clamp a round bead at the bottom.
Keyshape: CIRCLE -- radial subject; the bead's base touches the circular bound.
Plan: Bead r=5 at (24,39); hoop r=15 passes through the bead points (20,36) and (28,36), where the bead is split and each join is declared.
Reduction: Variant of brief 06 (same subject, separate result): the bead is seated between the ring ends instead of floating in the gap.
Construction reference: circle-dot (ring with an inner element); the seated join is original construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47a67469-8ea2-48c7-aa8a-95fc823049c7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/container/circle top circle 1_47a67469-8ea2-48c7-aa8a-95fc823049c7.svg'
AUTHOR = "claude-opus-5"
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/references/circle top circle 1_47a67469-8ea2-48c7-aa8a-95fc823049c7.svg'
BRIEF = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/07-captive-bead-ring-jewelry--47a67469-8ea2-48c7-aa8a-95fc823049c7.md'


class CaptiveBeadRingJewelryBatch003(Solo48):
    icon_id = 'captive-bead-ring-jewelry-batch-003'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('captive', 'bead', 'ring', 'jewelry', 'piercing', 'hoop')

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
        # Bead r=5 at (24,39); its base (24,44) reaches the radial bound.
        bx, by, br = 24, 39, 5
        left_join, right_join = (bx - 4, by - 3), (bx + 4, by - 3)  # integer points on the bead
        # Hoop r=15 through both joins (centre derived on x=24); the bead is split at the joins.
        self._run("hoop", left_join, [("A", right_join, 15, 15, True, True)])
        self._run("bead", left_join, [("A", right_join, br, br, True), ("A", left_join, br, br, True, True)], closed=True)
        self.relate("connect", "hoop", "bead")

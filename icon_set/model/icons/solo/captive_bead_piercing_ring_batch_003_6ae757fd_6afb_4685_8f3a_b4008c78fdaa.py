"""captive-bead-piercing-ring-batch-003: independent batch-003 SOLO48 result for brief 06.

Subject: An open circular piercing ring with a captive bead resting in its lower opening.
Keyshape: CIRCLE -- the ring is a circle about the canvas centre.
Plan: Ring r=20 about (24,24) open from (8,36) to (40,36); bead circle r=5 at (24,39) reaches the radial bound at its base.
Reduction: Bead kept detached as in the reference, 11 units clear of each ring end.
Construction reference: circle-dot (ring plus small concentric element).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6ae757fd-6afb-4685-8f3a-b4008c78fdaa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/container/circle top circle 1_6ae757fd-6afb-4685-8f3a-b4008c78fdaa.svg'
AUTHOR = "claude-opus-5"
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/references/circle top circle 1_6ae757fd-6afb-4685-8f3a-b4008c78fdaa.svg'
BRIEF = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/06-captive-bead-piercing-ring--6ae757fd-6afb-4685-8f3a-b4008c78fdaa.md'


class CaptiveBeadPiercingRingBatch003(Solo48):
    icon_id = 'captive-bead-piercing-ring-batch-003'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('captive', 'bead', 'ring', 'piercing', 'jewelry', 'hoop')

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
        # Open ring: r=20 about the centre, open at the bottom between (8,36) and (40,36).
        R = 20
        self._run("ring", (8, 36), [("A", (40, 36), R, R, True, True)])
        # Detached captive bead in the opening; its base reaches the radial bound (24,44).
        self._circle("bead", 24, 39, 5)

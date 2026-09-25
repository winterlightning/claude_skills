"""unlocked-security-padlock-batch-003: independent batch-003 SOLO48 result for brief 13.

Subject: An unlocked padlock: rounded body with the shackle raised and its right end free.
Keyshape: VRECT_L -- the lock with raised shackle is taller than wide.
Plan: Body 8..40 x 24..44 (r=4); shackle left leg at x=14 into an r=8 semicircle, right end stopping 10 above the body.
Reduction: As in the reference: no keyhole.
Construction reference: lock-open (shackle leaving the body on the left, free on the right).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a11bc25d-bb24-4eb3-ab89-b3565a788892'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/container/unlock_a11bc25d-bb24-4eb3-ab89-b3565a788892.svg'
AUTHOR = "claude-opus-5"
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/references/unlock_a11bc25d-bb24-4eb3-ab89-b3565a788892.svg'
BRIEF = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/13-unlocked-security-padlock--a11bc25d-bb24-4eb3-ab89-b3565a788892.md'


class UnlockedSecurityPadlockBatch003(Solo48):
    icon_id = 'unlocked-security-padlock-batch-003'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('unlock', 'padlock', 'open', 'security', 'lock')

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
        # Body 8..40 x 24..44 (r=4); shackle left leg x=14, r=8 arch, right end free at (30,14).
        b0, b1, bt, bb, r = 8, 40, 24, 44, 4
        sl, sr, sc, sr_end = 14, 30, 12, 14
        self._run("body", (b0 + r, bt), [
            ("L", (sl, bt)), ("L", (b1 - r, bt)), ("A", (b1, bt + r), r, r, True),
            ("L", (b1, bb - r)), ("A", (b1 - r, bb), r, r, True), ("L", (b0 + r, bb)),
            ("A", (b0, bb - r), r, r, True), ("L", (b0, bt + r)), ("A", (b0 + r, bt), r, r, True)], closed=True)
        self._run("shackle", (sl, bt), [
            ("L", (sl, sc)), ("A", (sr, sc), 8, 8, True), ("L", (sr, sr_end))])
        self.relate("connect", "body", "shackle")

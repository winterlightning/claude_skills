"""storage-box-with-lid-batch-003: independent batch-003 SOLO48 result for brief 08.

Subject: An archive storage box: a full-width lid band over a slightly narrower box with rounded lower corners.
Keyshape: SQUARE -- the box is about as tall as wide.
Plan: Lid band 6..42 x 6..14; the body hangs from the lid's lower edge, inset 4 on each side, with r=6 base corners.
Reduction: Plain lid and body as in the reference; no handle slot.
Construction reference: archive (lid band over body).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a461e83-5b52-4307-94e7-188e590f4dff'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/container/archive box_1a461e83-5b52-4307-94e7-188e590f4dff.svg'
AUTHOR = "claude-opus-5"
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/references/archive box_1a461e83-5b52-4307-94e7-188e590f4dff.svg'
BRIEF = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/08-storage-box-with-lid--1a461e83-5b52-4307-94e7-188e590f4dff.md'


class StorageBoxWithLidBatch003(Solo48):
    icon_id = 'storage-box-with-lid-batch-003'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'container'
    aliases = ()
    keywords = ('storage', 'box', 'lid', 'archive', 'container', 'carton')

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
        # Lid band 6..42 x 6..14 (r=2 top corners); body hangs from its lower edge.
        l0, l1, lt, lb, lr = 6, 42, 6, 14, 2
        b0, b1, bb, br = 10, 38, 42, 6
        self._run("lid", (l0 + lr, lt), [
            ("L", (l1 - lr, lt)), ("A", (l1, lt + lr), lr, lr, True), ("L", (l1, lb)),
            ("L", (b1, lb)), ("L", (b0, lb)), ("L", (l0, lb)), ("L", (l0, lt + lr)),
            ("A", (l0 + lr, lt), lr, lr, True)], closed=True)
        self._run("body", (b1, lb), [
            ("L", (b1, bb - br)), ("A", (b1 - br, bb), br, br, True), ("L", (b0 + br, bb)),
            ("A", (b0, bb - br), br, br, True), ("L", (b0, lb))])
        self.relate("connect", "lid", "body")

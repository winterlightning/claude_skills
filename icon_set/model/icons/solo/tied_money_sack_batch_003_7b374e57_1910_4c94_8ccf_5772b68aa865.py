"""tied-money-sack-batch-003: independent batch-003 SOLO48 result for brief 10.

Subject: A tied money sack: a flared mouth above a tie band and a round-bellied pouch.
Keyshape: SQUARE -- the pouch is about as wide as tall.
Plan: Mirrored about x=24: flared trapezoid mouth, tie band at y=16, Bezier shoulders meeting a half-ellipse base tangentially at (6,33) and (42,33).
Reduction: Loose tie string omitted; it would crowd the mouth corner at 48.
Construction reference: handbag (bag body construction); no direct sack match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7b374e57-1910-4c94-8ccf-5772b68aa865'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/container/pouch 1_7b374e57-1910-4c94-8ccf-5772b68aa865.svg'
AUTHOR = "claude-opus-5"
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/references/pouch 1_7b374e57-1910-4c94-8ccf-5772b68aa865.svg'
BRIEF = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/10-tied-money-sack--7b374e57-1910-4c94-8ccf-5772b68aa865.md'


class TiedMoneySackBatch003(Solo48):
    icon_id = 'tied-money-sack-batch-003'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('money', 'sack', 'bag', 'pouch', 'tied', 'savings')

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
        # Mirrored about x=24. Neck/tie band at y=16; mouth flares to the top edge.
        neck_l, neck_r = (19, 16), (29, 16)
        mouth_l, mouth_r = (15, 6), (33, 6)
        # Pouch: Bezier shoulders arrive vertically at the half-ellipse base (rx 18, ry 9).
        self._run("pouch", neck_l, [
            ("C", (6, 33), (15, 19), (6, 25)),
            ("A", (42, 33), 18, 9, False),
            ("C", neck_r, (42, 25), (33, 19)),
            ("L", neck_l)], closed=True)
        self._run("mouth", neck_l, [("L", mouth_l), ("L", mouth_r), ("L", neck_r)])
        self.relate("connect", "pouch", "mouth")

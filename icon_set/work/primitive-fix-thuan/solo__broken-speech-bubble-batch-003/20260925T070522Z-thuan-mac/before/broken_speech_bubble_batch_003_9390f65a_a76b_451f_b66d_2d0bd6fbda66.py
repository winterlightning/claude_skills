"""broken-speech-bubble-batch-003: independent batch-003 SOLO48 result for brief 01.

Subject: A square speech bubble with a lower-left tail whose top edge is split by a lightning-shaped crack.
Keyshape: HRECT_L -- the bubble is wider than tall and its tail drops below the body.
Plan: One closed outline traversed clockwise; the crack is a zigzag notch cut into the top edge, its tip 8 above the bottom edge.
Reduction: Crack reduced to three left and three right runs with >=8 centerline clearance across the notch.
Construction reference: message-square (straight tail dropping from the left wall into the bottom edge).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9390f65a-a76b-451f-b66d-2d0bd6fbda66'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/chat/language barrier broken bubble_9390f65a-a76b-451f-b66d-2d0bd6fbda66.svg'
AUTHOR = "claude-opus-5"
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/references/language barrier broken bubble_9390f65a-a76b-451f-b66d-2d0bd6fbda66.svg'
BRIEF = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/01-broken-speech-bubble--9390f65a-a76b-451f-b66d-2d0bd6fbda66.md'


class BrokenSpeechBubbleBatch003(Solo48):
    icon_id = 'broken-speech-bubble-batch-003'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'chat'
    aliases = ()
    keywords = ('speech', 'bubble', 'broken', 'crack', 'language', 'barrier', 'chat', 'miscommunication')

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
        # Bubble body (4..44 x 8..32, r=4); tail drops from the left wall to (4,40).
        left, right, top, bottom, r = 4, 44, 8, 32, 4
        tail_join, tail_tip = (12, bottom), (left, 40)
        # Lightning crack: left flank A-B-C to the tip, right flank D-E-F back to the edge.
        crack_left = [(17, top), (22, 14), (18, 17)]
        tip = (26, 24)  # 8 above the bottom edge
        crack_right = [(30, 16), (33, 13), (29, top)]
        self._run("bubble", (left + r, top), [
            ("L", crack_left[0]), ("L", crack_left[1]), ("L", crack_left[2]), ("L", tip),
            ("L", crack_right[0]), ("L", crack_right[1]), ("L", crack_right[2]),
            ("L", (right - r, top)), ("A", (right, top + r), r, r, True),
            ("L", (right, bottom - r)), ("A", (right - r, bottom), r, r, True),
            ("L", tail_join), ("L", tail_tip), ("L", (left, top + r)),
            ("A", (left + r, top), r, r, True)], closed=True)

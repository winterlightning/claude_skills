"""vibrating-mobile-device-batch-003: independent batch-003 SOLO48 result for brief 14.

Subject: A mobile phone between two vertical vibration bars.
Keyshape: SQUARE -- phone plus side bars form a square.
Plan: Mirrored about x=24: phone 14..34 x 6..42 (r=4), bars at x=6 and x=42 exactly 8 from the walls, home dot 9 above the base.
Reduction: Home dot added so the plain rectangle reads as a phone.
Construction reference: smartphone and vibrate (device with side motion marks).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e5eda811-8fbc-4a56-bb99-a31e94e69ea2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/container/rectangle stacked_e5eda811-8fbc-4a56-bb99-a31e94e69ea2.svg'
AUTHOR = "claude-opus-5"
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/references/rectangle stacked_e5eda811-8fbc-4a56-bb99-a31e94e69ea2.svg'
BRIEF = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/14-vibrating-mobile-device--e5eda811-8fbc-4a56-bb99-a31e94e69ea2.md'


class VibratingMobileDeviceBatch003(Solo48):
    icon_id = 'vibrating-mobile-device-batch-003'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('vibrate', 'phone', 'mobile', 'device', 'silent', 'buzz')

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
        # Mirrored about x=24: phone 14..34 x 6..42 (r=4) between two vibration bars.
        p0, p1, pt, pb, r = 14, 34, 6, 42, 4
        self._run("phone", (p0 + r, pt), [
            ("L", (p1 - r, pt)), ("A", (p1, pt + r), r, r, True), ("L", (p1, pb - r)),
            ("A", (p1 - r, pb), r, r, True), ("L", (p0 + r, pb)), ("A", (p0, pb - r), r, r, True),
            ("L", (p0, pt + r)), ("A", (p0 + r, pt), r, r, True)], closed=True)
        self.add_dot("home-button", (24, pb - 9))
        self.add_line("vibration-left", (6, 14), (6, 34))
        self.add_line("vibration-right", (42, 14), (42, 34))

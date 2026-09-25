"""video-camera-batch-003: independent batch-003 SOLO48 result for brief 15.

Subject: A video camera: rounded body with a flared lens housing on its right wall.
Keyshape: HRECT_M -- a wide, compact device.
Plan: Mirrored about y=24: body 4..32 x 10..38 (r=4); lens trapezoid attached at (32,20)/(32,28) flaring to x=44.
Reduction: Lens housing kept as a trapezoid with round joins.
Construction reference: video (body plus lens housing).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4cec3560-f13d-406e-81b3-750478c80c54'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/container/video 1_4cec3560-f13d-406e-81b3-750478c80c54.svg'
AUTHOR = "claude-opus-5"
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/references/video 1_4cec3560-f13d-406e-81b3-750478c80c54.svg'
BRIEF = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/15-video-camera-icon--4cec3560-f13d-406e-81b3-750478c80c54.md'


class VideoCameraBatch003(Solo48):
    icon_id = 'video-camera-batch-003'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('video', 'camera', 'record', 'movie', 'film')

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
        # Mirrored about y=24: body 4..32 x 10..38 (r=4); lens housing flares to x=44.
        b0, b1, bt, bb, r = 4, 32, 10, 38, 4
        j0, j1 = (b1, 20), (b1, 28)
        self._run("body", (b0 + r, bt), [
            ("L", (b1 - r, bt)), ("A", (b1, bt + r), r, r, True), ("L", j0), ("L", j1),
            ("L", (b1, bb - r)), ("A", (b1 - r, bb), r, r, True), ("L", (b0 + r, bb)),
            ("A", (b0, bb - r), r, r, True), ("L", (b0, bt + r)), ("A", (b0 + r, bt), r, r, True)], closed=True)
        self._run("lens", j0, [("L", (44, 14)), ("L", (44, 34)), ("L", j1)])
        self.relate("connect", "body", "lens")

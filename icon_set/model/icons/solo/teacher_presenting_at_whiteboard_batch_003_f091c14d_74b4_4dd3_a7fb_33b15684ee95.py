"""teacher-presenting-at-whiteboard-batch-003: independent batch-003 SOLO48 result for brief 09.

Subject: A standing teacher stick figure pointing into a bracket-shaped whiteboard.
Keyshape: SQUARE -- figure plus board form a square scene.
Plan: Stick figure from human_ref/full_body_ref.png: head r5 at (12,11), torso junction (12,24) 8 below the head outline; pointing arm leaves the torso at (12,26); board is an open bracket with r=4 corners.
Reduction: Outlined tunic body reduced to the shared stick figure; board kept as the reference's open bracket.
Construction reference: presentation (board frame); anatomy from the shared human reference.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f091c14d-74b4-4dd3-a7fb-33b15684ee95'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/container/teacher shool_f091c14d-74b4-4dd3-a7fb-33b15684ee95.svg'
AUTHOR = "claude-opus-5"
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/references/teacher shool_f091c14d-74b4-4dd3-a7fb-33b15684ee95.svg'
BRIEF = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-003/09-teacher-presenting-at-whiteboard--f091c14d-74b4-4dd3-a7fb-33b15684ee95.md'


class TeacherPresentingAtWhiteboardBatch003(Solo48):
    icon_id = 'teacher-presenting-at-whiteboard-batch-003'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'container'
    aliases = ()
    keywords = ('teacher', 'presenting', 'whiteboard', 'school', 'class', 'lesson')

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
        # Teacher stick figure (human_ref/full_body_ref.png): head r5, detached 8 above the torso.
        ax, hy, hr = 12, 11, 5
        neck, shoulder, hip = (ax, hy + hr + 8), (ax, 26), (ax, 34)
        self._circle("head", ax, hy, hr)
        self._run("torso", neck, [("L", shoulder), ("L", hip)])
        self._run("legs", (ax - 6, 42), [("L", hip), ("L", (ax + 6, 42))])
        self.relate("connect", "torso", "legs")
        self.add_line("pointing-arm", shoulder, (23, 22))
        self.relate("connect", "torso", "pointing-arm")
        # Whiteboard: open bracket with r=4 outer corners, facing the teacher.
        bt, bb, bx, r = 6, 32, 42, 4
        self._run("board", (26, bt), [
            ("L", (bx - r, bt)), ("A", (bx, bt + r), r, r, True), ("L", (bx, bb - r)),
            ("A", (bx - r, bb), r, r, True), ("L", (30, bb))])
        self.mark_human_figure("teacher", head="head", torso="torso-1", torso_junction="start")

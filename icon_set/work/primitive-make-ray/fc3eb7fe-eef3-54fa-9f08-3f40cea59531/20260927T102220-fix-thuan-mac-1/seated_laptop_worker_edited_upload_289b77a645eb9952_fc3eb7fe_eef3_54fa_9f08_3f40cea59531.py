from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fc3eb7fe-eef3-54fa-9f08-3f40cea59531'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-laptop-worker-edited-upload-289b77a645eb9952/20260927T101542Z-thuan-mac-1/reference/seated-laptop-worker-edited-upload-289b77a645eb9952_fc3eb7fe-eef3-54fa-9f08-3f40cea59531.svg'
AUTHOR = "claude-opus-5-5"


def _path(icon, name, start, steps, closed=False):
    """steps: (x, y) line | ((x, y), rx, ry, sweep[, large]) arc | ('c', c1, c2, end) cubic."""
    members, point = [], start
    for i, step in enumerate(steps):
        member = f"{name}-{i + 1}"
        if step[0] == 'c':
            icon.add_bezier(member, point, (step[1], step[2], step[3])); point = step[3]
        elif isinstance(step[0], (int, float)):
            icon.add_line(member, point, step); point = step
        else:
            end, rx, ry, sweep = step[:4]
            large = step[4] if len(step) > 4 else False
            icon.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep, large_arc=large); point = end
        members.append(member)
    icon.add_contour(name, *members, closed=closed)
    return members


def _circle(icon, name, cx, cy, r):
    """Full circle from four cardinal quarter arcs (certifiable spacing)."""
    return _path(icon, name, (cx, cy - r), [((cx + r, cy), r, r, True), ((cx, cy + r), r, r, True),
                                            ((cx - r, cy), r, r, True), ((cx, cy - r), r, r, True)], True)


class Drawing(Solo48):
    icon_id = 'seated-laptop-worker-edited-upload-289b77a645eb9952'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ()
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # Plan: side view, person on the right facing left. Desk with one leg on the
        # left; laptop screen leans back from its hinge on the desk top. The worker:
        # r4 head exactly 8 above a short vertical neck/torso stub, upright torso to
        # the hip on the chair seat, arm reaching down to the keyboard at the desk edge,
        # thigh level on the seat, shin down; chair = seat + tall back.
        self.add_line("desk-top-a", (6, 28), (10, 28))
        self.add_line("desk-top-b", (10, 28), (16, 28))
        self.add_line("desk-top-c", (16, 28), (24, 28))
        self.add_line("desk-leg", (10, 28), (10, 42))
        self.add_line("screen", (16, 28), (12, 14))
        self.add_contour("desk-top", "desk-top-a", "desk-top-b", "desk-top-c")
        self.relate("connect", "desk-leg", "desk-top")
        self.relate("connect", "screen", "desk-top")
        _circle(self, "head", 34, 10, 4)
        self.add_line("torso", (34, 22), (34, 24))
        self.add_line("torso-lower", (34, 24), (34, 36))
        self.add_line("arm", (34, 24), (24, 28))
        self.add_line("thigh", (34, 36), (28, 36))
        self.add_line("shin", (28, 36), (26, 42))
        self.add_line("seat", (34, 36), (42, 36))
        self.add_line("chair-back-a", (42, 22), (42, 36))
        self.add_line("chair-back-b", (42, 36), (42, 42))
        for a, b in (("torso", "torso-lower"), ("torso", "arm"), ("torso-lower", "arm"), ("torso-lower", "thigh"),
                     ("thigh", "shin"), ("torso-lower", "seat"), ("thigh", "seat"), ("seat", "chair-back-a"),
                     ("seat", "chair-back-b"), ("chair-back-a", "chair-back-b"), ("arm", "desk-top")):
            self.relate("connect", a, b)
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")

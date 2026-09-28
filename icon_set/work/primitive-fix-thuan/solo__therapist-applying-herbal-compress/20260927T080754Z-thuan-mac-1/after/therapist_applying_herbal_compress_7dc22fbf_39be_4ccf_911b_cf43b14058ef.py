from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7dc22fbf-39be-4ccf-911b-cf43b14058ef'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__therapist-applying-herbal-compress/20260927T080754Z-thuan-mac-1/reference/herbal compress people_7dc22fbf-39be-4ccf-911b-cf43b14058ef.svg'
AUTHOR = 'claude-opus-5-5'


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
    icon_id = 'therapist-applying-herbal-compress'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('therapist', 'applying', 'herbal', 'compress')

    def build(self) -> None:
        # therapist bust behind the patient: back rising from the patient, shoulder flowing into an arm that presses
        # (hand on the ball's upper-left 3-4-5 point) a tied herbal compress onto the patient's back; patient lies face down with the head beyond the right end
        _circle(self, "t-head", 10, 12, 4)
        self.add_line("t-back", (8, 32), (8, 28))
        _path(self, "t-arm", (8, 28), [('c', (8, 25.5), (9.5, 24), (12, 24)), (19, 24)])
        self.mark_human_figure("therapist", head="t-head", torso="t-arm-1", torso_junction="end")
        self.add_line("p-back-1", (8, 32), (23, 32))
        self.add_line("p-back-2", (23, 32), (25, 32))
        _path(self, "p-body", (25, 32), [((29, 36), 4, 4, True), ((25, 40), 4, 4, True), (8, 40),
                                          ((4, 36), 4, 4, True), ((8, 32), 4, 4, True)])
        _circle(self, "p-head", 41, 36, 3)
        # compress: r5 cloth ball (3-4-5 points) on the back, gathered into a knot with two ears
        _path(self, "ball", (23, 22), [((28, 27), 5, 5, True), ((23, 32), 5, 5, True), ((19, 30), 5, 5, True),
                                        ((18, 27), 5, 5, True), ((19, 24), 5, 5, True), ((23, 22), 5, 5, True)], True)
        self.add_line("tie-l", (23, 22), (22, 17))
        self.add_line("tie-r", (23, 22), (28, 18))
        for a, b in (("t-back", "p-back-1"), ("t-back", "p-body-4"), ("p-back-1", "p-body-4"), ("t-back", "t-arm-1"),
                     ("p-back-1", "p-back-2"), ("p-back-2", "p-body-1"),
                     ("ball-2", "p-back-1"), ("ball-3", "p-back-1"), ("ball-2", "p-back-2"), ("ball-3", "p-back-2"),
                     ("t-arm-2", "ball-4"), ("t-arm-2", "ball-5"), ("tie-l", "tie-r"), ("tie-l", "ball-5"), ("tie-l", "ball-1"), ("tie-r", "ball-5"), ("tie-r", "ball-1")):
            self.relate("connect", a, b)

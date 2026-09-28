from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '746d13b1-a442-5468-9399-69ec6e6fabf0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-shoulder-massage/20260927T101542Z-thuan-mac-1/reference/thai massage_746d13b1-a442-5468-9399-69ec6e6fabf0.svg'
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
    icon_id = 'seated-shoulder-massage'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('seated', 'shoulder', 'massage')

    def build(self) -> None:
        # Human reference: icon_set/references/human_ref/full_body_ref.png (stick figures, r4 heads,
        # short vertical neck segment exactly 8 below each head outline).
        # Therapist standing on the left, arm reaching to the seated client's shoulder.
        _circle(self, "therapist-head", 10, 10, 4)
        self.add_line("therapist-torso", (10, 22), (10, 24))
        _path(self, "therapist-body", (10, 24), [(10, 32), (7, 42)])
        self.add_line("therapist-leg-front", (10, 32), (14, 42))
        self.add_line("therapist-arm", (10, 24), (27, 30))
        self.mark_human_figure("therapist", head="therapist-head", torso="therapist-torso", torso_junction="start")
        # Client seated (thigh level, shin down) on the right.
        _circle(self, "client-head", 31, 14, 4)
        self.add_line("client-torso", (31, 26), (31, 30))
        _path(self, "client-body", (31, 30), [(31, 36), (42, 36), (42, 42)])
        self.add_line("client-shoulder", (27, 30), (31, 30))
        self.mark_human_figure("client", head="client-head", torso="client-torso", torso_junction="start")
        for a, b in (("therapist-torso", "therapist-body"), ("therapist-body", "therapist-leg-front"),
                     ("therapist-torso", "therapist-arm"), ("therapist-body", "therapist-arm"),
                     ("therapist-arm", "client-shoulder"), ("client-torso", "client-body"),
                     ("client-torso", "client-shoulder"), ("client-body", "client-shoulder")):
            self.relate("connect", a, b)

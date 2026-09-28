from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '542dfa8f-094e-4a0a-8c6a-e04692304231'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rocker-power-switch-in-rounded-square-mount/20260927T101542Z-thuan-mac-1/reference/rocker switch_542dfa8f-094e-4a0a-8c6a-e04692304231.svg'
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
    icon_id = 'rocker-power-switch-in-rounded-square-mount'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'electronics'
    categories = ('electronics', 'primitives')
    aliases = ()
    keywords = ('rocker', 'power', 'switch')

    def build(self) -> None:
        # Plan: rounded-square mount (r6 corners, square box (6,6)-(42,42)) built from
        # standalone sides joined to corner arcs; rocker = lower body box + upper face
        # tilted back, exactly 8 from the mount sides.
        self.add_line("mount-top", (12, 6), (36, 6))
        self.add_arc("mount-tr", (36, 6), (42, 12), radius_x=6, radius_y=6, sweep=True)
        self.add_line("mount-right", (42, 12), (42, 36))
        self.add_arc("mount-br", (42, 36), (36, 42), radius_x=6, radius_y=6, sweep=True)
        self.add_line("mount-bottom", (36, 42), (12, 42))
        self.add_arc("mount-bl", (12, 42), (6, 36), radius_x=6, radius_y=6, sweep=True)
        self.add_line("mount-left", (6, 36), (6, 12))
        self.add_arc("mount-tl", (6, 12), (12, 6), radius_x=6, radius_y=6, sweep=True)
        for a, b in (("mount-top", "mount-tr"), ("mount-tr", "mount-right"), ("mount-right", "mount-br"),
                     ("mount-br", "mount-bottom"), ("mount-bottom", "mount-bl"), ("mount-bl", "mount-left"),
                     ("mount-left", "mount-tl"), ("mount-tl", "mount-top")):
            self.relate("connect", a, b)
        _path(self, "rocker-body", (16, 23), [(16, 34), (28, 34), (28, 23)], False)
        _path(self, "rocker-face", (16, 23), [(21, 14), (34, 14), (28, 23), (16, 23)], True)
        self.relate("connect", "rocker-body", "rocker-face")

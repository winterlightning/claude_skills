from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'dddf7a3a-6638-50ed-98e0-a42054b2fcef'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__flaming-hand-torch/20260927T032039Z-thuan-mac-1/reference/trends torch_dddf7a3a-6638-50ed-98e0-a42054b2fcef.svg'
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
    icon_id = 'flaming-hand-torch'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'social'
    categories = ('social', 'primitives')
    aliases = ()
    keywords = ('torch', 'flame', 'fire', 'handle', 'cup', 'burning')

    def build(self) -> None:
        # CIRCLE keeps the torch tall and narrow: only the flame tip (24,4)
        # reaches radius 20; everything else stays inside it.
        # Flame: teardrop, right side swelling more, r6 base about (24,12).
        _path(self, 'flame', (24, 4), [('c', (27, 6), (30, 9), (30, 12)), ((24, 18), 6, 6, True),
                                       ((18, 12), 6, 6, True), ('c', (18, 9), (22, 7), (24, 4))], True)
        # Cup and grip as one silhouette: flat rim, rounded bowl narrowing
        # into a long straight handle.
        _path(self, 'torch', (14, 26), [(34, 26), ('c', (34, 29), (31, 32), (28, 32)), (28, 43), (20, 43),
                                        (20, 32), ('c', (17, 32), (14, 29), (14, 26))], True)

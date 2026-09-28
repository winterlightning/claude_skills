from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '858e31f1-454e-40a0-86f3-444df304e673'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__front-facing-bat-with-spread-wings/20260926T152555Z-thuan-mac-2/reference/bat fly_858e31f1-454e-40a0-86f3-444df304e673.svg'
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
    icon_id = 'front-facing-bat-with-spread-wings'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('front', 'facing', 'bat', 'with', 'spread', 'wings')

    def build(self) -> None:
        # Plan: frontal bat, one closed outline mirrored about x=24 on HRECT_L
        # (4..44 x 8..40). Left half: wing tip L1 -> outer wing edge bulging to the
        # left edge -> lower wing tip W -> two scallops -> bottom point C (24,40);
        # upper side: wing tip L1 -> deep concave top edge -> shoulder S -> pointed
        # ear E -> flat head top H.
        def mx(p):
            return (48 - p[0], p[1])
        L1, S, E, H, W, V1, C = (7, 8), (17, 21), (19, 8), (22, 14), (9, 38), (17, 36), (24, 40)
        ctl = {
            'outer1': ((5, 12), (4, 18)), 'outer2': ((4, 30), (6, 35)),
            'sc1': ((10, 28), (15, 26)), 'sc2': ((18, 28), (22, 28)), 'top': ((12, 20), (9, 15)),
        }
        steps = [
            ('c', *ctl['outer1'], (4, 24)),
            ('c', *ctl['outer2'], W),
            ('c', *ctl['sc1'], V1),
            ('c', *ctl['sc2'], C),
            ('c', mx(ctl['sc2'][1]), mx(ctl['sc2'][0]), mx(V1)),
            ('c', mx(ctl['sc1'][1]), mx(ctl['sc1'][0]), mx(W)),
            ('c', mx(ctl['outer2'][1]), mx(ctl['outer2'][0]), mx((4, 24))),
            ('c', mx(ctl['outer1'][1]), mx(ctl['outer1'][0]), mx(L1)),
            ('c', mx(ctl['top'][1]), mx(ctl['top'][0]), mx(S)),
            mx(E), mx(H), H, E, S,
            ('c', *ctl['top'], L1),
        ]
        _path(self, 'bat', L1, steps, closed=True)

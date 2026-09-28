from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '16f4051e-4e10-5f14-b1b6-8d6038274f05'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__curved-shrimp-tempura/20260927T091421Z-thuan-mac-1/reference/deep fied pawn shrimp tempura_16f4051e-4e10-5f14-b1b6-8d6038274f05.svg'
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
    icon_id = 'curved-shrimp-tempura'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('tempura', 'shrimp', 'prawn', 'fried', 'tail', 'seafood', 'food')

    def build(self) -> None:
        # Shrimp tempura standing up: a three-point tail fan at the top and a battered body that runs
        # down and curls right at the bottom (a J). The outer edge is a run of batter bumps (two cubics
        # per bump, meeting at a peak whose tangent is parallel to the bump's chord, so notches stay
        # crisp and the axis-aligned bumps give exact extremes: left x=8, bottom y=44, right x=40).
        # The inner edge of the curl is smooth; the tail tips give the top (4).
        steps = []

        def bump(a, p, b):
            mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
            ox, oy = (p[0] - mx) * 0.8, (p[1] - my) * 0.8
            tx, ty = (b[0] - a[0]) * 0.25, (b[1] - a[1]) * 0.25
            steps.append(('c', (a[0] + ox, a[1] + oy), (p[0] - tx, p[1] - ty), p))
            steps.append(('c', (p[0] + tx, p[1] + ty), (b[0] + ox, b[1] + oy), b))

        for a, p, b in (((15, 14), (11, 18), (13, 23)), ((13, 23), (8, 29), (13, 35)), ((13, 35), (13, 41), (19, 41)),
                        ((19, 41), (25, 44), (31, 41)), ((31, 41), (35, 42), (36, 39)), ((36, 39), (40, 34), (36, 29))):
            bump(a, p, b)
        steps += [('c', (32, 25), (27, 27), (27, 22)), (27, 14),
                  (33, 6), (26, 9), (24, 4), (20, 9), (13, 5), (15, 14)]
        _path(self, "shrimp", (15, 14), steps, True)

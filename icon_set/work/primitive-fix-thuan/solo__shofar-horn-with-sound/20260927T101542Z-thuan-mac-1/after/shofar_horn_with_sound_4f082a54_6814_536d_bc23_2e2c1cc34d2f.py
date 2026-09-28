from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4f082a54-6814-536d-bc23-2e2c1cc34d2f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__shofar-horn-with-sound/20260927T101542Z-thuan-mac-1/reference/rosh hashanah feast of trumpets_4f082a54-6814-536d-bc23-2e2c1cc34d2f.svg'
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
    icon_id = 'shofar-horn-with-sound'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('shofar', 'horn', 'with', 'sound')

    def build(self) -> None:
        import math

        def herm(name, knots, closed=False, k=0.38):
            """Hermite cubics through integer knots with tangent directions."""
            n = len(knots); members = []
            for i in range(n if closed else n - 1):
                (p1, t1), (p2, t2) = knots[i], knots[(i + 1) % n]
                L = math.dist(p1, p2) * k
                u1 = (t1[0] / math.hypot(*t1), t1[1] / math.hypot(*t1))
                u2 = (t2[0] / math.hypot(*t2), t2[1] / math.hypot(*t2))
                m = f"{name}-{i + 1}"
                self.add_bezier(m, p1, ((p1[0] + u1[0] * L, p1[1] + u1[1] * L), (p2[0] - u2[0] * L, p2[1] - u2[1] * L), p2))
                members.append(m)
            self.add_contour(name, *members, closed=closed)

        # Ram's horn: bell lens at top-left (L-R), U-shaped tube down and up to an angled
        # mouthpiece end (I-O, perpendicular to the 45-degree tube axis).
        L, R, I, O = (6, 10), (20, 16), (33, 21), (39, 27)
        herm("bell", [(L, (1, -0.6)), ((12, 7), (1, 0.1)), (R, (1, 0.9)), ((12, 17), (-1, -0.15)), (L, (-1, -0.6))])
        herm("horn-inner", [(R, (0, 1)), ((19, 24), (0, 1)), ((24, 31), (1, 0)), (I, (1, -1))])
        herm("horn-outer", [(L, (0, 1)), ((6, 26), (0, 1)), ((20, 42), (1, 0)), ((35, 34), (1, -1)), (O, (1, -1))])
        self.add_line("mouthpiece", I, O)
        for a, b in (("bell", "horn-inner"), ("bell", "horn-outer"), ("horn-inner", "mouthpiece"), ("horn-outer", "mouthpiece")):
            self.relate("connect", a, b)
        # Sound: two wavy lines beyond the mouthpiece.
        herm("sound", [((29, 9), (1, -0.8)), ((34, 6), (1, 0)), ((38, 10), (1, 0)), ((42, 7), (1, -0.8))])

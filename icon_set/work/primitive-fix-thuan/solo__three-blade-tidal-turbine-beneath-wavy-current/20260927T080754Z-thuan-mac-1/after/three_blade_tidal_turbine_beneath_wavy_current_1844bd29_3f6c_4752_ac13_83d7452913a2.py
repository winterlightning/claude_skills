from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1844bd29-3f6c-4752-ac13-83d7452913a2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-blade-tidal-turbine-beneath-wavy-current/20260927T080754Z-thuan-mac-1/reference/tidal energy 1_1844bd29-3f6c-4752-ac13-83d7452913a2.svg'
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
    icon_id = 'three-blade-tidal-turbine-beneath-wavy-current'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'ecology'
    categories = ('primitives', 'ecology')
    aliases = ()
    keywords = ('tidal', 'turbine', 'water', 'waves', 'energy', 'blades', 'current', 'ecology')

    def build(self) -> None:
        # tidal turbine: three curved lens blades (tips 16 from the hub, 120 degrees apart) under a wavy current
        import math
        H = (20, 26)
        def rot(rel, deg):
            a = math.radians(deg); x, y = rel
            return (H[0] + x * math.cos(a) - y * math.sin(a), H[1] + x * math.sin(a) + y * math.cos(a))
        out = [(9, -3), (7, -14), (0, -16)]
        back = [(-3, -13), (-3, -5)]
        for i, deg in enumerate((180, 300, 60)):
            a1, a2, tip = (rot(p, deg) for p in out)
            b1, b2 = (rot(p, deg) for p in back)
            tip = (round(tip[0]), round(tip[1]))
            _path(self, f"blade-{i + 1}", H, [('c', a1, a2, tip), ('c', b1, b2, H)], True)
        names = [f"blade-{i}-{j}" for i in (1, 2, 3) for j in (1, 2)]
        for i, a in enumerate(names):
            for b in names[i + 1:]:
                self.relate("connect", a, b)
        def wave(name, pts, h=3):
            _path(self, name, pts[0], [('c', (x0 + h, y0), (x1 - h, y1), (x1, y1)) for (x0, y0), (x1, y1) in zip(pts, pts[1:])])
        wave("current-1", [(19, 8), (27, 6), (35, 9), (42, 6)], 4)

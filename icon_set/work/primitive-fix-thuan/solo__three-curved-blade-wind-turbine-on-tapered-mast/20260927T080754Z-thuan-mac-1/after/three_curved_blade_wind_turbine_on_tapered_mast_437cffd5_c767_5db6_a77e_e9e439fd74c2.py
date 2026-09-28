from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '437cffd5-c767-5db6-a77e-e9e439fd74c2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-curved-blade-wind-turbine-on-tapered-mast/20260927T080754Z-thuan-mac-1/reference/renewable energy wind turbine_437cffd5-c767-5db6-a77e-e9e439fd74c2.svg'
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
    icon_id = 'three-curved-blade-wind-turbine-on-tapered-mast'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'ecology'
    categories = ('primitives', 'ecology')
    aliases = ()
    keywords = ('wind', 'turbine', 'blades', 'energy', 'mast', 'rotor', 'power', 'ecology')

    def build(self) -> None:
        # wind turbine: three curved lens blades 120 degrees apart from the hub, a mast down to a ground line
        import math
        H = (24, 20)
        def rot(p, deg):
            a = math.radians(deg); x, y = p[0] - H[0], p[1] - H[1]
            return (H[0] + x * math.cos(a) - y * math.sin(a), H[1] + x * math.sin(a) + y * math.cos(a))
        out = [(33, 17), (31, 6), (24, 4)]       # leading edge, bulging clockwise
        back = [(21, 7), (21, 15)]              # trailing edge back to the hub
        for i, deg in enumerate((0, 120, 240)):
            a1, a2, tip = (rot(p, deg) for p in out)
            b1, b2 = (rot(p, deg) for p in back)
            tip = (round(tip[0]), round(tip[1]))
            _path(self, f"blade-{i + 1}", H, [('c', a1, a2, tip), ('c', b1, b2, H)], True)
        self.add_line("mast", H, (24, 44))
        self.add_line("ground-l", (8, 44), (24, 44))
        self.add_line("ground-r", (24, 44), (40, 44))
        names = ["blade-1-1", "blade-1-2", "blade-2-1", "blade-2-2", "blade-3-1", "blade-3-2", "mast"]
        for i, a in enumerate(names):
            for b in names[i + 1:]:
                self.relate("connect", a, b)
        for g in ("ground-l", "ground-r"):
            self.relate("connect", "mast", g)
        self.relate("connect", "ground-l", "ground-r")

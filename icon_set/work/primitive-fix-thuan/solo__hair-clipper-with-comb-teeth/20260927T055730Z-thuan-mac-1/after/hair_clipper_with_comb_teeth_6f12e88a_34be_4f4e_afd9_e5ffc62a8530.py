from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6f12e88a-34be-4f4e-afd9-e5ffc62a8530'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hair-clipper-with-comb-teeth/20260927T055730Z-thuan-mac-1/reference/shaving machine_6f12e88a-34be-4f4e-afd9-e5ffc62a8530.svg'
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
    icon_id = 'hair-clipper-with-comb-teeth'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('hair', 'clipper', 'with', 'comb', 'teeth')

    def build(self) -> None:
        # cutting blade across the full width: bar with five upright comb teeth 8 apart
        xs = (8, 16, 24, 32, 40)
        for n, (a, b) in enumerate(zip(xs, xs[1:])):
            self.add_line(f"blade-{n}", (a, 12), (b, 12))
        for n in range(3):
            self.relate("connect", f"blade-{n}", f"blade-{n + 1}")
        for j, x in enumerate(xs):
            self.add_line(f"tooth-{j}", (x, 12), (x, 4))
            for n in range(4):
                self.relate("connect", f"tooth-{j}", f"blade-{n}")
        # narrower handle: neck curving in from the blade ends, straight walls, round bottom
        _path(self, "clipper", (8, 12), [
            ('c', (8, 16), (11, 16), (11, 20)),
            (11, 36), ((37, 36), 13, 8, False),
            (37, 20),
            ('c', (37, 16), (40, 16), (40, 12)),
        ])
        for n in range(4):
            self.relate("connect", "clipper", f"blade-{n}")
        # power button: an 8-wide arch-topped pill
        _path(self, "button", (20, 35), [(20, 30), ((28, 30), 4, 4, True), (28, 35), (20, 35)], closed=True)

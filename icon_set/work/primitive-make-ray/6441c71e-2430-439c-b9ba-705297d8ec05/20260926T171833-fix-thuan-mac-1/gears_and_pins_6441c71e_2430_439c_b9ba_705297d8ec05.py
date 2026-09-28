from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6441c71e-2430-439c-b9ba-705297d8ec05'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__gears-and-pins/20260926T171707Z-thuan-mac-1/reference/internet of thing graph service setting_6441c71e-2430-439c-b9ba-705297d8ec05.svg'
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
    icon_id = 'gears-and-pins'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'programing'
    categories = ('programing', 'primitives')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # 8-tooth gear: a quarter (tip, valley, diagonal tooth, valley) rotated four times about the hub.
        quarter = [(1, -7), (2, -4), (4, -5), (5, -4), (4, -2), (7, -1)]
        pts = []
        for k in range(4):
            for x, y in quarter:
                for _ in range(k):
                    x, y = -y, x
                pts.append((x, y))
        for name, cx in (('gear-left', 11), ('gear-right', 37)):
            p = [(cx + x, 15 + y) for x, y in pts]
            members = []
            for i in range(len(p)):
                m = f'{name}-{i}'
                self.add_line(m, p[i], p[(i + 1) % len(p)])
                members.append(m)
            self.add_contour(name, *members, closed=True)
        # graph pins: r3 ring heads on stems standing on the baseline y=40; the middle one is the peak
        for i, (x, y) in enumerate(((7, 33), (24, 28), (41, 33))):
            r = 3
            self.add_arc(f'pin-{i}-a', (x, y - r), (x + r, y), radius_x=r, sweep=True)
            self.add_arc(f'pin-{i}-b', (x + r, y), (x, y + r), radius_x=r, sweep=True)
            self.add_arc(f'pin-{i}-c', (x, y + r), (x - r, y), radius_x=r, sweep=True)
            self.add_arc(f'pin-{i}-d', (x - r, y), (x, y - r), radius_x=r, sweep=True)
            self.add_contour(f'pin-{i}-head', f'pin-{i}-a', f'pin-{i}-b', f'pin-{i}-c', f'pin-{i}-d', closed=True)
            self.add_line(f'pin-{i}-stem', (x, y + r), (x, 40))
            self.relate('connect', f'pin-{i}-head', f'pin-{i}-stem')

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'bb26d652-342b-4c2b-a76b-a3e5b0d67d4b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__front-loading-washing-machine/20260926T171659Z-thuan-mac-1/reference/laundry machine_bb26d652-342b-4c2b-a76b-a3e5b0d67d4b.svg'
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
    icon_id = 'front-loading-washing-machine'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'state')
    aliases = ()
    keywords = ('washer', 'washing', 'machine', 'laundry', 'appliance', 'door')

    def build(self) -> None:
        # Front-loading washer on VRECT_L: rounded cabinet (8,4)-(40,44), a
        # control dash and an indicator dot along the top, and the round door
        # (r8 about (24,28)) exactly 8 from the dash and the cabinet walls.
        # The cabinet walls and r4 corners are standalone connected parts so
        # the exact-8 gaps are measured straight-to-part and certify.
        r = 4
        pts = [(12, 4), (36, 4), (40, 8), (40, 40), (36, 44), (12, 44), (8, 40), (8, 8)]
        parts = []
        for i in range(0, 8, 2):
            a, b, c = pts[i], pts[i + 1], pts[(i + 2) % 8]
            self.add_line(f'wall-{i}', a, b)
            self.add_contour(f'wall-{i}-c', f'wall-{i}')
            self.add_arc(f'corner-{i}', b, c, radius_x=r, sweep=True)
            self.add_contour(f'corner-{i}-c', f'corner-{i}')
            parts += [f'wall-{i}-c', f'corner-{i}-c']
        for a, b in zip(parts, parts[1:] + parts[:1]):
            self.relate('connect', a, b)
        self.add_line('dial', (16, 12), (22, 12))
        self.add_dot('light', (31, 12))
        _circle(self, 'door', 24, 28, 8)

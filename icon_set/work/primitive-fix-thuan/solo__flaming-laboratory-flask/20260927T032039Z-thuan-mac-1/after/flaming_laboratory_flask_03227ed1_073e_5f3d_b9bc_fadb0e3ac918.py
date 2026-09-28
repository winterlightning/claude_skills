from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '03227ed1-073e-5f3d-b9bc-fadb0e3ac918'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__flaming-laboratory-flask/20260927T032039Z-thuan-mac-1/reference/lab flame bottle_03227ed1-073e-5f3d-b9bc-fadb0e3ac918.svg'
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
    icon_id = 'flaming-laboratory-flask'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'science'
    categories = ('science', 'primitives')
    aliases = ()
    keywords = ('flask', 'flame', 'laboratory', 'chemistry', 'liquid', 'experiment')

    def build(self) -> None:
        # Flame: tall pointed tongue over a notched base (the reference's
        # inner tongue), tip (23,4) leaning slightly left.
        _path(self, 'flame', (19, 16), [('c', (16, 12), (18, 8), (23, 4)), ('c', (25, 8), (32, 11), (29, 16)),
                                        (24, 13), (19, 16)], True)
        # Flask (Lucide flask-conical): lip, neck, straight 3:4 walls to sharp
        # bottom corners (10,44)/(38,44).
        _path(self, 'flask', (19, 24), [(19, 32), (16, 36), (10, 44), (38, 44), (32, 36), (29, 32), (29, 24)])
        _path(self, 'lip', (16, 24), [(19, 24), (29, 24), (32, 24)])
        for a, b in (('lip-1', 'flask-1'), ('lip-2', 'flask-1'), ('lip-2', 'flask-7'), ('lip-3', 'flask-7')):
            self.relate('connect', a, b)
        # Liquid level across the body.
        self.add_line('liquid', (16, 36), (32, 36))
        for m in ('flask-2', 'flask-3', 'flask-5', 'flask-6'):
            self.relate('connect', 'liquid', m)

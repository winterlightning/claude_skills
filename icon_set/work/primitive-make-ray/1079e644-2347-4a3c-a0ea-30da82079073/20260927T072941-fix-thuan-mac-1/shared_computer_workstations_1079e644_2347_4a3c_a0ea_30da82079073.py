from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1079e644-2347-4a3c-a0ea-30da82079073'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__shared-computer-workstations/20260927T072849Z-thuan-mac-1/reference/co working space monitors_1079e644-2347-4a3c-a0ea-30da82079073.svg'
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
    icon_id = 'shared-computer-workstations'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'office'
    categories = ('office', 'primitives')
    aliases = ()
    keywords = ('computer', 'monitor', 'desk', 'coworking', 'workstation', 'office')

    def build(self) -> None:
        # Co-working monitors (reference): two monitors on a long upper desk
        # with legs, a third monitor centred on a lower desk.
        def monitor(n, x, y, stand_to):
            _path(self, n, (x, y), [(x + 12, y), (x + 12, y + 8), (x + 6, y + 8), (x, y + 8), (x, y)], True)
            self.add_line(n + '-stand', (x + 6, y + 8), (x + 6, stand_to))
            self.relate('connect', n, n + '-stand')
        monitor('mon-left', 8, 4, 20)
        monitor('mon-right', 28, 4, 20)
        _path(self, 'desk-top', (8, 28), [(8, 20), (14, 20), (34, 20), (40, 20), (40, 28)])
        self.relate('connect', 'mon-left-stand', 'desk-top')
        self.relate('connect', 'mon-right-stand', 'desk-top')
        monitor('mon-front', 18, 28, 44)
        self.add_line('desk-front', (12, 44), (36, 44))
        self.relate('connect', 'mon-front-stand', 'desk-front')

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '19688650-b71a-496a-9e4f-98211e2e851e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__security-shield-with-four-network-nodes/20260927T072849Z-thuan-mac-1/reference/security hub shield_19688650-b71a-496a-9e4f-98211e2e851e.svg'
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
    icon_id = 'security-shield-with-four-network-nodes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'apps'
    categories = ('apps', 'primitives')
    aliases = ()
    keywords = ('security', 'shield', 'with', 'four', 'network', 'nodes')

    def build(self) -> None:
        # Shield with a centre divider, 16 wide, pointed tip at (24,38).
        _path(self, 'shield', (16, 18), [(24, 18), (32, 18), (32, 26), ('c', (32, 32), (28, 36), (24, 38)),
                                         ('c', (20, 36), (16, 32), (16, 26)), (16, 18)], True)
        self.add_line('divider', (24, 18), (24, 38))
        self.relate('connect', 'divider', 'shield')
        # Four network nodes (r3 rings) in the corners, each linked to the
        # shield: top nodes to the top corners, bottom nodes to the side feet.
        for n, (cx, cy), start, end in [('nw', (9, 9), (12, 9), (16, 18)), ('ne', (39, 9), (36, 9), (32, 18)),
                                        ('sw', (9, 39), (9, 36), (16, 26)), ('se', (39, 39), (39, 36), (32, 26))]:
            _circle(self, 'node-' + n, cx, cy, 3)
            self.add_line('link-' + n, start, end)
            self.relate('connect', 'link-' + n, 'node-' + n)
            self.relate('connect', 'link-' + n, 'shield')

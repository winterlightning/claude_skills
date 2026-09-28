from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'df9452bd-a8ba-5b0a-9276-1baccd6531a2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hierarchy-circle-root/20260927T032037Z-thuan-mac-1/reference/hierarchy_df9452bd-a8ba-5b0a-9276-1baccd6531a2.svg'
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
    icon_id = 'hierarchy-circle-root'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'programing'
    categories = ('programing', 'primitives')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # Plan: tree mirrored about x=24. Root r7 circle about (24,15) (top 8);
        # three connectors fan from its bottom node (24,22) to the top midpoints
        # of three 8x8 boxes (x4-12, 20-28, 36-44; y32-40) spaced 8 apart.
        _circle(self, 'root', 24, 15, 7)
        for name, x0 in (('left', 4), ('mid', 20), ('right', 36)):
            cx = x0 + 4
            _path(self, f'box-{name}', (cx, 32), [(x0 + 8, 32), (x0 + 8, 40), (x0, 40), (x0, 32), (cx, 32)], True)
            self.add_line(f'link-{name}', (24, 22), (cx, 32))
            self.relate('connect', f'link-{name}', f'box-{name}')
            self.relate('connect', f'link-{name}', 'root')
        for a, b in [('link-left', 'link-mid'), ('link-mid', 'link-right'), ('link-left', 'link-right')]:
            self.relate('connect', a, b)

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0fbcf6e4-e1c9-4228-8437-36dabfe32073'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__guarded-circular-saw-blade/20260926T171659Z-thuan-mac-1/reference/power tools circular saw_0fbcf6e4-e1c9-4228-8437-36dabfe32073.svg'
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
    icon_id = 'guarded-circular-saw-blade'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'tools'
    categories = ('primitives', 'tools')
    aliases = ()
    keywords = ('circular saw', 'saw', 'blade', 'guard', 'power tool', 'cutting', 'woodworking', 'teeth')

    def build(self) -> None:
        # Guarded circular saw on CIRCLE (r20 about (24,24)), mirrored about
        # x=24: the guard is the upper half-disc (r20 arc + base line); the
        # base line breaks at the blade's hub ring (r7); below it the blade
        # rim shows seven teeth whose tips sit on r20 lattice points and whose
        # valleys sit near r16-17 (at least 8.8 from the hub ring).
        _path(self, 'guard', (4, 24), [((44, 24), 20, 20, True)])
        _path(self, 'base-left', (4, 24), [(17, 24)])
        _path(self, 'base-right', (31, 24), [(44, 24)])
        _circle(self, 'hub', 24, 24, 7)
        _path(self, 'teeth', (4, 24), [
            (9, 29), (8, 36), (12, 36), (12, 40), (19, 40), (24, 44), (29, 40),
            (36, 40), (36, 36), (40, 36), (39, 29), (44, 24)])
        for a, b in (('guard', 'base-left'), ('guard', 'base-right'), ('hub', 'base-left'),
                     ('hub', 'base-right'), ('teeth', 'base-left'), ('teeth', 'base-right'),
                     ('teeth', 'guard')):
            self.relate('connect', a, b)

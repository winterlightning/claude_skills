from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'cb5d6e43-8c14-47cd-a965-fb2a738c8e11'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__forest-fire/20260926T182452Z-thuan-mac-1/reference/trees camp fire_cb5d6e43-8c14-47cd-a965-fb2a738c8e11.svg'
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
    icon_id = 'forest-fire'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'nature'
    categories = ('nature', 'primitives')
    aliases = ()
    keywords = ('forest fire', 'wildfire', 'trees', 'flame', 'smoke', 'campfire', 'pine', 'danger')

    def build(self) -> None:
        # Forest fire (reference "trees camp fire"): a flame at the lower left in
        # front of two pine trees. The front tree (apex (28,8), 1:4 flanks) is
        # tall; the back tree (apex (38,14)) is shorter and hides behind it, so
        # both share one outline that notches at J=(33,28) on the front flank.
        _path(self, 'flame', (4, 35), [('c', (4, 26), (10, 24), (9, 12)),
                                       ('c', (14, 18), (14, 28), (14, 35)),
                                       ((4, 35), 5, 5, True)], True)
        _path(self, 'trees', (22, 32), [(28, 8), (33, 28), (38, 14), (44, 32),
                                        (39, 32), (28, 32), (22, 32)], True)
        for name, x in (('trunk-front', 28), ('trunk-back', 39)):
            self.add_line(name, (x, 32), (x, 40))
            self.relate('connect', 'trees', name)

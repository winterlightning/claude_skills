from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '48b9ec2f-d1e5-4c68-a4c7-5794c4616469'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__insect-head-with-antennae/20260927T070909Z-thuan-mac-1/reference/insect cricket_48b9ec2f-d1e5-4c68-a4c7-5794c4616469.svg'
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
    icon_id = 'insect-head-with-antennae'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('insect', 'head', 'antennae', 'eyes', 'bug', 'cricket', 'face', 'nature')

    def build(self) -> None:
        # insect head, front view: r10 head about (24,22) with compound-eye lobes (r6) bulging at the
        # sides, antennae sweeping out to the top corners, mandibles hanging below
        _path(self, "head", (18, 14), [
            ((30, 14), 10, 10, True),                   # crown
            ((32, 16), 10, 10, True),
            ((32, 28), 6, 6, True),                     # right eye lobe (x=38)
            ((30, 30), 10, 10, True),
            ((18, 30), 10, 10, True),                   # jaw
            ((16, 28), 10, 10, True),
            ((16, 16), 6, 6, True),                     # left eye lobe (x=10)
            ((18, 14), 10, 10, True),
        ], closed=True)
        self.add_bezier("antenna-left", (18, 14), ((16, 8), (10, 6), (6, 6)))
        self.add_bezier("antenna-right", (30, 14), ((32, 8), (38, 6), (42, 6)))
        self.add_bezier("mandible-left", (18, 30), ((16, 36), (17, 40), (20, 42)))
        self.add_bezier("mandible-right", (30, 30), ((32, 36), (31, 40), (28, 42)))
        for p in ("antenna-left", "antenna-right", "mandible-left", "mandible-right"):
            self.relate("connect", "head", p)

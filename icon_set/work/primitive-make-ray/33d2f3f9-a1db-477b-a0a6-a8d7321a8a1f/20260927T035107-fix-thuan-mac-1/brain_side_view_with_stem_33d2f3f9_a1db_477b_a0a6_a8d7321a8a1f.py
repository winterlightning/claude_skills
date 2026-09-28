from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '33d2f3f9-a1db-477b-a0a6-a8d7321a8a1f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__brain-side-view-with-stem/20260927T032145Z-thuan-mac-1/reference/study brain 1_33d2f3f9-a1db-477b-a0a6-a8d7321a8a1f.svg'
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
    icon_id = 'brain-side-view-with-stem'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('brain', 'study', 'mind', 'neuroscience', 'thinking', 'learning', 'anatomy')

    def build(self) -> None:
        # side-view brain: back lobe r6 about (12,25), crown r13 about (25,19), front lobe r10 about (32,27);
        # flat underside, brain stem running off the bottom edge
        _path(self, "brain", (31, 42), [
            (28, 31),                                   # stem, back edge
            (12, 31),                                   # flat underside
            ((12, 19), 6, 6, True),                     # back lobe (left extreme x=6)
            ((38, 19), 13, 13, True),                   # crown (top y=6)
            ((38, 35), 10, 10, True),                   # front lobe (right extreme x=42)
            (40, 42),                                   # stem, front edge
        ])
        # inner fold rising from above the underside toward the crown
        self.add_bezier("fold", (20, 22), ((20, 19), (24, 17), (28, 17)))

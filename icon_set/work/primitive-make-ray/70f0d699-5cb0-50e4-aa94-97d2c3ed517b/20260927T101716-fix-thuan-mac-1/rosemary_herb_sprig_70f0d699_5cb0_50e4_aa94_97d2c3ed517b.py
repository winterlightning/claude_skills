from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '70f0d699-5cb0-50e4-aa94-97d2c3ed517b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rosemary-herb-sprig/20260927T101542Z-thuan-mac-1/reference/rosemary_70f0d699-5cb0-50e4-aa94-97d2c3ed517b.svg'
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
    icon_id = 'rosemary-herb-sprig'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('rosemary', 'herb', 'sprig')

    def build(self) -> None:
        # Stem on the axis (tip (24,4) and foot (24,44) reach r20); four needle pairs on a
        # 2:1 slope, 9 apart vertically (8.05 perpendicular), lengthening toward the base.
        attach = (10, 19, 28, 37)
        reach = (4, 4, 5, 5)
        stem_pts = [(24, 4)] + [(24, y) for y in attach] + [(24, 44)]
        stem = []
        for i in range(len(stem_pts) - 1):
            self.add_line(f"stem-{i + 1}", stem_pts[i], stem_pts[i + 1]); stem.append(f"stem-{i + 1}")
        self.add_contour("stem", *stem)
        for y, k in zip(attach, reach):
            for side, s in (("left", -1), ("right", 1)):
                name = f"needle-{side}-{y}"
                self.add_line(name, (24, y), (24 + s * 2 * k, y - k))
                self.relate("connect", "stem", name)

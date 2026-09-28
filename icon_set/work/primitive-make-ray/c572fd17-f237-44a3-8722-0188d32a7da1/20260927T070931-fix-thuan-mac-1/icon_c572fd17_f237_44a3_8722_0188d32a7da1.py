from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c572fd17-f237-44a3-8722-0188d32a7da1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__icon-symbol/20260927T070905Z-thuan-mac-1/reference/@_c572fd17-f237-44a3-8722-0188d32a7da1.svg'
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
    icon_id = 'icon-symbol'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('symbol',)

    def build(self) -> None:
        # Lucide `at-sign` at 2x: inner r8 ring about (24,24) tangent to the stem x=32; the stem
        # drops into an r6 tail hook up to the outer r20 ring's right cardinal, which sweeps almost
        # all the way round to end at the 3-4-5 point (36,40).
        _circle(self, "ring", 24, 24, 8)
        _path(self, "outer", (32, 16), [(32, 24), ((44, 24), 6, 6, False), ((36, 40), 20, 20, False, True)])
        self.relate("connect", "ring", "outer")

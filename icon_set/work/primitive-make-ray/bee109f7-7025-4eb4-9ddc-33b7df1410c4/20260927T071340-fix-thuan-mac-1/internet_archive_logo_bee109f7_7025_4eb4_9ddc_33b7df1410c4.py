from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'bee109f7-7025-4eb4-9ddc-33b7df1410c4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__internet-archive-logo/20260927T070909Z-thuan-mac-1/reference/internet archive logo_bee109f7-7025-4eb4-9ddc-33b7df1410c4.svg'
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
    icon_id = 'internet-archive-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('internet-archive', 'archive', 'library', 'columns', 'logo', 'brand', 'wayback')

    def build(self) -> None:
        # pediment: a flat trapezoid band over three outlined columns standing on the base line
        self.add_polyline("pediment", (8, 8), (40, 8), (44, 16), (4, 16), closed=True)
        xs = (4, 12, 20, 28, 36, 44)
        for n, (a, b) in enumerate(zip(xs, xs[1:])):
            self.add_line(f"base-{n}", (a, 40), (b, 40))
        for n in range(4):
            self.relate("connect", f"base-{n}", f"base-{n + 1}")
        for j, x in enumerate((4, 20, 36)):
            self.add_polyline(f"column-{j}", (x, 40), (x, 24), (x + 8, 24), (x + 8, 40))
            for n in range(5):
                self.relate("connect", f"column-{j}", f"base-{n}")

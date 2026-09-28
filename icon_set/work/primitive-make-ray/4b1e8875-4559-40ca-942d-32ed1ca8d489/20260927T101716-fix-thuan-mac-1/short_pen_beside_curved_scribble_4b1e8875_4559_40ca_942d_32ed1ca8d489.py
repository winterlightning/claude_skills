from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4b1e8875-4559-40ca-942d-32ed1ca8d489'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__short-pen-beside-curved-scribble/20260927T101542Z-thuan-mac-1/reference/pen draw 1_4b1e8875-4559-40ca-942d-32ed1ca8d489.svg'
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
    icon_id = 'short-pen-beside-curved-scribble'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('pen', 'scribble', 'drawing')

    def build(self) -> None:
        def smooth(name, pts):
            """Open Catmull-Rom cubics through integer knots."""
            n = len(pts); members = []
            for i in range(n - 1):
                p1, p2 = pts[i], pts[i + 1]
                p0 = pts[i - 1] if i > 0 else p1
                p3 = pts[i + 2] if i + 2 < n else p2
                c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
                c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
                m = f"{name}-{i + 1}"; self.add_bezier(m, p1, (c1, c2, p2)); members.append(m)
            self.add_contour(name, *members)

        # Pen on a 1:3 axis: sides 3x+y=112 and 3x+y=142 (offset (9,3)), symmetric r5 cap about
        # (37,16) ending on its rightmost point x=42, collar (28,28)-(37,31) above a nib with tip (29,40) on the axis.
        _path(self, "pen", (28, 28), [(33, 13), ((42, 16), 5, 5, True), (37, 31), (29, 40), (28, 28)], True)
        self.add_line("collar", (28, 28), (37, 31))
        self.relate("connect", "pen", "collar")
        # Scribble traced from the reference: sweep down-left into a loop, over a hump,
        # then a long stroke down-left ending in a short flick (kept 2x+y <= 66, 8+ from the pen).
        smooth("scribble", [(19, 6), (10, 9), (6, 16), (10, 23), (15, 22), (18, 21), (19, 25),
                            (16, 31), (11, 36), (12, 42)])

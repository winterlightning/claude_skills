from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0dfc3e66-f572-4961-ab0a-b37e1dd66822'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__separated-spreadsheet-rows/20260927T101542Z-thuan-mac-1/reference/split subset spreadsheet_0dfc3e66-f572-4961-ab0a-b37e1dd66822.svg'
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
    icon_id = 'separated-spreadsheet-rows'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('separated', 'spreadsheet', 'rows')

    def build(self) -> None:
        # Plan: a 3-column sheet; the top block keeps two rows, the last row is split
        # off below. A dashed cut line sits exactly between them (8 from each), in
        # place of the reference's separating arrows that cannot fit 8-unit spacing.
        xs = (8, 19, 29, 40)
        # top block: rows at y 4 / 12 / 20
        for y in (4, 12, 20):
            for i in range(3):
                self.add_line(f"top-h{y}-{i}", (xs[i], y), (xs[i + 1], y))
        for x in xs:
            self.add_line(f"top-v{x}-a", (x, 4), (x, 12))
            self.add_line(f"top-v{x}-b", (x, 12), (x, 20))
        for i in range(3):
            self.add_line(f"bot-h36-{i}", (xs[i], 36), (xs[i + 1], 36))
            self.add_line(f"bot-h44-{i}", (xs[i], 44), (xs[i + 1], 44))
        for x in xs:
            self.add_line(f"bot-v{x}", (x, 36), (x, 44))
        # connections at every shared grid node
        segs = {}
        for y in (4, 12, 20):
            for i in range(3):
                segs[f"top-h{y}-{i}"] = ((xs[i], y), (xs[i + 1], y))
        for x in xs:
            segs[f"top-v{x}-a"] = ((x, 4), (x, 12)); segs[f"top-v{x}-b"] = ((x, 12), (x, 20))
        for i in range(3):
            segs[f"bot-h36-{i}"] = ((xs[i], 36), (xs[i + 1], 36)); segs[f"bot-h44-{i}"] = ((xs[i], 44), (xs[i + 1], 44))
        for x in xs:
            segs[f"bot-v{x}"] = ((x, 36), (x, 44))
        names = list(segs)
        for i, a in enumerate(names):
            for b in names[i + 1:]:
                if set(segs[a]) & set(segs[b]):
                    self.relate("connect", a, b)
        for n, (x1, x2) in enumerate(((8, 12), (20, 28), (36, 40))):
            self.add_line(f"cut-{n}", (x1, 28), (x2, 28))

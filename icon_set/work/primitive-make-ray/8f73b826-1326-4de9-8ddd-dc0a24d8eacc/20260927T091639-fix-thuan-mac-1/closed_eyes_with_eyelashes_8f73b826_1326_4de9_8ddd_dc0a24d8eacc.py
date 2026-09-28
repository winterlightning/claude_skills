from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8f73b826-1326-4de9-8ddd-dc0a24d8eacc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__closed-eyes-with-eyelashes/20260927T091421Z-thuan-mac-1/reference/close two eyes_8f73b826-1326-4de9-8ddd-dc0a24d8eacc.svg'
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
    icon_id = 'closed-eyes-with-eyelashes'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('closed', 'eyes', 'with', 'eyelashes')

    def build(self) -> None:
        # Two closed eyes, mirrored about x = 24. Each lid is a smooth U through integer knots
        # (Catmull-Rom cubics); three lashes hang from the lid knots: a vertical centre lash and two
        # side lashes splayed outward 4:3. Outer lash tips (4,24) / (44,24) are the CIRCLE radius-20
        # extremes; the inner lash tips sit 8 apart between the eyes.
        def smooth(name, pts):
            ext = [pts[0]] + pts + [pts[-1]]
            steps = []
            for i in range(1, len(ext) - 2):
                p0, p1, p2, p3 = ext[i - 1], ext[i], ext[i + 1], ext[i + 2]
                c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
                c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
                steps.append(('c', c1, c2, p2))
            _path(self, name, pts[0], steps)

        for side, sx in (("left", 1), ("right", -1)):
            x = lambda v: v if sx == 1 else 48 - v
            e1, l1, m, l2, e2 = (x(5), 18), (x(8), 21), (x(12), 22), (x(16), 21), (x(19), 18)
            smooth(f"lid-{side}", [e1, l1, m, l2, e2])
            self.add_line(f"lash-{side}-outer", l1, (x(4), 24))
            self.add_line(f"lash-{side}-mid", m, (x(12), 27))
            self.add_line(f"lash-{side}-inner", l2, (x(20), 24))
            for lash in ("outer", "mid", "inner"):
                self.relate("connect", f"lid-{side}", f"lash-{side}-{lash}")

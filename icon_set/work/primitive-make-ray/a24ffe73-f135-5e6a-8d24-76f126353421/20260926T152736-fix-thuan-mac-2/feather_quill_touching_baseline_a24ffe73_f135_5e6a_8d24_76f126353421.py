from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a24ffe73-f135-5e6a-8d24-76f126353421'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__feather-quill-touching-baseline/20260926T152555Z-thuan-mac-2/reference/quill_a24ffe73-f135-5e6a-8d24-76f126353421.svg'
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
    icon_id = 'feather-quill-touching-baseline'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('feather', 'writing', 'pen')

    def build(self) -> None:
        # Plan: quill pen on SQUARE (Lucide feather construction: vane + shaft + barb).
        # Vane: left edge cubic from the base P to the tip T (42,6) in the top-right
        # corner; the upper right edge comes down from T to the notch corner R. The
        # barb runs from R inward along y=22 to the vein top V; the lower right edge
        # leaves the barb at Q, inset from R, so the notch reads as a step as in the
        # reference. The shaft continues from P at 45 degrees to the nib, which
        # touches the left end of the baseline (y=42).
        P, T, R, Q, V, NIB = (18, 30), (42, 6), (40, 22), (35, 22), (26, 22), (6, 42)
        _path(self, 'vane', P, [
            ('c', (13, 17), (22, 6), T),
            ('c', (42, 12), (41.5, 18), R),
            Q,
            ('c', (35, 30), (27, 34), P),
        ], closed=True)
        self.add_line('vein', P, V)
        self.add_line('barb', V, Q)
        self.add_line('shaft', P, NIB)
        self.add_line('baseline', NIB, (34, 42))
        self.relate('connect', 'vane', 'vein')
        self.relate('connect', 'vane', 'barb')
        self.relate('connect', 'vein', 'barb')
        self.relate('connect', 'vane', 'shaft')
        self.relate('connect', 'vein', 'shaft')
        self.relate('connect', 'shaft', 'baseline')

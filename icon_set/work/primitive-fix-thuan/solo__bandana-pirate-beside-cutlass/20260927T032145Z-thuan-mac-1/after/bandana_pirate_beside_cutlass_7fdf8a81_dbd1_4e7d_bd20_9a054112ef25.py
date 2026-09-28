from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7fdf8a81-dbd1-4e7d-bd20-9a054112ef25'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bandana-pirate-beside-cutlass/20260927T032145Z-thuan-mac-1/reference/pirate_7fdf8a81-dbd1-4e7d-bd20-9a054112ef25.svg'
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
    icon_id = 'bandana-pirate-beside-cutlass'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('cutlass', 'pirate', 'eyepatch', 'hat', 'person', 'portrait', 'seafarer', 'costume', 'adventure')

    def build(self) -> None:
        # human ref: icon_set/references/human_ref/user.svg. Off-centre bust on the axis x=17: circular jaw
        # and shoulder arc share that axis, jaw bottom exactly 4 above the shoulder top (touching ink).
        ax, cy, r = 17, 15, 8
        # bandana: the crown half of the head, closed by the band across the head's widest line
        self.add_arc("bandana", (ax - r, cy), (ax + r, cy), radius_x=r)
        self.add_line("band", (ax + r, cy), (ax - r, cy))
        self.add_contour("bandana-cap", "bandana", "band", closed=True)
        self.add_arc("jaw", (ax + r, cy), (ax - r, cy), radius_x=r)
        self.relate("connect", "bandana-cap", "jaw")
        # knot tail hanging from the back of the band
        self.add_line("tail", (ax - r, cy), (6, 24))
        self.relate("connect", "tail", "bandana-cap"); self.relate("connect", "tail", "jaw")
        # shoulders: one arc on the same axis, top at y = cy + r + 4
        top = cy + r + 4
        self.add_arc("shoulders", (ax - 11, 42), (ax + 11, 42), radius_x=11, radius_y=42 - top)
        self.relate("connect", "jaw", "shoulders")
        # cutlass: broad blade (straight back, curved edge) whose base is the guard, grip below
        _path(self, "blade", (34, 30), [(34, 6), ('c', (40, 8), (42, 14), (42, 22)), (42, 30), (34, 30)], closed=True)
        self.add_line("grip", (38, 30), (38, 42))
        self.relate("connect", "blade", "grip")

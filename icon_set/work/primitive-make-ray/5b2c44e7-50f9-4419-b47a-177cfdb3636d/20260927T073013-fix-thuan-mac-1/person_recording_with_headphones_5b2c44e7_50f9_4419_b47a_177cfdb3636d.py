from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5b2c44e7-50f9-4419-b47a-177cfdb3636d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-recording-with-headphones/20260927T072841Z-thuan-mac-1/reference/microphone podcast person_5b2c44e7-50f9-4419-b47a-177cfdb3636d.svg'
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
    icon_id = 'person-recording-with-headphones'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'audio'
    categories = ('audio', 'primitives')
    aliases = ()
    keywords = ('person', 'recording', 'with', 'headphones')

    def build(self) -> None:
        # studio microphone: pill head, stand, base
        _path(self, "mic", (4, 18), [((12, 18), 4, 4, True), (12, 28), ((4, 28), 4, 4, True), (4, 18)], closed=True)
        self.add_line("stand", (8, 32), (8, 40))
        self.add_line("base", (4, 40), (12, 40))
        self.relate("connect", "mic", "stand"); self.relate("connect", "stand", "base")
        # head in profile facing the mic: neck, chin, nose, forehead, crown, back of the head
        _path(self, "head", (28, 40), [
            (28, 34), (22, 31), (20, 24), (22, 16),
            ('c', (23, 10), (27, 8), (32, 8)),
            ('c', (39, 8), (44, 13), (44, 22)),
            ('c', (44, 30), (40, 32), (40, 40)),
        ])
        # headphones: band dropping from the crown to an r3 ear cup
        self.add_line("band", (32, 8), (32, 18))
        _circle(self, "ear-cup", 32, 21, 3)
        self.relate("connect", "head", "band"); self.relate("connect", "band", "ear-cup")

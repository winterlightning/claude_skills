from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '44669c46-5f1b-4268-ad2e-f9c53c88603f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__waving-hand-with-motion-arcs/20260927T083044Z-thuan-mac-1/reference/photo motion sensor_44669c46-5f1b-4268-ad2e-f9c53c88603f.svg'
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
    icon_id = 'waving-hand-with-motion-arcs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'chat'
    categories = ('primitives', 'chat')
    aliases = ()
    keywords = ('hand', 'gesture', 'palm', 'fingers', 'communication', 'touch', 'human', 'greeting')

    def build(self) -> None:
        # Plan (set open-hand construction, Lucide hand idiom): raised open hand - three 8-wide
        # fingers with r4 tips (middle tallest), creases hanging from the shared finger walls, a
        # low thumb sweeping out to the left, rounded palm heel - plus a motion arc (one cubic)
        # sweeping round the hand's upper left, 9+ clear of the index finger.
        _path(self, "hand", (18, 30), [(18, 14), ((26, 14), 4, 4, True), (26, 10),
                                        ((34, 10), 4, 4, True), (34, 14), ((42, 14), 4, 4, True), (42, 30),
                                        ((30, 42), 12, 12, True), (24, 42),
                                        ('c', (16, 42), (6, 40), (6, 35)), ('c', (6, 30), (14, 27), (18, 30))], closed=True)
        self.add_line("crease-1", (26, 14), (26, 22))
        self.add_line("crease-2", (34, 14), (34, 22))
        self.relate("connect", "crease-1", "hand-2", "hand-3")
        self.relate("connect", "crease-2", "hand-5", "hand-6")
        self.add_bezier("motion", (12, 6), ((9, 8), (7, 16), (9, 21)))

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fc6689dd-a028-5cb2-b326-1fe893e5518c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__canoe-paddler/20260926T182452Z-thuan-mac-1/reference/canoe person_fc6689dd-a028-5cb2-b326-1fe893e5518c.svg'
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
    icon_id = 'canoe-paddler'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'recreation'
    categories = ('primitives', 'recreation')
    aliases = ()
    keywords = ('canoe', 'paddler')

    def build(self) -> None:
        # Canoe paddler (reference): a person seated in a canoe, arm held forward
        # to a long paddle whose blade dips in at the gunwale.
        # Hull: straight gunwale y=32 rising to two raised tips, flat bottom y=40.
        _path(self, 'hull', (8, 32), [(16, 32), (27, 32), (40, 32),
                                      ('c', (42, 31), (43, 30), (44, 28)),
                                      ('c', (44, 35), (42, 40), (38, 40)),
                                      (10, 40),
                                      ('c', (6, 40), (4, 35), (4, 28)),
                                      ('c', (5, 30), (6, 31), (8, 32))], True)
        # Seated person (full_body_ref): r4 head straight above an upright torso,
        # 8 units between head outline and neck; the arm leaves the neck level.
        _circle(self, 'head', 16, 12, 4)
        self.add_line('torso', (16, 24), (16, 32))
        self.mark_human_figure('paddler', head='head', torso='torso', torso_junction='start')
        self.add_line('arm', (16, 24), (30, 24))
        # Paddle on a 3:8 slope through the hand at (30,24).
        self.add_line('paddle-top', (36, 8), (30, 24))
        self.add_line('paddle-shaft', (30, 24), (27, 32))
        for a, b in [('torso', 'arm'), ('torso', 'hull'), ('arm', 'paddle-top'), ('arm', 'paddle-shaft'),
                     ('paddle-top', 'paddle-shaft'), ('paddle-shaft', 'hull')]:
            self.relate('connect', a, b)

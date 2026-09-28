from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '79d7b1e9-d763-4618-aea0-fb1d2e59180b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__freestyle-swimmer/20260926T171659Z-thuan-mac-1/reference/swimming_79d7b1e9-d763-4618-aea0-fb1d2e59180b.svg'
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
    icon_id = 'freestyle-swimmer'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # Water: two Lucide-style wave rows (crests at x=9,29; troughs at 19,39),
        # 10 apart so the in-phase slopes keep 8 on centerlines.
        def wave(name, y0, end=44):
            steps = [('c', (5.2, y0 - 1), (6.4, y0 - 2), (9, y0 - 2)),
                     ('c', (14, y0 - 2), (14, y0 + 2), (19, y0 + 2)),
                     ('c', (24.2, y0 + 2), (23.8, y0 - 2), (29, y0 - 2)),
                     ('c', (34, y0 - 2), (34, y0 + 2), (39, y0 + 2))]
            if end == 44:
                steps.append(('c', (41.6, y0 + 2), (42.8, y0 + 1), (44, y0)))
            _path(self, name, (4, y0), steps)
        wave('wave-top', 28, end=39)
        wave('wave-bottom', 38)
        # Swimmer: level torso at the surface, head r4 exactly 8 ahead of the neck
        # (level head gap), recovering arm raised from the shoulder, elbow high.
        _circle(self, 'head', 40, 17, 4)
        self.add_line('torso-back', (14, 17), (24, 17))
        self.add_line('torso', (24, 17), (28, 17))
        self.add_line('upper-arm', (24, 17), (18, 8))
        self.add_line('forearm', (18, 8), (6, 12))
        self.add_contour('body', 'torso-back', 'torso')
        self.add_contour('arm', 'upper-arm', 'forearm')
        self.relate('connect', 'body', 'arm')
        self.mark_human_figure('swimmer', head='head', torso='torso', torso_junction='end')

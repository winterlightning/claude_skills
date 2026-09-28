from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c76e3bee-26aa-4b66-9845-18e5b5d46930'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__sitting-rabbit/20260927T072849Z-thuan-mac-1/reference/rabbit body_c76e3bee-26aa-4b66-9845-18e5b5d46930.svg'
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
    icon_id = 'sitting-rabbit'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('rabbit', 'bunny', 'sitting', 'ears', 'hare', 'animal', 'pet', 'easter')

    def build(self) -> None:
        # Sitting rabbit, front view (reference silhouette): two upright
        # 8-wide ears with r4 tips, domed head with cheeks, narrow neck and a
        # wide round-bottomed body; leg lines rise from the base.
        _path(self, 'rabbit', (12, 16), [(12, 8), ((20, 8), 4, 4, True), (20, 14), ('c', (22, 13), (26, 13), (28, 14)),
                                         (28, 8), ((36, 8), 4, 4, True), (36, 16),
                                         ('c', (39, 18), (39, 24), (35, 27)), ('c', (38, 30), (40, 34), (40, 38)),
                                         ((34, 44), 6, 6, True), (30, 44), (18, 44), (14, 44), ((8, 38), 6, 6, True),
                                         ('c', (8, 34), (10, 30), (13, 27)), ('c', (9, 24), (9, 18), (12, 16))], True)
        self.add_line('leg-left', (18, 44), (16, 38))
        self.add_line('leg-right', (30, 44), (32, 38))
        self.relate('connect', 'leg-left', 'rabbit')
        self.relate('connect', 'leg-right', 'rabbit')
        self.add_dot('eye-left', (20, 23))
        self.add_dot('eye-right', (28, 23))

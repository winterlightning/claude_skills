from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '764d4993-c502-42d1-9520-e7dd676c9d28'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-at-podium/20260927T083044Z-thuan-mac-1/reference/woman podium_764d4993-c502-42d1-9520-e7dd676c9d28.svg'
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
    icon_id = 'woman-speaking-at-lectern'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'users'
    categories = ('users', 'primitives')
    aliases = ()
    keywords = ('woman', 'podium', 'lectern', 'speaker', 'presentation', 'speech', 'female', 'talk')

    def build(self) -> None:
        # Plan (human ref user.svg; bust behind a prop): woman speaking at a podium as in the
        # reference. Lectern: top bar y33 across the canvas with sides tapering to the bottom.
        # Woman: r5 head with straight bob locks, exactly 8 above a standalone flat shoulder line;
        # r6 rounded shoulders rise from the bar (the bar is split at their feet).
        _circle(self, "head", 24, 11, 5)
        self.add_line("hair-left", (19, 11), (19, 16))
        self.add_line("hair-right", (29, 11), (29, 16))
        self.relate("connect", "hair-left", "head")
        self.relate("connect", "hair-right", "head")
        self.add_line("shoulder-top", (20, 24), (28, 24))
        _path(self, "shoulder-left", (14, 33), [(14, 30), ((20, 24), 6, 6, True)])
        _path(self, "shoulder-right", (28, 24), [((34, 30), 6, 6, True), (34, 33)])
        self.relate("connect", "shoulder-top", "shoulder-left", "shoulder-right")
        self.mark_human_figure("speaker", head="head", torso="shoulder-top", torso_junction="start")
        _path(self, "podium-bar", (6, 33), [(14, 33), (34, 33), (42, 33)])
        self.add_line("podium-left", (6, 33), (10, 42))
        self.add_line("podium-right", (42, 33), (38, 42))
        self.relate("connect", "podium-bar", "shoulder-left", "shoulder-right", "podium-left", "podium-right")

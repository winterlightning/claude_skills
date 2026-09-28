from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f8c3aa49-8c17-4f3a-ad5a-a05cee6ca75e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-long-hair-taking-photo/20260927T083044Z-thuan-mac-1/reference/taking pictures woman_f8c3aa49-8c17-4f3a-ad5a-a05cee6ca75e.svg'
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
    icon_id = 'woman-long-hair-taking-photo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'photography'
    categories = ('photography', 'primitives')
    aliases = ()
    keywords = ('woman', 'photographer', 'camera', 'taking pictures', 'photo', 'person', 'shooting', 'capture')

    def build(self) -> None:
        # Plan: woman with long hair taking a photo, as in the reference - the camera (x6..30,
        # y16..40, viewfinder hump in its top edge, r4 lens ring 8 clear of every wall) is held in
        # front of her face; behind it her long hair rises from the camera top over the crown
        # (y6) and falls straight down her back to shoulder level (x42); her shoulder slopes
        # from the camera's right side down to the bottom edge.
        # Camera walls are standalone lines so the lens ring's exact 8 to each is straight-to-straight.
        _path(self, "camera-top", (6, 16), [(8, 16), (10, 12), (16, 12), (18, 16), (22, 16), (30, 16)])
        _path(self, "camera-right", (30, 16), [(30, 30), (30, 40)])
        self.add_line("camera-bottom", (30, 40), (6, 40))
        self.add_line("camera-left", (6, 40), (6, 16))
        self.relate("connect", "camera-top", "camera-right", "camera-left")
        self.relate("connect", "camera-bottom", "camera-right", "camera-left")
        _circle(self, "lens", 18, 28, 4)
        _path(self, "hair", (22, 16), [('c', (22, 9), (26, 6), (32, 6)), ('c', (38, 6), (42, 12), (42, 20)), (42, 24)])
        self.relate("connect", "hair", "camera-top")
        # Her shoulder leaves the camera's right side and slopes to the bottom-right corner.
        self.add_bezier("shoulder", (30, 30), ((37, 30), (42, 35), (42, 42)))
        self.relate("connect", "shoulder", "camera-right")

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ad553831-37d6-49c3-9e91-05b93acad6fd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-hangouts-meet-logo/20260927T055624Z-thuan-mac-1/reference/google hangouts meet logo_ad553831-37d6-49c3-9e91-05b93acad6fd.svg'
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
    icon_id = 'google-hangouts-meet-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('google-meet', 'hangouts-meet', 'google', 'video-call', 'logo', 'brand', 'camera')

    def build(self) -> None:
        # speech bubble r20 about the centre; its tail drops at the lower right (vertical inner edge)
        _path(self, "bubble", (4, 24), [
            ((44, 24), 20, 20, True),
            ((36, 40), 20, 20, True),     # 12-16-20 point
            (24, 44),                     # tail tip on the bottom of the circle
            (24, 40),                     # tail's vertical inner edge
            ((12, 40), 13, 13, True),     # shallow belly back to the circle
            ((4, 24), 20, 20, True),
        ], closed=True)
        # video camera: body wider than tall, lens flaring to the right
        self.add_polyline("camera", (14, 18), (26, 18), (26, 22), (26, 26), (26, 30), (14, 30), closed=True)
        self.add_polyline("lens", (26, 22), (34, 19), (34, 29), (26, 26))
        self.relate("connect", "camera", "lens")

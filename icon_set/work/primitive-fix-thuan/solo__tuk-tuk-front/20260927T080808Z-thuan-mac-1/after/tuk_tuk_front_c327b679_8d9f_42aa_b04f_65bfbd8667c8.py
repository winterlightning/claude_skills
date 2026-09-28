from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c327b679-8d9f-42aa-b04f-65bfbd8667c8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tuk-tuk-front/20260927T080808Z-thuan-mac-1/reference/tuk tuk 1_c327b679-8d9f-42aa-b04f-65bfbd8667c8.svg'
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
    icon_id = 'tuk-tuk-front'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('tuk tuk', 'auto rickshaw', 'rickshaw', 'three wheeler', 'taxi', 'asia', 'vehicle', 'front')

    def build(self) -> None:
        # Plan (front view, Lucide car-front idiom): tapered canopy roof over a straight-sided
        # body with one central headlight, one front wheel under the centre, and the two rear
        # wheels outboard of the body (the tuk-tuk's wide rear axle), all on one mirror axis x24.
        self.add_line("body-top-l", (12, 18), (24, 18))
        self.add_line("body-top-r", (24, 18), (36, 18))
        self.add_line("body-right", (36, 18), (36, 34))
        self.add_line("body-bottom-r", (36, 34), (24, 34))
        self.add_line("body-bottom-l", (24, 34), (12, 34))
        self.add_line("body-left", (12, 34), (12, 18))
        self.add_contour("body", "body-top-l", "body-top-r", "body-right", "body-bottom-r",
                         "body-bottom-l", "body-left", closed=True)
        _path(self, "canopy", (12, 18), [(16, 8), (32, 8), (36, 18)])
        self.relate("connect", "canopy", "body")
        self.add_dot("headlight", (24, 26))
        self.add_line("wheel-front", (24, 34), (24, 40))
        self.relate("connect", "wheel-front", "body-bottom-r", "body-bottom-l")
        self.add_line("wheel-rear-left", (4, 28), (4, 40))
        self.add_line("wheel-rear-right", (44, 28), (44, 40))

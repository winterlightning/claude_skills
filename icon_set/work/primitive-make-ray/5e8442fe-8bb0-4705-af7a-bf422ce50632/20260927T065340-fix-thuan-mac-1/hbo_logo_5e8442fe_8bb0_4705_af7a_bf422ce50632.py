from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5e8442fe-8bb0-4705-af7a-bf422ce50632'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hbo-logo/20260927T061820Z-thuan-mac-1/reference/hbo logo_5e8442fe-8bb0-4705-af7a-bf422ce50632.svg'
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
    icon_id = 'hbo-logo'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('hbo', 'tv', 'streaming', 'wordmark', 'logo', 'brand', 'entertainment')

    def build(self) -> None:
        # "HBO" wordmark, three narrow letters (the most 40 units allow at 8 spacing): H with a
        # centred bar, B as a stem with two rounded half-elliptical bowls (rx6, ry7), and an
        # elliptical O (rx4, ry14) instead of a straight-sided pill; letters 9 apart.
        self.add_line("h-left", (4, 10), (4, 38))
        self.add_line("h-right", (12, 10), (12, 38))
        self.add_line("h-bar", (4, 24), (12, 24))
        self.relate("connect", "h-bar", "h-left"); self.relate("connect", "h-bar", "h-right")
        _path(self, "b", (21, 24), [(21, 10), ((21, 24), 6, 7, True), ((21, 38), 6, 7, True), (21, 24)], closed=True)
        _path(self, "o", (40, 10), [((44, 24), 4, 14, True), ((40, 38), 4, 14, True), ((36, 24), 4, 14, True),
                                    ((40, 10), 4, 14, True)], closed=True)

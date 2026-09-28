from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd5e38ad3-3442-57ac-9e2b-af7bbe8cc090'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bendable-phone/20260926T182452Z-thuan-mac-1/reference/bendable phone_d5e38ad3-3442-57ac-9e2b-af7bbe8cc090.svg'
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
    icon_id = 'bendable-phone'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('phone', 'bendable', 'flexible', 'smartphone', 'mobile', 'device', 'foldable')

    def build(self) -> None:
        # Bendable phone (reference): an upright slab whose long sides both bow
        # to the left (the bend), a short speaker/home slot near the bottom.
        # Left bow control 12 - 4/0.75 puts the cubic's extreme exactly on x=8.
        k = 12 - 4 / 0.75
        _path(self, 'body', (12, 4), [(40, 4),
                                      ('c', (k + 28, 16), (k + 28, 32), (40, 44)),
                                      (12, 44),
                                      ('c', (k, 32), (k, 16), (12, 4))], True)
        self.add_line('slot', (21, 35), (27, 35))

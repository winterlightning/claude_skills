from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '46c2e428-1adc-45b9-94af-8f84b6abfeda'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__couple-under-full-moon/20260927T091421Z-thuan-mac-1/reference/qiqiao festival_46c2e428-1adc-45b9-94af-8f84b6abfeda.svg'
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
    icon_id = 'couple-under-full-moon'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    human_construction = "bust"
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('couple', 'under', 'full', 'moon')

    def build(self) -> None:
        # Qixi couple under a full moon: the full moon (r5 ring) in the top-right corner and two busts
        # whose heads rest on their shoulder arches (jaw bottom 4 above the arch top, same centre x,
        # the bust contact). The woman in front at the left has an r5 head with an r3 hair bun on
        # top; the man behind at the right has an r4 head and a shoulder arch rising from the woman's
        # shoulder foot. Deliberately asymmetric so it does not read as a face.
        _circle(self, "moon", 37, 11, 5)
        _circle(self, "woman-head", 17, 27, 5)
        _circle(self, "woman-bun", 17, 19, 3)
        self.relate("connect", "woman-head", "woman-bun")
        _path(self, "woman-shoulders", (6, 42), [((17, 36), 11, 6, True), ((28, 42), 11, 6, True)])
        _path(self, "man-shoulders", (28, 42), [((35, 38), 7, 4, True), ((42, 42), 7, 4, True)])
        _circle(self, "man-head", 35, 30, 4)
        self.relate("connect", "woman-shoulders", "man-shoulders")
        self.relate("connect", "woman-head", "woman-shoulders")
        self.relate("connect", "man-head", "man-shoulders")

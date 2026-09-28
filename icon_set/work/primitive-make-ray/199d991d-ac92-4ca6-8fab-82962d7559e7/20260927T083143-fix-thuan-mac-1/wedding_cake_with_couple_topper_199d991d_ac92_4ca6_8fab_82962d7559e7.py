from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '199d991d-ac92-4ca6-8fab-82962d7559e7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wedding-cake-with-couple-topper/20260927T083044Z-thuan-mac-1/reference/wedding cake couple_199d991d-ac92-4ca6-8fab-82962d7559e7.svg'
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
    icon_id = 'wedding-cake-with-couple-topper'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'romance'
    categories = ('primitives', 'romance')
    aliases = ()
    keywords = ('cake', 'wedding', 'couple', 'topper', 'icing', 'celebration')

    def build(self) -> None:
        # Plan: wedding cake with the couple topper, as in the reference. The cake's top edge is
        # the scalloped icing drape (rx4/ry3 scallops between knots every 8 at y32); groom
        # (straight body, rounded shoulders) and bride (bell dress) stand on the drape knots,
        # each with an r4 head exactly 8 above a flat shoulder line; the bride stands
        # shorter (head 4 lower) so the two heads never pair up as eyes.
        scallops = [((x + 8, 32), 4, 3, False) for x in (8, 16, 24, 32)]
        _path(self, "cake", (8, 32), scallops + [(40, 41), ((37, 44), 3, 3, True), (11, 44), ((8, 41), 3, 3, True),
                                                 (8, 32)], closed=True)
        _circle(self, "groom-head", 12, 8, 4)
        _path(self, "groom-body", (8, 32), [(8, 23), ((11, 20), 3, 3, True), (13, 20), ((16, 23), 3, 3, True),
                                            (16, 32)])
        _circle(self, "bride-head", 32, 12, 4)
        _path(self, "bride-body", (24, 32), [(24, 30), (28, 24), (36, 24), (40, 30), (40, 32)])
        self.relate("connect", "groom-body", "cake")
        self.relate("connect", "bride-body", "cake")

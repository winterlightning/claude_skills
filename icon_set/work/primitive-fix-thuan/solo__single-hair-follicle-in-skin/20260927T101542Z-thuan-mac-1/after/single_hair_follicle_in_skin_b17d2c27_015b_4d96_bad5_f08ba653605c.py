from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b17d2c27-015b-4d96-bad5-f08ba653605c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__single-hair-follicle-in-skin/20260927T101542Z-thuan-mac-1/reference/hair skin_b17d2c27-015b-4d96-bad5-f08ba653605c.svg'
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
    icon_id = 'single-hair-follicle-in-skin'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('single', 'hair', 'follicle', 'in', 'skin')

    def build(self) -> None:
        # Skin line: flat at y=32 on both sides with a half-ellipse dip (rx14, ry10) to the
        # bottom edge. Hair bulb: teardrop leaning right (tip (28,6)) with an r7 round base
        # about (24,26) sitting 9 above the bottom of the dip.
        _path(self, "skin", (6, 32), [(10, 32), ((24, 42), 14, 10, False), ((38, 32), 14, 10, False), (42, 32)])
        _path(self, "bulb", (28, 6), [('c', (22, 11), (17, 18), (17, 26)), ((24, 33), 7, 7, False), ((31, 26), 7, 7, False),
                                      ('c', (31, 20), (27, 14), (28, 6))], True)

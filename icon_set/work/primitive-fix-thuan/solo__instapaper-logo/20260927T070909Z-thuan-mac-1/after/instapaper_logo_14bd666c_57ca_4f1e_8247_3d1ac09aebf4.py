from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '14bd666c-57ca-4f1e-8247-3d1ac09aebf4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__instapaper-logo/20260927T070909Z-thuan-mac-1/reference/instapaper logo_14bd666c-57ca-4f1e-8247-3d1ac09aebf4.svg'
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
    icon_id = 'instapaper-logo'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('instapaper', 'reading', 'letter-i', 'logo', 'brand', 'read-later', 'articles')

    def build(self) -> None:
        # outlined serif "I": 8-tall slab serifs, 8-wide stem, curved fillets under/over the serifs
        _path(self, "i", (10, 4), [
            (38, 4), (38, 12), (32, 12), ((28, 16), 4, 4, False),
            (28, 32), ((32, 36), 4, 4, False), (38, 36), (38, 44),
            (10, 44), (10, 36), (16, 36), ((20, 32), 4, 4, False),
            (20, 16), ((16, 12), 4, 4, False), (10, 12), (10, 4),
        ], closed=True)

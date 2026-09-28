from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '865c645b-5a95-4a0c-b2d5-6bcd8df193aa'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-drive-logo-1/20260926T160438Z-thuan-mac-2/reference/google drive logo 1_865c645b-5a95-4a0c-b2d5-6bcd8df193aa.svg'
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
    icon_id = 'google-drive-logo-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('google', 'drive', 'logo', 'logos')

    def build(self) -> None:
        # Plan: Google Drive mark on HRECT_L (4..44 x 8..40), outer outline mirrored
        # about x=24. Outer: flat top (16..32, y=8), slope-2 sides to (4,32)/(44,32),
        # chamfered lower corners to the base y=40 (10..38). Inner line as in the
        # reference: from the top-left vertex down parallel to the right side to
        # P (28,32), left along y=32 to Q (14,32), then down parallel to the left
        # side to the bottom-left vertex. Every band is 8+ wide (8.9 left, 8 bottom,
        # 14.3 right).
        TL, TR, R, BR, BL, L = (16, 8), (32, 8), (44, 32), (38, 40), (10, 40), (4, 32)
        self.add_polyline('outline', TL, TR, R, BR, BL, L, closed=True)
        self.add_polyline('fold', TL, (28, 32), (14, 32), BL)
        self.relate('connect', 'outline', 'fold')

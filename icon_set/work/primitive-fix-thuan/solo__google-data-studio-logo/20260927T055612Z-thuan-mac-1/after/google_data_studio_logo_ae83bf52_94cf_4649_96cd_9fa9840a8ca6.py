from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ae83bf52-94cf-4649-96cd-9fa9840a8ca6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-data-studio-logo/20260927T055612Z-thuan-mac-1/reference/google studio logo_ae83bf52-94cf-4649-96cd-9fa9840a8ca6.svg'
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
    icon_id = 'google-data-studio-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('google-data-studio', 'looker-studio', 'google', 'reports', 'logo', 'brand', 'data')

    def build(self) -> None:
        # Plan: three 8-tall pills with r4 caps, 8 apart: top x16..40 (y4..12),
        # bottom x16..40 (y36..44), middle x8..32 (y20..28) whose right end is
        # a full r4 circle about (28,24); its left arc is the concave divider.
        def pill(name, x0, x1, y0):
            r = 4; yc = y0 + r
            _path(self, name, (x0 + r, y0), [(x1 - r, y0), ((x1, yc), r, r, True), ((x1 - r, y0 + 8), r, r, True),
                                              (x0 + r, y0 + 8), ((x0, yc), r, r, True), ((x0 + r, y0), r, r, True)], True)
        pill('pill-top', 16, 40, 4)
        pill('pill-bottom', 16, 40, 36)
        _path(self, 'pill-mid', (12, 20), [(28, 20), ((32, 24), 4, 4, True), ((28, 28), 4, 4, True), (12, 28),
                                          ((8, 24), 4, 4, True), ((12, 20), 4, 4, True)], True)
        _path(self, 'knob-left', (28, 28), [((24, 24), 4, 4, True), ((28, 20), 4, 4, True)])
        self.relate('connect', 'knob-left', 'pill-mid')

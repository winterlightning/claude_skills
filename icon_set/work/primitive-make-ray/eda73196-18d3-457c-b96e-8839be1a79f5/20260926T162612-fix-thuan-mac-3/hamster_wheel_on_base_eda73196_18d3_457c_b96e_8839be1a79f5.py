from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'eda73196-18d3-457c-b96e-8839be1a79f5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hamster-wheel-on-base/20260926T162509Z-thuan-mac/reference/hamster toy_eda73196-18d3-457c-b96e-8839be1a79f5.svg'
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
    icon_id = 'hamster-wheel-on-base'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('hamster', 'wheel', 'on', 'base')

    def build(self) -> None:
        # Plan: hamster wheel standing on a flat base, as in the reference, on
        # HRECT_L (x 4..44, y 8..40). The wheel is an r17 rim about (24,25)
        # (apex (24,8)) that rests on the full-width base line y=40, meeting it
        # at the 8-15-17 points (16,40) and (32,40). A small r3 hub ring sits at
        # the wheel centre and two spokes run from its bottom point down to those
        # same rim/base junctions, forming the reference's A-frame.
        _path(self, 'wheel', (16, 40), [
            ((7, 25), 17, 17, True), ((24, 8), 17, 17, True), ((41, 25), 17, 17, True), ((32, 40), 17, 17, True),
        ])
        _path(self, 'base', (4, 40), [(16, 40), (32, 40), (44, 40)])
        _circle(self, 'hub', 24, 25, 3)
        _path(self, 'spokes', (16, 40), [(24, 28), (32, 40)])
        for a, b in (('wheel', 'base'), ('spokes', 'base'), ('spokes', 'wheel'), ('spokes', 'hub')):
            self.relate('connect', a, b)

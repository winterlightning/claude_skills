from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '79ee2543-57a6-47b2-878d-4e073d7ac97a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-podcasts-logo/20260927T061820Z-thuan-mac-1/reference/google podcast logo_79ee2543-57a6-47b2-878d-4e073d7ac97a.svg'
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
    icon_id = 'google-podcasts-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('google-podcasts', 'podcast', 'audio', 'waveform', 'logo', 'brand', 'google')

    def build(self) -> None:
        # five capsule bars (stroke-width pills) mirrored about x=24, 10 apart: short outer capsules,
        # 55% side capsules, tall centre capsule (reference proportions). Outlined capsules need
        # 16 per bar at 8 spacing, so five cannot be outlined in 40 units; three outlined read as "0|0".
        self.add_line("centre", (24, 8), (24, 40))
        for side, s in (("left", -1), ("right", 1)):
            self.add_line(f"bar-{side}", (24 + s * 10, 13), (24 + s * 10, 35))
            self.add_line(f"dot-{side}", (24 + s * 20, 21), (24 + s * 20, 27))

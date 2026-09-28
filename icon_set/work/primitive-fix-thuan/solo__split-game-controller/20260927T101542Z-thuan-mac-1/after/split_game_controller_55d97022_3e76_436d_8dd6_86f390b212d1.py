from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '55d97022-3e76-436d-8dd6-86f390b212d1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__split-game-controller/20260927T101542Z-thuan-mac-1/reference/nintendo switch controller logo_55d97022-3e76-436d-8dd6-86f390b212d1.svg'
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
    icon_id = 'split-game-controller'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'kids'
    categories = ('primitives', 'kids')
    aliases = ()
    keywords = ('split', 'game', 'controller')

    def build(self) -> None:
        # Plan: two detached joy-con halves 8 apart, mirrored about x=24. Each half:
        # rounded outer side (r8 quarters), straight inner edge; left stick high,
        # right button low (staggered so the pair does not read as eyes).
        for side, sx in (("left", 1), ("right", -1)):
            X = lambda x: x if sx == 1 else 48 - x
            sw = sx == 1
            self.add_line(f"{side}-top", (X(20), 8), (X(12), 8))
            self.add_arc(f"{side}-top-corner", (X(12), 8), (X(4), 16), radius_x=8, radius_y=8, sweep=not sw)
            self.add_line(f"{side}-outer", (X(4), 16), (X(4), 32))
            self.add_arc(f"{side}-bottom-corner", (X(4), 32), (X(12), 40), radius_x=8, radius_y=8, sweep=not sw)
            self.add_line(f"{side}-bottom", (X(12), 40), (X(20), 40))
            self.add_line(f"{side}-inner", (X(20), 40), (X(20), 8))
            parts = [f"{side}-{p}" for p in ("top", "top-corner", "outer", "bottom-corner", "bottom", "inner")]
            for a, b in zip(parts, parts[1:] + parts[:1]):
                self.relate("connect", a, b)
        self.add_dot("left-stick", (12, 18))
        self.add_dot("right-button", (36, 30))

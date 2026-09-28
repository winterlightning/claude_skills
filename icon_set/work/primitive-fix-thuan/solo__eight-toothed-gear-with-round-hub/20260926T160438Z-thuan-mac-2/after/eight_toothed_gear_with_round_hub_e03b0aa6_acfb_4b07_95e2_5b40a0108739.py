from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e03b0aa6-acfb-4b07-95e2-5b40a0108739'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__eight-toothed-gear-with-round-hub/20260926T160438Z-thuan-mac-2/reference/rust_e03b0aa6-acfb-4b07-95e2-5b40a0108739.svg'
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
    icon_id = 'eight-toothed-gear-with-round-hub'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('gear', 'cog', 'tooth', 'hub', 'machine', 'mechanical')

    def build(self) -> None:
        # Plan: eight-toothed gear on SQUARE, 8-fold symmetric about (24,24).
        # Tapered teeth share their valley points (radius ~14.3), so no tooth has
        # parallel sides: the cardinal tooth runs valley (18,11) -> flat tip
        # (22,6)-(26,6) -> valley (30,11); the diagonal tooth runs (30,11) -> tip
        # (35,10)-(38,13) -> (37,18). Rotating by 90-degree steps keeps integer
        # points. The round hub is an r5 ring, 9 clear of the valleys.
        base = [(18, 11), (22, 6), (26, 6), (30, 11), (35, 10), (38, 13)]
        def rot(p, k):
            dx, dy = p[0] - 24, p[1] - 24
            for _ in range(k):
                dx, dy = -dy, dx
            return (24 + dx, 24 + dy)
        pts = [rot(p, k) for k in range(4) for p in base]
        _path(self, 'gear', pts[0], pts[1:] + [pts[0]], closed=True)
        _circle(self, 'hub', 24, 24, 5)

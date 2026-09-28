from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3f82561f-9d37-4d45-ae59-9435eee5c605'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hail-cloud/20260926T171659Z-thuan-mac-1/reference/weather cloud hail_3f82561f-9d37-4d45-ae59-9435eee5c605.svg'
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
    icon_id = 'hail-cloud'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'weather'
    categories = ('weather', 'primitives')
    aliases = ()
    keywords = ('cloud', 'hail', 'precipitation', 'storm', 'weather', 'ice')

    def build(self) -> None:
        # Hail cloud on SQUARE, Lucide cloud construction: a small left lobe
        # (r6 about (12,20)), a big top lobe (r8 about (20,6+8)), a short
        # shoulder step, a right lobe (r6 about (36,20)) and a flat base at
        # y=26 (standalone so the exact-8 gap to the hail certifies).  Below,
        # three parallel 1:2 hail streaks, 10 apart, as in the reference.
        _path(self, 'cloud', (12, 26), [
            ((12, 14), 6, 6, True), ((28, 14), 8, 8, True), (36, 14), ((36, 26), 6, 6, True)])
        _path(self, 'cloud-base', (36, 26), [(12, 26)])
        self.relate('connect', 'cloud', 'cloud-base')
        for i, x in enumerate((16, 26, 36)):
            self.add_line(f'hail-{i}', (x, 34), (x - 4, 42))

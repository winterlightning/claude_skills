from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f234ad7a-ef0c-45ce-83bc-05f65b8c0143'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__domed-government-building/20260927T032037Z-thuan-mac-1/reference/official building 2_f234ad7a-ef0c-45ce-83bc-05f65b8c0143.svg'
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
    icon_id = 'domed-government-building'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'landmarks'
    categories = ('landmarks', 'primitives')
    aliases = ()
    keywords = ('government', 'official', 'building', 'dome', 'civic', 'parliament', 'institution', 'architecture')

    def build(self) -> None:
        # Plan: mirrored about x=24. Spire (24,6)-(24,10) on an r8 dome over a
        # drum (x16/x32, y18-28) with an overhanging cornice at y18; base
        # cornice y28 over five posts (x8..40, pitch 8) standing on the floor y42.
        parts = {}
        def seg(name, a, b):
            self.add_line(name, a, b); parts[name] = (a, b)
        _path(self, 'dome', (16, 28), [(16, 18), ((24, 10), 8, 8, True), ((32, 18), 8, 8, True), (32, 28)])
        parts['dome'] = ((16, 28), (32, 28), (16, 18), (24, 10), (32, 18))
        seg('spire', (24, 6), (24, 10))
        seg('cornice-l', (12, 18), (16, 18)); seg('cornice-m', (16, 18), (32, 18)); seg('cornice-r', (32, 18), (36, 18))
        xs = (8, 16, 24, 32, 40)
        seg('base-top-l', (6, 28), (8, 28)); seg('base-top-r', (40, 28), (42, 28))
        seg('floor-l', (6, 42), (8, 42)); seg('floor-r', (40, 42), (42, 42))
        for a, b in zip(xs, xs[1:]):
            seg(f'base-top-{a}', (a, 28), (b, 28)); seg(f'floor-{a}', (a, 42), (b, 42))
        for x in xs:
            seg(f'post-{x}', (x, 28), (x, 42))
        names = list(parts)
        for i, a in enumerate(names):
            for b in names[i + 1:]:
                if set(parts[a]) & set(parts[b]):
                    self.relate('connect', a, b)

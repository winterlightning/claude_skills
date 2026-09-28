from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2a8a6932-7b48-4c6a-9ce2-bee1909a4df6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__gabled-outpost-with-wide-door/20260927T055612Z-thuan-mac-1/reference/outpost_2a8a6932-7b48-4c6a-9ce2-bee1909a4df6.svg'
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
    icon_id = 'gabled-outpost-with-wide-door'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('building', 'architecture', 'structure', 'roof', 'property', 'exterior', 'construction', 'urban')

    def build(self) -> None:
        # Plan: mirrored about x=24. Gable roof 2:3 from peak (24,6) to eaves
        # (6,18)/(42,18) overhanging walls x9/x39 (meeting the roof at y16);
        # ground line y42; wide door x17..31 (8 from each wall) with r3 top
        # corners at y26.
        parts = {}
        def seg(name, a, b):
            self.add_line(name, a, b); parts[name] = (a, b)
        seg('roof-l-eave', (6, 18), (9, 16)); seg('roof-l', (9, 16), (24, 6))
        seg('roof-r', (24, 6), (39, 16)); seg('roof-r-eave', (39, 16), (42, 18))
        seg('wall-l', (9, 16), (9, 42)); seg('wall-r', (39, 16), (39, 42))
        xs = (6, 9, 17, 31, 39, 42)
        for a, b in zip(xs, xs[1:]):
            seg(f'ground-{a}', (a, 42), (b, 42))
        _path(self, 'door', (17, 42), [(17, 29), ((20, 26), 3, 3, True), (28, 26), ((31, 29), 3, 3, True), (31, 42)])
        parts['door'] = ((17, 42), (31, 42))
        names = list(parts)
        for i, a in enumerate(names):
            for b in names[i + 1:]:
                if set(parts[a]) & set(parts[b]):
                    self.relate('connect', a, b)

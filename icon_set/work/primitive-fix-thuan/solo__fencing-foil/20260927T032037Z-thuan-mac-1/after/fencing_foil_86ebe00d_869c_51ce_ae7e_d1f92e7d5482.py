from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '86ebe00d-869c-51ce-ae7e-d1f92e7d5482'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__fencing-foil/20260927T032037Z-thuan-mac-1/reference/sword fencing_86ebe00d-869c-51ce-ae7e-d1f92e7d5482.svg'
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
    icon_id = 'fencing-foil'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # Plan: foil on the 45-degree axis x+y=48, tip (42,6) to pommel end
        # (6,42). Bell guard = half disc about M(14,34): chord M+-(6,6), dome of
        # two quarter cubics through apex (20,28) facing the tip. The blade
        # leaves the apex; the grip joins the chord midpoint M.
        k = 3.32
        _path(self, 'guard', (8, 28), [
            ('c', (8 + k, 28 - k), (20 - k, 28 - k), (20, 28)),
            ('c', (20 + k, 28 + k), (20 + k, 40 - k), (20, 40)),
            (14, 34), (8, 28)], True)
        self.add_line('blade', (20, 28), (42, 6))
        self.add_line('grip', (6, 42), (14, 34))
        self.relate('connect', 'blade', 'guard')
        self.relate('connect', 'grip', 'guard')

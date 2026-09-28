from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fe56252b-63a4-4c32-b432-3b4c66d7e3fb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-digital-garage-logo/20260927T055612Z-thuan-mac-1/reference/google digital garage logo_fe56252b-63a4-4c32-b432-3b4c66d7e3fb.svg'
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
    icon_id = 'google-digital-garage-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('google-digital-garage', 'google', 'learning', 'logo', 'brand', 'training', 'stack')

    def build(self) -> None:
        # Plan: three folded bands stacked on a centre crease x=24, mirrored.
        # Fold lines (x8..40): L0 peak up (24,4)/(8,10), L1 peak up
        # (24,13)/(8,19), L2 flat y28, L3 V down (8,38)/(24,44); vertical
        # spacing 9 (8.4 on the 20-degree slopes) at every point.
        lines = {
            'l0': [(8, 10), (24, 4), (40, 10)],
            'l1': [(8, 19), (24, 13), (40, 19)],
            'l2': [(8, 28), (24, 28), (40, 28)],
            'l3': [(8, 38), (24, 44), (40, 38)],
        }
        parts = {}
        def seg(name, a, b):
            self.add_line(name, a, b); parts[name] = (a, b)
        for n, (a, m, b) in lines.items():
            seg(f'{n}-l', a, m); seg(f'{n}-r', m, b)
        keys = list(lines)
        for i in range(3):
            a, b = lines[keys[i]], lines[keys[i + 1]]
            seg(f'side-l-{i}', a[0], b[0]); seg(f'side-r-{i}', a[2], b[2]); seg(f'crease-{i}', a[1], b[1])
        names = list(parts)
        for i, a in enumerate(names):
            for b in names[i + 1:]:
                if set(parts[a]) & set(parts[b]):
                    self.relate('connect', a, b)

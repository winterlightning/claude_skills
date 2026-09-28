from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a1742ade-8a9f-4504-8d9d-4fb65f1c6277'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hamburger-reference-batch-011-01/20260926T160438Z-thuan-mac-2/reference/double burger_a1742ade-8a9f-4504-8d9d-4fb65f1c6277.svg'
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
    icon_id = 'hamburger-reference-batch-011-01'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('hamburger', 'burger', 'bun', 'food', 'sandwich', 'fastfood')

    def build(self) -> None:
        # Plan: hamburger on SQUARE, mirrored about x=24. Top bun: a half-ellipse
        # dome (rx18, ry12; top y=6) closed by its flat base at y=18. Filling: a
        # wave across the full width at y=29 (three periods, amplitude 2), 9 below
        # the bun base. Bottom bun: a shallow open tray (r3 corners) along the
        # bottom edge, its tips 10 below the wave ends, as in the reference.
        _path(self, 'top-bun', (6, 18), [
            ((24, 6), 18, 12, True), ((42, 18), 18, 12, True), (6, 18),
        ], closed=True)
        k = 8 / 3
        steps = []
        for i in range(6):
            x = 6 + 6 * i
            s = -1 if i % 2 == 0 else 1
            steps.append(('c', (x + 2, 29 + s * k), (x + 4, 29 + s * k), (x + 6, 29)))
        _path(self, 'filling', (6, 29), steps)
        _path(self, 'bottom-bun', (6, 39), [
            ((9, 42), 3, 3, False), (39, 42), ((42, 39), 3, 3, False),
        ])

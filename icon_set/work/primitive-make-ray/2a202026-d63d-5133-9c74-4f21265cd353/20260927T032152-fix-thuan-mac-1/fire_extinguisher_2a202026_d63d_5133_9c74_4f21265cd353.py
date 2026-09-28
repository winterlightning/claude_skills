from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2a202026-d63d-5133-9c74-4f21265cd353'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__fire-extinguisher/20260927T032037Z-thuan-mac-1/reference/safety fire extinguisher_2a202026-d63d-5133-9c74-4f21265cd353.svg'
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
    icon_id = 'fire-extinguisher'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('fire', 'extinguisher', 'safety', 'hose', 'cylinder', 'equipment')

    def build(self) -> None:
        # Plan: tall cylinder (x18..36, domed r9 shoulder, top 19, base 42 with
        # r4 corners); valve neck x=27 from the dome up to (27,6) with a junction
        # at (27,10): spray horn to the right (tube to 33, flared cone to x42)
        # and hose to the left (r6 bend, down x=8) ending in a T nozzle tip.
        _path(self, 'body', (27, 19), [((36, 28), 9, 9, True), (36, 38), ((32, 42), 4, 4, True), (22, 42),
                                       ((18, 38), 4, 4, True), (18, 28), ((27, 19), 9, 9, True)], True)
        self.add_line('neck', (27, 19), (27, 10))
        self.add_line('valve', (27, 10), (27, 6))
        self.add_line('horn-tube', (27, 10), (33, 10))
        self.add_line('horn-top', (33, 10), (42, 6))
        self.add_line('horn-bottom', (33, 10), (42, 14))
        _path(self, 'hose', (27, 10), [(14, 10), ((8, 16), 6, 6, False), (8, 32)])
        self.add_line('nozzle-l', (8, 32), (6, 32))
        self.add_line('nozzle-r', (8, 32), (10, 32))
        for a, b in [('neck', 'body'), ('neck', 'valve'), ('neck', 'horn-tube'), ('neck', 'hose'),
                     ('valve', 'horn-tube'), ('valve', 'hose'), ('horn-tube', 'hose'),
                     ('horn-tube', 'horn-top'), ('horn-tube', 'horn-bottom'), ('horn-top', 'horn-bottom'),
                     ('hose', 'nozzle-l'), ('hose', 'nozzle-r'), ('nozzle-l', 'nozzle-r')]:
            self.relate('connect', a, b)

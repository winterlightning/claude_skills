from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '308c7b26-332e-4a63-acca-d4c8af288d7f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-above-water/20260926T171659Z-thuan-mac-1/reference/safety drown hand_308c7b26-332e-4a63-acca-d4c8af288d7f.svg'
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
    icon_id = 'hand-above-water'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('hand', 'water', 'drowning', 'rescue', 'safety', 'waves')

    def build(self) -> None:
        # Drowning hand on VRECT_L, after Lucide `hand` at 2x: raised open hand
        # with the thumb (low, left) and three fingers, each 8 wide with r4
        # tips (middle tallest), sharing their walls down to the knuckles.  The
        # outer walls round (r8) into a short wrist; one Lucide-style wave
        # (crests y=40, troughs y=44) lies 9 below the wrist.
        _path(self, 'thumb', (8, 19), [(8, 18), ((16, 18), 4, 4, True)])
        _path(self, 'wall-1-top', (16, 10), [(16, 18)])
        _path(self, 'wall-1', (16, 18), [(16, 20)])
        _path(self, 'index', (16, 10), [((24, 10), 4, 4, True)])
        _path(self, 'wall-2-top', (24, 8), [(24, 10)])
        _path(self, 'wall-2', (24, 10), [(24, 20)])
        _path(self, 'middle', (24, 8), [((32, 8), 4, 4, True)])
        _path(self, 'wall-3-top', (32, 8), [(32, 10)])
        _path(self, 'wall-3', (32, 10), [(32, 20)])
        _path(self, 'ring', (32, 10), [((40, 10), 4, 4, True), (40, 19)])
        _path(self, 'palm-left', (8, 19), [((16, 27), 8, 8, False), (16, 31)])
        _path(self, 'palm-right', (40, 19), [((32, 27), 8, 8, True), (32, 31)])
        _path(self, 'water', (8, 42), [
            ('c', (9, 41), (10.5, 40), (12, 40)), ('c', (16, 40), (16, 44), (20, 44)),
            ('c', (24, 44), (24, 40), (28, 40)), ('c', (32, 40), (32, 44), (36, 44)),
            ('c', (37.5, 44), (39, 43), (40, 42))])
        links = [('thumb', 'wall-1-top'), ('thumb', 'wall-1'), ('wall-1-top', 'wall-1'),
                 ('wall-1-top', 'index'), ('index', 'wall-2-top'), ('index', 'wall-2'),
                 ('wall-2-top', 'wall-2'), ('wall-2-top', 'middle'), ('middle', 'wall-3-top'),
                 ('wall-3-top', 'wall-3'), ('wall-3-top', 'ring'), ('wall-3', 'ring'),
                 ('thumb', 'palm-left'), ('ring', 'palm-right')]
        for a, b in links:
            self.relate('connect', a, b)

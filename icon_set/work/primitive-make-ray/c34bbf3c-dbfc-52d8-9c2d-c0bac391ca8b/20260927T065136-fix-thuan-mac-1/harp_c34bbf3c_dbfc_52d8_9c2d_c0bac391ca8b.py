from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c34bbf3c-dbfc-52d8-9c2d-c0bac391ca8b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__harp/20260927T061820Z-thuan-mac-1/reference/harp_c34bbf3c-dbfc-52d8-9c2d-c0bac391ca8b.svg'
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
    icon_id = 'harp'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'music'
    categories = ('primitives', 'music')
    aliases = ()
    keywords = ('harp', 'string', 'instrument', 'orchestra', 'classical', 'music', 'plucked')

    def build(self) -> None:
        # concert harp: upright pillar on the left rising above the neck as a finial; a wavy neck
        # (dips, then rises to the crown) runs to the top of the 45-degree soundboard, which slants
        # down-left to the base; three strings of decreasing length hang from neck knots.
        self.add_line("finial", (6, 6), (6, 12))
        self.add_line("pillar", (6, 12), (6, 42))
        _path(self, "neck", (6, 12), [('c', (9, 12), (12, 13), (15, 14)), ('c', (18, 15), (20, 17), (23, 17)),
                                      ('c', (26, 17), (28, 13), (31, 13)), ('c', (35, 13), (39, 13), (42, 14))])
        _path(self, "board", (42, 14), [(31, 25), (23, 33), (15, 41), (14, 42)])
        self.add_line("base", (6, 42), (14, 42))
        self.add_line("string-1", (15, 14), (15, 41))
        self.add_line("string-2", (23, 17), (23, 33))
        self.add_line("string-3", (31, 13), (31, 25))
        for a, b in (("finial", "pillar"), ("finial", "neck"), ("pillar", "neck"), ("neck", "board"),
                     ("pillar", "base"), ("board", "base"),
                     ("string-1", "neck"), ("string-1", "board"), ("string-2", "neck"), ("string-2", "board"),
                     ("string-3", "neck"), ("string-3", "board")):
            self.relate("connect", a, b)

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0b063dc0-3f96-438d-b587-2f87393eb9fe'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hexagonal-molecular-ring-0b063dc0/20260926T164653Z-thuan-mac/reference/molecule cube_0b063dc0-3f96-438d-b587-2f87393eb9fe.svg'
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
    icon_id = 'hexagonal-molecular-ring-0b063dc0'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('hexagonal', 'molecular', 'ring')

    def build(self) -> None:
        # Plan: pointy-top hexagon ring with three hollow atoms on alternating
        # vertices (top, lower-right, lower-left) as in the reference, on SQUARE
        # (6..42). Atoms are r4 rings (centres (24,10), (38,30), (10,30)) so the
        # holes stay open at 48px; bonds meet them at cardinal points so every
        # join is an exact shared endpoint, and the lower bonds leave the atoms'
        # south points at the hexagon's 30-degree slope. Mirrored about x=24.
        _circle(self, 'top-atom', 24, 10, 4)
        _circle(self, 'right-atom', 38, 30, 4)
        _circle(self, 'left-atom', 10, 30, 4)
        _path(self, 'right-bond', (28, 10), [(38, 17), (38, 26)])
        _path(self, 'bottom-bond', (38, 34), [(24, 42), (10, 34)])
        _path(self, 'left-bond', (10, 26), [(10, 17), (20, 10)])
        for a, b in (('top-atom', 'right-bond'), ('right-bond', 'right-atom'), ('right-atom', 'bottom-bond'),
                     ('bottom-bond', 'left-atom'), ('left-atom', 'left-bond'), ('left-bond', 'top-atom')):
            self.relate('connect', a, b)

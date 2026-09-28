from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ca818990-142d-45b3-8a5b-0503758791a8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__frowning-tree-with-angular-nose/20260926T152555Z-thuan-mac-2/reference/mario tree 1_ca818990-142d-45b3-8a5b-0503758791a8.svg'
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
    icon_id = 'frowning-tree-with-angular-nose'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'video-games'
    categories = ('video-games', 'primitive', 'primitives')
    aliases = ()
    keywords = ('frowning', 'tree', 'with', 'angular', 'nose')

    def build(self) -> None:
        # Plan: cartoon tree with a face on SQUARE, mirrored about x=24.
        # Canopy: one closed cloud outline of cubic bumps (bump helper: apex = chord
        # midpoint + h * outward normal, so the horizontal/vertical chords give exact
        # extremes y=6, x=6, x=42). Shallow scallops span the trunk top.
        # Trunk: open walls x=11 and x=37 down to the bottom edge; the angular nose
        # juts left out of the left wall; eye dot and a frown arc on the axis,
        # each 9 clear of its neighbours.
        def bump(p, q, h):
            dx, dy = q[0] - p[0], q[1] - p[1]
            L = (dx * dx + dy * dy) ** 0.5
            nx, ny = dy / L * h * 4 / 3, -dx / L * h * 4 / 3
            return ('c', (p[0] + nx, p[1] + ny), (q[0] + nx, q[1] + ny), q)
        k = [(9, 11), (20, 11), (28, 11), (39, 11), (39, 18), (37, 21), (24, 21), (11, 21), (9, 18)]
        h = [5, 3, 5, 3, 2, 1, 1, 2, 3]
        steps = [bump(k[i], k[(i + 1) % len(k)], h[i]) for i in range(len(k))]
        _path(self, 'canopy', k[0], steps, closed=True)
        _path(self, 'trunk-left', (11, 21), [(11, 26), (6, 30), (11, 34), (11, 42)])
        self.add_line('trunk-right', (37, 21), (37, 42))
        self.add_dot('eye', (24, 30))
        self.add_arc('frown', (20, 42), (28, 42), radius_x=4, radius_y=3, sweep=True)
        self.relate('connect', 'canopy', 'trunk-left')
        self.relate('connect', 'canopy', 'trunk-right')

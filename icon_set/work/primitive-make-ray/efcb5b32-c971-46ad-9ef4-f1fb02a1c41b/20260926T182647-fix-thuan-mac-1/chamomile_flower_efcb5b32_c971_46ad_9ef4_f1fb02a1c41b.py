from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'efcb5b32-c971-46ad-9ef4-f1fb02a1c41b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__chamomile-flower/20260926T182452Z-thuan-mac-1/reference/chamomile_efcb5b32-c971-46ad-9ef4-f1fb02a1c41b.svg'
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
    icon_id = 'chamomile-flower'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'nature'
    categories = ('nature', 'primitives')
    aliases = ()
    keywords = ('chamomile', 'daisy', 'flower', 'petals', 'bloom', 'herbal', 'nature', 'botanical')

    def build(self) -> None:
        # Chamomile (reference): eight long rounded petals radiating from a
        # centre disc. The petal outline is one scalloped loop whose valleys sit
        # on the disc (lattice points (7,3)/(3,7), r ~7.6); each petal is two
        # cubics meeting tangent at an integer tip on the petal axis.
        import math
        C = 24
        valleys = [(7, 3), (3, 7), (-3, 7), (-7, 3), (-7, -3), (-3, -7), (3, -7), (7, -3)]
        tips = [(20, 0), (14, 14), (0, 20), (-14, 14), (-20, 0), (-14, -14), (0, -20), (14, -14)]
        W = 6.0      # half width of the petal at its tip handle
        L = 7.0      # radial handle leaving each valley
        members = []
        for i, t in enumerate(tips):
            a, b = valleys[i - 1], valleys[i]
            ang = math.atan2(t[1], t[0])
            ux, uy = math.cos(ang), math.sin(ang)
            px, py = -uy, ux
            T = (C + t[0], C + t[1])
            A = (C + a[0], C + a[1]); B = (C + b[0], C + b[1])
            # side leaving A heads out along the petal axis direction
            c1 = (A[0] + ux * L, A[1] + uy * L)
            sa = 1 if (a[0] * px + a[1] * py) > 0 else -1
            c2 = (T[0] + px * W * sa, T[1] + py * W * sa)
            c3 = (T[0] - px * W * sa, T[1] - py * W * sa)
            c4 = (B[0] + ux * L, B[1] + uy * L)
            self.add_bezier(f'petal-{i}-a', A, (c1, c2, T))
            self.add_bezier(f'petal-{i}-b', T, (c3, c4, B))
            members += [f'petal-{i}-a', f'petal-{i}-b']
        self.add_contour('petals', *members, closed=True)
        # centre disc through the same valleys: eight cubic arcs
        R = math.hypot(7, 3)
        disc = []
        pts = valleys
        for i in range(8):
            p, q = pts[i], pts[(i + 1) % 8]
            a0, a1 = math.atan2(p[1], p[0]), math.atan2(q[1], q[0])
            d = (a1 - a0) % (2 * math.pi)
            k = 4 / 3 * math.tan(d / 4) * R
            h1 = (C + p[0] - k * math.sin(a0), C + p[1] + k * math.cos(a0))
            h2 = (C + q[0] + k * math.sin(a1), C + q[1] - k * math.cos(a1))
            self.add_bezier(f'disc-{i}', (C + p[0], C + p[1]), (h1, h2, (C + q[0], C + q[1])))
            disc.append(f'disc-{i}')
        self.add_contour('disc', *disc, closed=True)
        self.relate('connect', 'petals', 'disc')

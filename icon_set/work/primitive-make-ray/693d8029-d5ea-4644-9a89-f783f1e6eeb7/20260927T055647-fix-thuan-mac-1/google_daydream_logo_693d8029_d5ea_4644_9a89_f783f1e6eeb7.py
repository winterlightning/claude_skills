from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '693d8029-d5ea-4644-9a89-f783f1e6eeb7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-daydream-logo/20260927T055612Z-thuan-mac-1/reference/google daydream logo_693d8029-d5ea-4644-9a89-f783f1e6eeb7.svg'
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
    icon_id = 'google-daydream-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('google-daydream', 'daydream', 'vr', 'google', 'logo', 'brand', 'cloud')

    def build(self) -> None:
        # Plan: Daydream pinwheel. 7 petal circles r6 centred 14 from (24,24),
        # neighbours tangent at shared valley knots. Petal k is its circle
        # traced clockwise from the valley with petal k-1, out over the apex
        # (the top apex (24,4) sets the CIRCLE extreme) to the valley with
        # petal k+1, then on along the same circle for TAIL degrees as the
        # inward hook. Knots are rounded to the grid once and shared; cubic
        # controls follow the exact circle, shifted with their knot.
        import math
        N, RC, R, TAIL = 7, 14, 6, 40
        C = (24, 24)
        step = 360 / N
        def rnd(p, limit=None):
            q = (math.floor(p[0] + 0.5), math.floor(p[1] + 0.5))
            while limit is not None and math.dist(q, C) > limit:
                q = (q[0] - (q[0] > C[0]) + (q[0] < C[0]), q[1] - (q[1] > C[1]) + (q[1] < C[1]))
            return q
        cen = [(C[0] + RC * math.sin(math.radians(k * step)), C[1] - RC * math.cos(math.radians(k * step))) for k in range(N)]
        def onc(P, deg):
            a = math.radians(deg)
            return (P[0] + R * math.sin(a), P[1] - R * math.cos(a))
        valley = [rnd(((cen[k - 1][0] + cen[k][0]) / 2, (cen[k - 1][1] + cen[k][1]) / 2)) for k in range(N)]
        def seg(P, a0, a1, g0, g1):
            kk = 0.97 * 4 / 3 * math.tan(math.radians(a1 - a0) / 4) * R  # 3% in: no overshoot past r20
            t0 = (math.cos(math.radians(a0)), math.sin(math.radians(a0)))
            t1 = (math.cos(math.radians(a1)), math.sin(math.radians(a1)))
            return ('c', (g0[0] + kk * t0[0], g0[1] + kk * t0[1]), (g1[0] - kk * t1[0], g1[1] - kk * t1[1]), g1)
        for k in range(N):
            ph = k * step
            P = cen[k]
            a0, a1 = ph - (90 + step / 2), ph + (90 + step / 2)
            v0, v1 = valley[k], valley[(k + 1) % N]
            apex = rnd(onc(P, ph), 20 if k == 0 else 19.5)  # only the top apex touches r20
            tail = rnd(onc(P, a1 + TAIL))
            _path(self, f'petal-{k}', v0, [seg(P, a0, ph, v0, apex), seg(P, ph, a1, apex, v1), seg(P, a1, a1 + TAIL, v1, tail)])
        for k in range(N):
            self.relate('connect', f'petal-{k}', f'petal-{(k + 1) % N}')

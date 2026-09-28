from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5ba73969-e47a-4042-a380-432ecc4c1397'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-workers-at-conveyor-belt/20260927T133656Z-thuan-mac-1/reference/factory assembly line worker_5ba73969-e47a-4042-a380-432ecc4c1397.svg'
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


def _smooth(icon, name, pts, closed=True):
    """Catmull-Rom through integer knots, as cubics (closed loop or open run)."""
    n = len(pts)
    members = []
    rng = range(n) if closed else range(n - 1)
    for i in rng:
        p1, p2 = pts[i], pts[(i + 1) % n]
        p0 = pts[i - 1] if (closed or i > 0) else p1
        p3 = pts[(i + 2) % n] if (closed or i + 2 < n) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        m = f"{name}-{i + 1}"
        icon.add_bezier(m, p1, (c1, c2, p2)); members.append(m)
    icon.add_contour(name, *members, closed=closed)
    return members


class Drawing(Solo48):
    icon_id = 'two-workers-at-conveyor-belt'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('factory', 'automation', 'industry', 'manufacturing', 'production', 'machine', 'robot', 'process')

    def build(self) -> None:
        # Two workers at a conveyor belt (reference): each faces right with a rounded back, a flat shoulder top
        # exactly 8 below a ring head (cap brim jutting forward), an upper arm dropping from the shoulder and a
        # forearm reaching forward onto the belt. The belt is a band across the bottom that both stand at.
        B, BB, T, HR, L, Rt = 36, 44, 20, 4, 8, 40
        HY = T - 8 - HR
        nodes = [L, Rt]
        for i, x0 in enumerate((8, 28)):
            n = f"w{i + 1}"
            hx = x0 + 5
            _circle(self, f"{n}-head", hx, HY, HR)
            self.add_line(f"{n}-brim", (hx + HR, HY), (hx + HR + 2, HY))
            self.relate("connect", f"{n}-head", f"{n}-brim")
            _path(self, f"{n}-back", (x0, B), [(x0, T + 5), ((x0 + 5, T), 5, 5, True)])
            self.add_line(f"{n}-torso", (x0 + 5, T), (x0 + 6, T)); self.add_contour(f"{n}-shoulder", f"{n}-torso")
            _path(self, f"{n}-arm", (x0 + 6, T), [((x0 + 9, T + 3), 3, 3, True), (x0 + 9, T + 8), (x0 + 12, B)])
            for c in ("back", "arm"):
                self.relate("connect", f"{n}-{c}", f"{n}-shoulder"); self.relate("connect", f"{n}-{c}", "belt")
            self.mark_human_figure(n, head=f"{n}-head", torso=f"{n}-torso", torso_junction="start")
            nodes += [x0, x0 + 12]
        nodes = sorted(set(nodes))
        steps = [(x, B) for x in nodes[1:]]
        _path(self, "belt", (nodes[0], B), steps + [(Rt, BB), (L, BB), (L, B)], True)

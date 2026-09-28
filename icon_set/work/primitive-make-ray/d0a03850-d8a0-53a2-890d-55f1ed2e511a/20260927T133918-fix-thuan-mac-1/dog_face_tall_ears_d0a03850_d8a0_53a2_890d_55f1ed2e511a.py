from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd0a03850-d8a0-53a2-890d-55f1ed2e511a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dog-face-tall-ears/20260927T133651Z-thuan-mac-1/reference/dog-face-tall-ears_d0a03850-d8a0-53a2-890d-55f1ed2e511a.svg'
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
    icon_id = 'dog-face-tall-ears'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals',)
    aliases = ()
    keywords = ('dog', 'canine', 'pet', 'face', 'tall ears', 'lucide')

    def build(self) -> None:
        # Dog face with tall upright ears: pointed ears, a broad cranium, and a boxy muzzle that steps in
        # below the cheeks (the muzzle is what separates it from a cat), with a solid nose on the muzzle.
        _path(self, "head", (8, 24), [(10, 4), (18, 14), (30, 14), (38, 4), (40, 24), (34, 32), (34, 40),
                                      ((30, 44), 4, 4, True), (18, 44), ((14, 40), 4, 4, True), (14, 32), (8, 24)], True)
        self.add_dot("eye-left", (17, 22))
        self.add_dot("eye-right", (31, 22))
        self.add_line("nose", (23, 35), (25, 35))

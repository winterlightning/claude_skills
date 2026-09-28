from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f404fb88-9a98-5205-866b-ada53c69d0f2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__girl-head-profile/20260926T152555Z-thuan-mac-2/reference/girl head_f404fb88-9a98-5205-866b-ada53c69d0f2.svg'
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
    icon_id = 'girl-head-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'users'
    categories = ('users', 'primitives')
    aliases = ()
    keywords = ('girl', 'woman', 'head', 'profile', 'face', 'hair', 'female', 'person')

    def build(self) -> None:
        # Plan: girl's head in profile facing right on SQUARE (naturally asymmetric;
        # a head silhouette on its own neck, so no detached-head flags apply).
        # Outline: neck front up to the jaw, chin, a pointed nose (rightmost x=42),
        # brow up to the hairline point F; the hair then domes over the top (y=6),
        # falls down the back (x=10), flares out to shoulder-length ends (leftmost
        # x=6) and sweeps under into the back of the neck, which runs to the bottom
        # edge. Inside: the neck back rises to a C-shaped ear (r4, 9 clear of the
        # hair), and the hairline curves from the ear top up to F.
        F = (36, 18)
        _path(self, 'outline', (31, 42), [
            (31, 37), (39, 33), (38, 29), (42, 27), (37, 23), F,
            ('c', (37, 11), (31, 6), (24, 6)),
            ('c', (15, 6), (10, 12), (10, 20)),
            (10, 28),
            ('c', (10, 31), (8, 34), (6, 36)),
            ('c', (10, 39), (16, 39), (21, 38)),
            (20, 42),
        ])
        self.add_line('neck-back', (21, 38), (23, 28))
        self.add_arc('ear', (23, 28), (23, 20), radius_x=4, sweep=True)
        self.add_bezier('hairline', (23, 20), ((27, 15), (32, 14), F))
        self.relate('connect', 'outline', 'neck-back')
        self.relate('connect', 'neck-back', 'ear')
        self.relate('connect', 'ear', 'hairline')
        self.relate('connect', 'hairline', 'outline')

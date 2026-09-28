from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '17ad6602-c748-513a-a410-1c550f7c60d8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__eagle-head-profile/20260926T160438Z-thuan-mac-2/reference/indian eagle_17ad6602-c748-513a-a410-1c550f7c60d8.svg'
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
    icon_id = 'eagle-head-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('eagle', 'head', 'profile', 'beak', 'bird', 'raptor', 'feathers', 'wildlife')

    def build(self) -> None:
        # Plan: eagle head in profile facing right on SQUARE (naturally asymmetric).
        # One closed outline: domed crown from the rear feather spike (6,22) over the
        # top (24,6) to the beak root B, where the beak's back edge drops to G; hooked upper beak to the tip T (42,23);
        # gape back to G; the throat curves down to the chin spike (38,42); jagged
        # neck feathers (spikes on the bottom edge and the left edge) lead back to
        # the rear spike. Fierce brow line with the eye hung from it.
        B, T, G = (34, 11), (42, 23), (35, 23)
        _path(self, 'head', (6, 22), [
            ('c', (8, 13), (15, 6), (24, 6)),
            ('c', (29, 6), (32, 8), B),
            ('c', (38, 12), (42, 16), T),
            G,
            ('c', (31, 26), (31, 34), (38, 42)),
            (27, 35), (22, 42), (19, 31), (10, 38), (13, 26), (6, 22),
        ], closed=True)
        self.add_line('brow', (20, 17), (26, 18))
        self.add_line('beak-edge', B, G)
        self.relate('connect', 'head', 'beak-edge')
        self.add_dot('eye', (25, 20))
        self.relate('connect', 'brow', 'eye')

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ad100aeb-0efd-4518-a526-a736e51e1704'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__gazelle-facing-right/20260926T152555Z-thuan-mac-2/reference/gazelle_ad100aeb-0efd-4518-a526-a736e51e1704.svg'
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
    icon_id = 'gazelle-facing-right'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('gazelle', 'facing', 'right')

    def build(self) -> None:
        # Plan: gazelle in profile facing right on SQUARE (naturally asymmetric).
        # Body: one closed outline - rounded rump (leftmost x=6), level back y=22,
        # neck curving up to the nape (30,11), forehead sloping to a round r3 muzzle
        # (rightmost x=42), jaw back to the throat, rounded chest, belly tucked up
        # between the leg pairs. A long S-curved horn sweeps back from the nape to
        # the top edge. Four thin legs in a walking stride: each pair diverges
        # (back leg slants back, front leg forward); feet 8+ apart.
        _path(self, 'body', (12, 22), [
            (26, 22),
            ('c', (28, 20), (29, 15), (30, 11)),
            (39, 15),
            ((39, 21), 3, 3, True),
            (35, 23),
            ('c', (35, 28), (36, 31), (34, 33)),
            (27, 33),
            ('c', (24, 31), (19, 31), (16, 33)),
            (9, 33),
            ('c', (7, 31.5), (6, 29.5), (6, 27)),
            ('c', (6, 24), (8.5, 22), (12, 22)),
        ], closed=True)
        self.add_bezier('horn', (30, 11), ((29, 8), (27, 6), (24, 6)))
        legs = [((9, 33), (7, 42)), ((16, 33), (17, 42)), ((27, 33), (25, 42)), ((34, 33), (35, 42))]
        for i, (top, foot) in enumerate(legs):
            self.add_line(f'leg-{i + 1}', top, foot)
            self.relate('connect', 'body', f'leg-{i + 1}')
        self.relate('connect', 'body', 'horn')

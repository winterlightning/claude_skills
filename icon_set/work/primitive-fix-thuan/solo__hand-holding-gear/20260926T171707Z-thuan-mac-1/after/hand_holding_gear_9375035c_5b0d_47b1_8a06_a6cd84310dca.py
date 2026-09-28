from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9375035c-5b0d-47b1-8a06-a6cd84310dca'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-gear/20260926T171707Z-thuan-mac-1/reference/workflow teamwork cog hand_9375035c-5b0d-47b1-8a06-a6cd84310dca.svg'
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
    icon_id = 'hand-holding-gear'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'work'
    categories = ('work', 'primitives')
    aliases = ()
    keywords = ('hand', 'gear', 'cog', 'holding', 'mechanism', 'teamwork')

    def build(self) -> None:
        # Six-tooth outline gear about C=(17,18): tapered teeth (tips r~12 at +-10 degrees,
        # valley corners r~8.6 at +-24 degrees) rounded to the grid and mirrored top/bottom,
        # with a hub dot. The curled fingers (an r8 lobe) replace its two right-hand teeth.
        cx, cy = 17, 18
        upper = [(-9, 0), (-11, -4), (-9, -8), (-5, -7), (-3, -8), (-2, -12), (2, -12), (3, -8), (5, -7), (9, -8)]
        lower = [(x, -y) for x, y in reversed(upper[1:])]
        outline = lower + upper
        p = [(cx + x, cy + y) for x, y in outline]
        members = []
        for i in range(len(p) - 1):
            self.add_line(f'gear-{i}', p[i], p[i + 1])
            members.append(f'gear-{i}')
        self.add_arc('fingers', p[-1], p[0], radius_x=8, sweep=True)
        members.append('fingers')
        self.add_contour('gear', *members, closed=True)
        self.add_dot('hub', (cx, cy))
        # Back of the hand rising from the knuckles and falling to the wrist.
        self.add_bezier('back', (26, 10), ((29, 6), (42, 6), (42, 20)))
        self.add_line('wrist-back', (42, 20), (42, 42))
        self.add_contour('hand-back', 'back', 'wrist-back')
        self.relate('connect', 'hand-back', 'gear')
        # Palm edge: from the lower tooth down to the inner wrist.
        self.add_bezier('palm', (19, 30), ((20, 35), (28, 35), (28, 42)))
        self.relate('connect', 'palm', 'gear')

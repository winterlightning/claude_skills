from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '080f96e6-002a-5f7e-a063-a50263d9aaeb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__water-skier-holding-tow-line/20260927T083044Z-thuan-mac-1/reference/nautic sports water skiing_080f96e6-002a-5f7e-a063-a50263d9aaeb.svg'
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
    icon_id = 'water-skier-holding-tow-line'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'recreation'
    categories = ('primitives', 'recreation')
    aliases = ()
    keywords = ('water', 'skier', 'holding', 'tow', 'line')

    def build(self) -> None:
        # Plan (human ref full_body_ref.png): water skier leaning back - r4 head 8 above a short
        # vertical neck stub, torso to the hip, straight arms reaching forward to the tow line
        # that runs off to the right, braced legs down to the feet standing in a Lucide-style
        # water line (cubic crests/troughs of amplitude 2 about y40, knots every 8).
        _circle(self, "head", 10, 10, 4)
        self.add_line("torso", (10, 22), (10, 24))
        self.add_line("torso-lean", (10, 24), (14, 32))
        self.mark_human_figure("skier", head="head", torso="torso", torso_junction="start")
        self.add_line("arms", (10, 24), (26, 20))
        self.add_line("tow-line", (26, 20), (42, 17))
        self.add_line("legs", (14, 32), (22, 40))
        a = 8 / 3
        steps, x, up = [], 6, False
        for nx in (14, 22, 30, 38):
            cy = 40 - a if up else 40 + a
            steps.append(('c', (x + 3, cy), (nx - 3, cy), (nx, 40)))
            x, up = nx, not up
        steps.append(('c', (40, 40 - a / 2), (41, 40 - a / 2), (42, 40)))
        _path(self, "water", (6, 40), steps)
        for p, q in (("torso", "torso-lean"), ("torso", "arms"), ("torso-lean", "arms"), ("arms", "tow-line"),
                     ("torso-lean", "legs")):
            self.relate("connect", p, q)
        self.relate("connect", "legs", "water-2", "water-3")

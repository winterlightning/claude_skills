from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd16f1f81-7844-565c-b3b8-1b41d8de6f51'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__avatar-korean-woman/20260927T032145Z-thuan-mac-1/reference/avatar korean woman_d16f1f81-7844-565c-b3b8-1b41d8de6f51.svg'
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
    icon_id = 'avatar-korean-woman'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('avatar', 'korean', 'woman')

    def build(self) -> None:
        # human ref: icon_set/references/human_ref/user.svg; avatar contact: circular jaw centred on x=24,
        # its bottom exactly 4 above the straight body-top line (touching ink).
        cx, cy, r = 24, 16, 10
        top = cy + r + 4
        self.add_arc("crown", (cx - r, cy), (cx + r, cy), radius_x=r)
        self.add_arc("jaw", (cx + r, cy), (cx - r, cy), radius_x=r)
        self.add_contour("head", "crown", "jaw", closed=True)
        # side-swept fringe from the left temple to the crown's 3-4-5 point (30,8)
        self.add_bezier("fringe", (cx - r, cy), ((20, 17), (26, 14), (30, 8)))
        # long hair falling from the temples to the shoulders
        self.add_line("hair-left", (cx - r, cy), (10, top))
        self.add_line("hair-right", (cx + r, cy), (38, top))
        for part in ("fringe", "hair-left", "hair-right"):
            self.relate("connect", "head", part)
        # shoulders and body-top, split where the collar and the jaw meet it
        _path(self, "shoulder-left", (10, top), [((6, 40), 4, 10, False), (6, 42)])
        _path(self, "shoulder-right", (38, top), [((42, 40), 4, 10, True), (42, 42)])
        xs = (10, 12, 24, 36, 38)
        names = ("body-top-a", "body-top-b", "body-top-c", "body-top-d")
        for name, a, b in zip(names, xs, xs[1:]):
            self.add_line(name, (a, top), (b, top))
        for a, b in zip(names, names[1:]):
            self.relate("connect", a, b)
        self.relate("connect", "shoulder-left", "body-top-a")
        self.relate("connect", "shoulder-right", "body-top-d")
        self.relate("connect", "hair-left", "body-top-a")
        self.relate("connect", "hair-left", "shoulder-left")
        self.relate("connect", "hair-right", "body-top-d")
        self.relate("connect", "hair-right", "shoulder-right")
        self.relate("connect", "head", "body-top-b")
        self.relate("connect", "head", "body-top-c")
        # wrap collar: the left lapel runs to the hem, the right lapel folds over and ends on it
        self.add_line("lapel-left-upper", (12, top), (22, 40))
        self.add_line("lapel-left-lower", (22, 40), (24, 42))
        self.add_line("lapel-right", (36, top), (22, 40))
        self.relate("connect", "lapel-left-upper", "body-top-a")
        self.relate("connect", "lapel-left-upper", "body-top-b")
        self.relate("connect", "lapel-right", "body-top-c")
        self.relate("connect", "lapel-right", "body-top-d")
        for a, b in (("lapel-left-upper", "lapel-left-lower"), ("lapel-left-upper", "lapel-right"),
                     ("lapel-left-lower", "lapel-right")):
            self.relate("connect", a, b)

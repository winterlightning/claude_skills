from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1a6bb88a-8366-58c0-b6a2-58ed57586fb3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__avatar-woman-store-clerk/20260927T032145Z-thuan-mac-1/reference/avatar woman store clerk_1a6bb88a-8366-58c0-b6a2-58ed57586fb3.svg'
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
    icon_id = 'avatar-woman-store-clerk'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('avatar', 'woman', 'store', 'clerk')

    def build(self) -> None:
        # human ref: icon_set/references/human_ref/user.svg; avatar contact: circular jaw centred on x=24,
        # its bottom exactly 4 above the straight body-top line (touching ink).
        cx, cy, r = 24, 16, 10
        top = cy + r + 4
        self.add_arc("crown", (cx - r, cy), (cx + r, cy), radius_x=r)
        self.add_arc("jaw", (cx + r, cy), (cx - r, cy), radius_x=r)
        self.add_contour("head", "crown", "jaw", closed=True)
        # straight-cut fringe: one shallow r20 arc temple to temple
        self.add_arc("fringe", (cx - r, cy), (cx + r, cy), radius_x=20, sweep=False)
        # chin-length bob: short flicks out from the temples
        self.add_line("bob-left", (cx - r, cy), (12, 22))
        self.add_line("bob-right", (cx + r, cy), (36, 22))
        for part in ("fringe", "bob-left", "bob-right"):
            self.relate("connect", "head", part)
        # rounded shoulders meeting a short body-top; apron straps drop from the shoulder corners
        self.add_line("body-top", (16, top), (cx, top))
        self.add_line("body-top-right", (cx, top), (32, top))
        self.add_arc("shoulder-left", (16, top), (6, 42), radius_x=10, radius_y=42 - top, sweep=False)
        self.add_arc("shoulder-right", (32, top), (42, 42), radius_x=10, radius_y=42 - top, sweep=True)
        self.relate("connect", "body-top", "body-top-right")
        self.relate("connect", "body-top", "shoulder-left")
        self.relate("connect", "body-top-right", "shoulder-right")
        self.relate("connect", "head", "body-top")
        self.relate("connect", "head", "body-top-right")
        # apron bib: two straps and the bib's top edge 8 below the collar line
        self.add_line("strap-left", (16, top), (16, 42))
        self.add_line("strap-right", (32, top), (32, 42))
        self.add_line("bib", (16, top + 8), (32, top + 8))
        for a, b in (("strap-left", "body-top"), ("strap-left", "shoulder-left"), ("strap-right", "body-top-right"),
                     ("strap-right", "shoulder-right"), ("bib", "strap-left"), ("bib", "strap-right")):
            self.relate("connect", a, b)

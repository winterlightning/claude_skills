from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '22284429-fd82-4a8b-99c0-c7586e3ab52d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__avatar-woman-air-hostess-1/20260927T032145Z-thuan-mac-1/reference/woman air hostess_22284429-fd82-4a8b-99c0-c7586e3ab52d.svg'
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
    icon_id = 'avatar-woman-air-hostess-1'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('avatar', 'woman', 'air', 'hostess', '1', 'bust', 'body', 'portrait')

    def build(self) -> None:
        # human ref: icon_set/references/human_ref/user.svg. Hat avatar: the face is the lower half of an
        # r10 head hung from the cap brim; jaw centred on x=24 touches body-top (bottom 4 above it).
        cx, cy, r = 24, 20, 10
        top = cy + r + 4
        # garrison cap: an upright band with the fold rising to a peak in the middle
        self.add_polyline("cap", (12, cy), (12, 12), (18, 12), (24, 6), (30, 12), (36, 12), (36, cy))
        self.add_line("brim-left", (12, cy), (cx - r, cy))
        self.add_line("brim", (cx - r, cy), (cx + r, cy))
        self.add_line("brim-right", (cx + r, cy), (36, cy))
        self.add_arc("jaw", (cx + r, cy), (cx - r, cy), radius_x=r)
        for a, b in (("cap", "brim-left"), ("brim-left", "brim"), ("brim", "brim-right"), ("brim-right", "cap"),
                     ("jaw", "brim"), ("jaw", "brim-left"), ("jaw", "brim-right")):
            self.relate("connect", a, b)
        # bob hair from under the cap down to the shoulders
        self.add_line("hair-left", (cx - r, cy), (10, top))
        self.add_line("hair-right", (cx + r, cy), (38, top))
        for side in ("left", "right"):
            for part in ("jaw", "brim", f"brim-{side}"):
                self.relate("connect", f"hair-{side}", part)
        # shoulders and body-top
        _path(self, "shoulder-left", (10, top), [((6, 42), 4, 42 - top, False)])
        _path(self, "shoulder-right", (38, top), [((42, 42), 4, 42 - top, True)])
        xs = (10, 12, 24, 36, 38)
        names = ("body-top-a", "body-top-b", "body-top-c", "body-top-d")
        for name, a, b in zip(names, xs, xs[1:]):
            self.add_line(name, (a, top), (b, top))
        for a, b in zip(names, names[1:]):
            self.relate("connect", a, b)
        self.relate("connect", "shoulder-left", "body-top-a"); self.relate("connect", "hair-left", "body-top-a")
        self.relate("connect", "hair-left", "shoulder-left")
        self.relate("connect", "shoulder-right", "body-top-d"); self.relate("connect", "hair-right", "body-top-d")
        self.relate("connect", "hair-right", "shoulder-right")
        self.relate("connect", "jaw", "body-top-b"); self.relate("connect", "jaw", "body-top-c")
        # neckerchief V from the collar corners to the hem
        self.add_polyline("scarf", (12, top), (24, 42), (36, top))
        for n in names:
            self.relate("connect", "scarf", n)

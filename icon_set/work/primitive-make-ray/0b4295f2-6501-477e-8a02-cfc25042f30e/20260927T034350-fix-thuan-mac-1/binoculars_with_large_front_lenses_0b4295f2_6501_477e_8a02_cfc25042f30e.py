from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0b4295f2-6501-477e-8a02-cfc25042f30e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__binoculars-with-large-front-lenses/20260927T032145Z-thuan-mac-1/reference/binoculars_0b4295f2-6501-477e-8a02-cfc25042f30e.svg'
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
    icon_id = 'binoculars-with-large-front-lenses'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('binoculars', 'with', 'large', 'front', 'lenses')

    def build(self) -> None:
        # two barrels mirrored about x=24; each: eyepiece dome, outer wall tapering out, big round front lens
        for side, s in (("left", -1), ("right", 1)):
            x = lambda d: 24 + s * d
            sw = s > 0
            _path(self, f"barrel-{side}", (x(4), 16), [
                ((x(16), 16), 6, 8, sw),     # eyepiece dome, top at y=8
                (x(20), 32),                      # outer wall tapering out to the lens
                ((x(4), 32), 8, 8, sw),           # front lens: lower half circle r8
                (x(4), 16),                       # straight inner wall
            ], closed=True)
            # lens rim where the tube meets the front lens
            self.add_line(f"rim-{side}", (x(18), 24), (x(4), 24))
            self.relate("connect", f"barrel-{side}", f"rim-{side}")
        # hinge bridge between the inner walls
        self.add_line("bridge", (20, 18), (28, 18))
        self.relate("connect", "bridge", "barrel-left"); self.relate("connect", "bridge", "barrel-right")

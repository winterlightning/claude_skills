from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e4cb7fec-5844-4dee-a6d5-ffcdc23d8d21'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__brain-with-two-inner-folds/20260927T032145Z-thuan-mac-1/reference/brain_e4cb7fec-5844-4dee-a6d5-ffcdc23d8d21.svg'
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
    icon_id = 'brain-with-two-inner-folds'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'primitives')
    aliases = ()
    keywords = ('brain', 'with', 'two', 'inner', 'folds')

    def build(self) -> None:
        # Lucide-style brain mirrored about the fissure x=24. Each hemisphere is two r10 lobes: upper about
        # (16,16) and lower about (16,32) (mirrored: 32), meeting at an inward notch on the 6-8-10 point
        # (10,24). The lobes leave the fissure at (24,10) / (24,38), also 6-8-10 points, forming V notches.
        for side, s in (("left", -1), ("right", 1)):
            x = lambda d: 24 + s * d
            ccw = s < 0
            _path(self, f"hemisphere-{side}", (24, 10), [
                ((x(14), 24), 10, 10, not ccw, True),
                ((24, 38), 10, 10, not ccw, True),
            ])
        self.add_line("fissure", (24, 10), (24, 38))
        # folds curling in from the side notches: upper-left fold rises, lower-right fold drops
        self.add_bezier("fold-left", (10, 24), ((13, 24), (16, 23), (16, 20)))
        self.add_bezier("fold-right", (38, 24), ((35, 24), (32, 25), (32, 28)))
        for a, b in (("hemisphere-left", "fold-left"), ("hemisphere-right", "fold-right"),
                     ("fissure", "hemisphere-left"), ("fissure", "hemisphere-right"),
                     ("hemisphere-left", "hemisphere-right")):
            self.relate("connect", a, b)

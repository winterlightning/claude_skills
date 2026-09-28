from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'bdd1577c-6f14-5bee-a41f-fac2b80017a7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hammerhead-shark/20260927T055730Z-thuan-mac-1/reference/shark hammer_bdd1577c-6f14-5bee-a41f-fac2b80017a7.svg'
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
    icon_id = 'hammerhead-shark'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('hammerhead', 'shark', 'head', 'fins', 'sea', 'ocean', 'fish', 'predator')

    def build(self) -> None:
        # hammerhead seen from above: the head bar across the top, a long body curving down and to the
        # right like a J into a forked tail
        _path(self, "shark", (18, 12), [
            (12, 12), ((12, 4), 4, 4, True),           # head bar, left end (x=8)
            (36, 4), ((36, 12), 4, 4, True),           # top of the bar (y=4), right end (x=40)
            (30, 12),                                  # underside of the bar
            (30, 28), ('c', (30, 32), (31, 34), (34, 36)),   # right flank
            (40, 32), (37, 39), (40, 44),              # forked tail (y=44)
            (30, 42),
            ('c', (22, 42), (18, 36), (18, 28)),       # left flank curving round the belly
            (18, 12),
        ], closed=True)
        # pectoral fins: single strokes sweeping back from each flank
        self.add_line("fin-left", (18, 20), (10, 28))
        self.add_line("fin-right", (30, 20), (36, 26))
        self.relate("connect", "shark", "fin-left"); self.relate("connect", "shark", "fin-right")

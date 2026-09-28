from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '49aa3ae9-4599-4f0a-839e-996103c1a778'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wireless-mouse-with-signal/20260927T083044Z-thuan-mac-1/reference/mouse remote_49aa3ae9-4599-4f0a-839e-996103c1a778.svg'
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
    icon_id = 'wireless-mouse-with-signal'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'computers'
    categories = ('computers', 'primitives')
    aliases = ()
    keywords = ('mouse', 'wireless', 'scroll wheel', 'computer', 'peripheral')

    def build(self) -> None:
        # Plan: wireless computer mouse as in the reference - a large capsule body (20 wide, r10
        # ends, y22..44) with a short scroll-wheel stroke, under two short flat signal arcs
        # (chord 12 sagitta 2 = r10; chord 24 sagitta 4 = r20 about the canvas centre).
        # Straight sides are standalone lines so the wheel's clearances are straight-to-straight.
        self.add_arc("mouse-top", (14, 32), (34, 32), radius_x=10, radius_y=10, sweep=True)
        self.add_line("mouse-right", (34, 32), (34, 34))
        self.add_arc("mouse-bottom", (34, 34), (14, 34), radius_x=10, radius_y=10, sweep=True)
        self.add_line("mouse-left", (14, 34), (14, 32))
        self.relate("connect", "mouse-top", "mouse-right", "mouse-left")
        self.relate("connect", "mouse-bottom", "mouse-right", "mouse-left")
        self.add_line("wheel", (24, 31), (24, 34))
        self.add_arc("signal-inner", (18, 15), (30, 15), radius_x=10, radius_y=10, sweep=True)
        self.add_arc("signal-outer", (12, 8), (36, 8), radius_x=20, radius_y=20, sweep=True)

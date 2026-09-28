from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'be90db18-f520-40cb-b813-e134392a43e1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__parasailing/20260927T084830Z-thuan-mac-1/reference/sport para sailing_be90db18-f520-40cb-b813-e134392a43e1.svg'
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
    icon_id = 'parasailing'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('parasailing', 'parachute', 'boat', 'tow', 'sport', 'sea', 'adventure', 'outdoors-batch-03')

    def build(self) -> None:
        # parasailing (reference): a parachute canopy high at the right, its lines converging on
        # the hanging rider, and a tow rope running down to a speedboat with its driver at the
        # bottom left. Before showed a loose C, a ring and a bar with no rope or lines.
        self.add_arc("canopy-left", (24, 15), (33, 6), radius_x=9, radius_y=9, sweep=True)
        self.add_arc("canopy-right", (33, 6), (42, 15), radius_x=9, radius_y=9, sweep=True)
        self.add_line("canopy-hem", (42, 15), (24, 15))
        self.add_contour("canopy", "canopy-left", "canopy-right", "canopy-hem", closed=True)
        _path(self, "rider", (33, 24), [((36, 27), 3, 3, True), ((33, 30), 3, 3, True), ((30, 27), 3, 3, True),
                                        ((33, 24), 3, 3, True)], True)
        self.add_line("line-left", (24, 15), (33, 24)); self.add_line("line-right", (42, 15), (33, 24))
        for n in ("line-left", "line-right"):
            self.relate("connect", n, "canopy"); self.relate("connect", n, "rider")
        self.relate("connect", "line-left", "line-right")
        _path(self, "hull", (6, 34), [((14, 42), 8, 8, False), (18, 42), (20, 34), (12, 34), (6, 34)], True)
        self.add_line("rope", (30, 27), (20, 34))
        self.relate("connect", "rope", "rider"); self.relate("connect", "rope", "hull")
        _circle(self, "driver-head", 12, 20, 3)
        self.add_line("driver", (12, 31), (12, 34))
        self.mark_human_figure("driver", head="driver-head", torso="driver", torso_junction="start")
        self.relate("connect", "driver", "hull")

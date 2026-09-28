from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '815209de-601e-4c97-a648-8b07b9972741'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__thread-spool-and-yarn-ball/20260927T080754Z-thuan-mac-1/reference/clothes design needle yarn_815209de-601e-4c97-a648-8b07b9972741.svg'
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
    icon_id = 'thread-spool-and-yarn-ball'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'clothes'
    categories = ('primitives', 'clothes')
    aliases = ()
    keywords = ('thread', 'spool', 'and', 'yarn', 'ball')

    def build(self) -> None:
        # thread spool (overhanging flanges, walls, one thread wrap) beside a yarn ball (r10) with a wrapped strand,
        # a pin with a round head and a plain knitting needle stuck in its top
        _path(self, "flange-top", (4, 18), [(6, 18), (14, 18), (16, 18)])
        _path(self, "flange-bot", (4, 40), [(6, 40), (14, 40), (16, 40)])
        _path(self, "wall-l", (6, 18), [(6, 29), (6, 40)])
        _path(self, "wall-r", (14, 18), [(14, 29), (14, 40)])
        self.add_line("wrap", (6, 29), (14, 29))
        for w in ("wall-l", "wall-r"):
            self.relate("connect", "wrap", f"{w}-1"); self.relate("connect", "wrap", f"{w}-2")
        self.relate("connect", "wall-l-1", "flange-top-1"); self.relate("connect", "wall-l-1", "flange-top-2")
        self.relate("connect", "wall-r-1", "flange-top-2"); self.relate("connect", "wall-r-1", "flange-top-3")
        self.relate("connect", "wall-l-2", "flange-bot-1"); self.relate("connect", "wall-l-2", "flange-bot-2")
        self.relate("connect", "wall-r-2", "flange-bot-2"); self.relate("connect", "wall-r-2", "flange-bot-3")
        # yarn ball r10 about (34,30), split at the 6-8-10 points the strand and needles use
        pts = [(28, 22), (40, 22), (44, 30), (40, 38), (34, 40), (28, 38), (24, 30), (26, 24), (28, 22)]
        _path(self, "ball", pts[0], [(p, 10, 10, True) for p in pts[1:]], True)
        self.add_line("strand", (26, 24), (40, 38))
        for m in ("ball-7", "ball-8", "ball-3", "ball-4"):
            self.relate("connect", "strand", m)
        self.add_line("pin", (28, 22), (25, 14))
        _circle(self, "pin-head", 25, 11, 3)
        self.relate("connect", "pin", "pin-head-2"); self.relate("connect", "pin", "pin-head-3")
        self.add_line("needle", (40, 22), (43, 8))
        for n in ("pin", "needle"):
            for m in ("ball-1", "ball-8" if n == "pin" else "ball-2"): self.relate("connect", n, m)

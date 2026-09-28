from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9879b825-1a99-4cc8-b5d3-ebca82cb7300'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__friends-embracing/20260926T171659Z-thuan-mac-1/reference/user friends_9879b825-1a99-4cc8-b5d3-ebca82cb7300.svg'
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
    icon_id = 'friends-embracing'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'users'
    categories = ('users', 'primitives')
    aliases = ()
    keywords = ('friends', 'embrace', 'hug', 'people', 'two', 'together', 'support', 'users')

    def build(self) -> None:
        # Two user.svg busts on SQUARE (r7 heads, shoulders 8 below), mirrored
        # about x=24; their shoulders meet in a tangent notch at (24,36).  Each
        # friend's arm wraps behind the other's back, so a hand (r4 ring) rests
        # on each outer shoulder corner: the embrace reads from both hands.
        _circle(self, 'head-left', 13, 13, 7)
        _circle(self, 'head-right', 35, 13, 7)
        _circle(self, 'hand-left', 10, 32, 4)
        _circle(self, 'hand-right', 38, 32, 4)
        self.add_line('left-shoulder-top', (10, 28), (16, 28))
        self.add_arc('left-shoulder-in', (16, 28), (24, 36), radius_x=8, sweep=True)
        self.add_line('notch', (24, 36), (24, 42))
        self.add_arc('right-shoulder-in', (24, 36), (32, 28), radius_x=8, sweep=True)
        self.add_line('right-shoulder-top', (32, 28), (38, 28))
        self.add_contour('shoulders', 'left-shoulder-top', 'left-shoulder-in', 'right-shoulder-in', 'right-shoulder-top')
        self.add_contour('middle', 'notch')
        self.add_line('left-side', (10, 36), (10, 42))
        self.add_line('right-side', (38, 36), (38, 42))
        self.relate('connect', 'shoulders', 'middle')
        self.relate('connect', 'hand-left', 'shoulders')
        self.relate('connect', 'hand-left', 'left-side')
        self.relate('connect', 'hand-right', 'shoulders')
        self.relate('connect', 'hand-right', 'right-side')
        self.mark_human_figure('left', head='head-left', torso='left-shoulder-top', torso_junction='start')
        self.mark_human_figure('right', head='head-right', torso='right-shoulder-top', torso_junction='end')

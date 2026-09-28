from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fc3c63fc-721e-43dd-a5cf-cb7496abf926'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__friends-arm-on-shoulder/20260926T171659Z-thuan-mac-1/reference/user friends 2_fc3c63fc-721e-43dd-a5cf-cb7496abf926.svg'
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
    icon_id = 'friends-arm-on-shoulder'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'users'
    categories = ('users', 'primitives')
    aliases = ()
    keywords = ('friends', 'people', 'two', 'shoulder', 'support', 'together', 'pair', 'users')

    def build(self) -> None:
        # Two user.svg busts on SQUARE (r7 heads, shoulders 8 below): the front
        # friend on the left, the friend behind on the right; their shoulders
        # meet in a tangent notch at (24,36).  The friend behind rests a hand
        # (r4 ring) on the front friend's far shoulder corner, so the front
        # outline starts and ends at the hand, as in the reference.
        _circle(self, 'head-front', 13, 13, 7)
        _circle(self, 'head-behind', 35, 13, 7)
        _circle(self, 'hand', 10, 32, 4)
        self.add_line('front-shoulder-top', (10, 28), (16, 28))
        self.add_arc('front-shoulder-right', (16, 28), (24, 36), radius_x=8, sweep=True)
        self.add_line('front-side-right', (24, 36), (24, 42))
        self.add_contour('front-body', 'front-shoulder-top', 'front-shoulder-right', 'front-side-right')
        self.add_line('front-side-left', (10, 36), (10, 42))
        self.add_arc('behind-shoulder-left', (24, 36), (32, 28), radius_x=8, sweep=True)
        self.add_line('behind-shoulder-top', (32, 28), (34, 28))
        self.add_arc('behind-shoulder-right', (34, 28), (42, 36), radius_x=8, sweep=True)
        self.add_line('behind-side', (42, 36), (42, 42))
        self.add_contour('behind-body', 'behind-shoulder-left', 'behind-shoulder-top', 'behind-shoulder-right', 'behind-side')
        self.relate('connect', 'front-body', 'behind-body')
        self.relate('connect', 'hand', 'front-body')
        self.relate('connect', 'hand', 'front-side-left')
        self.mark_human_figure('front', head='head-front', torso='front-shoulder-top', torso_junction='start')
        self.mark_human_figure('behind', head='head-behind', torso='behind-shoulder-top', torso_junction='end')

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '04994de3-17cd-4356-ab95-14fde2baca81'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__gamer-with-controller/20260926T171659Z-thuan-mac-1/reference/gamer_04994de3-17cd-4356-ab95-14fde2baca81.svg'
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
    icon_id = 'gamer-with-controller'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'recreation'
    categories = ('primitives', 'recreation')
    aliases = ()
    keywords = ('gamer', 'with', 'controller')

    def build(self) -> None:
        # Gamer on VRECT_L: user.svg head (r4) exactly 8 above a standalone
        # shoulder line; the shoulders round down (r8) into the hands, which
        # become a full-width gamepad: grips rounded (r4) at the bottom, a
        # shallow r5 notch (2 deep) between them, a d-pad plus and one button.
        # Straight walls are standalone connected parts so exact-8 gaps certify.
        _circle(self, 'head', 24, 8, 4)
        self.add_line('shoulders', (16, 20), (32, 20))
        self.add_contour('shoulders-c', 'shoulders')
        _path(self, 'shoulder-right', (32, 20), [((40, 28), 8, 8, True)])
        _path(self, 'wall-right', (40, 28), [(40, 40)])
        _path(self, 'pad-bottom', (40, 40), [
            ((36, 44), 4, 4, True), (28, 44), ((20, 44), 5, 5, False), (12, 44),
            ((8, 40), 4, 4, True)])
        _path(self, 'wall-left', (8, 40), [(8, 28)])
        _path(self, 'shoulder-left', (8, 28), [((16, 20), 8, 8, True)])
        chain = ['shoulders-c', 'shoulder-right', 'wall-right', 'pad-bottom', 'wall-left', 'shoulder-left']
        for a, b in zip(chain, chain[1:] + chain[:1]):
            self.relate('connect', a, b)
        self.add_line('dpad-h', (16, 31), (22, 31))
        self.add_line('dpad-v', (19, 28), (19, 34))
        self.relate('connect', 'dpad-h', 'dpad-v')
        self.add_dot('button', (30, 31))
        self.mark_human_figure('gamer', head='head', torso='shoulders', torso_junction='start')

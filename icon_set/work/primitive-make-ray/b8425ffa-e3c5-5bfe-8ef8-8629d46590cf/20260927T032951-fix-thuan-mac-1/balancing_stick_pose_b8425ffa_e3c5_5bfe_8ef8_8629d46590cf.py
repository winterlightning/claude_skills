from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b8425ffa-e3c5-5bfe-8ef8-8629d46590cf'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__balancing-stick-pose/20260927T032145Z-thuan-mac-1/reference/yoga balancing stick pose_b8425ffa-e3c5-5bfe-8ef8-8629d46590cf.svg'
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
    icon_id = 'balancing-stick-pose'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('balancing', 'stick', 'pose')

    def build(self) -> None:
        # Warrior III (balancing stick): level torso at y=14, arms reaching forward and the raised leg
        # lifting slightly (the reference's shallow V), standing leg dropping from the hip, head hanging
        # below the neck (human_ref full_body_ref.png).
        self.add_line("arms", (4, 10), (12, 14))
        self.add_line("torso", (12, 14), (28, 14))
        self.add_line("raised-leg", (28, 14), (44, 10))
        self.add_line("standing-leg", (28, 14), (28, 38))
        self.relate("connect", "arms", "torso")
        self.relate("connect", "torso", "raised-leg")
        self.relate("connect", "torso", "standing-leg")
        self.relate("connect", "raised-leg", "standing-leg")
        # head r5 at (12,27): top at y=22, exactly 8 below the neck on the level torso (4-unit ink gap)
        _circle(self, "head", 12, 27, 5)
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")

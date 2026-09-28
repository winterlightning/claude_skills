from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '756e0e62-d045-4387-8d15-670479377f26'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__golfer-swinging-club/20260926T171651Z-thuan-mac-1/reference/golf player_756e0e62-d045-4387-8d15-670479377f26.svg'
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
    icon_id = 'golfer-swinging-club'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('golf', 'golfer', 'club', 'swing', 'athlete', 'sport')

    def build(self) -> None:
        # Plan: the reference's golfer at the top of the backswing, on VRECT_L
        # (x 8..40, y 4..44), human_ref full_body vocabulary: r4 head straight
        # above a short vertical neck run (exact 8 gap), torso leaning back to
        # the hip, straight arms from the shoulder to the hands at the right
        # edge, the club running at 45 degrees from the hands back over the
        # head to the top edge with a short club head, the back leg straight down-left and the front
        # knee bent forward, as drawn.
        _circle(self, 'head', 15, 11, 4)
        self.add_line('torso', (15, 23), (15, 25))
        _path(self, 'body', (15, 25), [(19, 33)])
        _path(self, 'arms', (15, 25), [(40, 16)])
        _path(self, 'club', (40, 16), [(28, 4), (25, 4)])
        _path(self, 'back-leg', (19, 33), [(8, 44)])
        _path(self, 'front-leg', (19, 33), [(27, 36), (26, 44)])
        for a, b in (('torso', 'body'), ('torso', 'arms'), ('body', 'arms'), ('arms', 'club'), ('body', 'back-leg'),
                     ('body', 'front-leg'), ('back-leg', 'front-leg')):
            self.relate('connect', a, b)
        self.mark_human_figure('golfer', head='head', torso='torso', torso_junction='start')

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e028ee6d-d92d-5900-9c83-3bd4dee52a2d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__football-runner-extended-arm/20260926T171651Z-thuan-mac-1/reference/american football run ball_e028ee6d-d92d-5900-9c83-3bd4dee52a2d.svg'
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
    icon_id = 'football-runner-extended-arm'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('football', 'runner', 'extended', 'arm')

    def build(self) -> None:
        # Plan: runner carrying an American football, as in the reference, on
        # HRECT_L (x 4..44, y 8..40), human_ref full_body vocabulary: r4 head
        # straight above a short vertical neck run (exact 8 gap), torso
        # leaning to the hip, the stiff arm extended far back up-left with a
        # bent elbow, the other arm holding a 45-degree football (four cubics
        # through the seam ends, seam across the middle) out in front,
        # stance leg down-left, trailing leg behind.
        _circle(self, 'head', 24, 12, 4)
        self.add_line('torso', (24, 24), (24, 25))
        _path(self, 'body', (24, 25), [(21, 33)])
        _path(self, 'stiff-arm', (24, 25), [(14, 24), (4, 17)])
        _path(self, 'carry-arm', (24, 25), [(32, 30)])
        _path(self, 'ball', (32, 30), [('c', (32.0, 27.0), (33.0, 23.0), (35, 21)),
                                       ('c', (37.0, 19.0), (41.0, 18.0), (44, 18)),
                                       ('c', (44.0, 21.0), (43.0, 25.0), (41, 27)),
                                       ('c', (39.0, 29.0), (35.0, 30.0), (32, 30))], True)
        _path(self, 'seam', (35, 21), [(41, 27)])
        _path(self, 'stance-leg', (21, 33), [(16, 36), (14, 40)])
        _path(self, 'trail-leg', (21, 33), [(27, 38), (36, 40)])
        for a, b in (('torso', 'body'), ('torso', 'stiff-arm'), ('body', 'stiff-arm'), ('torso', 'carry-arm'), ('body', 'carry-arm'),
                     ('stiff-arm', 'carry-arm'), ('carry-arm', 'ball'), ('ball', 'seam'), ('body', 'stance-leg'), ('body', 'trail-leg'), ('stance-leg', 'trail-leg')):
            self.relate('connect', a, b)
        self.mark_human_figure('runner', head='head', torso='torso', torso_junction='start')

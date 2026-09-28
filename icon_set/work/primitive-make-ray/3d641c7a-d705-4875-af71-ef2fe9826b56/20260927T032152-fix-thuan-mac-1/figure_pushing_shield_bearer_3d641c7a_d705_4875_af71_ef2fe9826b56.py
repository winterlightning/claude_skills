from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3d641c7a-d705-4875-af71-ef2fe9826b56'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__figure-pushing-shield-bearer/20260927T032037Z-thuan-mac-1/reference/protest police shield_3d641c7a-d705-4875-af71-ef2fe9826b56.svg'
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
    icon_id = 'figure-pushing-shield-bearer'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'protection'
    categories = ('protection', 'primitives')
    aliases = ()
    keywords = ('protest', 'police', 'riot', 'shield', 'push', 'clash', 'figures', 'conflict')

    def build(self) -> None:
        # Plan: two stick figures (full_body_ref vocabulary, r5 heads, head gap
        # exactly 8 on centerlines above a vertical neck segment). Left: officer
        # holding a tall riot shield (x=6) with one arm. Right: protester leaning
        # in (hip set back) with a straight pushing arm, hand 8 short of the
        # officer's torso, legs in a lunge.
        _circle(self, 'officer-head', 18, 11, 5)
        self.add_line('officer-torso', (18, 24), (18, 28))
        self.add_line('officer-torso-low', (18, 28), (18, 33))
        self.add_line('shield-top', (6, 17), (6, 30))
        self.add_line('shield-bottom', (6, 30), (6, 37))
        self.add_line('officer-arm', (18, 28), (6, 30))
        self.add_line('officer-leg-l', (18, 33), (13, 42))
        self.add_line('officer-leg-r', (18, 33), (22, 42))
        _circle(self, 'rioter-head', 36, 11, 5)
        self.add_line('rioter-torso', (36, 24), (36, 26))
        self.add_line('rioter-torso-low', (36, 26), (39, 33))
        self.add_line('rioter-arm', (36, 26), (26, 26))
        self.add_line('rioter-leg-front', (39, 33), (32, 42))
        self.add_line('rioter-leg-back', (39, 33), (42, 42))
        for a, b in [('officer-torso', 'officer-torso-low'), ('officer-torso-low', 'officer-arm'),
                     ('officer-torso', 'officer-arm'), ('shield-top', 'shield-bottom'),
                     ('officer-arm', 'shield-top'), ('officer-arm', 'shield-bottom'),
                     ('officer-torso-low', 'officer-leg-l'), ('officer-torso-low', 'officer-leg-r'),
                     ('officer-leg-l', 'officer-leg-r'),
                     ('rioter-torso', 'rioter-torso-low'), ('rioter-torso', 'rioter-arm'),
                     ('rioter-torso-low', 'rioter-arm'),
                     ('rioter-torso-low', 'rioter-leg-front'), ('rioter-torso-low', 'rioter-leg-back'),
                     ('rioter-leg-front', 'rioter-leg-back')]:
            self.relate('connect', a, b)
        self.mark_human_figure('officer', head='officer-head', torso='officer-torso', torso_junction='start')
        self.mark_human_figure('protester', head='rioter-head', torso='rioter-torso', torso_junction='start')

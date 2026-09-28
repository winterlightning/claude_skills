from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '40f30170-9a8c-4510-88d6-0482efa9bc76'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hiker-with-staff-climbing-step/20260926T164653Z-thuan-mac/reference/trekking top_40f30170-9a8c-4510-88d6-0482efa9bc76.svg'
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
    icon_id = 'hiker-with-staff-climbing-step'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('hiker', 'with', 'staff', 'climbing', 'step', 'outdoors', 'outdoors-batch-04')

    def build(self) -> None:
        # Plan: hiker climbing with a staff, as in the reference, on VRECT_L
        # (x 8..40, y 4..44), in the shared stick-figure vocabulary
        # (human_ref/full_body_ref.png): r4 head straight above a vertical torso
        # (exact 8 centerline gap at the neck), a backpack with rounded outer
        # corners whose right side is the torso, a bent arm reaching forward to
        # grip the tall staff, the front leg raised onto a step (knee bent) and
        # the back leg pushing off.
        _circle(self, 'head', 22, 8, 4)
        self.add_line('torso', (22, 20), (22, 24))
        _path(self, 'body', (22, 24), [(22, 31), (22, 34)])
        _path(self, 'pack', (22, 20), [(12, 20), ((8, 24), 4, 4, False), (8, 27), ((12, 31), 4, 4, False), (22, 31)])
        _path(self, 'arm', (22, 24), [(30, 27), (40, 21)])
        _path(self, 'staff-top', (40, 10), [(40, 21)])
        _path(self, 'staff', (40, 21), [(40, 44)])
        _path(self, 'front-leg', (22, 34), [(31, 36), (31, 42)])
        _path(self, 'back-leg', (22, 34), [(15, 44)])
        for a, b in (('torso', 'body'), ('torso', 'pack'), ('body', 'pack'), ('body', 'arm'), ('arm', 'staff-top'),
                     ('arm', 'staff'), ('staff-top', 'staff'), ('body', 'front-leg'), ('body', 'back-leg'),
                     ('front-leg', 'back-leg')):
            self.relate('connect', a, b)
        self.mark_human_figure('hiker', head='head', torso='torso', torso_junction='start')

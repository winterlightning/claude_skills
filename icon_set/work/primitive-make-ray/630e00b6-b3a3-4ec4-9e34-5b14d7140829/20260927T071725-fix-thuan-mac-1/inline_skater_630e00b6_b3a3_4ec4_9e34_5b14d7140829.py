from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '630e00b6-b3a3-4ec4-9e34-5b14d7140829'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__inline-skater/20260927T070909Z-thuan-mac-1/reference/rollerblades person_630e00b6-b3a3-4ec4-9e34-5b14d7140829.svg'
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
    icon_id = 'inline-skater'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('inline', 'skater')

    def build(self) -> None:
        # inline skater (human ref full_body_ref.png): r3 head straight above a short vertical neck
        # segment (exact 8-unit centreline gap), torso leaning forward to the hip, arm swinging forward,
        # front leg bent down onto the skate blade, back leg kicked up behind
        _circle(self, "head", 30, 9, 3)
        self.add_line("torso", (30, 20), (30, 22))
        self.add_line("torso-lean", (30, 22), (24, 28))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        self.add_line("arm", (30, 22), (42, 16))
        self.add_polyline("front-leg", (24, 28), (32, 32), (30, 42))
        self.add_polyline("back-leg", (24, 28), (18, 22), (6, 24))
        self.add_line("skate-back", (22, 42), (30, 42))
        self.add_line("skate-front", (30, 42), (38, 42))
        for a, b in (("torso", "torso-lean"), ("torso", "arm"), ("torso-lean", "arm"), ("torso-lean", "front-leg"),
                     ("torso-lean", "back-leg"), ("front-leg", "back-leg"), ("front-leg", "skate-back"),
                     ("front-leg", "skate-front"), ("skate-back", "skate-front")):
            self.relate("connect", a, b)

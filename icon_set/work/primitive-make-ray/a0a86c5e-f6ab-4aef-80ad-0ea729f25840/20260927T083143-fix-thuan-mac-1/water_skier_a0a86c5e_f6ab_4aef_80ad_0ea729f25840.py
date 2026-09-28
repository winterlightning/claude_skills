from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a0a86c5e-f6ab-4aef-80ad-0ea729f25840'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__water-skier/20260927T083044Z-thuan-mac-1/reference/skating_a0a86c5e-f6ab-4aef-80ad-0ea729f25840.svg'
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
    icon_id = 'water-skier'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('water', 'skier', 'skiing', 'rider', 'glide', 'sport')

    def build(self) -> None:
        # Plan (human ref full_body_ref.png; reference pose): water skier riding a wave crest -
        # r4 head 8 above a short vertical neck stub, torso leaning back to a forward hip, braced
        # leg down to the foot on the wave crest, arms forward to the tow rope that rises and
        # levels off to the right. The wave is two cubic troughs (bottom exactly y42).
        _circle(self, "head", 10, 10, 4)
        self.add_line("torso", (10, 22), (10, 24))
        self.add_line("torso-lean", (10, 24), (14, 33))
        self.mark_human_figure("skier", head="head", torso="torso", torso_junction="start")
        self.add_line("arms", (10, 24), (23, 20))
        _path(self, "rope", (23, 20), [(31, 17), (42, 17)])
        self.add_line("leg", (14, 33), (24, 38))
        t = 38 + 4 / 0.75
        _path(self, "wave", (6, 38), [('c', (11, t), (19, t), (24, 38)), ('c', (29, t), (37, t), (42, 38))])
        for p, q in (("torso", "torso-lean"), ("torso", "arms"), ("torso-lean", "arms"), ("arms", "rope"),
                     ("torso-lean", "leg")):
            self.relate("connect", p, q)
        self.relate("connect", "leg", "wave")

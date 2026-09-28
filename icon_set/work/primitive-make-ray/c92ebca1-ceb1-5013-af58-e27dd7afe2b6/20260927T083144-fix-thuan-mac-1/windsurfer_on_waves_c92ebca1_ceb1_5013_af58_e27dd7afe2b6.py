from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c92ebca1-ceb1-5013-af58-e27dd7afe2b6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__windsurfer-on-waves/20260927T083044Z-thuan-mac-1/reference/sport windsurfing_c92ebca1-ceb1-5013-af58-e27dd7afe2b6.svg'
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
    icon_id = 'windsurfer-on-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'recreation'
    categories = ('primitives', 'recreation')
    aliases = ()
    keywords = ('windsurfer', 'on', 'waves')

    def build(self) -> None:
        # Plan (human ref full_body_ref.png; reference layout): tall sail on the left - 1:4 mast
        # (26,6)->(17,42) with lattice nodes, cubic leech bulging left to the clew, flat foot back to
        # the mast - and the rider on the right: r4 head 8 above a vertical neck stub, arms level
        # to the boom node on the mast, legs apart on the flat board.
        _path(self, "sail", (26, 6), [(21, 26), (19, 34), (8, 34), ('c', (6, 24), (10, 10), (26, 6))], closed=True)
        self.add_line("mast-foot", (19, 34), (17, 42))
        _path(self, "board", (6, 42), [(17, 42), (31, 42), (42, 42)])
        self.relate("connect", "mast-foot", "sail-2", "sail-3", "board-1", "board-2")
        _circle(self, "head", 37, 12, 4)
        self.add_line("torso", (37, 24), (37, 26))
        self.add_line("torso-lean", (37, 26), (37, 33))
        self.mark_human_figure("rider", head="head", torso="torso", torso_junction="start")
        self.add_line("arms", (37, 26), (21, 26))
        self.add_line("leg-front", (37, 33), (31, 42))
        self.add_line("leg-back", (37, 33), (42, 42))
        for p, q in (("torso", "torso-lean"), ("torso", "arms"), ("torso-lean", "arms"), ("torso-lean", "leg-front"),
                     ("torso-lean", "leg-back"), ("leg-front", "leg-back")):
            self.relate("connect", p, q)
        self.relate("connect", "arms", "sail-1", "sail-2")
        self.relate("connect", "leg-front", "board-2", "board-3")
        self.relate("connect", "leg-back", "board-3")

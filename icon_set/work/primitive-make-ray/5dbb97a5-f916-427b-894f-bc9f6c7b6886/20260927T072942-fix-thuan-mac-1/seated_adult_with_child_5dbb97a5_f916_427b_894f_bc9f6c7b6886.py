from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5dbb97a5-f916-427b-894f-bc9f6c7b6886'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-adult-with-child/20260927T072849Z-thuan-mac-1/reference/seat child_5dbb97a5-f916-427b-894f-bc9f6c7b6886.svg'
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
    icon_id = 'seated-adult-with-child'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('adult', 'child', 'seated', 'lap', 'priority', 'seat')

    def build(self) -> None:
        # Two seated stick figures (full_body_ref.png): adult on the left in
        # a chair with a curved back, smaller child beside. Each ring head
        # sits straight above its vertical neck, 8 on centerlines.
        _circle(self, 'adult-head', 16, 11, 5)
        self.add_line('adult-torso', (16, 24), (16, 33))
        _path(self, 'adult-leg', (16, 33), [(25, 33), (25, 42)])
        _path(self, 'chair', (6, 24), [(6, 37), ((10, 41), 4, 4, False)])
        self.add_line('chair-seat', (10, 41), (17, 41))
        self.relate('connect', 'chair', 'chair-seat')
        _circle(self, 'child-head', 34, 17, 4)
        self.add_line('child-torso', (34, 29), (34, 35))
        _path(self, 'child-leg', (34, 35), [(42, 35), (42, 42)])
        self.relate('connect', 'adult-torso', 'adult-leg')
        self.relate('connect', 'child-torso', 'child-leg')
        self.mark_human_figure('adult', head='adult-head', torso='adult-torso', torso_junction='start')
        self.mark_human_figure('child', head='child-head', torso='child-torso', torso_junction='start')

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '38f93e3b-3368-5ce7-82af-b9f5884e7642'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-scrubbing-face/20260927T072841Z-thuan-mac-1/reference/cleanser scrubing_38f93e3b-3368-5ce7-82af-b9f5884e7642.svg'
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
    icon_id = 'person-scrubbing-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('person', 'face', 'scrubbing', 'washing', 'pad', 'hygiene')

    def build(self) -> None:
        # bust washing the face (human ref user.svg): r9 head, shoulder arch exactly 8 below it; the hand
        # (r3) presses on the side of the face, forearm dropping from it; soap bubbles beside the head
        _circle(self, "head", 28, 15, 9)
        self.add_arc("shoulders", (18, 42), (42, 42), radius_x=12, radius_y=10)
        self.mark_human_figure("person", head="head", torso="shoulders", torso_junction="start")
        _circle(self, "hand", 16, 15, 3)
        self.add_line("forearm", (16, 18), (8, 42))
        self.relate("connect", "hand", "forearm"); self.relate("connect", "hand", "head")
        self.add_dot("bubble", (7, 7))
        self.add_dot("bubble-small", (6, 21))

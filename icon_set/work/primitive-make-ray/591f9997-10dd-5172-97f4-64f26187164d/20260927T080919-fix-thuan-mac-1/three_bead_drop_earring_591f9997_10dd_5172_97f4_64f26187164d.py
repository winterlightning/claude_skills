from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '591f9997-10dd-5172-97f4-64f26187164d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-bead-drop-earring/20260927T080754Z-thuan-mac-1/reference/earring_591f9997-10dd-5172-97f4-64f26187164d.svg'
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
    icon_id = 'three-bead-drop-earring'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'accessories'
    categories = ('primitives', 'accessories')
    aliases = ()
    keywords = ('earring', 'bead', 'drop', 'pearl', 'jewellery', 'jewelry', 'circle', 'accessory')

    def build(self) -> None:
        # hanging earring on one vertical axis: hook bead on a visible link, large bead, drop bead hung directly below
        _circle(self, "bead-top", 24, 9, 5)
        self.add_line("link-1", (24, 14), (24, 20))
        _circle(self, "bead-mid", 24, 28, 8)
        _circle(self, "bead-drop", 24, 40, 4)
        for a, b in (("bead-top-2", "link-1"), ("bead-top-3", "link-1"), ("link-1", "bead-mid-1"), ("link-1", "bead-mid-4"),
                     ("bead-mid-2", "bead-drop-1"), ("bead-mid-3", "bead-drop-1"), ("bead-mid-2", "bead-drop-4"), ("bead-mid-3", "bead-drop-4")):
            self.relate("connect", a, b)

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'adeca2a9-4991-40c1-9620-baf03987dc2a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__blazer-with-notched-lapels/20260927T032145Z-thuan-mac-1/reference/blazer_adeca2a9-4991-40c1-9620-baf03987dc2a.svg'
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
    icon_id = 'blazer-with-notched-lapels'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'clothes'
    categories = ('primitives', 'clothes')
    aliases = ()
    keywords = ('blazer', 'with', 'notched', 'lapels')

    def build(self) -> None:
        # blazer mirrored about x=24: sloped shoulders, sleeves widening to the cuffs, front edge to the hem
        _path(self, "jacket", (18, 6), [
            (10, 9), (6, 42), (15, 42),            # shoulder, left sleeve and cuff
            (24, 42), (33, 42),                    # hem, split where the front edge lands
            (42, 42), (38, 9),                     # right cuff and sleeve
            (30, 6), (18, 6),                      # shoulder and the back of the collar
        ], closed=True)
        # V opening: lapel edges from the collar corners to the button point, then the front edge
        self.add_polyline("opening", (18, 6), (24, 28), (30, 6))
        self.add_line("front", (24, 28), (24, 42))
        # sleeve seams from the cuffs up toward the armpits
        self.add_line("seam-left", (15, 42), (16, 30))
        self.add_line("seam-right", (33, 42), (32, 30))
        for a, b in (("jacket", "opening"), ("opening", "front"), ("front", "jacket"),
                     ("seam-left", "jacket"), ("seam-right", "jacket")):
            self.relate("connect", a, b)

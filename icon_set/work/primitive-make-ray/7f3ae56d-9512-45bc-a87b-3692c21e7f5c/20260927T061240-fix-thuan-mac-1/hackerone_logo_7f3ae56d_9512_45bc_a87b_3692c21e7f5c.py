from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7f3ae56d-9512-45bc-a87b-3692c21e7f5c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hackerone-logo/20260927T055730Z-thuan-mac-1/reference/hackerone logo_7f3ae56d-9512-45bc-a87b-3692c21e7f5c.svg'
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
    icon_id = 'hackerone-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('hackerone', 'security', 'bug-bounty', 'h1', 'logo', 'brand', 'hacker')

    def build(self) -> None:
        # outlined pill bar (8 wide, r4 ends)
        _path(self, "bar", (6, 10), [((14, 10), 4, 4, True), (14, 38), ((6, 38), 4, 4, True), (6, 10)], closed=True)
        # outlined "1": stem 8 wide with round ends; the flag runs down-left at 45 degrees
        # (edges 12 apart vertically = 8.5 apart) and ends in a round knob (r5 on the chord (6,6))
        _path(self, "one", (34, 10), [
            ((42, 10), 4, 4, True),          # stem top (y=6)
            (42, 38), ((34, 38), 4, 4, True),  # right wall, round foot (y=42)
            (34, 22),                          # left wall up to the flag
            (32, 24),                          # flag lower edge
            ((26, 18), 5, 5, True),            # flag knob
            (34, 10),                          # flag upper edge back to the stem top
        ], closed=True)

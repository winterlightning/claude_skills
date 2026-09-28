from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6b215bd5-479c-47e4-95de-5b4ecd941ea3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__face-exhaling-steam/20260926T162509Z-thuan-mac/reference/face nose steam_6b215bd5-479c-47e4-95de-5b4ecd941ea3.svg'
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
    icon_id = 'face-exhaling-steam'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('face', 'exhaling', 'steam')

    def build(self) -> None:
        # Plan: calm round face breathing steam out, as in the reference, on
        # CIRCLE. The head is an r20 ring left open at the bottom between the
        # 3-4-5 points (8,36) and (40,36). Inside radius 12: closed eyes as short
        # level dashes (15..19 and 29..33 at y=17; curved lids blob into hearts at
        # this size), a hooked profile nose (24,24) sweeping down-left and back to
        # (25,31). Two mirrored S-shaped steam wisps leave the open chin below
        # the nose, 10 apart at the top and swaying outward as they fall.
        _path(self, 'head', (8, 36), [
            ((4, 24), 20, 20, True), ((24, 4), 20, 20, True), ((44, 24), 20, 20, True), ((40, 36), 20, 20, True),
        ])
        self.add_line('eye-left', (15, 17), (19, 17))
        self.add_line('eye-right', (29, 17), (33, 17))
        self.add_bezier('nose', (24, 24), ((21, 28), (20, 31), (25, 31)))
        self.add_bezier('steam-left', (19, 38), ((16, 40), (20, 41), (18, 43)))
        self.add_bezier('steam-right', (29, 38), ((32, 40), (28, 41), (30, 43)))

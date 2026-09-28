from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'aad7affb-c237-432d-9b8a-f94d9548fdb7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__peopleman-moustache-avatar/20260926T180600Z-thuan-mac-1/reference/peopleman moustache_aad7affb-c237-432d-9b8a-f94d9548fdb7.svg'
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
    icon_id = 'peopleman-moustache-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('peopleman', 'moustache', 'portrait', 'bust')

    def build(self) -> None:
        # Man with a full beard and moustache (reference: head only). Crown
        # (rx14 ry13), centre-notched hairline, straight cheeks, and a closed beard:
        # the moustache top edge flicks out to wing points on the keyshape sides and
        # the bottom is three lobes (quarter r10, half r6, quarter r10) to the chin.
        _path(self, 'crown', (10, 17), [((24, 4), 14, 13, True), ((38, 17), 14, 13, True)])
        self.add_bezier('hairline-left', (10, 17), ((16, 17), (22, 16), (24, 12)))
        self.add_bezier('hairline-right', (24, 12), ((26, 16), (32, 17), (38, 17)))
        self.add_contour('hairline', 'hairline-left', 'hairline-right')
        self.relate('connect', 'crown', 'hairline')
        self.add_line('cheek-left', (10, 17), (10, 26))
        self.add_line('cheek-right', (38, 17), (38, 26))
        for c in ('cheek-left', 'cheek-right'):
            self.relate('connect', c, 'crown')
            self.relate('connect', c, 'hairline')
        _path(self, 'beard', (10, 26), [('c', (15, 25), (21, 25), (24, 28)), ('c', (27, 25), (33, 25), (38, 26)),
                                        (40, 28), ((30, 38), 10, 10, True), ((18, 38), 6, 6, True),
                                        ((8, 28), 10, 10, True), (10, 26)], True)
        self.relate('connect', 'beard', 'cheek-left')
        self.relate('connect', 'beard', 'cheek-right')

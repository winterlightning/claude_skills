from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'eb4576b3-c5b1-4d1c-8e23-fbb925182d9a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__flag-1/20260927T032037Z-thuan-mac-1/reference/flag 1_eb4576b3-c5b1-4d1c-8e23-fbb925182d9a.svg'
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
    icon_id = 'flag-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'social'
    categories = ('social', 'primitives')
    aliases = ()
    keywords = ('flag', 'social')

    def build(self) -> None:
        # Plan: waving flag. Straight hoist edge x=4 (10..36) continuing down as
        # a short pole stub to y40; top and bottom edges are the same wave
        # (crest x13, trough x33, horizontal tangents at every knot) offset by
        # 26; straight fly edge x=44.
        _path(self, 'flag', (4, 10), [
            ('c', (8, 8.5), (10, 8), (13, 8)),
            ('c', (20, 8), (26, 12), (33, 12)),
            ('c', (38, 12), (41, 11), (44, 10)),
            (44, 36),
            ('c', (41, 37), (38, 38), (33, 38)),
            ('c', (26, 38), (20, 34), (13, 34)),
            ('c', (10, 34), (8, 34.5), (4, 36)),
            (4, 10)], True)
        self.add_line('pole', (4, 36), (4, 40))
        self.relate('connect', 'pole', 'flag')

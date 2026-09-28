from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '36dab9b9-612f-5996-9e36-283d9015d62a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__equalizer-stereo/20260926T162509Z-thuan-mac/reference/equalizer stereo_36dab9b9-612f-5996-9e36-283d9015d62a.svg'
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
    icon_id = 'equalizer-stereo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'audio'
    categories = ('audio', 'primitives')
    aliases = ()
    keywords = ('equalizer', 'stereo', 'audio')

    def build(self) -> None:
        # Plan: three vertical slider tracks (x 10, 24, 38; y 6..42) as in the
        # reference, each broken by an r4 ring knob at a different height
        # (left middle, centre low, right high). Knob centres are 16+ apart and
        # 10 from the neighbouring tracks.
        for name, x, y in (('left', 10, 24), ('mid', 24, 32), ('right', 38, 16)):
            _circle(self, f'{name}-knob', x, y, 4)
            self.add_line(f'{name}-top', (x, 6), (x, y - 4))
            self.add_line(f'{name}-bottom', (x, y + 4), (x, 42))
            self.relate('connect', f'{name}-knob', f'{name}-top')
            self.relate('connect', f'{name}-knob', f'{name}-bottom')

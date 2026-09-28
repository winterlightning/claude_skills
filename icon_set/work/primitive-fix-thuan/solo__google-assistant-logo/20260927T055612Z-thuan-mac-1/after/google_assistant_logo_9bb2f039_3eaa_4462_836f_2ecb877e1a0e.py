from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9bb2f039-3eaa-4462-836f-2ecb877e1a0e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-assistant-logo/20260927T055612Z-thuan-mac-1/reference/google assistant logo_9bb2f039-3eaa-4462-836f-2ecb877e1a0e.svg'
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
    icon_id = 'google-assistant-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('google-assistant', 'google', 'assistant', 'voice', 'logo', 'brand', 'ai')

    def build(self) -> None:
        # Plan: the four Assistant dots as rings, every pair >= 8 apart on
        # centerlines: big r8 about (14,14) (left/top 6), small r3 about
        # (39,9) (right 42), medium r4 about (32,24), and r4 about (24,38)
        # (bottom 42).
        _circle(self, 'dot-big', 14, 14, 8)
        _circle(self, 'dot-small', 39, 9, 3)
        _circle(self, 'dot-mid', 32, 24, 4)
        _circle(self, 'dot-low', 24, 38, 4)

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e8555acb-9beb-49f8-8fcb-c5960dfa8ebb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__grooveshark-logo/20260927T055730Z-thuan-mac-1/reference/grooveshark logo_e8555acb-9beb-49f8-8fcb-c5960dfa8ebb.svg'
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
    icon_id = 'grooveshark-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('grooveshark', 'music', 'wave', 'logo', 'brand', 'streaming', 'audio')

    def build(self) -> None:
        # ring r20 split at its left and right cardinal points where the wave meets it
        self.add_arc("ring-top", (4, 24), (44, 24), radius_x=20)
        self.add_arc("ring-bottom", (44, 24), (4, 24), radius_x=20)
        self.add_contour("ring", "ring-top", "ring-bottom", closed=True)
        # the wave: rises from the left edge to a peak 8+ below the rim, falls away to the right edge
        _path(self, "wave", (4, 24), [
            ('c', (8, 22), (10, 14), (17, 14)),
            ('c', (25, 14), (30, 27), (36, 27)), ('c', (40, 27), (42, 26), (44, 24)),
        ])
        self.relate("connect", "ring", "wave")

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6a2e9ebc-ac7b-4760-8c0d-cb5e1101e6de'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__frustrated-face-with-angled-brows/20260926T152555Z-thuan-mac-2/reference/face persevering_6a2e9ebc-ac7b-4760-8c0d-cb5e1101e6de.svg'
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
    icon_id = 'frustrated-face-with-angled-brows'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('frustrated', 'face', 'with', 'angled', 'brows')

    def build(self) -> None:
        # Plan: persevering face on CIRCLE, mirrored about x=24. Rim r20. Inside the
        # rim every feature stays within radius ~11.4 of the centre (9 clear of the
        # rim). The reference's slanted brow + flat eye pair reduces to an open
        # chevron (brow arm down to the inner vertex, eye arm back out) - the
        # squeezed-shut eyes; vertices 8 apart. Frown: half-ellipse under them.
        _circle(self, 'rim', 24, 24, 20)
        _path(self, 'eye-left', (15, 17), [(20, 21), (15, 25)])
        _path(self, 'eye-right', (33, 17), [(28, 21), (33, 25)])
        self.add_arc('frown', (19, 34), (29, 34), radius_x=5, radius_y=3, sweep=True)

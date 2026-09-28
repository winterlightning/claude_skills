from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ec6a97bf-8b79-5217-9903-4d323ef660ad'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__man-indian-1-avatar/20260926T175624Z-thuan-mac-1/reference/man indian_ec6a97bf-8b79-5217-9903-4d323ef660ad.svg'
AUTHOR = 'claude-opus-5-5'


def _path(icon, name, start, steps, closed=False, ids=None):
    """steps: (x, y) line | ((x, y), rx, ry, sweep[, large]) arc | ('c', c1, c2, end) cubic."""
    members, point = [], start
    for i, step in enumerate(steps):
        member = (ids or {}).get(i, f"{name}-{i + 1}")
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
    icon_id = 'man-indian-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('man', 'indian', '1', 'portrait', 'bust')

    def build(self) -> None:
        # Man in a turban: r10 dome whose brow is an inverted V, with one wrap
        # fold from the dome's 6-8-10 point down to the V's peak; circular r10
        # jaw touching a bust with rounded square shoulders and a robe wrap
        # crossing from the right shoulder.  The chin beard is omitted: every
        # arch inside the jaw comes within 8 of the brow or the shoulder line.
        # Reference: human_ref/user.svg bust; supplied turban drawing.
        _path(self, 'head', (14, 14), [((24, 4), 10, 10, True), ((30, 6), 10, 10, True), ((34, 14), 10, 10, True),
                                      (34, 19), (34, 22), ((14, 22), 10, 10, True), (14, 19), (14, 14)], True)
        _path(self, 'brow', (14, 19), [(24, 14), (34, 19)])
        self.add_line('fold', (30, 6), (24, 14))
        for part in ('brow', 'fold'):
            self.relate('connect', 'head', part)
        self.relate('connect', 'fold', 'brow')
        _path(self, 'body', (8, 44), [(8, 40), ((12, 36), 4, 4, True), (24, 36), (36, 36), ((40, 40), 4, 4, True), (40, 44)],
              ids={2: 'body-top', 3: 'body-top-right'})
        self.relate('connect', 'head', 'body')
        self.add_line('robe', (36, 36), (24, 44))
        self.relate('connect', 'robe', 'body')

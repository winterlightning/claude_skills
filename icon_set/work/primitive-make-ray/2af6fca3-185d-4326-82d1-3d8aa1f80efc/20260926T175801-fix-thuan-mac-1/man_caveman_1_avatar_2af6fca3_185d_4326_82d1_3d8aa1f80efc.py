from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2af6fca3-185d-4326-82d1-3d8aa1f80efc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__man-caveman-1-avatar/20260926T175624Z-thuan-mac-1/reference/man caveman_2af6fca3-185d-4326-82d1-3d8aa1f80efc.svg'
AUTHOR = "claude-opus-5-5"


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
    icon_id = 'man-caveman-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('man', 'caveman', '1', 'portrait', 'bust')

    def build(self) -> None:
        # Caveman: a V topknot on a broad r10 dome head, a full beard
        # (moustache line over a circular r10 jaw) touching a broad bust
        # crossed by a one-shoulder hide strap.
        # Reference: human_ref/user.svg bust; supplied caveman drawing.
        _path(self, 'head', (24, 8), [((34, 18), 10, 10, True), (34, 22), ((14, 22), 10, 10, True),
                                     (14, 18), ((24, 8), 10, 10, True)], True)
        _path(self, 'knot', (20, 4), [(24, 8), (28, 4)])
        _path(self, 'beard', (14, 22), [('c', (19, 22), (21, 18), (24, 18)), ('c', (27, 18), (29, 22), (34, 22))])
        self.relate('connect', 'head', 'knot')
        self.relate('connect', 'head', 'beard')
        _path(self, 'body', (8, 44), [(8, 40), ((12, 36), 4, 4, True), (24, 36), (36, 36), ((40, 40), 4, 4, True), (40, 44)],
              ids={2: 'body-top', 3: 'body-top-right'})
        self.relate('connect', 'head', 'body')
        self.add_line('strap', (36, 36), (24, 44))
        self.relate('connect', 'strap', 'body')

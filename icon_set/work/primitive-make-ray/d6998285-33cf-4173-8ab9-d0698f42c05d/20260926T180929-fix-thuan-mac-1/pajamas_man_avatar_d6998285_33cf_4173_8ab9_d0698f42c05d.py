from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd6998285-33cf-4173-8ab9-d0698f42c05d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pajamas-man-avatar/20260926T180600Z-thuan-mac-1/reference/pajamas man_d6998285-33cf-4173-8ab9-d0698f42c05d.svg'
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
    icon_id = 'pajamas-man-avatar'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('pajamas', 'man', 'portrait', 'bust')

    def build(self) -> None:
        # Head in a drooping nightcap (reference: no body). Face = brim line and a
        # circular r10 jaw; the cap domes over the head and droops right to an r4
        # pompom ring beside the cheek.
        self.add_line('brim', (6, 24), (26, 24))
        _path(self, 'face', (6, 24), [(6, 32), ((16, 42), 10, 10, False), ((26, 32), 10, 10, False), (26, 24)])
        self.relate('connect', 'brim', 'face')
        self.add_arc('cap-dome', (6, 24), (16, 6), radius_x=10, radius_y=18, sweep=True)
        self.add_bezier('cap-top', (16, 6), ((30, 6), (38, 18), (38, 30)))
        self.add_line('cap-inner', (26, 24), (38, 30))
        self.add_contour('cap', 'cap-dome', 'cap-top')
        self.relate('connect', 'cap', 'brim')
        self.relate('connect', 'cap', 'face')
        self.relate('connect', 'cap-inner', 'brim')
        self.relate('connect', 'cap-inner', 'face')
        _circle(self, 'pompom', 38, 34, 4)
        self.relate('connect', 'pompom', 'cap')
        self.relate('connect', 'pompom', 'cap-inner')

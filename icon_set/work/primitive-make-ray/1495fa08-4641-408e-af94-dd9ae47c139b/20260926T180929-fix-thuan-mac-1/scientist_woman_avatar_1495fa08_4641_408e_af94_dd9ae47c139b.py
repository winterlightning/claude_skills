from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1495fa08-4641-408e-af94-dd9ae47c139b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__scientist-woman-avatar/20260926T180600Z-thuan-mac-1/reference/scientist woman_1495fa08-4641-408e-af94-dd9ae47c139b.svg'
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
    icon_id = 'scientist-woman-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('scientist', 'woman', 'portrait', 'bust')

    def build(self) -> None:
        # Scientist woman (reference): fedora (crown with rounded top on a
        # full-width brim), hair falling straight from under the brim, r8 face,
        # flat-topped shoulders with lapels opening down to the hem.
        self.add_line('brim-left', (8, 14), (16, 14))
        self.add_line('brim', (16, 14), (32, 14))
        self.add_line('brim-right', (32, 14), (40, 14))
        _path(self, 'crown', (16, 14), [(17, 8), ((24, 4), 7, 4, True), ((31, 8), 7, 4, True), (32, 14)])
        self.add_line('hair-left', (8, 14), (8, 22))
        self.add_line('hair-right', (40, 14), (40, 22))
        for a, b in [('brim-left', 'brim'), ('brim', 'brim-right'), ('crown', 'brim'), ('crown', 'brim-left'),
                     ('crown', 'brim-right'), ('hair-left', 'brim-left'), ('hair-right', 'brim-right')]:
            self.relate('connect', a, b)
        _path(self, 'face', (16, 14), [(16, 18), ((24, 26), 8, 8, False), ((32, 18), 8, 8, False), (32, 14)])
        for part in ('brim-left', 'brim', 'brim-right', 'crown'):
            self.relate('connect', 'face', part)
        _path(self, 'body-left', (8, 44), [(8, 38), ((16, 30), 8, 8, True)])
        self.add_line('body-top', (16, 30), (24, 30))
        self.add_line('body-top-right', (24, 30), (32, 30))
        _path(self, 'body-right', (32, 30), [((40, 38), 8, 8, True), (40, 44)])
        for a, b in [('body-left', 'body-top'), ('body-top', 'body-top-right'), ('body-top-right', 'body-right'),
                     ('face', 'body-top'), ('face', 'body-top-right')]:
            self.relate('connect', a, b)
        self.add_line('lapel-left', (16, 30), (21, 44))
        self.add_line('lapel-right', (32, 30), (27, 44))
        for lap, part in [('lapel-left', 'body-left'), ('lapel-left', 'body-top'), ('lapel-right', 'body-top-right'), ('lapel-right', 'body-right')]:
            self.relate('connect', lap, part)

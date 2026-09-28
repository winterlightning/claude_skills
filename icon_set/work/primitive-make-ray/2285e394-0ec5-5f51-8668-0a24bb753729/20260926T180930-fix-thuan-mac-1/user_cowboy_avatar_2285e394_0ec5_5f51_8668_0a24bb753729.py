from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2285e394-0ec5-5f51-8668-0a24bb753729'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__user-cowboy-avatar/20260926T180600Z-thuan-mac-1/reference/user-cowboy-avatar_2285e394-0ec5-5f51-8668-0a24bb753729.svg'
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
    icon_id = 'user-cowboy-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('avatars',)
    aliases = ()
    keywords = ('user', 'cowboy', 'portrait', 'bust')

    def build(self) -> None:
        # Cowboy: pinched crown on an upturned brim, r8 face hung from the brim
        # at the crown feet, broad shoulders touching the chin.
        self.add_bezier('brim-left', (8, 10), ((10, 14), (13, 16), (16, 16)))
        self.add_line('brim', (16, 16), (24, 16))
        self.add_line('brim-r', (24, 16), (32, 16))
        self.add_bezier('brim-right', (32, 16), ((35, 16), (38, 14), (40, 10)))
        self.add_contour('hat-brim', 'brim-left', 'brim', 'brim-r', 'brim-right')
        _path(self, 'crown', (16, 16), [(18, 4), (24, 8), (30, 4), (32, 16)])
        self.relate('connect', 'crown', 'hat-brim')
        _path(self, 'face', (16, 16), [(16, 20), ((24, 28), 8, 8, False), ((32, 20), 8, 8, False), (32, 16)])
        self.relate('connect', 'face', 'hat-brim')
        self.relate('connect', 'face', 'crown')
        _path(self, 'shoulders', (8, 44), [((24, 32), 16, 12, True), ((40, 44), 16, 12, True)])
        self.relate('connect', 'face', 'shoulders')

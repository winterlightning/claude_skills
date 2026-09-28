from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '44ee4e62-4052-5cd9-b8ce-7733bb2ccec0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__combine-harvester-front-header/20260927T091421Z-thuan-mac-1/reference/harvester storage_44ee4e62-4052-5cd9-b8ce-7733bb2ccec0.svg'
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
    icon_id = 'combine-harvester-front-header'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'farming'
    categories = ('farming', 'primitives')
    aliases = ()
    keywords = ('agricultural', 'combine', 'harvester')

    def build(self) -> None:
        # Combine harvester, side view facing left. One outline: a grain tank that is wider at the top
        # ((4,8)-(22,8) tapering to (8,28)/(19,20)), a low body, and a cab block at the rear
        # (x 30..44, y 16..32). The floor rests on the tops of a big r6 front wheel (22,34) and a small
        # r4 rear wheel (40,36). The unloading auger runs from the tank top over the cab, 8 above it;
        # the header hangs from the front corner as a low scoop.
        _path(self, "body", (8, 28), [(4, 8), (22, 8), (19, 20), (30, 20), (30, 16), (44, 16), (44, 32), (40, 32),
                                      (36, 32), (36, 28), (22, 28), (8, 28)], True)
        _circle(self, "wheel-front", 22, 34, 6)
        _circle(self, "wheel-rear", 40, 36, 4)
        self.add_line("auger", (22, 8), (40, 8))
        _path(self, "header", (8, 28), [(4, 40), (9, 40)])
        for part in ("wheel-front", "wheel-rear", "auger", "header"):
            self.relate("connect", "body", part)

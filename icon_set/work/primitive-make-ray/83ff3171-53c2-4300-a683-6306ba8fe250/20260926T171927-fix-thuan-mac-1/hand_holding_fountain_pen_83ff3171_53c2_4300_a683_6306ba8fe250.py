from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '83ff3171-53c2-4300-a683-6306ba8fe250'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-fountain-pen/20260926T171659Z-thuan-mac-1/reference/workflow coaching hand pen_83ff3171-53c2-4300-a683-6306ba8fe250.svg'
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
    icon_id = 'hand-holding-fountain-pen'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'work'
    categories = ('work', 'primitives')
    aliases = ()
    keywords = ('hand', 'pen', 'fountain', 'writing', 'grip', 'nib')

    def build(self) -> None:
        # Fist holding a fountain pen on SQUARE: three curled fingers (8 wide,
        # r4 knuckles on top at y=6, walls ending 8 above the finger-tip line)
        # grip a pen tube 8 wide (y=18..26) whose pointed nib reaches x=6; the
        # pen's lower edge continues through the fist as the curled finger line.  Below
        # the pen the palm rounds (r4) into a wrist to the bottom edge.
        # Every piece is its own contour, split at each junction, and pieces
        # that share an endpoint are declared connected.
        ends = {}

        def line(name, a, b):
            self.add_line(name, a, b); self.add_contour(name + '-c', name); ends[name + '-c'] = (a, b)

        pen_top = [10, 18]
        for i, (a, b) in enumerate(zip(pen_top, pen_top[1:])):
            line(f'pen-top-{i}', (a, 18), (b, 18))
        for i, (a, b) in enumerate(zip([10, 18], [18, 42])):
            line(f'pen-bottom-{i}', (a, 26), (b, 26))
        line('nib-top', (6, 22), (10, 18))
        line('nib-bottom', (6, 22), (10, 26))
        for i, cx in enumerate((22, 30, 38)):
            self.add_arc(f'knuckle-{i}', (cx - 4, 10), (cx + 4, 10), radius_x=4, sweep=True)
            self.add_contour(f'knuckle-{i}-c', f'knuckle-{i}'); ends[f'knuckle-{i}-c'] = ((cx - 4, 10), (cx + 4, 10))
        line('wall-0-top', (18, 18), (18, 10))
        line('wall-0-low', (18, 26), (18, 18))
        line('wall-1', (26, 18), (26, 10))
        line('wall-2', (34, 18), (34, 10))
        line('wall-3-top', (42, 10), (42, 18))
        line('wall-3-low', (42, 18), (42, 26))
        _path(self, 'palm-left', (18, 26), [(18, 30), ((22, 34), 4, 4, False), (22, 42)])
        _path(self, 'palm-right', (42, 26), [(42, 30), ((38, 34), 4, 4, True), (38, 42)])
        ends['palm-left'] = ((18, 26), (22, 42))
        ends['palm-right'] = ((42, 26), (38, 42))
        names = sorted(ends)
        for i, a in enumerate(names):
            for b in names[i + 1:]:
                if set(ends[a]) & set(ends[b]):
                    self.relate('connect', a, b)

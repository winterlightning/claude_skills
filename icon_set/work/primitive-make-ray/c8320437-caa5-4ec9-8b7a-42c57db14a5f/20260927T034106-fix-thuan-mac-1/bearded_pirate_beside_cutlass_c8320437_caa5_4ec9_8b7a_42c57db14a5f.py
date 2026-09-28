from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c8320437-caa5-4ec9-8b7a-42c57db14a5f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bearded-pirate-beside-cutlass/20260927T032145Z-thuan-mac-1/reference/pirate_c8320437-caa5-4ec9-8b7a-42c57db14a5f.svg'
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
    icon_id = 'bearded-pirate-beside-cutlass'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('cutlass', 'pirate', 'eyepatch', 'hat', 'person', 'portrait', 'seafarer', 'costume', 'adventure')

    def build(self) -> None:
        # human ref: icon_set/references/human_ref/user.svg. Bust on the axis x=16: hat, bearded face, and
        # shoulders that meet the beard's lower edges so the beard point hangs over the chest.
        ax, by = 16, 16
        # hat: half-disc crown (r8) closed by the brim line, brim tips turned up like a tricorn
        self.add_arc("crown", (ax - 8, by), (ax + 8, by), radius_x=8)
        self.add_line("brim", (ax + 8, by), (ax - 8, by))
        self.add_contour("hat", "crown", "brim", closed=True)
        self.add_line("tip-left", (ax - 8, by), (6, by - 3))
        self.add_line("tip-right", (ax + 8, by), (26, by - 3))
        self.relate("connect", "hat", "tip-left"); self.relate("connect", "hat", "tip-right")
        # bearded face hanging from the brim line; lower edges split where the shoulders land
        _path(self, "beard", (ax - 6, by), [(ax - 6, by + 10), (ax - 3, by + 14), (ax, by + 18),
                                            (ax + 3, by + 14), (ax + 6, by + 10), (ax + 6, by)])
        self.relate("connect", "beard", "hat")
        self.add_arc("shoulder-left", (6, 42), (ax - 3, by + 14), radius_x=7, radius_y=42 - by - 14)
        self.add_arc("shoulder-right", (ax + 3, by + 14), (26, 42), radius_x=7, radius_y=42 - by - 14)
        self.relate("connect", "beard", "shoulder-left"); self.relate("connect", "beard", "shoulder-right")
        # cutlass: broad blade (straight back, curved edge) whose base is the guard, grip below
        _path(self, "blade", (34, 30), [(34, 6), ('c', (40, 8), (42, 14), (42, 22)), (42, 30), (34, 30)], closed=True)
        self.add_line("grip", (38, 30), (38, 42))
        self.relate("connect", "blade", "grip")

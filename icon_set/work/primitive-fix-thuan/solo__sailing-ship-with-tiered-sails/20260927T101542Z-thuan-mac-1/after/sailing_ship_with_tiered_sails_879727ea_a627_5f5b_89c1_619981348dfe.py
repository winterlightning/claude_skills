from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '879727ea-a627-5f5b-89c1-619981348dfe'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__sailing-ship-with-tiered-sails/20260927T101542Z-thuan-mac-1/reference/piracy ship_879727ea-a627-5f5b-89c1-619981348dfe.svg'
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
    icon_id = 'sailing-ship-with-tiered-sails'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'crime'
    categories = ('crime', 'primitives')
    aliases = ()
    keywords = ('sailing', 'ship', 'with', 'tiered', 'sails')

    def build(self) -> None:
        # Reference layout: one mast through two bowl sails hanging from overhanging yards,
        # over a hull with a raised pointed bow (left) and a raised stern (right).
        _path(self, "mast", (22, 4), [(22, 11), (22, 20), (22, 27), (22, 36)])
        _path(self, "topsail", (12, 4), [(13, 4), (22, 4), (31, 4), (32, 4), (31, 4),
                                        ((22, 11), 9, 7, True), ((13, 4), 9, 7, True)])
        _path(self, "course", (8, 20), [(9, 20), (22, 20), (35, 20), (36, 20), (35, 20),
                                       ((22, 27), 13, 7, True), ((9, 20), 13, 7, True)])
        _path(self, "hull", (8, 32), [(15, 36), (22, 36), (32, 36), (40, 32), (40, 39),
                                      ('c', (40, 42), (38, 44), (35, 44)), (16, 44),
                                      ('c', (12, 44), (8, 39), (8, 32))], True)
        for a, b in (("mast", "topsail"), ("mast", "course"), ("mast", "hull")):
            self.relate("connect", a, b)

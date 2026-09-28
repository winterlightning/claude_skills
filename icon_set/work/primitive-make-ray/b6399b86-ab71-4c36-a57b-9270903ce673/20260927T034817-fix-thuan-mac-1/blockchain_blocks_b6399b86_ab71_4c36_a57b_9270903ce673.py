from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b6399b86-ab71-4c36-a57b-9270903ce673'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__blockchain-blocks/20260927T032145Z-thuan-mac-1/reference/amazon managed blockchain_b6399b86-ab71-4c36-a57b-9270903ce673.svg'
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
    icon_id = 'blockchain-blocks'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'programing'
    categories = ('programing', 'primitives')
    aliases = ()
    keywords = ('blockchain', 'blocks', 'chain', 'ledger', 'link', 'sequence', 'crypto', 'arrow')

    def build(self) -> None:
        # horizontal chain on the centre line: block, link, block, then an arrow to the next block
        self.add_polyline("block-1", (6, 19), (16, 19), (16, 24), (16, 29), (6, 29), closed=True)
        self.add_polyline("block-2", (24, 19), (34, 19), (34, 24), (34, 29), (24, 29), (24, 24), closed=True)
        self.add_line("link", (16, 24), (24, 24))
        self.add_line("shaft", (34, 24), (44, 24))       # tip at radius 20: sets the CIRCLE fit
        self.add_polyline("head", (40, 20), (44, 24), (40, 28))
        for a, b in (("block-1", "link"), ("link", "block-2"), ("block-2", "shaft"), ("shaft", "head")):
            self.relate("connect", a, b)

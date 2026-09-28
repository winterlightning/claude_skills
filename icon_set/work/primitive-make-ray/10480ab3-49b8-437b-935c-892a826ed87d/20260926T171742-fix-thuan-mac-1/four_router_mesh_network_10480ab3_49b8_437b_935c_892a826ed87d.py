from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '10480ab3-49b8-437b-935c-892a826ed87d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__four-router-mesh-network/20260926T171651Z-thuan-mac-1/reference/mesh wifi 2_10480ab3-49b8-437b-935c-892a826ed87d.svg'
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
    icon_id = 'four-router-mesh-network'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('mesh', 'wifi', 'routers', 'network', 'wireless', 'nodes', 'connection')

    def build(self) -> None:
        # Plan: the reference's 2x2 mesh of routers with broken (wireless)
        # links, on HRECT_L (x 4..44, y 8..40) so a link fits between the
        # routers of each row. Each router is a 12x8 box (four standalone
        # connected edges, so the 8-unit gaps certify) with two antennas
        # rising 4 from its top edge, 8 apart; one repeated definition,
        # translated to the four corners. Links at 8-unit clearance: a dot
        # between the routers of each row. A centre dot for the cross link read as
        # a colon, so it is left out.
        def router(tag, x, y):
            # x, y = top-left of the box; antennas at x+2 and x+10
            self.add_line(f'{tag}-top-a', (x, y), (x + 2, y))
            self.add_line(f'{tag}-top-b', (x + 2, y), (x + 10, y))
            self.add_line(f'{tag}-top-c', (x + 10, y), (x + 12, y))
            self.add_line(f'{tag}-right', (x + 12, y), (x + 12, y + 8))
            self.add_line(f'{tag}-bottom', (x + 12, y + 8), (x, y + 8))
            self.add_line(f'{tag}-left', (x, y + 8), (x, y))
            self.add_line(f'{tag}-ant-l', (x + 2, y - 4), (x + 2, y))
            self.add_line(f'{tag}-ant-r', (x + 10, y - 4), (x + 10, y))
            for a, b in (('top-a', 'top-b'), ('top-b', 'top-c'), ('top-c', 'right'), ('right', 'bottom'), ('bottom', 'left'),
                         ('left', 'top-a'), ('ant-l', 'top-a'), ('ant-l', 'top-b'), ('ant-r', 'top-b'), ('ant-r', 'top-c')):
                self.relate('connect', f'{tag}-{a}', f'{tag}-{b}')

        router('tl', 4, 12)
        router('tr', 32, 12)
        router('bl', 4, 32)
        router('br', 32, 32)
        self.add_dot('link-top', (24, 16))
        self.add_dot('link-bottom', (24, 36))

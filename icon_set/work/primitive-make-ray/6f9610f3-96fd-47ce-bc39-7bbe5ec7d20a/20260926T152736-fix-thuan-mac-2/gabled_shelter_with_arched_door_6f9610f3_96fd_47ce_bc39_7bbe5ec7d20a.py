from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6f9610f3-96fd-47ce-bc39-7bbe5ec7d20a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__gabled-shelter-with-arched-door/20260926T152555Z-thuan-mac-2/reference/shelter_6f9610f3-96fd-47ce-bc39-7bbe5ec7d20a.svg'
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
    icon_id = 'gabled-shelter-with-arched-door'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('gabled', 'shelter', 'with', 'arched', 'door')

    def build(self) -> None:
        # Plan: gabled shelter on SQUARE, mirrored about x=24. 45-degree roof from the
        # apex (24,6) to the eaves (6,24)/(42,24); walls x=10/38 hang from the roof
        # at (10,20)/(38,20) to the floor y=42. The arched door (r5 arch, 19..29)
        # stands on the floor, 9 clear of both walls and 11 below the roof.
        _path(self, 'house', (10, 20), [
            (24, 6), (38, 20), (38, 42), (29, 42), (29, 27),
            ((19, 27), 5, 5, False),
            (19, 42), (10, 42), (10, 20),
        ], closed=True)
        self.add_line('eave-left', (10, 20), (6, 24))
        self.add_line('eave-right', (38, 20), (42, 24))
        self.relate('connect', 'house', 'eave-left')
        self.relate('connect', 'house', 'eave-right')

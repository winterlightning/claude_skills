from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3b2a855e-6ab2-51bc-8612-b388126ed3ff'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__global-network-nodes-batch-018-12/20260926T160438Z-thuan-mac-2/reference/cross region data delivery_3b2a855e-6ab2-51bc-8612-b388126ed3ff.svg'
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
    icon_id = 'global-network-nodes-batch-018-12'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'networks'
    categories = ('primitives', 'networks')
    aliases = ()
    keywords = ('network', 'globe', 'nodes', 'links', 'data', 'connections', 'graph', 'global')

    def build(self) -> None:
        # Plan: global network on CIRCLE. Rim r20. Three node rings (r3) in a
        # triangle about the centre (left A, upper-right B, lower-right C), ~9 from
        # the centre so they stay 8+ inside the rim and 9+ from each other. Links
        # run between the nodes from their cardinal points; two spokes run from A
        # and B out to the rim, as in the reference.
        _path(self, 'rim', (24, 4), [
            ((40, 12), 20, 20, True), ((44, 24), 20, 20, True), ((24, 44), 20, 20, True),
            ((4, 24), 20, 20, True), ((24, 4), 20, 20, True),
        ], closed=True)  # split at (40,12), where spoke-b meets it
        _circle(self, 'node-a', 15, 24, 3)
        _circle(self, 'node-b', 28, 16, 3)
        _circle(self, 'node-c', 28, 32, 3)
        self.add_line('link-ab', (18, 24), (25, 16))
        self.add_line('link-ac', (18, 24), (25, 32))
        self.add_line('link-bc', (28, 19), (28, 29))
        self.add_line('spoke-a', (12, 24), (4, 24))
        self.add_line('spoke-b', (31, 16), (40, 12))
        for l, a, b in (('link-ab', 'node-a', 'node-b'), ('link-ac', 'node-a', 'node-c'), ('link-bc', 'node-b', 'node-c')):
            self.relate('connect', a, l)
            self.relate('connect', b, l)
        self.relate('connect', 'link-ab', 'link-ac')
        self.relate('connect', 'node-a', 'spoke-a')
        self.relate('connect', 'rim', 'spoke-a')
        self.relate('connect', 'node-b', 'spoke-b')
        self.relate('connect', 'rim', 'spoke-b')

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1259b062-7e36-4616-83b9-d5d1aa90e70f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__delivery-worker-beside-loaded-hand-truck/20260927T091421Z-thuan-mac-1/reference/warehouse cart worker_1259b062-7e36-4616-83b9-d5d1aa90e70f.svg'
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
    icon_id = 'delivery-worker-beside-loaded-hand-truck'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'delivery'
    human_construction = "bust"
    categories = ('delivery', 'primitives')
    aliases = ()
    keywords = ('worker', 'cart', 'handtruck', 'parcel', 'delivery', 'courier', 'person', 'warehouse')

    def build(self) -> None:
        # Warehouse worker beside a loaded hand truck, as in the reference. Left: the hand truck - an
        # upright frame with a grip angled back at the top, a parcel standing on the toe plate against
        # the frame, and an r3 wheel under the frame foot. Right: the worker as a bust - r6 head with a
        # cap visor pointing toward the truck, resting on an r8 shoulder dome (bust contact: jaw bottom
        # 4 above the dome top, same centre x) over a tapered body.
        _path(self, "parcel", (14, 22), [(4, 22), (4, 34), (14, 34), (14, 22)], True)
        _path(self, "frame", (14, 22), [(14, 12), (18, 8)])
        _circle(self, "wheel", 14, 37, 3)
        self.relate("connect", "parcel", "frame")
        self.relate("connect", "parcel", "wheel")
        _circle(self, "head", 36, 14, 6)
        self.add_line("visor", (30, 14), (25, 14))
        self.relate("connect", "head", "visor")
        _path(self, "body", (28, 32), [((36, 24), 8, 8, True), ((44, 32), 8, 8, True), (42, 40), (30, 40), (28, 32)], True)
        self.relate("connect", "head", "body")

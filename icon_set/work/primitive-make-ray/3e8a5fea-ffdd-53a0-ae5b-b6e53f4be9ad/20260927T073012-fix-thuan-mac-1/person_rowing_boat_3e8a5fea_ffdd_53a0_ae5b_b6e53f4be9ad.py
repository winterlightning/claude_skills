from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3e8a5fea-ffdd-53a0-ae5b-b6e53f4be9ad'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-rowing-boat/20260927T072841Z-thuan-mac-1/reference/canoe person_3e8a5fea-ffdd-53a0-ae5b-b6e53f4be9ad.svg'
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
    icon_id = 'person-rowing-boat'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('rowing', 'boat', 'canoe', 'person', 'paddle', 'water', 'sport', 'outdoors', 'outdoors-batch-01')

    def build(self) -> None:
        # rowing boat: gunwale and a hull 8 deep with raked bow and stern
        xs = (4, 8, 22, 38, 40, 44)
        for n, (a, b) in enumerate(zip(xs, xs[1:])):
            self.add_line(f"gunwale-{n}", (a, 32), (b, 32))
        for n in range(4):
            self.relate("connect", f"gunwale-{n}", f"gunwale-{n + 1}")
        self.add_polyline("hull", (8, 32), (12, 40), (36, 40), (40, 32))
        for n in (0, 1, 3, 4):
            self.relate("connect", "hull", f"gunwale-{n}")
        # rower (human ref full_body_ref.png): r3 head 8 above the torso seated at the gunwale, arms reaching
        # forward to the oar handle; the oar's loom runs down to the oarlock on the gunwale
        _circle(self, "head", 22, 11, 3)
        self.add_line("torso", (22, 22), (22, 32))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        self.add_line("arms", (22, 23), (34, 20))
        self.add_line("oar", (34, 20), (38, 32))
        for a, b in (("torso", "gunwale-1"), ("torso", "gunwale-2"), ("torso", "arms"), ("arms", "oar"),
                     ("oar", "gunwale-2"), ("oar", "gunwale-3")):
            self.relate("connect", a, b)

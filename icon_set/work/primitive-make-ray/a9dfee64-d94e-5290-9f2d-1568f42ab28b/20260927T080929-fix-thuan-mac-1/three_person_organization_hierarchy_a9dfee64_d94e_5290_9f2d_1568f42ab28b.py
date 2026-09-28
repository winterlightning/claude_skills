from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a9dfee64-d94e-5290-9f2d-1568f42ab28b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-person-organization-hierarchy/20260927T080754Z-thuan-mac-1/reference/workflow teamwork hierarchy_a9dfee64-d94e-5290-9f2d-1568f42ab28b.svg'
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
    icon_id = 'three-person-organization-hierarchy'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'companies'
    categories = ('primitives', 'companies')
    aliases = ()
    keywords = ('three-person', 'organization', 'hierarchy')

    def build(self) -> None:
        def bust(name, cx, top, hw=6):
            """User silhouette as one keyhole outline: r5 head arc into rounded shoulders on a flat base (17 tall).
            Members: 1 shoulder-r, 2 side-r, 3 base-r, 4 base-l, 5 side-l, 6 shoulder-l, 7 head-l, 8 head-r."""
            cy = top + 5
            base = top + 17
            return _path(self, name, (cx + 3, cy + 4), [
                ('c', (cx + hw - 1, cy + 5), (cx + hw, cy + 7), (cx + hw, cy + 10)),
                (cx + hw, base), (cx, base), (cx - hw, base), (cx - hw, cy + 10),
                ('c', (cx - hw, cy + 7), (cx - hw + 1, cy + 5), (cx - 3, cy + 4)),
                ((cx, top), 5, 5, True), ((cx + 3, cy + 4), 5, 5, True)], True)
        # org chart: lead user silhouette on top, V connector from its base to two team user silhouettes
        bust("lead", 24, 4)
        bust("team-l", 13, 27, 5)
        bust("team-r", 35, 27, 5)
        self.add_line("link-l", (24, 21), (13, 27))
        self.add_line("link-r", (24, 21), (35, 27))
        for a in ("lead-3", "lead-4"):
            self.relate("connect", "link-l", a); self.relate("connect", "link-r", a)
        self.relate("connect", "link-l", "link-r")
        for s in ("l", "r"):
            self.relate("connect", f"link-{s}", f"team-{s}-7"); self.relate("connect", f"link-{s}", f"team-{s}-8")

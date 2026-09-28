from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '81218b42-9d67-4c6c-851c-ea4c4841fcdd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hologram-video-house-projector/20260927T032039Z-thuan-mac-1/reference/virtual house_81218b42-9d67-4c6c-851c-ea4c4841fcdd.svg'
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
    icon_id = 'hologram-video-house-projector'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('hologram', 'projector', 'house', 'video', 'play', 'virtual-home', 'projection')

    def build(self) -> None:
        # House: 1:2 roof (x+2y=32 / -x+2y=-16) with eaves out to the
        # keyshape sides, walls x=12/36, floor y=29.
        _path(self, 'roof', (8, 12), [(12, 10), (24, 4), (36, 10), (40, 12)])
        _path(self, 'walls', (12, 10), [(12, 29), (24, 29), (36, 29), (36, 10)])
        self.relate('connect', 'roof-1', 'walls-1')
        self.relate('connect', 'roof-2', 'walls-1')
        self.relate('connect', 'roof-3', 'walls-4')
        self.relate('connect', 'roof-4', 'walls-4')
        # Play mark: a folded stroke run (top edge, bottom edge, return stub)
        # that the 4-unit stroke paints as a solid triangle without leaving
        # an enclosed sliver.
        _path(self, 'play', (21, 17), [(21, 16), (25, 18), (21, 20)])
        # Projector: lens ring resting on the base line; the light cone runs
        # from the lens top up to the house floor corners.
        _circle(self, 'lens', 24, 41, 3)
        _path(self, 'base', (14, 44), [(24, 44), (34, 44)])
        self.relate('connect', 'lens', 'base')
        _path(self, 'beam-left', (12, 29), [(24, 38)])
        _path(self, 'beam-right', (36, 29), [(24, 38)])
        for a, b in [('beam-left', 'walls'), ('beam-right', 'walls'), ('beam-left', 'lens'),
                     ('beam-right', 'lens'), ('beam-left', 'beam-right')]:
            self.relate('connect', a, b)

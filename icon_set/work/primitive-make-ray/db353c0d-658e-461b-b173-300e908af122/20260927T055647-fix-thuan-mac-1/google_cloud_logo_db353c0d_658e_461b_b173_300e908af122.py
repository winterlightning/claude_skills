from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'db353c0d-658e-461b-b173-300e908af122'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-cloud-logo/20260927T055612Z-thuan-mac-1/reference/google cloud logo_db353c0d-658e-461b-b173-300e908af122.svg'
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
    icon_id = 'google-cloud-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('google-cloud', 'google', 'cloud', 'logo', 'brand', 'hosting', 'platform')

    def build(self) -> None:
        # Plan: Google Cloud mark. Cloud outline = crest cubics over (26,8),
        # a right lobe to (44,29), a flat floor y40 and an r10 left lobe
        # (left 4). Inside: the inner arc leaves the lobe junction (14,20) and
        # curls over to (30,24); an inner base line y32 (x16..32) sits 8 above
        # the floor, as the reference's nested cloud cut.
        self.add_bezier('crest', (14, 20), ((14, 12), (20, 8), (26, 8)), ((34, 8), (38, 14), (38, 20)))
        self.add_bezier('right', (38, 20), ((42, 21), (44, 24), (44, 29)), ((44, 35), (39, 40), (33, 40)))
        self.add_line('floor', (33, 40), (14, 40))
        self.add_arc('left', (14, 40), (14, 20), radius_x=10)
        self.add_contour('outline', 'crest', 'right')
        self.add_contour('lobe', 'left')
        self.relate('connect', 'floor', 'outline')
        self.relate('connect', 'floor', 'lobe')
        self.relate('connect', 'lobe', 'outline')
        self.add_bezier('inner-arc', (14, 20), ((21, 17), (29, 17), (30, 24)))
        self.add_contour('inner', 'inner-arc')
        self.relate('connect', 'lobe', 'inner')
        self.relate('connect', 'outline', 'inner')
        self.add_line('base', (16, 32), (32, 32))

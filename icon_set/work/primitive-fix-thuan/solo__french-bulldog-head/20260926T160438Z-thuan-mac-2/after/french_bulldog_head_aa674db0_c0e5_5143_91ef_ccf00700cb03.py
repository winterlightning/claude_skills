from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'aa674db0-c0e5-5143-91ef-ccf00700cb03'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__french-bulldog-head/20260926T160438Z-thuan-mac-2/reference/french bulldog_aa674db0-c0e5-5143-91ef-ccf00700cb03.svg'
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
    icon_id = 'french-bulldog-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'pets'
    categories = ('pets', 'primitives')
    aliases = ()
    keywords = ('dog', 'french-bulldog', 'frenchie', 'head', 'breed', 'bat-ears', 'pet')

    def build(self) -> None:
        # Plan: French bulldog head, one closed outline mirrored about x=24 on SQUARE.
        # Left half from the flat head top: the big bat ear rises to its tip (9,6),
        # its outer edge bulges down to the left edge and tucks in at the ear base,
        # the cheek bulges out, and the jowl lobe rounds to the bottom edge and
        # back up to the centre cusp M (24,38). A short nose line rises from M.
        def mx(p):
            return (48 - p[0], p[1])
        left = [  # from the head top (18,19) round the left side to M
            ('c', (15, 14), (12, 9), (9, 6)),
            ('c', (7, 7), (6, 10), (6, 14)),
            ('c', (6, 18), (6.5, 20), (8, 22)),
            ('c', (9, 24), (11, 25), (14, 26)),
            ('c', (11, 29), (11, 37), (15, 40)),
            ('c', (16.5, 41.5), (18, 42), (20, 42)),
            ('c', (22, 42), (24, 40), (24, 38)),
        ]
        steps = list(left)
        # right half back from M up to the head top (30,19), reversed and mirrored
        pts = [(18, 19)] + [s[-1] if s[0] == 'c' else s for s in left]
        for i in range(len(left) - 1, -1, -1):
            s, start = left[i], pts[i]
            if s[0] == 'c':
                steps.append(('c', mx(s[2]), mx(s[1]), mx(start)))
            else:
                steps.append(mx(start))
        steps.append((18, 19))
        _path(self, 'head', (18, 19), steps, closed=True)
        self.add_line('nose', (24, 38), (24, 34))
        self.relate('connect', 'head', 'nose')

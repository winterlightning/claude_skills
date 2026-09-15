"""Broaden and raise the doorway to balance the house interior, replacing the small cramped arched opening with a clearer entrance.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7e1b4154-d8c8-4476-9bd1-f79afb9ddf9e'
SOURCE_PATH = 'pictographic-primitives/interface-essential/house_7e1b4154-d8c8-4476-9bd1-f79afb9ddf9e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class House7e1b4154(Solo48):
    icon_id = 'house-7e1b4154-centerline-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('house', 'interface-essential')

    def build(self):

        def path(name, start, commands, closed=False):
            members = []
            previous = start
            for i, cmd in enumerate(commands):
                eid = f'{name}-{i}'
                members.append(eid)
                if cmd[0] == 'L':
                    self.add_line(eid, previous, cmd[1])
                elif cmd[0] == 'C':
                    self.add_bezier(eid, previous, tuple(cmd[1:]))
                elif cmd[0] == 'A':
                    self.add_arc(eid, previous, cmd[1], radius_x=cmd[2], radius_y=cmd[3], sweep=cmd[4])
                previous = cmd[-1] if cmd[0] == 'C' else cmd[1]
            self.add_contour(name, *members, closed=closed)

        def oval(name, cx, cy, rx, ry=None):
            ry = rx if ry is None else ry
            path(name, (cx - rx, cy), [('A', (cx, cy - ry), rx, ry, True), ('A', (cx + rx, cy), rx, ry, True), ('A', (cx, cy + ry), rx, ry, True), ('A', (cx - rx, cy), rx, ry, True)], True)

        def circle_nodes(name, cx, cy, r, nodes=()):
            import math
            pts = set(nodes) | {(cx - r, cy), (cx + r, cy), (cx, cy - r), (cx, cy + r)}
            assert all(((x - cx) ** 2 + (y - cy) ** 2 == r * r for x, y in pts))
            pts = sorted(pts, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
            path(name, pts[0], [('A', pt, r, r, True) for pt in pts[1:] + pts[:1]], True)

        def rounded(name, x1, y1, x2, y2, r):
            path(name, (x1 + r, y1), [('L', (x2 - r, y1)), ('A', (x2, y1 + r), r, r, True), ('L', (x2, y2 - r)), ('A', (x2 - r, y2), r, r, True), ('L', (x1 + r, y2)), ('A', (x1, y2 - r), r, r, True), ('L', (x1, y1 + r)), ('A', (x1 + r, y1), r, r, True)], True)
        self.add_polyline('roof', (6, 24), (10, 20), (24, 6), (38, 20), (42, 24))
        path('walls', (10, 20), [('L', (10, 38)), ('A', (14, 42), 4, 4, False), ('L', (19, 42)), ('L', (19, 32)), ('A', (24, 27), 5, 5, True), ('A', (29, 32), 5, 5, True), ('L', (29, 42)), ('L', (34, 42)), ('A', (38, 38), 4, 4, False), ('L', (38, 20))])
        self.relate('connect', 'roof', 'walls')
    variant_of = 'house-7e1b4154'
    variant_label = 'Batch 01 centerline repair'

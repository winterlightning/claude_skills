"""Canoe paddler: move the hand onto the real paddle node (31,20), and seat the torso on the gunwale at (12,32). Split the receiver at that exact contact. Radius4 head (17,12), shoulder (17,24), exact4 ink gap.

Reconstruct canoe paddler using its inspected source pose and full_body_ref.png. Head radius 4, center (17, 12), actual torso junction (17, 24): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Reconstruct canoe paddler using its inspected source pose and full_body_ref.png. Head radius 4, center (17, 12), actual torso junction (17, 24): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Canoe Paddler. Seated right-facing paddler with a raised paddle and curved bow; omit decorative waves.
Keyshape HRECT_L, visible extremes (2, 6, 46, 42); centerline envelope inset by 2.
Construction: Lucide person-standing: a circular head and sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fc6689dd-a028-5cb2-b326-1fe893e5518c'
SOURCE_PATH = 'pictographic-primitives/recreation/canoe person_fc6689dd-a028-5cb2-b326-1fe893e5518c.svg'
AUTHOR = 'gpt-6'

class CanoePaddler(Solo48):
    icon_id = 'canoe-paddler'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/recreation'
    aliases = ()
    keywords = ('canoe', 'paddler')

    def ring(self, name, x, y, r):
        self.add_arc(name + '-a', (x - r, y), (x + r, y), radius_x=r)
        self.add_arc(name + '-b', (x + r, y), (x - r, y), radius_x=r)
        self.add_contour(name, name + '-a', name + '-b', closed=True)

    def branches(self, branches):
        parts = []
        for name, points in branches:
            members = []
            for i, (a, b) in enumerate(zip(points, points[1:])):
                key = f'{name}-{i}'
                self.add_line(key, a, b)
                members.append(key)
                parts.append((key, a, b))
            if len(members) > 1:
                self.add_contour(name, *members)
        for i, (name, a, b) in enumerate(parts):
            for other, c, d in parts[i + 1:]:
                if a in (c, d) or b in (c, d):
                    self.relate('connect', name, other)

    def build(self):
        """Canoe paddler: move the hand onto the real paddle node (31,20), and seat the torso on the gunwale at (12,32). Split the receiver at that exact contact. Radius4 head (17,12), shoulder (17,24), exact4 ink gap."""
        self.add_arc('head-a', (13, 12), (21, 12), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('head-b', (21, 12), (13, 12), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_bezier('paddler-1', (12, 32), *(((13.25, 28.5), (17.0, 27.124099870362663), (17, 24)),))
        self.add_line('paddler-2', (17, 24), (25, 25))
        self.add_line('paddler-3', (25, 25), (31, 20))
        self.add_line('paddle-1', (39, 8), (31, 20))
        self.add_line('paddle-2', (31, 20), (23, 32))
        self.add_line('hull-1', (4, 32), (11, 40))
        self.add_line('hull-2', (11, 40), (35, 40))
        self.add_arc('bow', (35, 40), (43, 32), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('tip', (43, 32), (44, 29))
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('paddle', *('paddle-1', 'paddle-2'), closed=False)
        self.add_contour('canoe', *('hull-1', 'hull-2', 'bow', 'tip'), closed=False)
        self.add_contour('paddler', *('paddler-1',), closed=False)
        self.add_contour('paddler-section-1', *('paddler-2', 'paddler-3'), closed=False)
        self.relate('connect', *('paddler', 'paddle'))
        self.relate('connect', *('paddler-1', 'paddler-2'))
        self.relate('connect', *('paddler-2', 'paddler-3'))
        self.relate('connect', *('head-a', 'head-b'))
        self.relate('connect', *('paddler-1', 'paddler-2'))
        self.relate('connect', *('paddler-2', 'paddler-3'))
        self.relate('connect', *('paddle-1', 'paddle-2'))
        self.relate('connect', *('hull-1', 'hull-2'))
        self.relate('connect', *('hull-2', 'bow'))
        self.relate('connect', *('bow', 'tip'))
        self.branches([('gunwale', [(4, 32), (12, 32), (23, 32)])])
        self.relate('connect', 'paddler-1', 'gunwale-0')
        self.relate('connect', 'paddler-1', 'gunwale-1')
        self.relate('connect', 'paddler-3', 'paddle-1')
        self.relate('connect', 'paddler-3', 'paddle-2')
        self.relate('connect', 'paddle-2', 'gunwale-1')
        self.relate('connect', 'hull-1', 'gunwale-0')

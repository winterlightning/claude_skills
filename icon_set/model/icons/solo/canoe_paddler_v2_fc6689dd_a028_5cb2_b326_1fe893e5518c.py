"""Reconstruct canoe paddler using its inspected source pose and full_body_ref.png. Head radius 4, center (17, 12), actual torso junction (17, 24): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Canoe Paddler. Seated right-facing paddler with a raised paddle and curved bow; omit decorative waves.
Keyshape HRECT_L, visible extremes (2, 6, 46, 42); centerline envelope inset by 2.
Construction: Lucide person-standing: a circular head and sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fc6689dd-a028-5cb2-b326-1fe893e5518c'
SOURCE_PATH = 'pictographic-primitives/recreation/canoe person_fc6689dd-a028-5cb2-b326-1fe893e5518c.svg'
AUTHOR = 'gpt-6'

class CanoePaddlerVariant2(Solo48):
    icon_id = 'canoe-paddler-v2'
    variant_of = 'canoe-paddler'
    variant_label = 'Visual reconstruction after full 500-icon audit'
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
        """Reconstruct canoe paddler using its inspected source pose and full_body_ref.png. Head radius 4, center (17, 12), actual torso junction (17, 24): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.ring('head', 17, 12, 4)
        self.add_bezier('paddler-1', (12, 30), *(((13.25, 28.5), (17.0, 27.124099870362663), (17, 24)),))
        self.add_line('paddler-2', (17, 24), (25, 25))
        self.add_line('paddler-3', (25, 25), (34, 14))
        self.add_line('paddle-1', (39, 8), (31, 20))
        self.add_line('paddle-2', (31, 20), (23, 32))
        self.add_line('gunwale', (4, 32), (23, 32))
        self.add_line('hull-1', (4, 32), (11, 40))
        self.add_line('hull-2', (11, 40), (35, 40))
        self.add_arc('bow', (35, 40), (43, 32), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('tip', (43, 32), (44, 29))
        self.add_contour('paddler', *('paddler-1', 'paddler-2', 'paddler-3'), closed=False)
        self.add_contour('paddle', *('paddle-1', 'paddle-2'), closed=False)
        self.add_contour('canoe', *('hull-1', 'hull-2', 'bow', 'tip'), closed=False)
        self.relate('connect', *('paddler', 'paddle'))
        self.relate('connect', *('paddler', 'gunwale'))
        self.relate('connect', *('paddle', 'gunwale'))
        self.relate('connect', *('canoe', 'gunwale'))

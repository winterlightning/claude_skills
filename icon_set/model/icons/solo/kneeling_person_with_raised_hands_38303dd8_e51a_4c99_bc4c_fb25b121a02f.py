"""Reconstruct kneeling person with raised hands using its inspected source pose and full_body_ref.png. Head radius 6, center (28, 10), actual torso junction (28, 24): squared distance 196, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Reconstruct kneeling person with raised hands using its inspected source pose and full_body_ref.png. Head radius 6, center (28, 10), actual torso junction (28, 24): squared distance 196, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A left-facing kneeling worshipper with hands raised before the chest. Keep folded legs, forward arms and head; combine the paired arms into one readable gesture."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '38303dd8-e51a-4c99-bc4c-fb25b121a02f'
SOURCE_PATH = 'pictographic-primitives/religion/islam pray_38303dd8-e51a-4c99-bc4c-fb25b121a02f.svg'
AUTHOR = 'gpt-6'

class KneelingPersonWithRaisedHands(Solo48):
    icon_id = 'kneeling-person-with-raised-hands'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'religion'
    aliases = ()
    keywords = ('person', 'kneeling', 'prayer', 'hand', 'gesture', 'worship')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name + '-top', (cx - rx, cy), (cx + rx, cy), radius_x=rx, radius_y=ry)
        self.add_arc(name + '-bottom', (cx + rx, cy), (cx - rx, cy), radius_x=rx, radius_y=ry)
        self.add_contour(name, name + '-top', name + '-bottom', closed=True)

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
        """Reconstruct kneeling person with raised hands using its inspected source pose and full_body_ref.png. Head radius 6, center (28, 10), actual torso junction (28, 24): squared distance 196, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.add_arc('head-a', (22, 10), (34, 10), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('head-b', (34, 10), (22, 10), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_bezier('back-1', (28, 24), *(((28.0, 27.92), (31.75, 31.5), (33, 34)),))
        self.add_line('back-2', (33, 34), (25, 44))
        self.add_line('back-3', (25, 44), (40, 44))
        self.add_line('arm', (28, 24), (17, 31))
        self.add_line('forearm', (17, 31), (8, 22))
        self.add_line('front-1', (19, 33), (20, 37))
        self.add_line('front-2', (20, 37), (13, 44))
        self.add_line('front-3', (13, 44), (25, 44))
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('front', *('front-1', 'front-2', 'front-3'), closed=False)
        self.relate('connect', *('arm', 'forearm'))
        self.relate('connect', *('back', 'arm'))
        self.relate('connect', *('front', 'back'))
        self.add_contour('back', *('back-1',), closed=False)
        self.add_contour('back-section-1', *('back-2', 'back-3'), closed=False)
        self.relate('connect', 'back-1', 'back-2')
        self.relate('connect', 'back-2', 'back-3')
        self.relate('connect', 'head-a', 'head-b')
        self.relate('connect', 'back-1', 'back-2')
        self.relate('connect', 'back-1', 'arm')
        self.relate('connect', 'back-2', 'back-3')
        self.relate('connect', 'back-2', 'front-3')
        self.relate('connect', 'back-3', 'front-3')
        self.relate('connect', 'arm', 'forearm')
        self.relate('connect', 'front-1', 'front-2')
        self.relate('connect', 'front-2', 'front-3')

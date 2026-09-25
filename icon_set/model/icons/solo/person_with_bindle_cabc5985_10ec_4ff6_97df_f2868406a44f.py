"""Reconstruct person with bindle using its inspected source pose and full_body_ref.png. Head radius 6, center (34, 10), actual torso junction (34, 24): squared distance 196, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A person strides right with a tied bundle carried on a shoulder stick. Lucide person-standing informs the stride. The knot and fingers are reduced; the bundle and carrying pole remain distinct physical parts."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cabc5985-10ec-4ff6-97df-f2868406a44f'
SOURCE_PATH = 'pictographic-primitives/users/user homeless poverty 1_cabc5985-10ec-4ff6-97df-f2868406a44f.svg'
AUTHOR = 'gpt-6'

class PersonWithBindle(Solo48):
    icon_id = 'person-with-bindle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'users'
    categories = ('users', 'primitives')
    aliases = ()
    keywords = ('homeless', 'bindle', 'walking', 'traveller', 'person', 'bundle', 'poverty', 'wanderer')

    def circle(self, name, cx, cy, r):
        pts = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy), (cx, cy - r)]
        ids = []
        for i, (a, b) in enumerate(zip(pts, pts[1:])):
            eid = name + '-' + str(i)
            self.add_arc(eid, a, b, radius_x=r)
            ids.append(eid)
        self.add_contour(name, *ids, closed=True)

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
        """Reconstruct person with bindle using its inspected source pose and full_body_ref.png. Head radius 6, center (34, 10), actual torso junction (34, 24): squared distance 196, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.ring('head', 34, 10, 6)
        self.add_line('bundle-left', (13, 6), (8, 16))
        self.add_arc('bundle-bottom', (8, 16), (18, 16), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('bundle-right', (18, 16), (13, 6))
        self.add_line('pole', (18, 16), (26, 26))
        self.add_line('torso-1', (26, 26), (34, 24))
        self.add_bezier('torso-2', (34, 24), *(((34.0, 27.92), (26.5, 31.5), (24, 34)),))
        self.add_line('arm-1', (34, 24), (33, 31))
        self.add_line('arm-2', (33, 31), (39, 27))
        self.add_line('legs-1', (16, 44), (24, 34))
        self.add_line('legs-2', (24, 34), (32, 37))
        self.add_line('legs-3', (32, 37), (40, 44))
        self.add_contour('bundle', *('bundle-left', 'bundle-bottom', 'bundle-right'), closed=True)
        self.add_contour('torso', *('torso-1', 'torso-2'), closed=False)
        self.add_contour('arm', *('arm-1', 'arm-2'), closed=False)
        self.add_contour('legs', *('legs-1', 'legs-2', 'legs-3'), closed=False)
        self.relate('connect', *('bundle', 'pole'))
        self.relate('connect', *('pole', 'torso'))
        self.relate('connect', *('torso', 'arm'))
        self.relate('connect', *('torso', 'legs'))

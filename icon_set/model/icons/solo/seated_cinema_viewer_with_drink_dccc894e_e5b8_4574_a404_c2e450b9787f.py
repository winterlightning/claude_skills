"""Reconstruct seated cinema viewer with drink using its inspected source pose and full_body_ref.png. Head radius 5, center (32, 11), actual torso junction (32, 24): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Reclining cinema viewer with cup, bent straw, chair and extended leg; background screen and duplicate leg contour omitted for clarity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dccc894e-e5b8-4574-a404-c2e450b9787f'
SOURCE_PATH = 'pictographic-primitives/movies/movies sit drink_dccc894e-e5b8-4574-a404-c2e450b9787f.svg'
AUTHOR = 'gpt-6'

class SeatedCinemaViewerWithDrink(Solo48):
    icon_id = 'seated-cinema-viewer-with-drink'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'movies'
    aliases = ()
    keywords = ('cinema', 'viewer', 'seat', 'drink', 'screen', 'movie')

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
        """Reconstruct seated cinema viewer with drink using its inspected source pose and full_body_ref.png. Head radius 5, center (32, 11), actual torso junction (32, 24): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.ring('head', 32, 11, 5)
        self.add_line('cup-1', (6, 16), (10, 16))
        self.add_line('cup-2', (10, 16), (14, 16))
        self.add_line('cup-3', (14, 16), (14, 24))
        self.add_line('cup-4', (14, 24), (6, 24))
        self.add_line('cup-5', (6, 24), (6, 16))
        self.add_line('straw-1', (10, 16), (10, 10))
        self.add_line('straw-2', (10, 10), (16, 8))
        self.add_line('arm-1', (14, 24), (24, 24))
        self.add_line('arm-2', (24, 24), (32, 24))
        self.add_bezier('torso', (32, 24), *(((32.0, 27.577708763999663), (29.0, 30.0), (28, 32)),))
        self.add_line('chair-1', (42, 20), (38, 42))
        self.add_line('chair-2', (38, 42), (22, 42))
        self.add_line('chair-3', (22, 42), (18, 32))
        self.add_line('chair-4', (18, 32), (20, 32))
        self.add_line('chair-5', (20, 32), (28, 32))
        self.add_line('chair-6', (28, 32), (34, 32))
        self.add_line('leg-1', (28, 32), (20, 32))
        self.add_line('leg-2', (20, 32), (6, 38))
        self.add_contour('cup', *('cup-1', 'cup-2', 'cup-3', 'cup-4', 'cup-5'), closed=True)
        self.add_contour('straw', *('straw-1', 'straw-2'), closed=False)
        self.add_contour('arm', *('arm-1', 'arm-2'), closed=False)
        self.add_contour('chair', *('chair-1', 'chair-2', 'chair-3', 'chair-4', 'chair-5', 'chair-6'), closed=False)
        self.add_contour('leg', *('leg-1', 'leg-2'), closed=False)
        self.relate('connect', *('straw', 'cup'))
        self.relate('connect', *('arm', 'cup'))
        self.relate('connect', *('torso', 'arm'))
        self.relate('connect', *('chair', 'torso'))
        self.relate('connect', *('leg', 'torso'))
        self.relate('connect', *('leg', 'chair'))

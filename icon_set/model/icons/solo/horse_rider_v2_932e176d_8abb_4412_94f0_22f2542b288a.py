"""Reconstruct horse rider using its inspected source pose and full_body_ref.png. Head radius 5, center (24, 11), actual torso junction (19, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct horse rider using its inspected source pose and full_body_ref.png. Head radius 5, center (24, 11), actual torso junction (19, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct horse rider using its inspected source pose and full_body_ref.png. Head radius 5, center (24, 11), actual torso junction (19, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Horse Rider, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '932e176d-8abb-4412-94f0-22f2542b288a'
SOURCE_PATH = 'pictographic-primitives/sports/sport horse riding_932e176d-8abb-4412-94f0-22f2542b288a.svg'
AUTHOR = 'gpt-6'

class HorseRiderVariant2(Solo48):
    icon_id = 'horse-rider-v2'
    variant_of = 'horse-rider'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('horse', 'rider', 'equestrian', 'helmet', 'animal', 'sport')

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
        """Reconstruct horse rider using its inspected source pose and full_body_ref.png. Head radius 5, center (24, 11), actual torso junction (19, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch."""
        self.add_arc('head-a', (19, 11), (29, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('head-b', (29, 11), (19, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_bezier('rider-1', (19, 23), *(((18.102930477716107, 25.15296685348134), (15.25, 25.25), (14, 26)),))
        self.add_line('rider-2', (14, 26), (22, 29))
        self.add_line('rider-3', (22, 29), (20, 37))
        self.add_line('arms-1', (19, 23), (26, 26))
        self.add_line('arms-2', (26, 26), (34, 18))
        self.add_line('horse-1', (14, 26), (28, 28))
        self.add_line('horse-2', (28, 28), (34, 18))
        self.add_line('horse-3', (34, 18), (38, 18))
        self.add_line('horse-4', (38, 18), (42, 26))
        self.add_line('horse-5', (42, 26), (34, 26))
        self.add_line('horse-6', (34, 26), (31, 34))
        self.add_line('horse-7', (31, 34), (38, 38))
        self.add_line('horse-8', (38, 38), (37, 42))
        self.add_line('rear-leg-1', (14, 26), (12, 34))
        self.add_line('rear-leg-2', (12, 34), (8, 42))
        self.add_line('tail-1', (6, 32), (8, 27))
        self.add_line('tail-2', (8, 27), (14, 26))
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('arms', *('arms-1', 'arms-2'), closed=False)
        self.add_contour('horse', *('horse-1', 'horse-2', 'horse-3', 'horse-4', 'horse-5', 'horse-6', 'horse-7', 'horse-8'), closed=False)
        self.add_contour('rear-leg', *('rear-leg-1', 'rear-leg-2'), closed=False)
        self.add_contour('tail', *('tail-1', 'tail-2'), closed=False)
        self.relate('connect', *('rider', 'arms'))
        self.relate('connect', *('rider', 'horse'))
        self.relate('connect', *('arms', 'horse'))
        self.relate('connect', *('horse', 'rear-leg'))
        self.relate('connect', *('horse', 'tail'))
        self.relate('connect', *('rider', 'rear-leg'))
        self.relate('connect', *('rider', 'tail'))
        self.relate('connect', *('tail', 'rear-leg'))
        self.add_contour('rider', *('rider-1',), closed=False)
        self.add_contour('rider-section-1', *('rider-2', 'rider-3'), closed=False)
        self.relate('connect', 'rider-1', 'rider-2')
        self.relate('connect', 'rider-2', 'rider-3')
        self.relate('connect', 'head-a', 'head-b')
        self.relate('connect', 'rider-1', 'rider-2')
        self.relate('connect', 'rider-1', 'arms-1')
        self.relate('connect', 'rider-1', 'horse-1')
        self.relate('connect', 'rider-1', 'rear-leg-1')
        self.relate('connect', 'rider-1', 'tail-2')
        self.relate('connect', 'rider-2', 'rider-3')
        self.relate('connect', 'rider-2', 'horse-1')
        self.relate('connect', 'rider-2', 'rear-leg-1')
        self.relate('connect', 'rider-2', 'tail-2')
        self.relate('connect', 'arms-1', 'arms-2')
        self.relate('connect', 'arms-2', 'horse-2')
        self.relate('connect', 'arms-2', 'horse-3')
        self.relate('connect', 'horse-1', 'horse-2')
        self.relate('connect', 'horse-1', 'rear-leg-1')
        self.relate('connect', 'horse-1', 'tail-2')
        self.relate('connect', 'horse-2', 'horse-3')
        self.relate('connect', 'horse-3', 'horse-4')
        self.relate('connect', 'horse-4', 'horse-5')
        self.relate('connect', 'horse-5', 'horse-6')
        self.relate('connect', 'horse-6', 'horse-7')
        self.relate('connect', 'horse-7', 'horse-8')
        self.relate('connect', 'rear-leg-1', 'rear-leg-2')
        self.relate('connect', 'rear-leg-1', 'tail-2')
        self.relate('connect', 'tail-1', 'tail-2')

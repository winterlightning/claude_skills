"""Reconstruct windsurfer holding sail using its inspected source pose and full_body_ref.png. Head radius 4, center (12, 13), actual torso junction (12, 25): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct windsurfer holding sail using its inspected source pose and full_body_ref.png. Head radius 4, center (12, 13), actual torso junction (12, 25): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct windsurfer holding sail using its inspected source pose and full_body_ref.png. Head radius 4, center (12, 13), actual torso junction (12, 25): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Windsurfer Holding Sail. A left-leaning windsurfer grips the sail; retain bent knees and sailboard, omit second arm and sail seam.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide sailboat: coherent sail outline and a structurally attached mast. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3541bc83-1790-4f3d-b629-f2530a4a05c6'
SOURCE_PATH = 'pictographic-primitives/recreation/nautic sports sailing person_3541bc83-1790-4f3d-b629-f2530a4a05c6.svg'
AUTHOR = 'gpt-6'

class WindsurferHoldingSail(Solo48):
    icon_id = 'windsurfer-holding-sail'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'recreation'
    categories = ('primitives', 'recreation')
    aliases = ()
    keywords = ('windsurfer', 'holding', 'sail')

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
        """Reconstruct windsurfer holding sail using its inspected source pose and full_body_ref.png. Head radius 4, center (12, 13), actual torso junction (12, 25): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch."""
        self.add_arc('head-a', (8, 13), (16, 13), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('head-b', (16, 13), (8, 13), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sail-mast-1', (26, 6), (28, 16))
        self.add_line('sail-mast-2', (28, 16), (32, 36))
        self.add_arc('sail-edge', (26, 6), (42, 27), radius_x=30, radius_y=28, large_arc=False, sweep=True)
        self.add_line('sail-foot', (42, 27), (32, 36))
        self.add_line('rider-1', (12, 42), (17, 33))
        self.add_line('rider-2', (17, 33), (8, 28))
        self.add_bezier('rider-3', (8, 28), *(((9.0, 27.25), (12.0, 27.0), (12, 25)),))
        self.add_line('rider-4', (12, 25), (21, 25))
        self.add_line('rider-5', (21, 25), (28, 16))
        self.add_line('board-1', (6, 42), (12, 42))
        self.add_line('board-2', (12, 42), (32, 42))
        self.add_line('board-3', (32, 42), (42, 37))
        self.add_line('mast-base', (32, 36), (32, 42))
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('sail-mast', *('sail-mast-1', 'sail-mast-2'), closed=False)
        self.add_contour('sail', *('sail-edge', 'sail-foot'), closed=False)
        self.add_contour('board', *('board-1', 'board-2', 'board-3'), closed=False)
        self.relate('connect', *('sail', 'sail-mast'))
        self.relate('connect', *('rider', 'rider-5'))
        self.relate('connect', *('rider-5', 'sail-mast'))
        self.relate('connect', *('mast-base', 'sail'))
        self.relate('connect', *('mast-base', 'sail-mast'))
        self.relate('connect', *('mast-base', 'board'))
        self.relate('connect', *('rider', 'board'))
        self.add_contour('rider', *('rider-1', 'rider-2'), closed=False)
        self.add_contour('rider-section-1', *('rider-3',), closed=False)
        self.add_contour('rider-section-2', *('rider-4',), closed=False)
        self.relate('connect', 'rider-1', 'rider-2')
        self.relate('connect', 'rider-2', 'rider-3')
        self.relate('connect', 'rider-3', 'rider-4')
        self.relate('connect', 'head-a', 'head-b')
        self.relate('connect', 'sail-mast-1', 'sail-mast-2')
        self.relate('connect', 'sail-mast-1', 'sail-edge')
        self.relate('connect', 'sail-mast-1', 'rider-5')
        self.relate('connect', 'sail-mast-2', 'sail-foot')
        self.relate('connect', 'sail-mast-2', 'rider-5')
        self.relate('connect', 'sail-mast-2', 'mast-base')
        self.relate('connect', 'sail-edge', 'sail-foot')
        self.relate('connect', 'sail-foot', 'mast-base')
        self.relate('connect', 'rider-1', 'rider-2')
        self.relate('connect', 'rider-1', 'board-1')
        self.relate('connect', 'rider-1', 'board-2')
        self.relate('connect', 'rider-2', 'rider-3')
        self.relate('connect', 'rider-3', 'rider-4')
        self.relate('connect', 'rider-4', 'rider-5')
        self.relate('connect', 'board-1', 'board-2')
        self.relate('connect', 'board-2', 'board-3')
        self.relate('connect', 'board-2', 'mast-base')
        self.relate('connect', 'board-3', 'mast-base')

"""Reconstruct wakeboarder using its inspected source pose and full_body_ref.png. Head radius 4, center (35, 10), actual torso junction (35, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct wakeboarder using its inspected source pose and full_body_ref.png. Head radius 4, center (35, 10), actual torso junction (35, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct wakeboarder using its inspected source pose and full_body_ref.png. Head radius 4, center (35, 10), actual torso junction (35, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Wakeboarder. Wakeboarder leans back against a triangular tow handle above a rounded board; reduce the paired legs to one bent leg and omit doubled arms.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide person-standing: a circular head and sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2baefd97-8c64-5fc2-8c4b-0c6018001d00'
SOURCE_PATH = 'pictographic-primitives/recreation/sport wakeboarding_2baefd97-8c64-5fc2-8c4b-0c6018001d00.svg'
AUTHOR = 'gpt-6'

class Wakeboarder(Solo48):
    icon_id = 'wakeboarder'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/recreation'
    aliases = ()
    keywords = ('wakeboarder',)

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
        """Reconstruct wakeboarder using its inspected source pose and full_body_ref.png. Head radius 4, center (35, 10), actual torso junction (35, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch."""
        self.add_arc('head-a', (31, 10), (39, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('head-b', (39, 10), (31, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('rider-1', (21, 22), (35, 22))
        self.add_bezier('rider-2', (35, 22), *(((35.0, 24.154065922853803), (33.5, 25.75), (33, 27)),))
        self.add_line('rider-3', (33, 27), (26, 29))
        self.add_line('rider-4', (26, 29), (23, 34))
        self.add_line('handle-1', (9, 20), (21, 12))
        self.add_line('handle-2', (21, 12), (21, 22))
        self.add_line('handle-3', (21, 22), (21, 28))
        self.add_line('handle-4', (21, 28), (9, 20))
        self.add_line('rope', (6, 20), (9, 20))
        self.add_line('board-top-1', (18, 34), (23, 34))
        self.add_line('board-top-2', (23, 34), (38, 34))
        self.add_arc('board-right', (38, 34), (38, 42), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('board-bottom', (38, 42), (18, 42))
        self.add_arc('board-left', (18, 42), (18, 34), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('handle', *('handle-1', 'handle-2', 'handle-3', 'handle-4'), closed=True)
        self.add_contour('board', *('board-top-1', 'board-top-2', 'board-right', 'board-bottom', 'board-left'), closed=True)
        self.relate('connect', *('rope', 'handle'))
        self.relate('connect', *('handle', 'rider'))
        self.relate('connect', *('board', 'rider'))
        self.add_contour('rider', *('rider-1',), closed=False)
        self.add_contour('rider-section-1', *('rider-2',), closed=False)
        self.add_contour('rider-section-2', *('rider-3', 'rider-4'), closed=False)
        self.relate('connect', 'rider-1', 'rider-2')
        self.relate('connect', 'rider-2', 'rider-3')
        self.relate('connect', 'rider-3', 'rider-4')
        self.relate('connect', 'head-a', 'head-b')
        self.relate('connect', 'rider-1', 'rider-2')
        self.relate('connect', 'rider-1', 'handle-2')
        self.relate('connect', 'rider-1', 'handle-3')
        self.relate('connect', 'rider-2', 'rider-3')
        self.relate('connect', 'rider-3', 'rider-4')
        self.relate('connect', 'rider-4', 'board-top-1')
        self.relate('connect', 'rider-4', 'board-top-2')
        self.relate('connect', 'handle-1', 'handle-2')
        self.relate('connect', 'handle-1', 'handle-4')
        self.relate('connect', 'handle-1', 'rope')
        self.relate('connect', 'handle-2', 'handle-3')
        self.relate('connect', 'handle-3', 'handle-4')
        self.relate('connect', 'handle-4', 'rope')
        self.relate('connect', 'board-top-1', 'board-top-2')
        self.relate('connect', 'board-top-1', 'board-left')
        self.relate('connect', 'board-top-2', 'board-right')
        self.relate('connect', 'board-right', 'board-bottom')
        self.relate('connect', 'board-bottom', 'board-left')

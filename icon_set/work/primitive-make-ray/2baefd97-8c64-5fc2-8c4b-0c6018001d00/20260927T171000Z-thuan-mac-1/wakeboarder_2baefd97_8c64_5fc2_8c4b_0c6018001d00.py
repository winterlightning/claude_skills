"""Reconstruct wakeboarder using its inspected source pose and full_body_ref.png. Head radius 4, center (35, 10), actual torso junction (35, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct wakeboarder using its inspected source pose and full_body_ref.png. Head radius 4, center (35, 10), actual torso junction (35, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct wakeboarder using its inspected source pose and full_body_ref.png. Head radius 4, center (35, 10), actual torso junction (35, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Wakeboarder. Wakeboarder leans back against a triangular tow handle above a rounded board; reduce the paired legs to one bent leg and omit doubled arms.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide person-standing: a circular head and sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2baefd97-8c64-5fc2-8c4b-0c6018001d00'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wakeboarder/20260927T160114Z-thuan-mac-1/reference/sport wakeboarding_2baefd97-8c64-5fc2-8c4b-0c6018001d00.svg'
AUTHOR = "gpt-6"

class Wakeboarder(Solo48):
    icon_id = 'wakeboarder'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'recreation'
    categories = ('primitives', 'recreation')
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
        # Tow handle, arm, leaning rider, and board are tied at actual joints.
        self.add_arc('head-a',(31,10),(39,10),radius_x=4)
        self.add_arc('head-b',(39,10),(31,10),radius_x=4)
        self.add_contour('head','head-a','head-b',closed=True)
        self.add_polyline('handle',(9,20),(21,12),(21,28),closed=True)
        self.add_line('rope',(6,20),(9,20))
        self.relate('connect','rope','handle')
        self.add_line('arm',(21,22),(35,22))
        self.relate('connect','arm','handle')
        self.add_bezier('rider-leg',(35,22),((36,27),(29,31),(23,34)))
        self.relate('connect','arm','rider-leg')
        self.add_line('board-top-left',(18,34),(23,34))
        self.add_line('board-top-right',(23,34),(38,34))
        self.add_arc('board-right',(38,34),(38,42),radius_x=4)
        self.add_line('board-bottom',(38,42),(18,42))
        self.add_arc('board-left',(18,42),(18,34),radius_x=4)
        self.add_contour('board','board-top-left','board-top-right','board-right','board-bottom','board-left',closed=True)
        self.relate('connect','rider-leg','board')
        self.mark_human_figure('person',head='head',torso='rider-leg',torso_junction='start')

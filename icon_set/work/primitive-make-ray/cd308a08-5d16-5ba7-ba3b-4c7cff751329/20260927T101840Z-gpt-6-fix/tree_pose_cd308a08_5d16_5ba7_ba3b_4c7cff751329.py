"""Reconstruct tree pose using its inspected source pose and full_body_ref.png. Head radius 5, center (24, 11), actual torso junction (24, 24): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Reconstruct tree pose using its inspected source pose and full_body_ref.png. Head radius 5, center (24, 11), actual torso junction (24, 24): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A figure balances on one straight leg while the opposite foot rests against its inner side, forming a triangular knee opening. Both arms curve overhead around the circular head.
Construction: Bounds (8,6)-(40,42). Mirror overhead arms, but retain the single folded knee and straight supporting leg. Triangle of bent knee remains open.
Lucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'cd308a08-5d16-5ba7-ba3b-4c7cff751329'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tree-pose/20260927T101610Z-thuan-mac-1/reference/yoga tree pose_cd308a08-5d16-5ba7-ba3b-4c7cff751329.svg'
AUTHOR = 'gpt-6'

class TreePose(Solo48):
    icon_id = 'tree-pose'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('tree', 'pose', 'yoga', 'exercise')

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
        """Arms wrap above the head as in the original tree pose; the bent leg stays distinct."""
        self.add_arc('head-top',(20,13),(28,13),radius_x=4,sweep=True)
        self.add_arc('head-bottom',(28,13),(20,13),radius_x=4,sweep=True)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_bezier('left-upper',(14,4),((11,7),(10,10),(10,14)))
        self.add_bezier('left-lower',(10,14),((10,20),(13,22),(17,25)))
        self.add_contour('left-arm','left-upper','left-lower')
        self.add_bezier('right-lower',(31,25),((35,22),(38,20),(38,14)))
        self.add_bezier('right-upper',(38,14),((38,10),(37,7),(34,4)))
        self.add_contour('right-arm','right-lower','right-upper')
        self.add_line('left-shoulder',(17,25),(24,25))
        self.add_line('right-shoulder',(24,25),(31,25))
        self.add_line('torso',(24,25),(24,44))
        self.add_polyline('bent-leg',(24,34),(38,38),(24,44))
        for a,b in [('left-arm','left-shoulder'),('right-arm','right-shoulder'),('left-shoulder','right-shoulder'),('left-shoulder','torso'),('right-shoulder','torso'),('torso','bent-leg')]:
            self.relate('connect',a,b)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

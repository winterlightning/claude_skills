"""Fresh revision of racing-cyclist.

Original and rejected SVG compared before drawing. The rider and small wheels read as a standing figure; enlarged the wheels and shifted the limbs into a riding pose.
"""
# Repair: Lengthen the racing back and thigh, retain both wheels and connect the hands to the actual fork. Exact 13-5=8 head gap.
"""Reconstruct racing cyclist using its inspected source pose and full_body_ref.png. Head radius 5, center (30, 11), actual torso junction (25, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct racing cyclist using its inspected source pose and full_body_ref.png. Head radius 5, center (30, 11), actual torso junction (25, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct racing cyclist using its inspected source pose and full_body_ref.png. Head radius 5, center (30, 11), actual torso junction (25, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Racing cyclist, authored on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1cb7d2ba-c91a-4cd1-bd29-7ebbabf08914'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-fix-thuan/solo__racing-cyclist/20260927T153833Z-thuan-mac-1/reference/race_1cb7d2ba-c91a-4cd1-bd29-7ebbabf08914.svg'
AUTHOR = 'gpt-6'

class RacingCyclist(Solo48):
    icon_id = 'racing-cyclist'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('racing', 'cyclist')

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
        # Bicyclist on two equal wheels; intentionally leaned forward.
        def circle(name,cx,cy,r):
            self.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-a',name+'-b',closed=True)
        circle('rear-wheel',10,34,6)
        circle('front-wheel',38,34,6)
        circle('head',26,12,4)
        self.add_line('torso',(26,24),(16,26))
        self.add_polyline('arms',(26,24),(32,26),(38,28))
        self.add_polyline('leg',(16,26),(20,32))
        self.add_polyline('frame',(10,28),(20,32),(30,28),(38,28))
        self.relate('connect','arms','torso')
        self.relate('connect','leg','torso')
        self.relate('connect','leg','frame')
        self.relate('connect','frame','rear-wheel')
        self.relate('connect','frame','front-wheel')
        self.relate('connect','arms','frame')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

# Refinement: Lift the helping hand and mattress edge away from the standing leg.
# Repair: Shorten the free forearm so it clears the right thigh.
"""Reconstruct person beside bed using its inspected source pose and full_body_ref.png. Head radius 6, center (36, 12), actual torso junction (36, 26): squared distance 196, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A standing person stands at the right end of a low bed with a raised pillow. Lucide person-standing and bed-single inform limbs and the bed rail; hands and mattress thickness detail are reduced."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '46e8e840-52d0-4c78-aab3-c23fdb5e0ef4'
SOURCE_PATH = 'pictographic-primitives/users/neutral actions share_46e8e840-52d0-4c78-aab3-c23fdb5e0ef4.svg'
AUTHOR = 'gpt-6'

class PersonBesideBed(Solo48):
    icon_id = 'person-beside-bed'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'users'
    categories = ('users', 'primitives')
    aliases = ()
    keywords = ('person', 'bed', 'hotel', 'room', 'sleep', 'share', 'accommodation', 'rest')

    def circle(self, name, cx, cy, radius):
        top, bottom = ((cx, cy - radius), (cx, cy + radius))
        self.add_arc(name + '-a', top, bottom, radius_x=radius)
        self.add_arc(name + '-b', bottom, top, radius_x=radius)
        self.add_contour(name, name + '-a', name + '-b', closed=True)

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
        """Reconstruct person beside bed using its inspected source pose and full_body_ref.png. Head radius 6, center (36, 12), actual torso junction (36, 26): squared distance 196, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.ring('head', 36, 12, 6)
        self.add_bezier('torso-1', (36, 26), *(((36.0, 29.2), (36.0, 32.0), (36, 34)),))
        self.add_line('arms-1', (24, 32), (36, 26))
        self.add_line('arms-2', (36, 26), (42, 29))
        self.add_line('legs-1', (32, 42), (36, 34))
        self.add_line('legs-2', (36, 34), (40, 42))
        self.add_line('bed-post-1', (6, 26), (6, 30))
        self.add_line('bed-post-2', (6, 30), (6, 42))
        self.add_line('mattress-1', (6, 30), (14, 30))
        self.add_line('mattress-2', (14, 30), (18, 32))
        self.add_line('mattress-3', (18, 32), (24, 32))
        self.add_line('mattress-4', (24, 32), (24, 42))
        self.add_line('mattress-5', (24, 42), (6, 42))
        self.add_contour('torso', *('torso-1',), closed=False)
        self.add_contour('arms', *('arms-1', 'arms-2'), closed=False)
        self.add_contour('legs', *('legs-1', 'legs-2'), closed=False)
        self.add_contour('bed-post', *('bed-post-1', 'bed-post-2'), closed=False)
        self.add_contour('mattress', *('mattress-1', 'mattress-2', 'mattress-3', 'mattress-4', 'mattress-5'), closed=False)
        self.relate('connect', *('torso', 'arms'))
        self.relate('connect', *('torso', 'legs'))
        self.relate('connect', *('bed-post', 'mattress'))
        self.relate('connect', *('arms', 'mattress'))
        self.mark_human_figure('person', head='head', torso='torso-1', torso_junction='start')

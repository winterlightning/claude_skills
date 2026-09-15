"""Reconstruct fortune teller reading using its inspected source pose and full_body_ref.png. Head radius 5, center (12, 11), actual torso junction (12, 24): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Reconstruct fortune teller reading using its inspected source pose and full_body_ref.png. Head radius 5, center (12, 11), actual torso junction (12, 24): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Fortune teller reading.

Symbol plan: shared integer nodes preserve contour order, repeated stations and real
attachments. The SQUARE visible envelope is (4, 4, 44, 44).
The parent remains available for comparison.
Human construction: icon_set/references/human_ref/full_body_ref.png and
icon_set/references/human_ref/user.svg. Circular head radius 5,
with exactly 8 units of centerline head-to-body separation (4 visible units)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b3dff2fa-37b5-4c07-a64d-1c001573067f'
SOURCE_PATH = 'pictographic-primitives/culture/batch-03/sphere teller_b3dff2fa-37b5-4c07-a64d-1c001573067f.svg'
AUTHOR = 'gpt-6'

class FortuneTellerReading(Solo48):
    icon_id = 'fortune-teller-reading'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture/objects'
    aliases = ()
    keywords = ('fortune teller', 'crystal ball', 'divination', 'psychic', 'reading', 'mystic', 'seance', 'future')

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
        """Reconstruct fortune teller reading using its inspected source pose and full_body_ref.png. Head radius 5, center (12, 11), actual torso junction (12, 24): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.add_arc('head-a', (7, 11), (17, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('head-b', (17, 11), (7, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_bezier('seated-body-0', (12, 24), *(((12.0, 27.64), (7.5, 31.5), (6, 34)),))
        self.add_line('seated-body-1', (6, 34), (14, 34))
        self.add_line('seated-body-2', (14, 34), (18, 42))
        self.add_line('reaching-arm', (12, 24), (20, 32))
        self.add_arc('ball-top', (26, 20), (42, 20), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('ball-br', (42, 20), (34, 28), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('ball-bl', (34, 28), (26, 20), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('stand', (34, 28), (34, 34))
        self.add_line('table-0', (29, 34), (34, 34))
        self.add_line('table-1', (34, 34), (42, 34))
        self.add_line('table-leg', (34, 34), (34, 42))
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('ball', *('ball-top', 'ball-br', 'ball-bl'), closed=True)
        self.add_contour('table', *('table-0', 'table-1'), closed=False)
        self.relate('connect', *('reaching-arm', 'seated-body'))
        self.relate('connect', *('ball', 'stand'))
        self.relate('connect', *('stand', 'table'))
        self.relate('connect', *('table-leg', 'table'))
        self.relate('connect', *('table-leg', 'stand'))
        self.add_contour('seated-body', *('seated-body-0',), closed=False)
        self.add_contour('seated-body-section-1', *('seated-body-1', 'seated-body-2'), closed=False)
        self.relate('connect', 'seated-body-0', 'seated-body-1')
        self.relate('connect', 'seated-body-1', 'seated-body-2')
        self.relate('connect', 'head-a', 'head-b')
        self.relate('connect', 'seated-body-0', 'seated-body-1')
        self.relate('connect', 'seated-body-0', 'reaching-arm')
        self.relate('connect', 'seated-body-1', 'seated-body-2')
        self.relate('connect', 'ball-top', 'ball-br')
        self.relate('connect', 'ball-top', 'ball-bl')
        self.relate('connect', 'ball-br', 'ball-bl')
        self.relate('connect', 'ball-br', 'stand')
        self.relate('connect', 'ball-bl', 'stand')
        self.relate('connect', 'stand', 'table-0')
        self.relate('connect', 'stand', 'table-1')
        self.relate('connect', 'stand', 'table-leg')
        self.relate('connect', 'table-0', 'table-1')
        self.relate('connect', 'table-0', 'table-leg')
        self.relate('connect', 'table-1', 'table-leg')

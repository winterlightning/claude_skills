"""Reconstruct person running through doorway using its inspected source pose and full_body_ref.png. Head radius 4, center (23, 18), actual torso junction (23, 30): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct person running through doorway using its inspected source pose and full_body_ref.png. Head radius 4, center (23, 18), actual torso junction (23, 30): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A person runs through an open doorway with one arm and both legs spread across its opening. Two tall jambs join across the top and end in short outward feet.

Construction: Runner crosses a door frame; jamb breaks occur where the arms pass through. Bounds (6,6)-(42,42).
Lucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e1e6b172-0589-49ee-9311-e9b8ae8c07ff'
SOURCE_PATH = 'pictographic-primitives/wayfinding/safety exit door_e1e6b172-0589-49ee-9311-e9b8ae8c07ff.svg'
AUTHOR = 'gpt-6'

class PersonRunningThroughDoorway(Solo48):
    icon_id = 'person-running-through-doorway'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('exit', 'doorway', 'running', 'person', 'escape', 'safety')

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
        """Reconstruct person running through doorway using its inspected source pose and full_body_ref.png. Head radius 4, center (23, 18), actual torso junction (23, 30): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch."""
        self.add_arc('person-head-a', (19, 18), (27, 18), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('person-head-b', (27, 18), (19, 18), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_bezier('person-body-1', (23, 30), *(((23.0, 32.0), (20.75, 33.0), (20, 34)),))
        self.add_line('person-arms-1', (6, 28), (14, 30))
        self.add_line('person-arms-2', (14, 30), (23, 30))
        self.add_line('person-arms-3', (23, 30), (34, 32))
        self.add_line('person-arms-4', (34, 32), (42, 32))
        self.add_line('person-legs-1', (14, 42), (20, 34))
        self.add_line('person-legs-2', (20, 34), (28, 40))
        self.add_line('person-legs-3', (28, 40), (34, 40))
        self.add_line('door-top-1', (6, 18), (6, 6))
        self.add_line('door-top-2', (6, 6), (42, 6))
        self.add_line('door-top-3', (42, 6), (42, 22))
        self.add_line('door-bottom', (42, 32), (42, 42))
        self.add_contour('person-head', *('person-head-a', 'person-head-b'), closed=True)
        self.add_contour('person-body', *('person-body-1',), closed=False)
        self.add_contour('person-arms', *('person-arms-1', 'person-arms-2', 'person-arms-3', 'person-arms-4'), closed=False)
        self.add_contour('person-legs', *('person-legs-1', 'person-legs-2', 'person-legs-3'), closed=False)
        self.add_contour('door-top', *('door-top-1', 'door-top-2', 'door-top-3'), closed=False)
        self.relate('connect', *('person-body', 'person-arms'))
        self.relate('connect', *('person-body', 'person-legs'))
        self.relate('connect', *('door-bottom', 'person-arms'))

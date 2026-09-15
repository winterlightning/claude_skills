# Refinement: Lower the squat hips and belt together to open both shoulder-to-belly gaps.
# Refinement: Raise the hands fully above the squat hip line.
# Repair: Lift both outstretched hands away from the squat thighs symmetrically.
"""Sumo wrestler: retain the topknot, broad belly, loincloth and squat. Radius5 head(24,13); shoulder edges(19,25) and(29,25) are each exactly13 from the center, leaving4 painted clearance. Both body edges lead away from the head. Source and full_body_ref.png inspected; mirror the stance about x24.

Sumo Wrestler, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9ed19462-8339-482a-a209-2c66f9e595f9'
SOURCE_PATH = 'pictographic-primitives/sports/sumo_9ed19462-8339-482a-a209-2c66f9e595f9.svg'
AUTHOR = 'gpt-6'

class SumoWrestler(Solo48):
    icon_id = 'sumo-wrestler'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('sumo', 'wrestler', 'wrestling', 'athlete', 'combat', 'sport')

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
        """Sumo wrestler: retain the topknot, broad belly, loincloth and squat. Radius5 head(24,13); shoulder edges(19,25) and(29,25) are each exactly13 from the center, leaving4 painted clearance. Both body edges lead away from the head. Source and full_body_ref.png inspected; mirror the stance about x24."""
        self.add_arc('head-r', (24, 8), (24, 18), radius_x=5)
        self.add_arc('head-l', (24, 18), (24, 8), radius_x=5)
        self.add_contour('head', 'head-r', 'head-l', closed=True)
        self.add_line('topknot', (24, 6), (24, 8))
        self.relate('connect', 'head', 'topknot')
        self.branches([('body', [(19, 25), (14, 33), (20, 33), (28, 33), (34, 33), (29, 25)]), ('left-arm', [(19, 25), (6, 22)]), ('right-arm', [(29, 25), (42, 22)]), ('left-leg', [(14, 33), (10, 37), (10, 42)]), ('right-leg', [(34, 33), (38, 37), (38, 42)]), ('belt', [(20, 33), (20, 41), (28, 41), (28, 33)])])
        self.mark_human_figure('person', head='head', torso='body-0', torso_junction='start')

# Follow-up review: Lucide flame: broad connected counter; preserve three pointed tongues and both brick courses. HRECT_L centerline extremes (4,8)-(44,40).
# Variant of brick-firewall-v2; parent file remains unchanged.
"""A flame rises from a staggered brick wall. Three masonry courses reduce to two, retaining alternating joints and the flame silhouette. Lucide flame informs the outer curved lobe; deliberate flame asymmetry preserves the tongues.
SOLO48 HRECT_L, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '31873389-9f53-4271-a274-ace8612680cd'
SOURCE_PATH = 'pictographic-primitives/programing/firewall_31873389-9f53-4271-a274-ace8612680cd.svg'
AUTHOR = 'gpt-6'

class BrickFirewall(Solo48):
    icon_id = 'brick-firewall'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/programming'
    aliases = ()
    keywords = ('firewall', 'fire', 'flame', 'wall', 'bricks', 'security', 'network', 'protection')

    def build(self) -> None:

        def ring(name, x, y, r):
            self.add_arc(name + '-right', (x, y - r), (x, y + r), radius_x=r)
            self.add_arc(name + '-left', (x, y + r), (x, y - r), radius_x=r)
            self.add_contour(name, name + '-right', name + '-left', closed=True)

        def node(name, x, y, w, h):
            self.add_polyline(name, (x, y), (x + w // 2, y), (x + w, y), (x + w, y + h), (x + w // 2, y + h), (x, y + h), closed=True)

        def join(*names):
            from itertools import combinations
            for a, b in combinations(names, 2):
                self.relate('connect', a, b)
        self.add_polyline('wall', (4, 24), (16, 24), (32, 24), (44, 24), (44, 32), (44, 40), (24, 40), (4, 40), (4, 32), closed=True)
        self.add_polyline('course', (4, 32), (16, 32), (24, 32), (32, 32), (44, 32))
        join('wall', 'course')
        for x in (16, 32):
            self.add_line(f'upper-joint-{x}', (x, 24), (x, 32))
            join(f'upper-joint-{x}', 'wall')
            join(f'upper-joint-{x}', 'course')
        self.add_line('lower-joint', (24, 32), (24, 40))
        join('lower-joint', 'wall')
        join('lower-joint', 'course')
        self.add_arc('flame-left', (16, 24), (14, 18), radius_x=10)
        tongue_points = ((14, 18), (18, 12), (20, 16), (28, 8), (32, 16), (38, 12))
        for i, (a, b) in enumerate(zip(tongue_points, tongue_points[1:]), 1):
            self.add_line(f'flame-tongues-{i}', a, b)
        self.add_arc('flame-right', (38, 12), (32, 24), radius_x=10)
        self.add_contour('flame', 'flame-left', 'flame-tongues-1', 'flame-tongues-2', 'flame-tongues-3', 'flame-tongues-4', 'flame-tongues-5', 'flame-right')
        join('wall', 'flame')

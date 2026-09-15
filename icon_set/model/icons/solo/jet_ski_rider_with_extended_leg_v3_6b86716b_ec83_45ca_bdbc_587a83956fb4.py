"""Jet ski: replace the disconnected zigzag with an identifiable shoulder, curved torso, one planted leg and one rearward extended leg. Radius5 head (22,11), shoulder (22,24), exact4 ink gap; upper torso vertical tangent. Original jet-ski pose and full_body_ref.png inspected; coherent Lucide sailboat hull construction supports equipment simplification.

Jet ski: replace the disconnected zigzag with an identifiable shoulder, curved torso, one planted leg and one rearward extended leg. Radius5 head (22,11), shoulder (22,24), exact4 ink gap; upper torso vertical tangent. Original jet-ski pose and full_body_ref.png inspected; coherent Lucide sailboat hull construction supports equipment simplification.

Jet Ski Rider Jumping a Wave. Left-facing jet ski rider above a curling wave; rear leg extends behind the rider. Omit duplicate body outlines and extra wave crests.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide sailboat: unified side silhouette; person-standing: sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6b86716b-ec83-45ca-bdbc-587a83956fb4'
SOURCE_PATH = 'pictographic-primitives/recreation/sport jet skiing 1_6b86716b-ec83-45ca-bdbc-587a83956fb4.svg'
AUTHOR = 'gpt-6'

class JetSkiRiderWithExtendedLegVariant3(Solo48):
    icon_id = 'jet-ski-rider-with-extended-leg-v3'
    variant_of = 'jet-ski-rider-with-extended-leg-v2'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/recreation'
    aliases = ()
    keywords = ('jet', 'ski', 'rider', 'with', 'extended', 'leg')

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
        """Jet ski: replace the disconnected zigzag with an identifiable shoulder, curved torso, one planted leg and one rearward extended leg. Radius5 head (22,11), shoulder (22,24), exact4 ink gap; upper torso vertical tangent. Original jet-ski pose and full_body_ref.png inspected; coherent Lucide sailboat hull construction supports equipment simplification."""
        self.ring('head', 22, 11, 5)
        self.add_bezier('torso', (22, 24), ((22, 27), (26, 29), (26, 32)))
        self.branches([('arm', [(22, 24), (14, 28), (6, 28)]), ('handle', [(6, 28), (6, 32)]), ('leg-down', [(26, 32), (23, 36)]), ('leg-extended', [(26, 32), (34, 30), (42, 30)]), ('hull', [(6, 32), (14, 34), (23, 36), (38, 39)]), ('water', [(6, 42), (10, 42)])])
        for part in ['arm-0', 'leg-down-0', 'leg-extended-0']:
            self.relate('connect', 'torso', part)

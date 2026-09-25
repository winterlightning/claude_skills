"""Jet-ski rider: reconstruct a complete hull, actual handlebar grip, planted foot and visibly extended rear leg. Radius5 head (19,11), shoulder(24,23), squared separation169 gives exact4 painted clearance. Upper torso tangent follows the forward lean. Source extended-leg rider and updated full_body_ref.png inspected; omit secondary water marks to give the craft and rider room instead of collapsing the limbs. Lucide sailboat informs coherent hull joins.

Jet-ski rider: reconstruct a complete hull, actual handlebar grip, planted foot and visibly extended rear leg. Radius5 head (19,11), shoulder(24,23), squared separation169 gives exact4 painted clearance. Upper torso tangent follows the forward lean. Source extended-leg rider and updated full_body_ref.png inspected; omit secondary water marks to give the craft and rider room instead of collapsing the limbs. Lucide sailboat informs coherent hull joins.

Jet ski: replace the disconnected zigzag with an identifiable shoulder, curved torso, one planted leg and one rearward extended leg. Radius5 head (22,11), shoulder (22,24), exact4 ink gap; upper torso vertical tangent. Original jet-ski pose and full_body_ref.png inspected; coherent Lucide sailboat hull construction supports equipment simplification.

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

class JetSkiRiderWithExtendedLeg(Solo48):
    icon_id = 'jet-ski-rider-with-extended-leg'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'recreation'
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
        """Jet-ski rider: reconstruct a complete hull, actual handlebar grip, planted foot and visibly extended rear leg. Radius5 head (19,11), shoulder(24,23), squared separation169 gives exact4 painted clearance. Upper torso tangent follows the forward lean. Source extended-leg rider and updated full_body_ref.png inspected; omit secondary water marks to give the craft and rider room instead of collapsing the limbs. Lucide sailboat informs coherent hull joins."""
        self.add_arc('head-a', (14, 11), (24, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('head-b', (24, 11), (14, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_bezier('torso', (24, 23), *(((26, 27), (29, 28), (32, 29)),))
        self.add_line('arm-0', (24, 23), (17, 26))
        self.add_line('arm-1', (17, 26), (6, 26))
        self.add_line('handle-0', (6, 26), (6, 34))
        self.add_line('planted-leg-0', (32, 29), (28, 34))
        self.add_line('extended-leg-0', (32, 29), (42, 24))
        self.add_line('deck-0', (6, 34), (28, 34))
        self.add_line('deck-1', (28, 34), (42, 34))
        self.add_line('stern-0', (42, 34), (42, 42))
        self.add_line('stern-1', (42, 42), (14, 42))
        self.add_arc('bow', (14, 42), (6, 34), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('arm', *('arm-0', 'arm-1'), closed=False)
        self.add_contour('deck', *('deck-0', 'deck-1'), closed=False)
        self.add_contour('stern', *('stern-0', 'stern-1'), closed=False)
        self.relate('connect', *('arm-0', 'arm-1'))
        self.relate('connect', *('arm-1', 'handle-0'))
        self.relate('connect', *('handle-0', 'deck-0'))
        self.relate('connect', *('planted-leg-0', 'extended-leg-0'))
        self.relate('connect', *('planted-leg-0', 'deck-0'))
        self.relate('connect', *('planted-leg-0', 'deck-1'))
        self.relate('connect', *('deck-0', 'deck-1'))
        self.relate('connect', *('deck-1', 'stern-0'))
        self.relate('connect', *('stern-0', 'stern-1'))
        self.relate('connect', *('bow', 'stern-1'))
        self.relate('connect', *('bow', 'deck-0'))
        self.relate('connect', *('bow', 'handle-0'))
        self.relate('connect', *('torso', 'arm-0'))
        self.relate('connect', *('torso', 'planted-leg-0'))
        self.relate('connect', *('torso', 'extended-leg-0'))

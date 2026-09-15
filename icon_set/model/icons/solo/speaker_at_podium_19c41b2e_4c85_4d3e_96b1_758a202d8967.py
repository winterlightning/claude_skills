"""Radius6 head (27,12), shoulders top26: exact4 painted clearance. Keep the microphone and podium, with a symmetric shoulder arch beneath the centered head.

Keep the podium and sash/microphone construction. Place the centered head at (27, 12) with radius5, exactly4 painted units above the existing shoulders. Shared full_body_ref.png bust vocabulary; preserve equipment asymmetry.

Speaker behind podium with bent microphone on the left. SQUARE extremes 6,6–42,42. Lucide user-round head and shoulders; microphone reduced to stem and angled head; offset speaker preserves space."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '19c41b2e-4c85-4d3e-96b1-758a202d8967'
SOURCE_PATH = 'pictographic-primitives/social/election speech 1_19c41b2e-4c85-4d3e-96b1-758a202d8967.svg'
AUTHOR = 'gpt-6'

class SpeakerAtPodium(Solo48):
    icon_id = 'speaker-at-podium'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/social'
    aliases = ()
    keywords = ('speaker', 'podium', 'microphone', 'speech', 'person', 'address')

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
        """Radius6 head (27,12), shoulders top26: exact4 painted clearance. Keep the microphone and podium, with a symmetric shoulder arch beneath the centered head."""
        self.ring('head', 27, 12, 6)
        self.add_arc('shoulders', (16, 32), (38, 32), radius_x=11, radius_y=6, large_arc=False, sweep=True)
        self.add_line('podium-1', (8, 42), (6, 32))
        self.add_line('podium-2', (6, 32), (42, 32))
        self.add_line('podium-3', (42, 32), (40, 42))
        self.add_line('microphone-1', (10, 32), (6, 21))
        self.add_line('microphone-2', (6, 21), (12, 15))
        self.add_contour('podium', *('podium-1', 'podium-2', 'podium-3'), closed=False)
        self.add_contour('microphone', *('microphone-1', 'microphone-2'), closed=False)
        self.relate('connect', *('shoulders', 'podium'))
        self.relate('connect', *('microphone', 'podium'))

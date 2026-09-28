"""Centered radius5 head (24,9), shoulder top22: exact4 painted gap. Smooth shared shoulder curves preserve the sashed podium speaker and VRECT_L envelope.

Keep the podium and sash/microphone construction. Place the centered head at (24, 10) with radius5, exactly4 painted units above the existing shoulders. Shared full_body_ref.png bust vocabulary; preserve equipment asymmetry.

Frontal sashed speaker behind a lectern. VRECT_XL extremes 8,4–40,44. Lucide user-round circular head and mirrored shoulder arcs; reduce sash to diagonal band edge."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f701cb6e-f3f6-46f0-b896-7436b770c007'
SOURCE_PATH = 'pictographic-primitives/social/election politician podium man_f701cb6e-f3f6-46f0-b896-7436b770c007.svg'
AUTHOR = 'gpt-6'

class SashedSpeakerAtPodium(Solo48):
    icon_id = 'sashed-speaker-at-podium'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'social'
    categories = ('social', 'primitives')
    aliases = ()
    keywords = ('person', 'speaker', 'podium', 'sash', 'politician', 'election')

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
        """Centered radius5 head (24,9), shoulder top22: exact4 painted gap. Smooth shared shoulder curves preserve the sashed podium speaker and VRECT_L envelope."""
        self.ring('head', 24, 9, 5)
        self.add_bezier('shoulder-left', (12, 34), *(((12, 27), (15, 22), (20, 22)),))
        self.add_line('shoulder-top', (20, 22), (28, 22))
        self.add_bezier('shoulder-right', (28, 22), *(((33, 22), (36, 27), (36, 34)),))
        self.add_line('podium-1', (8, 44), (8, 34))
        self.add_line('podium-2', (8, 34), (12, 34))
        self.add_line('podium-3', (12, 34), (36, 34))
        self.add_line('podium-4', (36, 34), (40, 34))
        self.add_line('podium-5', (40, 34), (40, 44))
        self.add_line('sash', (28, 22), (16, 34))
        self.add_contour('body', *('shoulder-left', 'shoulder-top', 'shoulder-right'), closed=False)
        self.add_contour('podium', *('podium-1', 'podium-2', 'podium-3', 'podium-4', 'podium-5'), closed=False)
        self.relate('connect', *('body', 'podium'))
        self.relate('connect', *('body', 'sash'))
        self.relate('connect', *('sash', 'podium'))

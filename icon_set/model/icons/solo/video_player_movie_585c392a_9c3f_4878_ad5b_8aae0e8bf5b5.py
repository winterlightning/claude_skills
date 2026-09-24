"""video player movie: repaired SOLO48 composition.
Plan: Closed playback triangle and matching frame corners.
Keyshape: VRECT_L reserves room for both player rails.
Reduction: No components omitted; play triangle widened.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '585c392a-9c3f-4878-ad5b-8aae0e8bf5b5'
SOURCE_PATH = 'pictographic-primitives/video/video player movie_585c392a-9c3f-4878-ad5b-8aae0e8bf5b5.svg'
AUTHOR = "gpt-6"
CONSTRUCTION_REFERENCES = 'square-play, monitor'

class Drawing(Solo48):
    icon_id = 'video-player-movie'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('video', 'player', 'movie')

    def box(self, n, x, y, w, h, r=3):
        pts = [(x + r, y), (x + w - r, y), (x + w, y + r), (x + w, y + h - r), (x + w - r, y + h), (x + r, y + h), (x, y + h - r), (x, y + r)]
        nodes = {'player': [(8, 12), (40, 12), (8, 36), (40, 36)]}.get(n, [])
        members = []
        for (i, a) in enumerate(pts):
            z = pts[(i + 1) % 8]
            if i % 2:
                part = n + str(i)
                self.add_arc(part, a, z, radius_x=r)
                members.append(part)
            else:
                inner = [p for p in nodes if p != a and p != z and ((z[0] - a[0]) * (p[1] - a[1]) == (z[1] - a[1]) * (p[0] - a[0])) and (min(a[0], z[0]) <= p[0] <= max(a[0], z[0])) and (min(a[1], z[1]) <= p[1] <= max(a[1], z[1]))]
                inner.sort(key=lambda p: (p[0] - a[0]) ** 2 + (p[1] - a[1]) ** 2)
                chain = [a] + inner + [z]
                for (j, (u, v)) in enumerate(zip(chain, chain[1:])):
                    part = n + str(i) + '-' + str(j)
                    self.add_line(part, u, v)
                    members.append(part)
        self.add_contour(n, *members, closed=True)

    def play(self, x, y, w, h):
        self.add_polyline('play', (x, y), (x + w, y + h // 2), (x, y + h), closed=True)

    def build(self):
        self.box('player', 8, 4, 32, 40, 3)
        for (i, y) in enumerate((12, 36)):
            self.add_line('rail-' + str(i), (8, y), (40, y))
            self.relate('connect', 'player', 'rail-' + str(i))
        self.play(17, 20, 14, 8)

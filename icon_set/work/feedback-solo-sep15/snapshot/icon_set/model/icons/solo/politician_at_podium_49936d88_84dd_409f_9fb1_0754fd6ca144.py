"""Keep the podium and sash/microphone construction. Place the centered head at (24, 11) with radius5, exactly4 painted units above the existing shoulders. Shared full_body_ref.png bust vocabulary; preserve equipment asymmetry.

Lucide user-round informs head and shoulders; broad podium and one sash stroke retained."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '49936d88-84dd-409f-9fb1-0754fd6ca144'
SOURCE_PATH = 'pictographic-primitives/school-learning/election politician podium neutral_49936d88-84dd-409f-9fb1-0754fd6ca144.svg'
AUTHOR = 'gpt-6'

class PoliticianAtPodium(Solo48):
    icon_id = 'politician-at-podium'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'society/elections'
    aliases = ()
    keywords = ('politician', 'podium', 'speech', 'sash', 'person', 'election')

    def circle(self, name, x, y, r):
        pts = [(x, y - r), (x + r, y), (x, y + r), (x - r, y), (x, y - r)]
        ids = []
        for j, (a, b) in enumerate(zip(pts, pts[1:])):
            eid = name + '-' + str(j)
            self.add_arc(eid, a, b, radius_x=r)
            ids.append(eid)
        self.add_contour(name, *ids, closed=True)

    def bust(self, name, x, y, r=2, width=5):
        self.circle(name + '-head', x, y, r)
        self.add_arc(name + '-sl', (x - width, y + 7), (x, y + r), radius_x=width, radius_y=7 - r)
        self.add_arc(name + '-sr', (x, y + r), (x + width, y + 7), radius_x=width, radius_y=7 - r)
        self.add_contour(name + '-shoulders', name + '-sl', name + '-sr')
        self.relate('connect', name + '-head', name + '-shoulders')

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
        """Keep the podium and sash/microphone construction. Place the centered head at (24, 11) with radius5, exactly4 painted units above the existing shoulders. Shared full_body_ref.png bust vocabulary; preserve equipment asymmetry."""
        self.ring('head', 24, 11, 5)
        self.add_arc('shoulder-left', (12, 32), (20, 24), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('shoulder-top', (20, 24), (28, 24))
        self.add_arc('shoulder-right', (28, 24), (36, 32), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('ledge-1', (6, 32), (12, 32))
        self.add_line('ledge-2', (12, 32), (36, 32))
        self.add_line('ledge-3', (36, 32), (42, 32))
        self.add_line('sash', (28, 24), (20, 32))
        self.add_line('leg-left', (12, 32), (14, 42))
        self.add_line('leg-right', (36, 32), (34, 42))
        self.add_contour('shoulders', *('shoulder-left', 'shoulder-top', 'shoulder-right'), closed=False)
        self.add_contour('ledge', *('ledge-1', 'ledge-2', 'ledge-3'), closed=False)
        self.relate('connect', *('sash', 'shoulders'))
        self.relate('connect', *('sash', 'ledge'))
        self.relate('connect', *('shoulders', 'ledge'))
        self.relate('connect', *('leg-left', 'ledge'))
        self.relate('connect', *('leg-left', 'shoulders'))
        self.relate('connect', *('leg-right', 'ledge'))
        self.relate('connect', *('leg-right', 'shoulders'))

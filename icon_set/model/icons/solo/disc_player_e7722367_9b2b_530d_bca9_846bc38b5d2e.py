"""Replace the hub ring with a dot at the exact disc center (24,21). Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e7722367-9b2b-530d-bca9-846bc38b5d2e'
SOURCE_PATH = 'pictographic-primitives/video/video player device_e7722367-9b2b-530d-bca9-846bc38b5d2e.svg'
AUTHOR = 'gpt-6'

class DiscPlayer(Solo48):
    icon_id = 'disc-player'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    aliases = ()
    keywords = ('disc', 'player', 'dvd', 'cd', 'media', 'device', 'video')

    def circle(self, name, cx, cy, r):
        self.add_arc(name + '-top', (cx - r, cy), (cx + r, cy), radius_x=r)
        self.add_arc(name + '-bottom', (cx + r, cy), (cx - r, cy), radius_x=r)
        self.add_contour(name, name + '-top', name + '-bottom', closed=True)

    def rounded(self, name, x, y, w, h, r):
        pts = [(x + r, y), (x + w - r, y), (x + w, y + r), (x + w, y + h - r), (x + w - r, y + h), (x + r, y + h), (x, y + h - r), (x, y + r)]
        ids = []
        for i, a in enumerate(pts):
            b = pts[(i + 1) % 8]
            ident = name + '-' + str(i)
            ids.append(ident)
            if i % 2:
                self.add_arc(ident, a, b, radius_x=r)
            else:
                self.add_line(ident, a, b)
        self.add_contour(name, *ids, closed=True)

    def build(self):
        """Symbol plan: Replace the hub ring with a dot at the exact disc center (24,21). Reference: Lucide disc: shared center for rim and hub."""
        self.add_arc('disc', (12, 30), (36, 30), radius_x=15, large_arc=True)
        self.add_dot('hub', (24, 21))
        self.add_line('top-left', (9, 30), (12, 30))
        self.add_line('top-middle', (12, 30), (36, 30))
        self.add_line('top-right', (36, 30), (39, 30))
        self.add_arc('tr', (39, 30), (42, 33), radius_x=3)
        self.add_line('right', (42, 33), (42, 35))
        self.add_arc('br', (42, 35), (39, 38), radius_x=3)
        self.add_line('bottom-right', (39, 38), (36, 38))
        self.add_line('bottom-middle', (36, 38), (12, 38))
        self.add_line('bottom-left', (12, 38), (9, 38))
        self.add_arc('bl', (9, 38), (6, 35), radius_x=3)
        self.add_line('left', (6, 35), (6, 33))
        self.add_arc('tl', (6, 33), (9, 30), radius_x=3)
        self.add_contour('player', 'top-left', 'top-middle', 'top-right', 'tr', 'right', 'br', 'bottom-right', 'bottom-middle', 'bottom-left', 'bl', 'left', 'tl', closed=True)
        for part in ['top-left', 'top-middle', 'top-right']:
            self.relate('connect', 'disc', part)
        for label, x, parts in [('left', 12, ['bottom-left', 'bottom-middle']), ('right', 36, ['bottom-right', 'bottom-middle'])]:
            self.add_line(label + '-foot', (x, 38), (x, 42))
            for part in parts:
                self.relate('connect', label + '-foot', part)

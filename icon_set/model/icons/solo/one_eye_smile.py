"""One eye smile (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '18e73746-a8ab-59ae-9a0b-eaa957c620bb'
SOURCE_PATH = 'pictographic-primitives/smileys/one eye smile_18e73746-a8ab-59ae-9a0b-eaa957c620bb.svg'
AUTHOR = 'gpt-6'

class OneEyeSmile(Solo48):
    icon_id = 'one-eye-smile'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('one', 'eye', 'smile', 'smileys')

    def _circle(self, name, x, y, r, ry=None):
        ry = r if ry is None else ry
        self.add_arc(name + '-a', (x - r, y), (x + r, y), radius_x=r, radius_y=ry)
        self.add_arc(name + '-b', (x + r, y), (x - r, y), radius_x=r, radius_y=ry)
        self.add_contour(name, name + '-a', name + '-b', closed=True)

    def _path(self, name, start, parts, closed=False):
        ids = []
        p = start
        for j, s in enumerate(parts):
            i = f'{name}-{j}'
            q = s[1]
            if s[0] == 'L':
                self.add_line(i, p, q)
            else:
                self.add_arc(i, p, q, radius_x=s[2], radius_y=s[3], sweep=s[4])
            ids.append(i)
            p = q
        self.add_contour(name, *ids, closed=closed)

    def build(self):
        self._circle('face', 24, 24, 20)
        self._circle('eye', 19, 19, 4)
        self.add_polyline('wink', (33, 17), (31, 20), (33, 23))
        self.add_arc('smile', (16, 32), (32, 32), radius_x=10, radius_y=4, sweep=False)

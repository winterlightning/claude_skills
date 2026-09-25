"""Power outlet type m (electronics), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '68088998-e38f-468c-abce-f0acea61ead3'
SOURCE_PATH = 'pictographic-primitives/electronics/power outlet type m_68088998-e38f-468c-abce-f0acea61ead3.svg'
AUTHOR = 'gpt-6'

class PowerOutletTypeM(Solo48):
    icon_id = 'power-outlet-type-m'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    categories = ('electronics', 'primitives')
    aliases = ()
    keywords = ('power', 'outlet', 'type', 'm', 'electronics')

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
        self._circle('case', 24, 24, 20)
        for n, x, y in [('earth', 24, 16), ('left', 16, 28), ('right', 32, 28)]:
            self._circle(n, x, y, 3)

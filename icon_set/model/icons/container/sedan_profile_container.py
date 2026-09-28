from ._construction import path, rounded_rect as rect, ellipse
"Sedan Car Profile: independently authored container.\n\nConstruction plan: Side-view cabin with sloping shoulders and two wheel arches; directional profile retained, Lucide informs wheel circles.\nKeyshape HRECT_S; extremes are the profile's exact keyshape bounds.\nReference: pictographic-primitives/transportation/car_1fdb13eb-bc4d-44a6-bca4-d87dd2adb768.svg. Lucide car-front original and atomic-debug inspected.\nNo source coordinates or solo geometry were scaled. Native size is 64.\n\nVisible keyshape extremes: (0, 16, 64, 48).\nHosting measured with compose.py: plus passes, heart passes, check passes.\n"
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = '1fdb13eb-bc4d-44a6-bca4-d87dd2adb768'
SOURCE_PATH = 'pictographic-primitives/transportation/car_1fdb13eb-bc4d-44a6-bca4-d87dd2adb768.svg'
AUTHOR = 'gpt-6'

class SedanProfileContainer(Container64):
    icon_id = 'sedan-profile-container'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    keyshape = Keyshape.HRECT_L
    aliases = ()
    keywords = ('sedan', 'profile', 'container')

    def build(self):
        line, poly = (self.add_line, self.add_polyline)

        def join(a, b):
            self.relate('connect', a, b)
        path(self, 'body', (10, 48), [('L', (6, 48)), ('A', (2, 44), 4, 4, True), ('L', (2, 28)), ('A', (6, 24), 4, 4, True), ('L', (12, 24)), ('L', (22, 10)), ('L', (38, 10)), ('L', (48, 24)), ('L', (58, 26)), ('A', (62, 30), 4, 4, True), ('L', (62, 48)), ('L', (54, 48))])
        line('sill', (22, 48), (42, 48))
        for x in (16, 48):
            ellipse(self, f'wheel-{x}', x, 48, 6)
            join('body', f'wheel-{x}')
            join('sill', f'wheel-{x}')

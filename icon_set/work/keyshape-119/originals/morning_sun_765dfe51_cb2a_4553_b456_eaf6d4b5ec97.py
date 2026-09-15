"""A broad semicircular arc rises from a straight horizon, with a small circular sun interrupting its upper-right side. Short rays surround the sun and an upright mark stands above the arc.

Dropped minor rays; preserved the sun on its respective side of the daylight arc.
Construction reference: Lucide sun: centered circle; daylight arc deliberately interrupted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '765dfe51-cb2a-4553-b456-eaf6d4b5ec97'
SOURCE_PATH = 'pictographic-primitives/weather/day morning_765dfe51-cb2a-4553-b456-eaf6d4b5ec97.svg'
AUTHOR = 'gpt-6'

class MorningSun(Solo48):
    icon_id = 'morning-sun'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('morning', 'sun', 'daylight', 'horizon', 'dawn', 'weather')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_arc('sun-top', (28, 16), (42, 16), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('sun-bottom', (42, 16), (28, 16), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_contour('sun', 'sun-top', 'sun-bottom', closed=True)
        self.add_arc('day-arc', (6, 40), (18, 22), radius_x=16, radius_y=18, sweep=True, large_arc=False)
        self.add_line('horizon', (6, 40), (42, 40))
        self.relate("connect", 'day-arc', 'horizon')

"""An open-bottom sun has a rounded crown and five short rays extending upward and sideways. Three straight horizontal fog bands lie below it, with slightly staggered lengths.

Reduced rays to three and reflection/fog to two lines; central vertical symmetry.
Construction reference: Lucide sun and sunrise: semicircular sun and detached ray marks.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30d98354-a12f-456c-96ae-4ebb052e5a63'
SOURCE_PATH = 'pictographic-primitives/weather/mist sun_30d98354-a12f-456c-96ae-4ebb052e5a63.svg'
AUTHOR = 'gpt-6'

class SunFog(Solo48):
    icon_id = 'sun-fog'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    aliases = ()
    keywords = ('sun', 'fog', 'mist', 'haze', 'weather', 'daylight')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_arc('sun', (10, 22), (38, 22), radius_x=14, radius_y=14, sweep=True, large_arc=False)
        self.add_line('horizon', (4, 32), (44, 32))
        self.add_line('reflection', (16, 40), (32, 40))

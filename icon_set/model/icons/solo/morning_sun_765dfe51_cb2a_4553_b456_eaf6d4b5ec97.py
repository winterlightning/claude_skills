'Morning sun: a round rising sun above the curved horizon, with exact HRECT_L extent.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '765dfe51-cb2a-4553-b456-eaf6d4b5ec97'
SOURCE_PATH = 'pictographic-primitives/weather/day morning_765dfe51-cb2a-4553-b456-eaf6d4b5ec97.svg'
AUTHOR = 'gpt-6'

class MorningSun(Solo48):
    icon_id = 'morning-sun'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    categories = ("weather", "primitives")
    aliases = ()
    keywords = ('morning', 'sun', 'daylight', 'horizon', 'dawn', 'weather')

    def build(self) -> None:
        self.add_arc('sun-top', (28,16), (44,16), radius_x=8, radius_y=8)
        self.add_arc('sun-bottom', (44,16), (28,16), radius_x=8, radius_y=8)
        self.add_contour('sun', 'sun-top', 'sun-bottom', closed=True)

        self.add_bezier('day-arc',(4,40),((4,32),(10,25),(17,23)))
        self.add_line('horizon',(4,40),(44,40))
        self.relate('connect','day-arc','horizon')

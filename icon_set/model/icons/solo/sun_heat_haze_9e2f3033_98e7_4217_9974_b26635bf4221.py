"""An open-bottom sun with short outward rays sits above three wavy horizontal bands. The lower bands become shorter, forming a tapered stack beneath the rounded sun.

Removed small rays and the smallest haze band; retained sun and wavy heat bands.
Construction reference: Lucide sun: simple round solar crown; repeated tangent wave pattern.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9e2f3033-98e7-4217-9974-b26635bf4221'
SOURCE_PATH = 'pictographic-primitives/weather/heat wax seal_9e2f3033-98e7-4217-9974-b26635bf4221.svg'
AUTHOR = 'gpt-6'

class SunHeatHaze(Solo48):
    icon_id = 'sun-heat-haze'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    aliases = ()
    keywords = ('sun', 'heat', 'haze', 'hot', 'weather', 'climate')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_bezier('sun',(12, 20),*(((11.5, 13.372583), (17.372583, 8.0), (24.0, 8)), ((30.627417, 8), (36.5, 13.372583), (36, 20))))
        self.add_bezier('haze-0-a',(4, 29),*(((6.08858053, 29.34499033), (10.45846765, 29.56411011), (15.0, 29.56411011)), ((18.83322588, 29.56411011), (22.32913558, 29.34499033), (24, 29))))
        self.add_bezier('haze-0-b',(24, 29),*(((25.67086442, 28.65500967), (29.16677412, 28.43588989), (33.0, 28.43588989)), ((37.54153235, 28.43588989), (41.91141947, 28.65500967), (44, 29))))
        self.add_arc('haze-1-a',(4,39),(24,39),radius_x=10,radius_y=1,sweep=False)
        self.add_arc('haze-1-b',(24,39),(44,39),radius_x=10,radius_y=1)
        self.add_contour('haze-0',*('haze-0-a', 'haze-0-b'),closed=False)
        self.add_contour('haze-1',*('haze-1-a', 'haze-1-b'),closed=False)

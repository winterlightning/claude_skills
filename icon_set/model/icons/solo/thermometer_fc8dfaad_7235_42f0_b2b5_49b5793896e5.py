"""An upright thermometer has a narrow rounded stem widening into a circular bulb at the bottom. A thin internal column rises from a small round reservoir within the bulb.

Widened stem and bulb; omitted inner reservoir circle, preserving the temperature column.
Construction reference: Lucide thermometer: rounded stem flows into enlarged bulb.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fc8dfaad-7235-42f0-b2b5-49b5793896e5'
SOURCE_PATH = 'pictographic-primitives/weather/temperature thermometer_fc8dfaad-7235-42f0-b2b5-49b5793896e5.svg'
AUTHOR = 'gpt-6'

class Thermometer(Solo48):
    icon_id = 'thermometer'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    aliases = ()
    keywords = ('thermometer', 'temperature', 'heat', 'cold', 'measurement', 'weather')

    def build(self) -> None:
        # Live VRECT_XL visible bounds: (6, 2, 42, 46).
        self.add_arc('cap', (15, 13), (33, 13), radius_x=9, radius_y=9, sweep=True, large_arc=False)
        self.add_line('stem-right', (33, 13), (33, 27))
        self.add_line('shoulder-right', (33, 27), (40, 35))
        self.add_arc('bulb', (40, 35), (8, 35), radius_x=16, radius_y=9, sweep=True, large_arc=False)
        self.add_line('shoulder-left', (8, 35), (15, 27))
        self.add_line('stem-left', (15, 27), (15, 13))
        self.add_contour('outline', 'cap', 'stem-right', 'shoulder-right', 'bulb', 'shoulder-left', 'stem-left', closed=True)
        self.add_line('column', (24, 15), (24, 35))

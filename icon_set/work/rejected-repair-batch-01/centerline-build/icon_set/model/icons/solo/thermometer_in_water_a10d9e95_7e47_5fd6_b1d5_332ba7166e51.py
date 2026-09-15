"""An upright thermometer with three scale marks and water below. SQUARE ink (6,6)-(42,42). Lucide thermometer informed the round bulb; two small crests and a broader lower wave preserve the coolant symbol."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a10d9e95-7e47-5fd6-b1d5-332ba7166e51'
SOURCE_PATH = 'pictographic-primitives/transportation/buoy_a10d9e95-7e47-5fd6-b1d5-332ba7166e51.svg'
SOURCE_REFERENCES = (('a10d9e95-7e47-5fd6-b1d5-332ba7166e51', 'pictographic-primitives/transportation/buoy_a10d9e95-7e47-5fd6-b1d5-332ba7166e51.svg'),)
AUTHOR = 'gpt-6'

class ThermometerInWater(Solo48):
    icon_id = 'thermometer-in-water'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('thermometer', 'coolant', 'temperature', 'water', 'warning', 'engine', 'dashboard', 'gauge')

    def build(self) -> None:
        self.add_polyline('stem',(24,6),(24,14),(24,22))
        self.add_arc('bulb-right',(24,22),(24,30),radius_x=4)
        self.add_arc('bulb-left',(24,30),(24,22),radius_x=4)
        self.add_contour('bulb','bulb-right','bulb-left',closed=True)
        self.relate('connect','stem','bulb')
        for i,y in enumerate((6,14,22)):
            self.add_line(f'scale-{i}',(24,y),(36-i*2,y))
            self.relate('connect',f'scale-{i}','stem')
        self.relate('connect','scale-2','bulb')
        for i,x in enumerate((6,36)):
            self.add_arc(f'crest-{i}',(x,31),(x+6,31),radius_x=5,radius_y=5)
        self.add_arc('wave-left',(6,41),(24,41),radius_x=15,radius_y=5)
        self.add_arc('wave-right',(24,41),(42,41),radius_x=15,radius_y=5,sweep=False)
        self.add_contour('wave','wave-left','wave-right')

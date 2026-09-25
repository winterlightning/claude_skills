'Engine silhouette: deliberate mechanical corners with 8-unit inlet and cap clearances.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c52b8c01-47ae-59ce-bbfb-9594b8bcc540'
SOURCE_PATH = 'pictographic-primitives/transportation/car engine_c52b8c01-47ae-59ce-bbfb-9594b8bcc540.svg'
AUTHOR = 'gpt-6'

class CarEngineTransportation(Solo48):
    icon_id = 'car-engine-transportation'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('car', 'engine', 'transportation')

    def build(self):
        # Engine silhouette: deliberate mechanical corners with 8-unit inlet and cap clearances.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('engine',(12,24),(12,16),(28,16),(34,22),(44,22),(44,40),(22,40),(16,32),(4,32))
        l('intake',(4,20),(4,36))
        l('intake-top',(4,24),(12,24))
        link('connect','intake-top','intake')
        link('connect','intake-top','engine')
        link('connect','intake','engine')
        l('cap',(16,8),(28,8))
        l('cap-neck',(22,8),(22,16))
        link('connect','cap-neck','cap')
        link('connect','cap-neck','engine')

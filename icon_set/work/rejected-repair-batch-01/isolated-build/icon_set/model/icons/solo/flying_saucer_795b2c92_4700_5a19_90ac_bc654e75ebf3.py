"""flying-saucer: reconstructed from the supplied transportation reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '795b2c92-4700-5a19-90ac-bc654e75ebf3'
SOURCE_PATH = 'pictographic-primitives/transportation/ship_795b2c92-4700-5a19-90ac-bc654e75ebf3.svg'
AUTHOR = 'gpt-6'


class FlyingSaucer(Solo48):
    icon_id = 'flying-saucer'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('ufo', 'flying saucer', 'spaceship', 'alien', 'spacecraft', 'sci-fi', 'space', 'vehicle')

    def build(self) -> None:
        # Envelope repair: shared boundary nodes and cardinal curve extrema;
        # retain the subject, grid, stroke, and declared physical joins.

        # Dome and disc share two nodes; paired landing struts mirror around x=24.
        self.add_arc('dome',(14,18),(34,18),radius_x=10)
        self.add_line('disc-top',(14,18),(34,18))
        self.add_arc('disc-upper-right',(34,18),(44, 25),radius_x=10,radius_y=7)
        self.add_arc('disc-lower-right',(44, 25),(34,32),radius_x=10,radius_y=7)
        self.add_line('disc-bottom',(34,32),(14,32))
        self.add_arc('disc-lower-left',(14,32),(4, 25),radius_x=10,radius_y=7)
        self.add_arc('disc-upper-left',(4, 25),(14,18),radius_x=10,radius_y=7)
        self.add_contour('disc','disc-top','disc-upper-right','disc-lower-right','disc-bottom','disc-lower-left','disc-upper-left',closed=True)
        for part in ['disc-top','disc-upper-left','disc-upper-right']: self.relate('connect','dome',part)
        for side,x,end,arc in [('left',14,10,'disc-lower-left'),('right',34,38,'disc-lower-right')]:
            self.add_line('leg-'+side,(x,32),(end,40))
            self.relate('connect','leg-'+side,arc)
            self.relate('connect','leg-'+side,'disc-bottom')

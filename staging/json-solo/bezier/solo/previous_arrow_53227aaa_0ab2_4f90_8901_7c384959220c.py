"""Previous arrow (state), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '53227aaa-0ab2-4f90-8901-7c384959220c'
SOURCE_PATH = 'icons-json/state/previous arrow_53227aaa-0ab2-4f90-8901-7c384959220c.json'
AUTHOR = 'json_to_solo'

class PreviousArrowState(Solo48):
    icon_id = 'previous-arrow-state'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('previous', 'arrow', 'state')

    def build(self):
        self.add_line('e0', (16, 4), (8, 12))
        self.add_line('e1', (17, 20), (8, 12))
        self.add_line('e2', (20, 44), (25, 44))
        self.add_line('e3', (25, 12), (8, 12))
        self.add_bezier('e4', (25, 44), ((25.9, 44), (26.95, 43.664), (27.81, 43.427)), ((34.63, 41.564), (39.99, 35), (39.99, 28.491)), ((39.99, 28.41), (40, 28.339), (40, 28.258)), ((40, 28.257), (40, 28.256), (40, 28.255)), ((40, 27.936), (39.99, 27.627), (39.99, 27.309)), ((39.99, 20.982), (35.18, 14.909), (28.62, 12.927)), ((27.52, 12.6), (26.17, 12), (25, 12)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e4', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')

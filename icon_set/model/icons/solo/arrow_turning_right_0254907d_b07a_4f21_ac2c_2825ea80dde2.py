'An arrow rises from the lower left, bends smoothly right and ends in an open arrowhead. Square extremes (6,6)-(42,42) preserve its upright arrangement. Lucide corner-up-right contributes tangent-continuous elbow construction and shared arrow tip. One quarter-circle joins vertical and horizontal shaft runs; arrowhead arms mirror about y=16. No details omitted.'
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '0254907d-b07a-4f21-ac2c-2825ea80dde2'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/right turn 1_0254907d-b07a-4f21-ac2c-2825ea80dde2.svg'
AUTHOR = 'gpt-6-astra'
class Drawing(Solo48):
    icon_id = 'arrow-turning-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitive', 'primitives')
    aliases = ['Curved Right Turn Arrow']
    keywords = ['arrow', 'turning', 'right']
    def build(self):
        tip=(42,16)
        self.add_line('rise',(6,42),(6,30))
        self.add_arc('turn',(6,30),(20,16),radius_x=14)
        self.add_line('run',(20,16),tip)
        self.add_contour('shaft','rise','turn','run')
        self.add_polyline('point',(32,6),tip,(32,26))
        self.relate('connect','shaft','point')

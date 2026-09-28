"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '2a3f04f0-a404-41db-90b7-a6ee5813413b'
SOURCE_PATH = 'pictographic-primitives/symbol/messages bubble round heart_2a3f04f0-a404-41db-90b7-a6ee5813413b.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('oval speech bubble', 'lower-left pointed tail', 'outlined heart')

class Drawing(Sub32):
    icon_id = 'heart-speech-bubble-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    keywords = ('heart', 'speech', 'bubble')


    STROKE_WIDTH = 4
    PATH_STROKE_WIDTHS = {'frame': 4}
    COMPACT_EXCEPTION = 'Complete source composition with uniform 4px strokes. Spacing and grid findings are retained for review.'
    def to_record(self):
        record=super().to_record()
        record['style']['path_stroke_widths']=dict(self.PATH_STROKE_WIDTHS)
        record['compact_exception']=self.COMPACT_EXCEPTION
        return record

    def build(self):
        # The rounded speech enclosure owns a distinct pointed lower-left tail.
        self.add_bezier('bubble-top',(7,23),((4,21),(2,18),(2,15)),((2,8),(8,2),(16,2)),((24,2),(30,8),(30,15)),((30,22),(23,26),(16,26)),((14,26),(12,26),(11,25)))
        self.add_line('tail-1',(11,25),(4,30))
        self.add_line('tail-2',(4,30),(7,23))
        self.add_contour('frame','bubble-top','tail-1','tail-2',closed=True)
        self.add_bezier('heart',(16,11),((11,5),(6,11),(10,15)),((12,17),(14,19),(16,21)),((18,19),(20,17),(22,15)),((26,11),(21,5),(16,11)))


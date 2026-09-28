"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '6913cf31-3e4e-45e7-8c23-c3afd631eee3'
SOURCE_PATH = 'pictographic-primitives/war/shield skull_6913cf31-3e4e-45e7-8c23-c3afd631eee3.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('shield outline with curved top and pointed base', 'skull with open-bottom jaw', 'two eye dots', 'detached central jaw stroke')

class Drawing(Sub32):
    icon_id = 'skull-security-shield-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'war'
    categories = ('war', 'primitives')
    keywords = ('skull', 'security', 'protection', 'shield')
    STROKE_WIDTH = 4
    PATH_STROKE_WIDTHS = {'frame': 4}
    COMPACT_EXCEPTION = 'User requested uniform 4px strokes on a 32px canvas. Spacing and grid findings are retained for review.'
    def to_record(self):
        record=super().to_record()
        record['style']['path_stroke_widths']=dict(self.PATH_STROKE_WIDTHS)
        record['compact_exception']=self.COMPACT_EXCEPTION
        return record

    def build(self):
        self.add_bezier('shield',(2,5),((10,1),(22,1),(30,5)),((30,11),(30,16),(29,20)),((27,25),(21,28),(16,30)),((11,28),(5,25),(3,20)),((2,16),(2,11),(2,5)))
        self.add_contour('frame','shield',closed=True)
        self.skull(top=10,bottom=23,open_jaw=True)

    def skull(self,top=9,bottom=23,open_jaw=False):
        # Symmetric cranium, narrowing cheek/jaw contour, two eye dots and one
        # central jaw/tooth stroke. No nose or extra teeth are invented.
        self.add_bezier('cranium',(12,bottom),((12,bottom-1),(12,bottom-3),(11,bottom-3)),((8,bottom-4),(8,top+6),(9,top+3)),((10,top-1),(14,top-2),(16,top-2)),((18,top-2),(22,top-1),(23,top+3)),((24,top+6),(24,bottom-4),(21,bottom-3)),((20,bottom-3),(20,bottom-1),(20,bottom)))
        if not open_jaw:
            self.add_line('jaw-bottom',(20,bottom),(12,bottom))
            self.add_contour('skull','cranium','jaw-bottom',closed=True)
        self.add_dot('eye-left',(13,top+6))
        self.add_dot('eye-right',(19,top+6))
        self.add_line('tooth',(16,bottom-3),(16,bottom))
        if not open_jaw:self.relate('connect','tooth','jaw-bottom')


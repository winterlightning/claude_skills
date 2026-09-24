"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '8ef6cba7-fc72-409e-8c56-94c0f9bb6077'
SOURCE_PATH = 'pictographic-primitives/symbol/messages bubble square skull_8ef6cba7-fc72-409e-8c56-94c0f9bb6077.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('rounded rectangular speech bubble', 'lower-left tail', 'skull with closed jaw', 'two eye dots', 'one central jaw divider')

class Drawing(Sub32):
    icon_id = 'skull-speech-bubble-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    keywords = ('skull', 'speech', 'bubble')
    STROKE_WIDTH = 4
    PATH_STROKE_WIDTHS = {'frame': 4}
    COMPACT_EXCEPTION = 'User requested uniform 4px strokes on a 32px canvas. Spacing and grid findings are retained for review.'
    def to_record(self):
        record=super().to_record()
        record['style']['path_stroke_widths']=dict(self.PATH_STROKE_WIDTHS)
        record['compact_exception']=self.COMPACT_EXCEPTION
        return record

    def build(self):
        self.message()
        self.skull(top=10,bottom=21)

    def message(self):
        self.add_line('frame-top',(4,2),(28,2))
        self.add_arc('frame-tr',(28,2),(30,4),radius_x=2)
        self.add_line('frame-right',(30,4),(30,23))
        self.add_arc('frame-br',(30,23),(28,25),radius_x=2)
        tail=[(28,25),(15,25),(9,30),(9,25),(4,25)]
        for i,(a,b) in enumerate(zip(tail,tail[1:]),1):self.add_line(f'frame-tail-{i}',a,b)
        self.add_arc('frame-bl',(4,25),(2,23),radius_x=2)
        self.add_line('frame-left',(2,23),(2,4))
        self.add_arc('frame-tl',(2,4),(4,2),radius_x=2)
        self.add_contour('frame','frame-top','frame-tr','frame-right','frame-br',*[f'frame-tail-{i}' for i in range(1,5)],'frame-bl','frame-left','frame-tl',closed=True)

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


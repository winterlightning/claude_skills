"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '147e6d81-0d21-49c9-8726-0fadea0fff54'
SOURCE_PATH = 'pictographic-primitives/symbol/messages bubble with heart_147e6d81-0d21-49c9-8726-0fadea0fff54.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('rounded square speech bubble', 'lower-left tail', 'complete heart outline')

class Drawing(Sub32):
    icon_id = 'heart-square-message-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    keywords = ('message', 'bubble', 'with', 'heart')


    def build(self):
        self.message()
        self.add_bezier('heart',(16,11),((12,7),(8,11),(11,14)),((13,16),(14,17),(16,18)),((18,17),(19,16),(21,14)),((24,11),(20,7),(16,11)))

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


"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '692b5811-84ae-4db0-8d66-219feaafec3e'
SOURCE_PATH = 'pictographic-primitives/symbol/messages bubble square bitcoin_692b5811-84ae-4db0-8d66-219feaafec3e.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('rounded square speech bubble', 'lower-left tail', 'Bitcoin B with two bowls', 'two top and bottom currency ticks')

class Drawing(Sub32):
    icon_id = 'bitcoin-square-message-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    keywords = ('bitcoin', 'message', 'speech', 'bubble')


    def build(self):
        self.message()
        self.bitcoin()

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

    def bitcoin(self):
        # Two stacked bowls, left stem, two top/bottom currency ticks.
        self.add_line('b-top',(10,9),(17,9))
        self.add_bezier('b-bowls',(17,9),((24,9),(24,14),(17,14)),((25,14),(25,19),(17,19)))
        self.add_line('b-bottom',(17,19),(10,19))
        self.add_contour('b-outer','b-top','b-bowls','b-bottom')
        self.add_line('b-middle',(12,14),(17,14))
        self.add_line('stem',(12,7),(12,21))
        self.add_line('tick-top',(18,7),(18,9))
        self.add_line('tick-bottom',(18,19),(18,21))
        self.relate('connect','stem','b-top','b-bottom','b-middle')
        self.relate('connect','b-bowls','b-middle','tick-top','tick-bottom')


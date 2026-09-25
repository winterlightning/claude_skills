"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '1b6ce2a0-ce30-49ce-99cf-a772bb04245d'
SOURCE_PATH = 'pictographic-primitives/symbol/messages bubble round bitcoin_1b6ce2a0-ce30-49ce-99cf-a772bb04245d.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('oval speech bubble', 'lower-left tail', 'Bitcoin B with two bowls', 'two top and bottom currency ticks')

class Drawing(Sub32):
    icon_id = 'bitcoin-oval-message-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    keywords = ('bitcoin', 'speech', 'bubble')


    def build(self):
        self.oval_message()
        self.bitcoin()

    def oval_message(self):
        self.add_bezier('bubble',(7,23),((4,21),(2,18),(2,15)),((2,8),(8,2),(16,2)),((24,2),(30,8),(30,15)),((30,23),(23,27),(16,27)),((14,27),(12,26),(11,25)))
        self.add_line('tail-lower',(11,25),(4,30))
        self.add_line('tail-upper',(4,30),(7,23))
        self.add_contour('frame','bubble','tail-lower','tail-upper',closed=True)

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


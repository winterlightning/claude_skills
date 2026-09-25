"""House: A house has a pointed gable roof, short projecting eaves, and a rectangular body interrupted below by a rounded doorway. Generate this component alone; exclude Circle Frame.

Construction: A peaked roof projects over walls; an arched doorway interrupts the lower outline.
Keyshape: SQUARE; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '37b7d84a-3d3a-4e68-9fa0-db3c6d240895'
SOURCE_PATH = 'pictographic-primitives/state/house circle_37b7d84a-3d3a-4e68-9fa0-db3c6d240895.svg'
AUTHOR = 'gpt-6'


class HouseSub(Sub32):
    icon_id = 'house-sub'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('house', 'pointed', 'gable', 'roof', 'short', 'projecting', 'eaves', 'rectangular')

    def build(self):
        self.add_polyline('roof',(2,14),(16,2),(30,14))
        self.add_line('left-wall',(4,12),(4,28))
        self.add_arc('left-corner',(4,28),(6,30),radius_x=2,sweep=False)
        self.add_line('left-base',(6,30),(12,30))
        self.add_line('door-left',(12,30),(12,24))
        self.add_arc('door-top',(12,24),(20,24),radius_x=4)
        self.add_line('door-right',(20,24),(20,30))
        self.add_line('right-base',(20,30),(26,30))
        self.add_arc('right-corner',(26,30),(28,28),radius_x=2,sweep=False)
        self.add_line('right-wall',(28,28),(28,12))
        self.add_contour('house','left-wall','left-corner','left-base','door-left','door-top','door-right','right-base','right-corner','right-wall')
        self.relate('connect','roof','house')

"""A left-facing whale with a rounded body, raised tail and forked water spout."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2977768a-df8d-5260-854a-5df367e6906c'
SOURCE_PATH = 'pictographic-primitives/animals/whale body_2977768a-df8d-5260-854a-5df367e6906c.svg'
AUTHOR = 'gpt-6'


class WhaleWithSpout(Solo48):
    icon_id = 'whale-with-spout'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('whale', 'spout', 'water', 'sea', 'ocean', 'marine', 'tail', 'mammal')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_bezier('back', (6, 31), *(((6, 25.50920143), (9.85418684, 20.56542937), (16, 19)),))
        self.add_arc('saddle', (16, 19), (35, 24), radius_x=18, radius_y=18, large_arc=False, sweep=False)
        self.add_line('tail-neck', (35, 24), (36, 16))
        self.add_arc('tail-left', (36, 16), (34, 6), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_line('fluke-1', (34, 6), (40, 11))
        self.add_line('fluke-2', (40, 11), (42, 6))
        self.add_bezier('tail-right', (42, 6), *(((42, 10.28124692), (42, 14.71875308), (42, 19)),))
        self.add_arc('rump', (42, 19), (25, 42), radius_x=27, radius_y=27, large_arc=False, sweep=True)
        self.add_arc('belly', (25, 42), (6, 31), radius_x=23, radius_y=15, large_arc=False, sweep=True)
        self.add_line('eye', (15, 29), (15, 29))
        self.add_bezier('spray-left', (8, 6), *(((11.2325716, 6), (14.39737339, 7.16125546), (16, 10)),))
        self.add_bezier('spray-right', (16, 10), *(((17.60262661, 7.16125546), (20.7674284, 6), (24, 6)),))
        self.add_contour('whale', *('back', 'saddle', 'tail-neck', 'tail-left', 'fluke-1', 'fluke-2', 'tail-right', 'rump', 'belly'), closed=True)
        self.add_contour('spout', *('spray-left', 'spray-right'), closed=False)

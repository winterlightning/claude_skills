"""Equalizer (audio), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7b5f7ef4-2b7e-52f6-a1e1-348ac33fec76'
SOURCE_PATH = 'pictographic-primitives/audio/equalizer_7b5f7ef4-2b7e-52f6-a1e1-348ac33fec76.svg'
AUTHOR = 'gpt-6'

class Equalizer7b5f7ef4(Solo48):
    icon_id = 'equalizer-7b5f7ef4'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    categories = ('audio', 'primitives')
    aliases = ()
    keywords = ('equalizer', 'audio')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (40, 13), (40, 8))
        self.add_line('e1', (40, 21), (40, 39))
        self.add_line('e2', (8, 26), (8, 9))
        self.add_line('e3', (8, 40), (8, 34))
        self.add_line('e4', (24, 19), (24, 9))
        self.add_line('e5', (24, 27), (24, 40))
        self.add_arc('e6-top', (20, 23), (28, 23), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('e6-bottom', (28, 23), (20, 23), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('e7-top', (36, 16), (44, 16), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('e7-bottom', (44, 16), (36, 16), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('e8-top', (4, 31), (12, 31), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('e8-bottom', (12, 31), (4, 31), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e2',), closed=False)
        self.add_contour('c3', *('e3',), closed=False)
        self.add_contour('c4', *('e4',), closed=False)
        self.add_contour('c5', *('e5',), closed=False)
        self.add_contour('e7', *('e7-top', 'e7-bottom'), closed=True)
        self.add_contour('e8', *('e8-top', 'e8-bottom'), closed=True)
        self.add_contour('e6', *('e6-top', 'e6-bottom'), closed=True)
        self.relate('connect', *('c0', 'e7'))
        self.relate('connect', *('c1', 'e7'))
        self.relate('connect', *('c2', 'e8'))
        self.relate('connect', *('c3', 'e8'))
        self.relate('connect', *('c4', 'e6'))
        self.relate('connect', *('c5', 'e6'))

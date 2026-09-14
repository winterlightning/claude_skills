"""Microphone (audio), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '88610259-450b-43f2-85da-95879335b5f2'
SOURCE_PATH = 'icons-json/audio/microphone_88610259-450b-43f2-85da-95879335b5f2.json'
AUTHOR = 'gpt-6'

class Microphone88610259(Solo48):
    icon_id = 'microphone-88610259'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('microphone', 'audio')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (24, 44), (24, 39))
        self.add_line('e1', (15, 20), (15, 11))
        self.add_line('e2', (32, 12), (32, 22))
        self.add_arc('e3', (8, 26), (25, 39), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_arc('e4', (23, 38), (40, 25), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_arc('e5-1', (15, 11), (24, 4), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('e5-2', (24, 4), (32, 12), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('e6-1', (32, 22), (23, 29), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('e6-2', (23, 29), (15, 20), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_contour('c0', *('e3',), closed=False)
        self.add_contour('c1', *('e4',), closed=False)
        self.add_contour('c2', *('e0',), closed=False)
        self.add_contour('c3', *('e1', 'e5-1', 'e5-2', 'e2', 'e6-1', 'e6-2'), closed=True)
        self.relate('connect', *('c0', 'c1'))
        self.relate('connect', *('c2', 'c0'))
        self.relate('connect', *('c2', 'c1'))

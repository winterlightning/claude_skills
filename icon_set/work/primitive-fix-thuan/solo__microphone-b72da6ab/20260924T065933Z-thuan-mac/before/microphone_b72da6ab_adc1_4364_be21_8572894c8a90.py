"""Microphone (audio), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b72da6ab-adc1-4364-be21-8572894c8a90'
SOURCE_PATH = 'pictographic-primitives/audio/microphone_b72da6ab-adc1-4364-be21-8572894c8a90.svg'
AUTHOR = 'gpt-6'

class MicrophoneB72da6ab(Solo48):
    icon_id = 'microphone-b72da6ab'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('microphone', 'audio')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (16, 13), (21, 13))
        self.add_line('e1', (24, 39), (24, 44))
        self.add_line('e2', (16, 11), (16, 20))
        self.add_line('e3', (32, 21), (32, 11))
        self.add_line('e4-1', (8, 22), (8, 25))
        self.add_arc('e4-2', (8, 25), (11, 34), radius_x=18, radius_y=18, large_arc=False, sweep=False)
        self.add_arc('e4-3', (11, 34), (20, 41), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_arc('e4-4', (20, 41), (40, 26), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_arc('e4-5', (40, 26), (40, 23), radius_x=25, radius_y=25, large_arc=False, sweep=True)
        self.add_line('e5-1', (32, 11), (29, 6))
        self.add_arc('e5-2', (29, 6), (24, 4), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_arc('e5-3', (24, 4), (19, 6), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_arc('e5-4', (19, 6), (16, 11), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_arc('e6-1', (16, 20), (21, 28), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_arc('e6-2', (21, 28), (32, 21), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5'), closed=False)
        self.add_contour('c3', *('e5-1', 'e5-2', 'e5-3', 'e5-4', 'e2', 'e6-1', 'e6-2', 'e3'), closed=True)
        self.relate('connect', *('c0', 'c3'))
        self.relate('connect', *('c1', 'c2'))

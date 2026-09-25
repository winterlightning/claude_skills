"""tv control next: repaired SOLO48 composition.
Plan: Screen/stand junction and coherent triangular playback mark.
Keyshape: SQUARE reserves width for the triangle and stop bar.
Reduction: Screen corners squared to reserve the enlarged symbol clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '99b37bd2-37e1-42f8-b918-e34adc73280d'
SOURCE_PATH = 'pictographic-primitives/other/tv control next_99b37bd2-37e1-42f8-b918-e34adc73280d.svg'
AUTHOR = "gpt-6"
CONSTRUCTION_REFERENCES = 'monitor, square-play'

class Drawing(Solo48):
    icon_id = 'tv-control-next'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('tv', 'control', 'next')

    def build(self):
        self.add_polyline('screen', (6, 6), (42, 6), (42, 34), (24, 34), (6, 34), closed=True)
        self.add_line('stand', (24, 34), (24, 42))
        self.add_polyline('foot', (16, 42), (24, 42), (32, 42))
        self.relate('connect', 'screen', 'stand')
        self.relate('connect', 'stand', 'foot')
        self.add_polyline('play', (14, 14), (25, 20), (14, 26), closed=True)
        self.add_line('next-bar', (34, 14), (34, 26))

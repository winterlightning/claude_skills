"""tv control previous: repaired SOLO48 composition.
Plan: Screen/stand junction and coherent triangular playback mark.
Keyshape: SQUARE reserves width for the triangle and stop bar.
Reduction: Screen corners squared to reserve the enlarged symbol clearance.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '16b19145-212f-42bd-b9b5-ab0936754a35'
SOURCE_PATH = 'pictographic-primitives/other/tv control previous_16b19145-212f-42bd-b9b5-ab0936754a35.svg'
AUTHOR = "gpt-6"
CONSTRUCTION_REFERENCES = 'monitor, square-play'

class Drawing(Solo48):
    icon_id = 'tv-control-previous'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('tv', 'control', 'previous')

    def build(self):
        self.add_polyline('screen', (6, 6), (42, 6), (42, 34), (24, 34), (6, 34), closed=True)
        self.add_line('stand', (24, 34), (24, 42))
        self.add_polyline('foot', (16, 42), (24, 42), (32, 42))
        self.relate('connect', 'screen', 'stand')
        self.relate('connect', 'stand', 'foot')
        self.add_polyline('previous-triangle', (34, 14), (23, 20), (34, 26), closed=True)
        self.add_line('previous-bar', (14, 14), (14, 26))

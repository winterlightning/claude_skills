"""A long handle and flared mop skirt with two strands; collar and third strand omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0d6dd25a-6788-5c55-8749-cd5be70cf1e1'
SOURCE_PATH = 'pictographic-primitives/tools/floor mop wet_0d6dd25a-6788-5c55-8749-cd5be70cf1e1.svg'
AUTHOR = 'gpt-6'

class WetFloorMop(Solo48):
    icon_id = 'wet-floor-mop'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tools'
    categories = ('primitives', 'tools')
    aliases = ()
    keywords = ('mop', 'floor', 'cleaning', 'wet', 'wash', 'janitor', 'housekeeping', 'chores')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_line('handle', (24, 4), (24, 22))
        self.add_polyline('head', (24, 22), (15, 22), (8, 42), (40, 42), (33, 22), (24, 22))
        self.relate('connect', 'handle', 'head')
        for i, x in enumerate((19, 29)):
            self.add_line('strand' + str(i), (x, 33), (x, 44))
            self.relate('connect', 'strand' + str(i), 'head')

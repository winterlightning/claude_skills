"""A long handle and flared mop skirt with two strands; collar and third strand omitted."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0d6dd25a-6788-5c55-8749-cd5be70cf1e1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wet-floor-mop/20260927T145855Z-thuan-mac-1/reference/floor mop wet_0d6dd25a-6788-5c55-8749-cd5be70cf1e1.svg'
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
        self.add_polyline('head', (24, 22), (16, 22), (8, 42), (40, 42), (32, 22), (24, 22))
        self.relate('connect', 'handle', 'head')
        # The flared skirt carries the mop silhouette without crowded inner strands.

"""Independent 32px profile of angular-gear.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '8ce3c661-d221-45e9-90b3-0342f52ed76e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cog_8ce3c661-d221-45e9-90b3-0342f52ed76e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8ce3c661-d221-45e9-90b3-0342f52ed76e', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cog_8ce3c661-d221-45e9-90b3-0342f52ed76e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/angular-gear',)
SOLO_SOURCE_ICON_IDS = ('angular-gear',)
REFERENCE_EXPORT_SHA256 = '7802da3818f98233be9a5798d5aa8799bd463a1b1b324d855b3b446722903f5c'

class Drawing(Sub32):
    icon_id = 'angular-gear-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Eight angular teeth, small closed centre hole.
        self.add_polyline('gear', (19, 6), (17, 2), (15, 2), (13, 6), (11, 7), (7, 5), (5, 7), (7, 11), (6, 13), (2, 15), (2, 17), (6, 19), (7, 21), (5, 25), (7, 27), (11, 25), (13, 26), (15, 30), (17, 30), (19, 26), (21, 25), (25, 27), (27, 25), (25, 21), (26, 19), (30, 17), (30, 15), (26, 13), (25, 11), (27, 7), (25, 5), (21, 7), closed=True)
        self.add_arc('hole-top', (14, 16), (18, 16), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('hole-bottom', (18, 16), (14, 16), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('hole', 'hole-top', 'hole-bottom', closed=True)

"""Independent 32px profile of water-skier.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'a0a86c5e-f6ab-4aef-80ad-0ea729f25840'
SOURCE_PATH = 'pictographic-primitives/sports/skating_a0a86c5e-f6ab-4aef-80ad-0ea729f25840.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a0a86c5e-f6ab-4aef-80ad-0ea729f25840', 'pictographic-primitives/sports/skating_a0a86c5e-f6ab-4aef-80ad-0ea729f25840.svg'),)
PROFILE_SOURCE_KEYS = ('solo/water-skier',)
SOLO_SOURCE_ICON_IDS = ('water-skier',)
REFERENCE_EXPORT_SHA256 = 'f6760282f2933c613cc9c2d3a4de3112970eeb34c16fa176f58121184039cd12'

class Drawing(Sub32):
    icon_id = 'water-skier-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'sports'
    categories = ('sports', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Water skier: head dot, torso, arms holding the tow rope, legs on a ski with an upturned tip.
        self.add_arc('head-1', (6, 6), (10, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('head-2', (10, 6), (6, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('torso', (10, 16), (12, 22))
        self.add_polyline('rope', (10, 16), (20, 14), (30, 12))
        self.add_polyline('leg-back', (12, 22), (8, 25), (10, 28))
        self.add_line('ski', (2, 28), (24, 28))
        self.add_arc('tip', (24, 28), (30, 22), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_contour('ski-all', 'ski', 'tip')
        self.relate('connect', 'torso', 'rope')
        self.relate('connect', 'torso', 'leg-back')
        self.relate('connect', 'leg-back', 'ski-all')

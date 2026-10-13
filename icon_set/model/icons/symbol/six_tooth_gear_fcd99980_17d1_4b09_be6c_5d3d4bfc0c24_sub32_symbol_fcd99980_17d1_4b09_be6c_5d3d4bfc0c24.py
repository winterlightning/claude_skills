"""Independent 32px profile of six-tooth-gear-fcd99980-17d1-4b09-be6c-5d3d4bfc0c24.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'fcd99980-17d1-4b09-be6c-5d3d4bfc0c24'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cog_fcd99980-17d1-4b09-be6c-5d3d4bfc0c24.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fcd99980-17d1-4b09-be6c-5d3d4bfc0c24', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cog_fcd99980-17d1-4b09-be6c-5d3d4bfc0c24.svg'), ('fe49e273-5964-4f58-94cd-8a4c93927aa8', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cog_fe49e273-5964-4f58-94cd-8a4c93927aa8.svg'))
PROFILE_SOURCE_KEYS = ('solo/six-tooth-gear-fcd99980-17d1-4b09-be6c-5d3d4bfc0c24', 'solo/six-tooth-gear-fe49e273-5964-4f58-94cd-8a4c93927aa8')
SOLO_SOURCE_ICON_IDS = ('six-tooth-gear-fcd99980-17d1-4b09-be6c-5d3d4bfc0c24', 'six-tooth-gear-fe49e273-5964-4f58-94cd-8a4c93927aa8')
REFERENCE_EXPORT_SHA256 = 'beffb725677918e8916f986dfd03c6b483ed9ecd4ad14720739bac140e23a783'

class DrawingContainerSymbol(Sub32):
    icon_id = 'six-tooth-gear-fcd99980-17d1-4b09-be6c-5d3d4bfc0c24-sub32-symbol'
    related_origin_icon_id = 'six-tooth-gear-fcd99980-17d1-4b09-be6c-5d3d4bfc0c24-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/six-tooth-gear-fcd99980-17d1-4b09-be6c-5d3d4bfc0c24-sub32'
    counterpart_icon_id = 'six-tooth-gear-fcd99980-17d1-4b09-be6c-5d3d4bfc0c24-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Six trapezoid teeth that taper enough to keep the 4-unit rule, small closed centre hole.
        self.add_polyline('gear', (20, 6), (18, 2), (14, 2), (12, 6), (10, 7), (5, 7), (2, 11), (5, 15), (5, 17), (2, 21), (5, 25), (10, 25), (12, 26), (14, 30), (18, 30), (20, 26), (22, 25), (27, 25), (30, 21), (27, 17), (27, 15), (30, 11), (27, 7), (22, 7), closed=True)
        self.add_arc('hole-top', (14, 16), (18, 16), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('hole-bottom', (18, 16), (14, 16), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('hole', 'hole-top', 'hole-bottom', closed=True)

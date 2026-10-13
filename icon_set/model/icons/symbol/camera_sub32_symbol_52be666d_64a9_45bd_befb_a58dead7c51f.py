"""Independent 32px profile of camera.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '52be666d-64a9-45bd-befb-a58dead7c51f'
SOURCE_PATH = 'pictographic-primitives/video/camera_52be666d-64a9-45bd-befb-a58dead7c51f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('52be666d-64a9-45bd-befb-a58dead7c51f', 'pictographic-primitives/video/camera_52be666d-64a9-45bd-befb-a58dead7c51f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/camera',)
SOLO_SOURCE_ICON_IDS = ('camera',)
REFERENCE_EXPORT_SHA256 = 'ad6f73f47f717d597656ebf1a435fe80ec00c42ecdd36e93beec425caeaf4394'

class DrawingContainerSymbol(Sub32):
    icon_id = 'camera-sub32-symbol'
    related_origin_icon_id = 'camera-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/camera-sub32'
    counterpart_icon_id = 'camera-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'video'
    categories = ('video', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 8), (7, 8))
        self.add_line('p1-r1-2', (7, 8), (11, 4))
        self.add_line('p1-r1-3', (11, 4), (21, 4))
        self.add_line('p1-r1-4', (21, 4), (25, 8))
        self.add_line('p1-r1-5', (25, 8), (27, 8))
        self.add_arc('p1-r1-6', (27, 8), (30, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (30, 11), (30, 25))
        self.add_arc('p1-r1-8', (30, 25), (27, 28), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (27, 28), (5, 28))
        self.add_arc('p1-r1-10', (5, 28), (2, 25), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-11', (2, 25), (2, 11))
        self.add_arc('p1-r1-12', (2, 11), (5, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_arc('p2-r1-1', (12, 16), (20, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (20, 16), (12, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)

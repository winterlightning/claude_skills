# Centerline repair: continuous intended straight runs and matched tangent directions.
# Variant of camera-video-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of camera-video.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '0313a853-8fee-401d-b021-0624788b6cd1'
SOURCE_PATH = 'pictographic-primitives/video/camera_0313a853-8fee-401d-b021-0624788b6cd1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0313a853-8fee-401d-b021-0624788b6cd1', 'pictographic-primitives/video/camera_0313a853-8fee-401d-b021-0624788b6cd1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/camera-video',)
SOLO_SOURCE_ICON_IDS = ('camera-video',)
REFERENCE_EXPORT_SHA256 = 'd4b74fffb8aa265f90be6f63f1b5a9f56bfd66a97711e19372ff224c24dd6836'

class DrawingVariant3(Sub32):
    icon_id = 'camera-video-sub32-v3'
    variant_of = 'camera-video-sub32-v2'
    variant_label = 'Continuous centerlines'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'video'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (5, 8), (10, 8))
        self.add_bezier('p1-r1-2', (10, 8), ((11, 8), (11, short_low), (13, short_low)))
        self.add_line('p1-r1-3', (13, short_low), (19, short_low))
        self.add_bezier('p1-r1-4', (19, short_low), ((21, short_low), (21, 8), (22, 8)))
        self.add_line('p1-r1-5', (22, 8), (27, 8))
        self.add_arc('p1-r1-6', (27, 8), (30, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (30, 11), (30, 25))
        self.add_arc('p1-r1-8', (30, 25), (27, short_high), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (27, short_high), (5, short_high))
        self.add_arc('p1-r1-10', (5, short_high), (2, 25), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-11', (2, 25), (2, 11))
        self.add_arc('p1-r1-12', (2, 11), (5, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_line('p2-r1-1', (16, 17), (16, 17))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)

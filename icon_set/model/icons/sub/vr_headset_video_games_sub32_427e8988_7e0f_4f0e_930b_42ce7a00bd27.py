"""Independent 32px profile of vr-headset-video-games.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '427e8988-7e0f-4f0e-930b-42ce7a00bd27'
SOURCE_PATH = 'pictographic-primitives/video-games/vr headset_427e8988-7e0f-4f0e-930b-42ce7a00bd27.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('427e8988-7e0f-4f0e-930b-42ce7a00bd27', 'pictographic-primitives/video-games/vr headset_427e8988-7e0f-4f0e-930b-42ce7a00bd27.svg'),)
PROFILE_SOURCE_KEYS = ('solo/vr-headset-video-games',)
SOLO_SOURCE_ICON_IDS = ('vr-headset-video-games',)
REFERENCE_EXPORT_SHA256 = '8b696ecad104c8d91f8c3d2c8f79cfaa09bc696a421c41c38fc45e3fe12f67e5'

class Drawing(Sub32):
    icon_id = 'vr-headset-video-games-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'video-games'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 5), (24, 5))
        self.add_arc('p1-r1-2', (24, 5), (30, 10), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 10), (30, 22))
        self.add_arc('p1-r1-4', (30, 22), (24, 27), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (24, 27), (22, 27))
        self.add_bezier('p1-r1-6', (22, 27), ((19, 27), (19, 22), (16, 22)))
        self.add_bezier('p1-r1-7', (16, 22), ((13, 22), (13, 27), (10, 27)))
        self.add_line('p1-r1-8', (10, 27), (8, 27))
        self.add_arc('p1-r1-9', (8, 27), (2, 22), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-10', (2, 22), (2, 10))
        self.add_arc('p1-r1-11', (2, 10), (8, 5), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)

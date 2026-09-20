"""Independent 32px profile of speaker-with-one-sound-wave.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0fc7f807-680d-4e95-81e5-b189561e0157'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/volume 1_0fc7f807-680d-4e95-81e5-b189561e0157.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0fc7f807-680d-4e95-81e5-b189561e0157', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/volume 1_0fc7f807-680d-4e95-81e5-b189561e0157.svg'),)
PROFILE_SOURCE_KEYS = ('solo/speaker-with-one-sound-wave',)
SOLO_SOURCE_ICON_IDS = ('speaker-with-one-sound-wave',)
REFERENCE_EXPORT_SHA256 = '469f6172667bc7ff717cab37d0d81638f99c3d5dbf0721580d456833e1d20a53'

class Drawing(Sub32):
    icon_id = 'speaker-with-one-sound-wave-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/container-components'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 12), (8, 12))
        self.add_line('p1-r1-2', (8, 12), (17, 5))
        self.add_line('p1-r1-3', (17, 5), (17, 27))
        self.add_line('p1-r1-4', (17, 27), (8, 20))
        self.add_line('p1-r1-5', (8, 20), (2, 20))
        self.add_line('p1-r1-6', (2, 20), (2, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_arc('p2-r1-1', (24, 8), (24, 24), radius_x=6, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)

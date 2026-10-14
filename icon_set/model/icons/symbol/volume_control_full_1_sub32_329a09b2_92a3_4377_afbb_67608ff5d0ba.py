"""Independent 32px profile of volume-control-full-1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '329a09b2-92a3-4377-afbb-67608ff5d0ba'
SOURCE_PATH = 'pictographic-primitives/audio/volume control full 1_329a09b2-92a3-4377-afbb-67608ff5d0ba.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('329a09b2-92a3-4377-afbb-67608ff5d0ba', 'pictographic-primitives/audio/volume control full 1_329a09b2-92a3-4377-afbb-67608ff5d0ba.svg'), ('9908ced6-c069-485f-a3f0-c6840a25f58e', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/volume high_9908ced6-c069-485f-a3f0-c6840a25f58e.svg'), ('ce974c56-ba13-40f8-bcc7-d0c05f09f26f', 'pictographic-primitives/interface-essential/volume_ce974c56-ba13-40f8-bcc7-d0c05f09f26f.svg'))
PROFILE_SOURCE_KEYS = ('solo/volume-control-full-1', 'solo/volume-interface-essential')
SOLO_SOURCE_ICON_IDS = ('volume-control-full-1', 'volume-interface-essential')
REFERENCE_EXPORT_SHA256 = '835b33cb73a7df552b5a053ab6a9f6c79ac97d5f15b7d0a9455cd971b81ed882'

class Drawing(Sub32):
    icon_id = 'volume-control-full-1-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'audio'
    categories = ('audio', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Volume full: speaker horn and two sound waves, 4 units apart.
        self.add_polyline('speaker', (2, 12), (10, 6), (10, 26), (2, 20), closed=True)
        self.add_arc('wave-1', (18, 12), (18, 20), radius_x=2, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('wave-2', (28, 4), (28, 28), radius_x=2, radius_y=12, large_arc=False, sweep=True)

"""Independent 32px profile of pacman.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ea992b74-1d7b-5d1a-9380-854e5151b7ed'
SOURCE_PATH = 'pictographic-primitives/video-games/pacman_ea992b74-1d7b-5d1a-9380-854e5151b7ed.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ea992b74-1d7b-5d1a-9380-854e5151b7ed', 'pictographic-primitives/video-games/pacman_ea992b74-1d7b-5d1a-9380-854e5151b7ed.svg'), ('d162e891-6c21-47e5-ab18-e1fc863c5dc5', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-08/pacman_d162e891-6c21-47e5-ab18-e1fc863c5dc5.svg'))
PROFILE_SOURCE_KEYS = ('solo/pacman',)
SOLO_SOURCE_ICON_IDS = ('pacman',)
REFERENCE_EXPORT_SHA256 = 'fa702239bb1096ccaeaa67d0b2aa1a62395454b09ae46de4388333866b20dfc6'

class Drawing(Sub32):
    icon_id = 'pacman-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'video-games'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (27, 9), ((25, 5), (21, 2), (17, 2)))
        self.add_arc('p1-r1-2', (17, 2), (17, 30), radius_x=13, radius_y=14, large_arc=False, sweep=False)
        self.add_bezier('p1-r1-3', (17, 30), ((21, 30), (25, 27), (27, 23)))
        self.add_line('p1-r1-4', (27, 23), (18, 16))
        self.add_line('p1-r1-5', (18, 16), (27, 9))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)

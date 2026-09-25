"""Independent 32px profile of diagonal-telephone-receiver.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '86f150b1-cf66-5caf-8e7c-715833861202'
SOURCE_PATH = 'pictographic-primitives/phones/phone_86f150b1-cf66-5caf-8e7c-715833861202.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('86f150b1-cf66-5caf-8e7c-715833861202', 'pictographic-primitives/phones/phone_86f150b1-cf66-5caf-8e7c-715833861202.svg'), ('1701ca48-aa5b-4e61-a6fd-9be91a706783', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/phone 1_1701ca48-aa5b-4e61-a6fd-9be91a706783.svg'))
PROFILE_SOURCE_KEYS = ('solo/diagonal-telephone-receiver',)
SOLO_SOURCE_ICON_IDS = ('diagonal-telephone-receiver',)
REFERENCE_EXPORT_SHA256 = 'e0df6f28f5da68870a4115d7f3b7dfeafc63d7d270093e6a7849e0ce490e3ca1'

class Drawing(Sub32):
    icon_id = 'diagonal-telephone-receiver-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'phones'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (7, 2), (10, 2))
        self.add_arc('p1-r1-2', (10, 2), (13, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (13, 5), (13, 8))
        self.add_arc('p1-r1-4', (13, 8), (10, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (10, 11), (21, 22), radius_x=19, radius_y=19, large_arc=False, sweep=False)
        self.add_line('p1-r1-6', (21, 22), (24, 19))
        self.add_line('p1-r1-7', (24, 19), (27, 19))
        self.add_arc('p1-r1-8', (27, 19), (30, 22), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (30, 22), (30, 27))
        self.add_arc('p1-r1-10', (30, 27), (27, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-11', (27, 30), (25, 30))
        self.add_arc('p1-r1-12', (25, 30), (2, 7), radius_x=23, radius_y=23, large_arc=False, sweep=True)
        self.add_arc('p1-r1-13', (2, 7), (7, 2), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', closed=False)

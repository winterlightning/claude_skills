"""Independent 32px profile of sending-mail-envelope-batch-008-15.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b16d6d74-2c11-46d0-b165-8f50e0a4a4c2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/emails/send email_b16d6d74-2c11-46d0-b165-8f50e0a4a4c2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b16d6d74-2c11-46d0-b165-8f50e0a4a4c2', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/emails/send email_b16d6d74-2c11-46d0-b165-8f50e0a4a4c2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/sending-mail-envelope-batch-008-15',)
SOLO_SOURCE_ICON_IDS = ('sending-mail-envelope-batch-008-15',)
REFERENCE_EXPORT_SHA256 = '5631ead95eadd72655a34cbcf6758f40761ceb5c7ee930cad1373d86330c633e'

class Drawing(Sub32):
    icon_id = 'sending-mail-envelope-batch-008-15-sub32'
    keyshape = Keyshape.HRECT_L
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'emails'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (12, 6), (30, 6))
        self.add_line('p1-r1-2', (30, 6), (30, 26))
        self.add_line('p1-r1-3', (30, 26), (12, 26))
        self.add_line('p1-r1-4', (12, 26), (12, 6))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (12, 6), (21, 15))
        self.add_line('p2-r1-2', (21, 15), (30, 6))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (2, 12), (6, 12))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 20), (6, 20))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-2')
        self.relate("connect", 'p1-r1-2', 'p2-r1-2')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')

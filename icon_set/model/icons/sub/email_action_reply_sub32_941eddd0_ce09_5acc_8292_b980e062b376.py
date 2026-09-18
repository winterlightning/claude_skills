"""Independent 32px profile of email-action-reply.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '941eddd0-ce09-5acc-8292-b980e062b376'
SOURCE_PATH = 'pictographic-primitives/emails/email action reply_941eddd0-ce09-5acc-8292-b980e062b376.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('941eddd0-ce09-5acc-8292-b980e062b376', 'pictographic-primitives/emails/email action reply_941eddd0-ce09-5acc-8292-b980e062b376.svg'),)
PROFILE_SOURCE_KEYS = ('solo/email-action-reply',)
SOLO_SOURCE_ICON_IDS = ('email-action-reply',)
REFERENCE_EXPORT_SHA256 = '3e2b32341fc81eb07f6704b6b3010cf5cd6d5f937c95a632cf15768c77ab71c4'

class Drawing(Sub32):
    icon_id = 'email-action-reply-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'emails'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (13, 19), (13, 26))
        self.add_line('p1-r1-2', (13, 26), (2, 15))
        self.add_line('p1-r1-3', (2, 15), (13, 5))
        self.add_line('p1-r1-4', (13, 5), (13, 11))
        self.add_bezier('p1-r1-5', (13, 11), ((24, 11), (30, 17), (30, 27)))
        self.add_bezier('p1-r1-6', (30, 27), ((24, 21), (20, 19), (13, 19)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)

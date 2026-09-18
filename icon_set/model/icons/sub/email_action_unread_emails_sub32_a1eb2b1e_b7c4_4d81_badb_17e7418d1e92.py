"""Independent 32px profile of email-action-unread-emails.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a1eb2b1e-b7c4-4d81-badb-17e7418d1e92'
SOURCE_PATH = 'pictographic-primitives/emails/email action unread_a1eb2b1e-b7c4-4d81-badb-17e7418d1e92.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a1eb2b1e-b7c4-4d81-badb-17e7418d1e92', 'pictographic-primitives/emails/email action unread_a1eb2b1e-b7c4-4d81-badb-17e7418d1e92.svg'),)
PROFILE_SOURCE_KEYS = ('solo/email-action-unread-emails',)
SOLO_SOURCE_ICON_IDS = ('email-action-unread-emails',)
REFERENCE_EXPORT_SHA256 = '5cd1e40be8bc1724f6a68a79e27429301168c7fac24d21e03a8299609b3114a0'

class Drawing(Sub32):
    icon_id = 'email-action-unread-emails-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'emails'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 12), (8, 12))
        self.add_line('p1-r1-2', (8, 12), (22, 12))
        self.add_arc('p1-r1-3', (22, 12), (24, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (24, 15), (24, 20))
        self.add_line('p1-r1-5', (24, 20), (24, 24))
        self.add_arc('p1-r1-6', (24, 24), (22, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (22, 27), (8, 27))
        self.add_line('p1-r1-8', (8, 27), (5, 27))
        self.add_arc('p1-r1-9', (5, 27), (2, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-10', (2, 24), (2, 20))
        self.add_line('p1-r1-11', (2, 20), (2, 15))
        self.add_arc('p1-r1-12', (2, 15), (5, 12), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_line('p2-r1-1', (2, 15), (13, 22))
        self.add_line('p2-r1-2', (13, 22), (24, 15))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (8, 12), (8, 8))
        self.add_arc('p3-r1-2', (8, 8), (10, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p3-r1-3', (10, 5), (27, 5))
        self.add_arc('p3-r1-4', (27, 5), (30, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p3-r1-5', (30, 8), (30, 17))
        self.add_arc('p3-r1-6', (30, 17), (27, 20), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p3-r1-7', (27, 20), (24, 20))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', closed=False)
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-2')
        self.relate("connect", 'p1-r1-4', 'p2-r1-2')
        self.relate("connect", 'p1-r1-4', 'p3-r1-7')
        self.relate("connect", 'p1-r1-5', 'p3-r1-7')
        self.relate("connect", 'p1-r1-11', 'p2-r1-1')
        self.relate("connect", 'p1-r1-12', 'p2-r1-1')

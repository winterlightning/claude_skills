"""Independent 32px profile of usb.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e4b1f036-4c20-4e55-975c-b249f0a098fc'
SOURCE_PATH = 'pictographic-primitives/state/usb_e4b1f036-4c20-4e55-975c-b249f0a098fc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e4b1f036-4c20-4e55-975c-b249f0a098fc', 'pictographic-primitives/state/usb_e4b1f036-4c20-4e55-975c-b249f0a098fc.svg'),)
PROFILE_SOURCE_KEYS = ('solo/usb',)
SOLO_SOURCE_ICON_IDS = ('usb',)
REFERENCE_EXPORT_SHA256 = '8569afa12f1a5809791eafab748edcae54ae265cef077bc2423d71be566d38fa'

class Drawing(Sub32):
    icon_id = 'usb-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (9, 12), (9, 2))
        self.add_line('p1-r1-2', (9, 2), (23, 2))
        self.add_line('p1-r1-3', (23, 2), (23, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (9, 12), (23, 12))
        self.add_arc('p2-r1-2', (23, 12), (27, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (27, 16), (27, 26))
        self.add_arc('p2-r1-4', (27, 26), (23, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-5', (23, 30), (9, 30))
        self.add_arc('p2-r1-6', (9, 30), (5, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-7', (5, 26), (5, 16))
        self.add_arc('p2-r1-8', (5, 16), (9, 12), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-8')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-2')

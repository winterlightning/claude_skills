'Barcode: three evenly spaced bars in a smooth frame, with 10-unit border clearance.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '489f79de-538e-42b6-b17b-4132665a5a1b'
SOURCE_PATH = 'pictographic-primitives/shopping/barcode_489f79de-538e-42b6-b17b-4132665a5a1b.svg'
AUTHOR = 'gpt-6'

class BarcodeShopping(Solo48):
    icon_id = 'barcode-shopping'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('barcode', 'shopping')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('frame-0', (10, 8), (38, 8))
        self.add_arc('frame-1', (38, 8), (44, 14), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('frame-2', (44, 14), (44, 34))
        self.add_arc('frame-3', (44, 34), (38, 40), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('frame-4', (38, 40), (10, 40))
        self.add_arc('frame-5', (10, 40), (4, 34), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('frame-6', (4, 34), (4, 14))
        self.add_arc('frame-7', (4, 14), (10, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('bar-14', (14, 18), (14, 30))
        self.add_line('bar-24', (24, 18), (24, 30))
        self.add_line('bar-34', (34, 18), (34, 30))
        self.add_contour('frame', *('frame-0', 'frame-1', 'frame-2', 'frame-3', 'frame-4', 'frame-5', 'frame-6', 'frame-7'), closed=True)

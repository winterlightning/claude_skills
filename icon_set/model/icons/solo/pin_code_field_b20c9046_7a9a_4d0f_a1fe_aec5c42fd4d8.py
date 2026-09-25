'PIN field: even entry spacing, smooth frame and an upright cursor.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b20c9046-7a9a-4d0f-a1fe-aec5c42fd4d8'
SOURCE_PATH = 'pictographic-primitives/symbol/keycode_b20c9046-7a9a-4d0f-a1fe-aec5c42fd4d8.svg'
AUTHOR = 'gpt-6'


class PinCodeField(Solo48):
    icon_id = 'pin-code-field'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('pin', 'code', 'password', 'input', 'field', 'keycode', 'passcode', 'security')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('field-0', (8, 8), (40, 8))
        self.add_arc('field-1', (40, 8), (44, 12), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('field-2', (44, 12), (44, 36))
        self.add_arc('field-3', (44, 36), (40, 40), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('field-4', (40, 40), (8, 40))
        self.add_arc('field-5', (8, 40), (4, 36), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('field-6', (4, 36), (4, 12))
        self.add_arc('field-7', (4, 12), (8, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('digit-14', (14, 28), (15, 28))
        self.add_line('digit-24', (24, 28), (25, 28))
        self.add_line('cursor', (34, 18), (34, 30))
        self.add_contour('field', *('field-0', 'field-1', 'field-2', 'field-3', 'field-4', 'field-5', 'field-6', 'field-7'), closed=True)

# Variant of mailbox-arched; parent file remains unchanged.
"""An arched front-facing mailbox with a slot and two feet. VRECT_L extremes (8,6)-(40,42). Lucide mailbox informs the coherent rounded housing, adapted to the source front view. Retain slot, bottom bar and sidewall feet."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fda9a667-bd1e-4cf3-8b31-404409a91c95'
SOURCE_PATH = 'pictographic-primitives/symbol/mailbox_fda9a667-bd1e-4cf3-8b31-404409a91c95.svg'
AUTHOR = 'gpt-6'

class MailboxArchedVariant2(Solo48):
    icon_id = 'mailbox-arched-v2'
    variant_of = 'mailbox-arched'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('mailbox', 'mail', 'post', 'letter', 'postbox', 'delivery', 'inbox', 'postal')

    def build(self) -> None:
        self.add_line('left-foot', (8, 42), (8, 36))
        self.add_line('left-wall', (8, 36), (8, 20))
        self.add_arc('roof', (8, 20), (40, 20), radius_x=16)
        self.add_line('right-wall', (40, 20), (40, 36))
        self.add_line('right-foot', (40, 36), (40, 42))
        self.add_contour('shell', 'left-foot', 'left-wall', 'roof', 'right-wall', 'right-foot')
        self.add_line('bottom', (8, 36), (40, 36))
        self.relate('connect', 'shell', 'bottom')
        self.add_line('slot', (18, 23), (30, 23))

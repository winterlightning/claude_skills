"""Paper plane with a shared diagonal fold and a broad triangular wing. Lucide send informs the common crease endpoint; omit the tiny lower tail notch."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5ab1b54c-8465-4e9b-8c3a-8bf86a471550'
SOURCE_PATH = 'pictographic-primitives/logos/telegram logo_5ab1b54c-8465-4e9b-8c3a-8bf86a471550.svg'
AUTHOR = 'gpt-6'

class TelegramLogo(Solo48):
    icon_id = 'telegram-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('telegram', 'messenger', 'paper-plane', 'chat', 'logo', 'brand', 'send')

    def build(self):
        # Plan: Paper plane with a shared diagonal fold and a broad triangular wing. Lucide send informs the common crease endpoint; omit the tiny lower tail notch.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_polyline('plane',(6,22),(42,6),(34,42),(20,30),closed=True)
        self.add_line('fold',(20,30),(42,6));self.relate('connect','plane','fold')


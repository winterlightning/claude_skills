"""microphone-sound: approved original model.

Construction: Desk microphone on a broad foot, with a transverse grille and a direct stem.
Keyshape: VRECT_L; exact SOLO48 envelope.
Construction reference: audio-lines from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = 'f991ef0f-2aa9-4924-9670-c07e3215f3a9'
SOURCE_PATH = 'pictographic-primitives/state/microphone sound_f991ef0f-2aa9-4924-9670-c07e3215f3a9.svg'
AUTHOR = 'gpt-6'

class MicrophoneSound(Solo48):
    icon_id = 'microphone-sound'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('microphone', 'sound', 'state')
    keyshape = Keyshape.VRECT_L

    def build(self):
        box(self, 'capsule', 16, 4, 32, 28, 8, ys=(16,), xs=(24,))
        line(self, 'grille', (16, 16), (32, 16))
        line(self, 'stem', (24, 28), (24, 44))
        line(self, 'foot', (8, 44), (40, 44))
        contacts(self)

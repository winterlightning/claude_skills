"""sound: approved original model.

Construction: Sound waveform with two smooth peaks and a central trough, using continuous cubic tangents.
Keyshape: HRECT_L; exact SOLO48 envelope.
Construction reference: audio-lines from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = '515cc7f7-bcd9-45db-903d-f6e55e4d3b45'
SOURCE_PATH = 'pictographic-primitives/interface-essential/sound_515cc7f7-bcd9-45db-903d-f6e55e4d3b45.svg'
AUTHOR = 'gpt-6'

class Sound(Solo48):
    icon_id = 'sound'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('sound', 'interface-essential')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self, 'wave', (4, 24), ('C', (9, 24), (9, 8), (14, 8)), ('C', (19, 8), (19, 40), (24, 40)), ('C', (29, 40), (29, 8), (34, 8)), ('C', (39, 8), (39, 24), (44, 24)))
        contacts(self)

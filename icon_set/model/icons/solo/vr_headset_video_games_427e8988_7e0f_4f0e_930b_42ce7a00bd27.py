"""vr-headset-video-games: approved original model.

Construction: VR gaming headset with a flat brow, vertical temples and rounded rectangular ends around the nose saddle.
Keyshape: HRECT_L; exact SOLO48 envelope.
Construction reference: gamepad-2 from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = '427e8988-7e0f-4f0e-930b-42ce7a00bd27'
SOURCE_PATH = 'pictographic-primitives/video-games/vr headset_427e8988-7e0f-4f0e-930b-42ce7a00bd27.svg'
AUTHOR = 'gpt-6'

class VrHeadsetVideoGames(Solo48):
    icon_id = 'vr-headset-video-games'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('vr', 'headset', 'video-games')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self, 'goggles', (12, 8), ('L', (36, 8)), ('A', 8, 8, True, (44, 16)), ('L', (44, 32)), ('A', 8, 8, True, (36, 40)), ('L', (32, 40)), ('C', (28, 40), (28, 32), (24, 32)), ('C', (20, 32), (20, 40), (16, 40)), ('L', (12, 40)), ('A', 8, 8, True, (4, 32)), ('L', (4, 16)), ('A', 8, 8, True, (12, 8)), closed=True)
        contacts(self)

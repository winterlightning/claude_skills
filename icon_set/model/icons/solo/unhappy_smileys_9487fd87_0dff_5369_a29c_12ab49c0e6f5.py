"""unhappy-smileys: approved original model.

Construction: Unhappy face with simple dot eyes and a narrow arched frown; distinguish it from the anxious curved-eye face.
Keyshape: CIRCLE; exact SOLO48 envelope.
Construction reference: circle from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = '9487fd87-0dff-5369-a29c-12ab49c0e6f5'
SOURCE_PATH = 'pictographic-primitives/smileys/unhappy_9487fd87-0dff-5369-a29c-12ab49c0e6f5.svg'
AUTHOR = 'gpt-6'

class UnhappySmileys(Solo48):
    icon_id = 'unhappy-smileys'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    categories = ('smileys', 'primitives')
    aliases = ()
    keywords = ('unhappy', 'smileys')
    keyshape = Keyshape.CIRCLE

    def build(self):
        ellipse(self, 'face', 24, 24, 20)
        self.add_dot('eye-left', (17, 17))
        self.add_dot('eye-right', (31, 17))
        path(self, 'mouth', (18, 33), ('C', (21, 27), (27, 27), (30, 33)))
        contacts(self)

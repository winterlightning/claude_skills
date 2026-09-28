"""Square brand frame with tall and short vertical cards. Reduce each narrow outlined card to a round-ended stroke, preserving the two unequal columns."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b5624ad1-41e0-4b00-a5d0-3a48fcd68187'
SOURCE_PATH = 'pictographic-primitives/logos/trello logo_b5624ad1-41e0-4b00-a5d0-3a48fcd68187.svg'
AUTHOR = 'gpt-6'

class TrelloLogo(Solo48):
    icon_id = 'trello-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('trello', 'atlassian', 'kanban', 'board', 'logo', 'brand', 'project-management')

    def build(self):
        # Plan: Square brand frame with tall and short vertical cards. Reduce each narrow outlined card to a round-ended stroke, preserving the two unequal columns.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_polyline('frame',(6,6),(42,6),(42,42),(6,42),closed=True)
        self.add_line('left-card',(18,16),(18,32));self.add_line('right-card',(30,16),(30,24))


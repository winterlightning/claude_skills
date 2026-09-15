"""information: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '13718512-f145-41c1-8a96-ce57c5ff8408'
SOURCE_PATH = 'pictographic-primitives/symbol/information_13718512-f145-41c1-8a96-ce57c5ff8408.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Information(Solo48):
    icon_id = 'information'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('information', 'symbol')

    def build(self):
        # Plan: VRECT_L; level cap stroke, centered dot-bar and exact upright stem.
        # Reference: Geometric typographic construction.
        self.add_line('dot-bar',(19,4),(29,4))
        self.add_polyline('stem',(8,18),(24,18),(24,44))
        self.add_line('foot',(8,44),(40,44))
        self.relate('connect','stem','foot')

"""Complete TS letter pair in a square envelope. Omit the surrounding square and reduce lettering to single strokes so both letters remain readable."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a4009091-89bd-4fb0-8c0c-bcc11872068d'
SOURCE_PATH = 'pictographic-primitives/logos/type script logo_a4009091-89bd-4fb0-8c0c-bcc11872068d.svg'
AUTHOR = 'gpt-6'

class TypescriptLogo(Solo48):
    icon_id = 'typescript-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('typescript', 'ts', 'programming', 'language', 'logo', 'brand', 'developer')

    def build(self):
        # Plan: Complete TS letter pair in a square envelope. Omit the surrounding square and reduce lettering to single strokes so both letters remain readable.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_polyline('t-top',(6,6),(13,6),(20,6));self.add_line('t-stem',(13,6),(13,42));self.relate('connect','t-top','t-stem')
        self.add_bezier('s',(42,12),((42,6),(28,2),(28,14)),((28,22),(42,23),(42,32)),((42,44),(28,44),(28,36)))


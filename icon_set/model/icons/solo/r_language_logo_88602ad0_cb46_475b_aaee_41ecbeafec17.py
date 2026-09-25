"""An open oval swoosh wraps the upper-left of a monoline R. Retain asymmetric lower-right placement; reduce the heavy letter outline."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '88602ad0-cb46-475b-aaee-41ecbeafec17'
SOURCE_PATH = 'pictographic-primitives/logos/r logo_88602ad0-cb46-475b-aaee-41ecbeafec17.svg'
AUTHOR = 'gpt-6'

class RLanguageLogo(Solo48):
    icon_id = 'r-language-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('r', 'r-language', 'statistics', 'programming', 'logo', 'brand', 'data')

    def build(self):
        # Plan: An open oval swoosh wraps the upper-left of a monoline R. Retain asymmetric lower-right placement; reduce the heavy letter outline.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_bezier('swoosh',(14,32),((6,30),(6,24),(6,20)),((6,12),(14,6),(24,6)),((34,6),(42,10),(42,16)))
        self.add_polyline('stem',(24,22),(24,32),(24,42))
        self.add_arc('bowl',(24,22),(24,32),radius_x=12,radius_y=5)
        self.add_line('leg',(24,32),(42,42))
        self.relate('connect','stem','bowl')
        self.relate('connect','stem','leg')
        self.relate('connect','bowl','leg')


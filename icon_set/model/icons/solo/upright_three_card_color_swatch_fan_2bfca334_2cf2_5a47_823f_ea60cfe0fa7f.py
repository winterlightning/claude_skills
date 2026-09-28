from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2bfca334-2cf2-5a47-823f-ea60cfe0fa7f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/palette sample_2bfca334-2cf2-5a47-823f-ea60cfe0fa7f.svg'
AUTHOR = 'gpt-6'


class UprightThreeCardColorSwatchFan(Solo48):
    icon_id = 'upright-three-card-color-swatch-fan'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('swatches', 'color', 'cards', 'fan', 'palette', 'pivot', 'samples', 'design')

    def build(self) -> None:
        # Upright front card, diagonal middle, horizontal rear; shared lower pivot.
        self.add_polyline('front',(6,6),(22,6),(22,18),(22,38),(22,42),(6,42),closed=True)
        self.add_dot('pivot',(14,32))
        self.add_polyline('middle',(22,18),(32,8),(42,18),(32,28),(22,38))
        self.add_polyline('rear',(32,28),(42,28),(42,42),(22,42))
        self.relate('connect','front','middle');self.relate('connect','middle','rear');self.relate('connect','front','rear')

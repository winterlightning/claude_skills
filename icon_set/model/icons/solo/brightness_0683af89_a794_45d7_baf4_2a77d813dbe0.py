'Brightness: round sun and eight reflected rays with clear, equal cardinal spacing.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0683af89-a794-45d7-baf4-2a77d813dbe0'
SOURCE_PATH = 'pictographic-primitives/interface-essential/brightness_0683af89-a794-45d7-baf4-2a77d813dbe0.svg'
AUTHOR = 'gpt-6'

class Brightness(Solo48):
    icon_id = 'brightness'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('brightness', 'interface-essential')

    def build(self) -> None:
        self.add_arc('sun-top', (19,24), (29,24), radius_x=5, radius_y=5)
        self.add_arc('sun-bottom', (29,24), (19,24), radius_x=5, radius_y=5)
        self.add_contour('sun', 'sun-top', 'sun-bottom', closed=True)

        for i,(a,b) in enumerate((((24,6),(24,10)),((24,38),(24,42)),((6,24),(10,24)),((38,24),(42,24)),((12,12),(14,14)),((34,14),(36,12)),((12,36),(14,34)),((34,34),(36,36)))):
            self.add_line(f'ray-{i}',a,b)

"""A diagonal shovel with pointed blade and open D-grip; thin shaft is a single stroke."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '69c463da-b062-552f-b3f7-b27cd2fdbbf0'
SOURCE_PATH = 'pictographic-primitives/tools/tools shovel_69c463da-b062-552f-b3f7-b27cd2fdbbf0.svg'
AUTHOR = 'gpt-6'

class Shovel(Solo48):
    icon_id = 'shovel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    categories = ("primitives", "tools")
    aliases = ()
    keywords = ('shovel', 'spade', 'dig', 'garden', 'construction', 'earth', 'digging', 'tool')

    def build(self) -> None:


        self.add_polyline('blade',(6,26),(14,18),(30,34),(22,42),(6,42),closed=True)
        self.add_line('shaft',(22,26),(34,14))
        self.add_polyline('grip',(26,6),(42,6),(42,22),(26,6),closed=True)
        self.relate('connect','shaft','blade')
        self.relate('connect','shaft','grip')

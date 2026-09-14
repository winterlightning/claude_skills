'Dill sprig: preserve the natural lean and asymmetric curved branches with clear branch spacing.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ed3fa5b-9e28-4066-bff3-a2cb767df09d'
SOURCE_PATH = 'icons-json/food/dill_4ed3fa5b-9e28-4066-bff3-a2cb767df09d.json'
AUTHOR = 'gpt-6'

class Dill(Solo48):
    icon_id = 'dill'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('dill', 'food')

    def build(self) -> None:
        self.add_bezier('stem',(24,42),((23,40),(23,38),(24,36)),((24,35),(24,34),(24,33)),((23,30),(23,26),(24,23)),((25,20),(25,17),(26,14)),((27,10),(28,8),(29,6)))
        self.add_bezier('left-low',(24,36),((14,38),(9,34),(8,29)))
        self.add_bezier('right-low',(24,33),((34,34),(39,30),(42,25)))
        self.add_bezier('left-high',(24,23),((15,24),(9,20),(6,14)))
        self.add_bezier('right-high',(26,14),((33,15),(36,13),(38,10)))
        # Explicit shared endpoints define the same leaning organic stem.
        self.relate('connect','stem','left-low')
        self.relate('connect','stem','right-low')
        self.relate('connect','stem','left-high')
        self.relate('connect','stem','right-high')

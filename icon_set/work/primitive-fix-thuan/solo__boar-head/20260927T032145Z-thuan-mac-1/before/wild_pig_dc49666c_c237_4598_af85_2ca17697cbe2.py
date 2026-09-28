'Boar: preserve pointed ears and the broad oval snout, with four clear facial dots and real cheek attachments.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dc49666c-c237-4598-af85-2ca17697cbe2'
SOURCE_PATH = 'pictographic-primitives/animals/wild pig_dc49666c-c237-4598-af85-2ca17697cbe2.svg'
AUTHOR = 'gpt-6'


class BoarHead(Solo48):
    icon_id = 'boar-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    categories = ("animals", "primitives")
    aliases = ()
    keywords = ('boar', 'pig', 'head', 'ears', 'silhouette', 'face', 'wild', 'animal')

    def build(self) -> None:
        self.add_polyline('crown',(6,24),(6,6),(16,9),(32,9),(42,6),(42,24))
        self.add_bezier('right-cheek',(42,24),((42,28),(40,31),(37,33)))
        self.add_bezier('left-cheek',(11,33),((8,31),(6,28),(6,24)))
        self.relate('connect','crown','left-cheek');self.relate('connect','crown','right-cheek')
        self.add_arc('snout-top',(11,33),(37,33),radius_x=13,radius_y=9)
        self.add_arc('snout-bottom',(37,33),(11,33),radius_x=13,radius_y=9)
        self.add_contour('snout','snout-top','snout-bottom',closed=True)
        self.relate('connect','snout','left-cheek');self.relate('connect','snout','right-cheek')
        self.add_dot('eye-left',(15,17));self.add_dot('eye-right',(33,17))
        self.add_dot('nostril-left',(20,33));self.add_dot('nostril-right',(28,33))

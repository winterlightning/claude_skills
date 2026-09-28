'Outstretched statue with long robe and pedestal. Sleeve outlines and diagonal cloth fold omitted for native-size clarity.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd6731d45-e9f7-4836-bc3f-af5734247f8c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__christ-the-redeemer/20260927T032022Z-thuan-mac-1/reference/christ the reedemer_d6731d45-e9f7-4836-bc3f-af5734247f8c.svg'
AUTHOR = "gpt-6"

class ChristTheRedeemer(Solo48):
    icon_id = 'christ-the-redeemer'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "landmarks"
    categories = ("landmarks", "primitives")
    aliases = ()
    keywords = ('christ the redeemer', 'rio', 'brazil', 'statue', 'monument', 'figure', 'landmark', 'religion')

    def build(self) -> None:
        # Outstretched arms, hanging sleeves, a long robe, and a flared plinth.
        self.add_arc('head-upper', (21, 9), (27, 9), radius_x=3)
        self.add_arc('head-lower', (27, 9), (21, 9), radius_x=3)
        self.add_contour('head', 'head-upper', 'head-lower', closed=True)
        self.add_polyline(
            'robe-and-sleeves', (6, 20), (10, 20), (10, 26),
            (18, 26), (18, 34), (30, 34), (30, 26),
            (38, 26), (38, 20), (42, 20),
        )
        self.add_polyline('plinth', (18, 34), (14, 42), (34, 42), (30, 34))
        self.relate('connect', 'robe-and-sleeves', 'plinth')

"""A pig head facing an apple on a rectangular panel.
Symbol plan and construction: piggy-bank and apple: animal contour and lobed fruit construction; source supplies the asymmetric arrangement.
Keyshape: HRECT_L widens the apple panel while retaining the pig at left.
Omissions: Tiny nostril omitted; apple enlarged. Ear retained after an earless numeric pass lost too much identity.
Review: Blocked: pig-upper has only 0.1751 internal ink clearance over 4.1048 units. Ear remains congested in both themes. Six candidates saved; the earless pass is not accepted."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1c6d508d-38fb-4b6a-bfe9-e20ebd9e9bf4'
SOURCE_PATH = 'pictographic-primitives/outdoors/outdoors pig apple_1c6d508d-38fb-4b6a-bfe9-e20ebd9e9bf4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'outdoors-pig-apple'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('outdoors', 'pig', 'apple')




    def build(self):
        self.add_polyline('panel',(14,25),(14,8),(44,8),(44,40),(24,40))
        self.add_bezier('pig-lower',(4,40),((7,34),(8,33),(12,31)),((13,30),(14,27),(14,25)))
        self.add_bezier('pig-upper',(14,25),((10,24),(9,21),(8,17)),((6,14),(5,14),(4,14)),((4,18),(4,20),(4,22)))
        self.add_contour('pig','pig-lower','pig-upper');self.relate('connect','panel','pig')
        self.add_bezier('apple',(29,21),((25,18),(22,20),(23,25)),((24,31),(27,32),(29,30)),((31,32),(34,31),(35,25)),((36,20),(33,18),(29,21)))
        self.add_line('apple-stem',(29,21),(31,16));self.relate('connect','apple','apple-stem')

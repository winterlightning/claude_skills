'Diving boat: preserve its intentional tilt and curved bow, with a smooth sea and sufficient clear separation.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '204ae051-9164-4427-9aed-ae16980f534d'
SOURCE_PATH = 'icons-json/recreation/diving boat_204ae051-9164-4427-9aed-ae16980f534d.json'
AUTHOR = 'gpt-6'

class DivingBoat(Solo48):
    icon_id = 'diving-boat'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'recreation'
    aliases = ()
    keywords = ('diving', 'boat', 'recreation')

    def build(self) -> None:
        # Preserve the inclined bow and mast, with a separate smooth wave below.
        self.add_line('hull-back',(10,28),(24,21))
        self.add_line('hull-front',(24,21),(38,14))
        self.add_bezier('bow',(38,14),((38,19),(37,25),(34,28)))
        self.add_contour('hull','hull-back','hull-front','bow')
        self.add_polyline('mast',(16,8),(18,12),(24,21))
        self.add_polyline('crossbar',(14,14),(18,12),(22,10))
        self.relate('connect','mast','hull');self.relate('connect','mast','crossbar')
        self.add_bezier('sea',(4,40),((7,40),(7,38),(9,38)),((11,38),(11,40),(14,40)),((17,40),(17,38),(19,38)),((21,38),(21,40),(24,40)),((27,40),(27,38),(29,38)),((31,38),(31,40),(34,40)),((37,40),(37,38),(39,38)),((41,38),(41,40),(44,40)))

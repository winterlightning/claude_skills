"""dress-clothes: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6d38ebdf-a077-54d8-b2cd-fd37cdddfcde'
SOURCE_PATH = 'pictographic-primitives/clothes/dress_6d38ebdf-a077-54d8-b2cd-fd37cdddfcde.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class DressClothes(Solo48):
    icon_id = 'dress-clothes'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('dress', 'clothes')

    def build(self):
        # Plan: VRECT_L; paired straps, mirrored bodice, flowing skirt and centered hem.
        # Reference: Geometric mirrored garment; retain V versus sweetheart neckline distinction.
        self.add_line('left-strap',(16,4),(16,9))
        self.add_bezier('left-bodice',(16,9),((14,12),(18,17),(17,20)))
        self.add_bezier('left-skirt',(17,20),((15,26),(10,34),(8,40)))
        self.add_bezier('hem',(8,40),((13,42),(18,44),(24,44)),((30,44),(35,42),(40,40)))
        self.add_bezier('right-skirt',(40,40),((38,34),(33,26),(31,20)))
        self.add_bezier('right-bodice',(31,20),((30,17),(34,12),(32,9)))
        self.add_line('right-strap',(32,9),(32,4))
        self.add_contour('dress','left-strap','left-bodice','left-skirt','hem','right-skirt','right-bodice','right-strap')

        self.add_bezier('neckline',(16,9),((20,9),(21,10),(24,12)),((27,10),(28,9),(32,9)))
        self.relate('connect','neckline','dress')

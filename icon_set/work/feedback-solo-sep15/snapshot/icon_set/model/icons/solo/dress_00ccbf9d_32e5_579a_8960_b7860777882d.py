"""dress-00ccbf9d: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00ccbf9d-32e5-579a-8960-b7860777882d'
SOURCE_PATH = 'pictographic-primitives/clothes/dress_00ccbf9d-32e5-579a-8960-b7860777882d.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Dress(Solo48):
    icon_id = 'dress-00ccbf9d'
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

        self.add_polyline('neckline',(16,9),(24,14),(32,9))
        self.relate('connect','neckline','dress')

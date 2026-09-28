"""Sneezing Face with Tissue; independently reconstructed on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c599cef4-d857-592c-9a9b-c8fc87fd39c3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__sneezing-face-with-tissue/20260927T101636Z-thuan-mac-1/reference/nose blow_c599cef4-d857-592c-9a9b-c8fc87fd39c3.svg'
AUTHOR = "gpt-6"


class SneezingFaceWithTissue(Solo48):
    icon_id = 'sneezing-face-with-tissue'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases = ()
    keywords = ('sneezing', 'tissue', 'nose', 'cold', 'face', 'emoji')

    def build(self) -> None:
        # Complete side cheeks frame the prominent folded tissue under closed eyes.
        self.add_arc('head-top',(6,24),(42,24),radius_x=18)
        self.add_bezier('cheek-right',(42,24),((42,31),(39,36),(34,38)))
        self.add_bezier('cheek-left',(14,40),((9,36),(6,31),(6,24)))
        self.add_contour('face','head-top','cheek-right',closed=False)
        self.add_contour('left-cheek','cheek-left',closed=False)
        for side,x in (('left',18),('right',30)):
            self.add_arc('eye-'+side,(x-1,18),(x+1,18),radius_x=2,sweep=False)
        self.add_polyline('tissue',(24,26),(34,38),(25,42),(14,40),closed=True)
        self.relate('connect','face','tissue')
        self.relate('connect','left-cheek','tissue')

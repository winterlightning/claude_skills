"""safety-helmet-construction: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '990d7f69-ffaf-5940-bacc-e3c7ad205e17'
SOURCE_PATH = 'pictographic-primitives/construction/safety helmet_990d7f69-ffaf-5940-bacc-e3c7ad205e17.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class SafetyHelmetConstruction(Solo48):
    icon_id = 'safety-helmet-construction'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('safety', 'helmet', 'construction')

    def build(self):
        # Plan: HRECT_L; mirrored shell and brim, smooth crest and identical ridge corners.
        # Reference: Geometric mirrored shell; source retains the protective ridge.
        self.add_bezier('left-shell',(18,11),((11,13),(7,20),(7,29)))
        self.add_bezier('left-brim',(7,29),((5,29),(4,31),(4,33)),((4,37),(15,40),(24,40)))
        self.add_bezier('right-brim',(24,40),((33,40),(44,37),(44,33)),((44,31),(43,29),(41,29)))
        self.add_bezier('right-shell',(41,29),((41,20),(37,13),(30,11)))
        self.add_contour('shell','left-shell','left-brim','right-brim','right-shell')
        self.add_arc('ridge-left',(18,11),(21,8),radius_x=3)
        self.add_line('ridge-top',(21,8),(27,8))
        self.add_arc('ridge-right',(27,8),(30,11),radius_x=3)
        self.add_contour('ridge','ridge-left','ridge-top','ridge-right')
        self.add_line('rib-left',(18,11),(19,23))
        self.add_line('rib-right',(30,11),(29,23))
        self.relate('connect','ridge','shell')
        for name in ['rib-left','rib-right']:
            self.relate('connect',name,'ridge')
            self.relate('connect',name,'shell')

"""phone-with-starburst: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9ee0961-b35e-48ac-b567-d69d398bf9fc'
SOURCE_PATH = 'pictographic-primitives/symbol/phone with starburst_c9ee0961-b35e-48ac-b567-d69d398bf9fc.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class PhoneWithStarburst(Solo48):
    icon_id = 'phone-with-starburst'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('phone', 'with', 'starburst', 'symbol')

    def build(self):
        # Plan: HRECT_L; mirrored receiver ends and centered signal rays; smooth outer arch.
        # Reference: Geometric receiver construction.
        self.add_bezier('outer-left',(4,35),((4,25),(13,23),(24,23)))
        self.add_bezier('outer-right',(24,23),((35,23),(44,25),(44,35)))
        self.add_arc('right-corner',(44,35),(39,40),radius_x=5)
        self.add_line('right-end',(39,40),(36,40))
        self.add_arc('right-inner',(36,40),(32,36),radius_x=4)
        self.add_line('right-neck',(32,36),(32,33))
        self.add_line('inner',(32,33),(16,33))
        self.add_line('left-neck',(16,33),(16,36))
        self.add_arc('left-inner',(16,36),(12,40),radius_x=4)
        self.add_line('left-end',(12,40),(9,40))
        self.add_arc('left-corner',(9,40),(4,35),radius_x=5)
        self.add_contour('receiver','outer-left','outer-right','right-corner','right-end','right-inner','right-neck','inner','left-neck','left-inner','left-end','left-corner',closed=True)
        self.add_line('ray-center',(24,8),(24,14))
        for side in [-1,1]:self.add_line('ray-'+str(side),(24+side*13,10),(24+side*10,15))

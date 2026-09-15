"""monument: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7f142849-8b23-40f0-aba8-d7cdaa500f99'
SOURCE_PATH = 'pictographic-primitives/symbol/monument_7f142849-8b23-40f0-aba8-d7cdaa500f99.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Monument(Solo48):
    icon_id = 'monument'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('monument', 'symbol')

    def build(self):
        # Plan: SQUARE; circular dome centered on a mirrored base; exact finial contact.
        # Reference: Geometric dome and shared axis.
        self.add_line('base',(6,42),(42,42))
        self.add_bezier('right-base',(42,42),((41,35),(39,29),(35,29)))
        self.add_line('ledge',(35,29),(13,29))
        self.add_bezier('left-base',(13,29),((9,29),(7,35),(6,42)))
        self.add_contour('pedestal','base','right-base','ledge','left-base',closed=True)
        self.add_line('left-wall',(13,29),(13,23))
        self.add_arc('dome-left',(13,23),(24,12),radius_x=11)
        self.add_arc('dome-right',(24,12),(35,23),radius_x=11)
        self.add_line('right-wall',(35,23),(35,29))
        self.add_contour('dome','left-wall','dome-left','dome-right','right-wall')
        self.add_line('finial',(24,6),(24,12))
        self.relate('connect','dome','pedestal')
        self.relate('connect','finial','dome')

"""tray: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '028a2382-a657-4cdb-802e-defa023b4886'
SOURCE_PATH = 'pictographic-primitives/symbol/tray_028a2382-a657-4cdb-802e-defa023b4886.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class Tray(Solo48):
    icon_id = 'tray'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('tray', 'symbol')

    def build(self):
        # HRECT_L (4,8)-(44,40); symmetric serving dome with a connected knob.
        # Construction reference: Lucide headphones: circular dome tangent to sides
        self.add_line('base',(4,40),(44,40))
        self.add_line('left',(8,40),(8,28))
        self.add_arc('dome',(8,28),(40,28),radius_x=16)
        self.add_line('right',(40,28),(40,40))
        self.add_contour('cover','left','dome','right')
        self.add_line('knob',(24,8),(24,12))
        self.relate('connect','base','cover')
        self.relate('connect','knob','cover')

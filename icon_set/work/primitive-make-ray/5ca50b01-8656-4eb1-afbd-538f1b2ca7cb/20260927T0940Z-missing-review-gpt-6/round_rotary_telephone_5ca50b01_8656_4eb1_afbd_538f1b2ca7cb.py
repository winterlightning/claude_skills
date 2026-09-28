"""Rotary telephone with rounded base and central dial; finger stop omitted to preserve clearance."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5ca50b01-8656-4eb1-afbd-538f1b2ca7cb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__round-rotary-telephone/20260927T084430Z-thuan-mac-1/reference/phone retro_5ca50b01-8656-4eb1-afbd-538f1b2ca7cb.svg'
AUTHOR = 'gpt-6'

class RoundRotaryTelephone(Solo48):
    icon_id = 'round-rotary-telephone'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'phones'
    categories = ('phones', 'primitives')
    aliases = ()
    keywords = ('telephone', 'rotary', 'vintage', 'dial', 'receiver', 'landline')

    def build(self):
        # Lucide phone: a broad receiver bow above a deep round rotary housing.
        # Keep the receiver ends separated from the housing so the 4-pixel strokes breathe.
        self.add_arc('receiver-left',(6,17),(16,6),radius_x=11,radius_y=11)
        self.add_line('receiver-top',(16,6),(32,6))
        self.add_arc('receiver-right',(32,6),(42,17),radius_x=11,radius_y=11)
        self.add_contour('receiver','receiver-left','receiver-top','receiver-right')
        self.add_line('housing-left',(10,25),(10,30))
        self.add_arc('housing-bottom',(10,30),(38,30),radius_x=14,radius_y=12,sweep=False)
        self.add_line('housing-right',(38,30),(38,25))
        self.add_contour('housing','housing-left','housing-bottom','housing-right')
        self.add_arc('dial-top',(19,29),(29,29),radius_x=5)
        self.add_arc('dial-bottom',(29,29),(19,29),radius_x=5)
        self.add_contour('dial','dial-top','dial-bottom',closed=True)

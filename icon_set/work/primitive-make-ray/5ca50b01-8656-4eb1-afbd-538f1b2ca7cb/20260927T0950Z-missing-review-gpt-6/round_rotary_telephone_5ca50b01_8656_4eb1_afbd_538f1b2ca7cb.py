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
        self.add_line('receiver-top',(16,6),(32,6))
        self.add_arc('receiver-r',(32,6),(42,16),radius_x=10)
        receiver_low=((42,16),(42,17),(34,17),(34,14),(24,14),(14,14),(14,17),(6,17),(6,16))
        for i,(a,b) in enumerate(zip(receiver_low,receiver_low[1:]),1): self.add_line(f'receiver-low-{i}',a,b)
        self.add_arc('receiver-l',(6,16),(16,6),radius_x=10)
        self.add_contour('receiver','receiver-top','receiver-r',*[f'receiver-low-{i}' for i in range(1,9)],'receiver-l',closed=True)
        self.add_line('housing-left',(10,25),(10,30))
        self.add_arc('housing-bottom',(10,30),(38,30),radius_x=14,radius_y=12,sweep=False)
        self.add_line('housing-right',(38,30),(38,25))
        self.add_contour('housing','housing-left','housing-bottom','housing-right')
        self.add_arc('dial-top',(19,28),(29,28),radius_x=5)
        self.add_arc('dial-bottom',(29,28),(19,28),radius_x=5)
        self.add_contour('dial','dial-top','dial-bottom',closed=True)

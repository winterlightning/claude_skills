"""Rock horns with separated outer fingers, folded central fingers and crossing thumb. VRECT_XL centerlines 8,4–40,44. Lucide hand-metal informs repeated finger caps and semicircular palm; omit palm crease."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a3500fb2-e18f-4ff3-91fa-a696fee3e6b0'
SOURCE_PATH = 'pictographic-primitives/social/mood rock_a3500fb2-e18f-4ff3-91fa-a696fee3e6b0.svg'
AUTHOR = 'gpt-6'

class RockHornsHand(Solo48):
    icon_id = 'rock-horns-hand'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "social"
    aliases = ()
    keywords = ('hand', 'rock', 'horns', 'gesture', 'finger', 'music')

    def build(self):
        # Shared 8-unit finger widths, 16-unit center spacing; rounded palm.
        self.add_line('index-outside',(8,28),(8,8))
        self.add_arc('index-tip',(8,8),(16,8),radius_x=4)
        self.add_line('index-inside',(16,8),(16,22))
        self.add_arc('folded-middle',(16,22),(24,22),radius_x=4)
        self.add_arc('folded-ring',(24,22),(32,22),radius_x=4)
        self.add_line('little-inside',(32,22),(32,8))
        self.add_arc('little-tip',(32,8),(40,8),radius_x=4)
        self.add_line('little-outside',(40,8),(40,28))
        self.add_arc('palm-bottom',(40,28),(8,28),radius_x=16)
        self.add_contour('hand','index-outside','index-tip','index-inside','folded-middle','folded-ring','little-inside','little-tip','little-outside','palm-bottom',closed=True)
        self.add_line('thumb-top',(40,28),(25,28))
        self.add_arc('thumb-end',(25,28),(25,36),radius_x=4,sweep=False)
        self.add_line('thumb-bottom',(25,36),(32,36))
        self.add_contour('thumb','thumb-top','thumb-end','thumb-bottom')
        self.relate('connect','hand','thumb')

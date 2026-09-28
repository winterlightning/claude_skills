"""Three detached rounded blades inside a circular rim. The source's tiny almond openings become solid marks at 48 pixels."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '20697f6b-e6a3-48c1-8c44-46bea9f5204c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__circle-with-three-blades/20260927T032022Z-thuan-mac-1/reference/tools testflight_20697f6b-e6a3-48c1-8c44-46bea9f5204c.svg'
AUTHOR = 'gpt-6'

class CircleWithThreeBlades(Solo48):
    icon_id = 'circle-with-three-blades'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('propeller', 'blades', 'testflight', 'beta', 'app', 'circle', 'fan')

    def build(self):
        # Three outlined blades share a central hub and sit well inside the ring.
        self.add_arc('ring-left', (24, 4), (24, 44), radius_x=20, sweep=False)
        self.add_arc('ring-right', (24, 44), (24, 4), radius_x=20, sweep=False)
        self.add_contour('ring', 'ring-left', 'ring-right', closed=True)
        # Detached rounded strokes stand for the three separate source blades.
        self.add_line('blade-top', (24, 13), (24, 19))
        self.add_line('blade-left', (16, 30), (20, 26))
        self.add_line('blade-right', (32, 30), (28, 26))

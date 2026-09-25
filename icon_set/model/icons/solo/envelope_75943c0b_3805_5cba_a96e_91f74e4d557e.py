'Envelope: restore connected folds and rounded corners; preserve the full envelope rather than shrinking detached fragments.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '75943c0b-3805-5cba-a96e-91f74e4d557e'
SOURCE_PATH = 'pictographic-primitives/emails/envelope_75943c0b-3805-5cba-a96e-91f74e4d557e.svg'
AUTHOR = 'gpt-6'

class Envelope(Solo48):
    icon_id = 'envelope'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    categories = ('emails', 'primitives')
    aliases = ()
    keywords = ('envelope', 'emails')

    def build(self) -> None:
        # Rounded envelope shell and continuous folded flap; diagonal returns meet the flap exactly.
        self.add_line('top',(8,8),(40,8))
        self.add_arc('tr',(40,8),(44,12),radius_x=4)
        self.add_line('right',(44,12),(44,36))
        self.add_arc('br',(44,36),(40,40),radius_x=4)
        self.add_line('bottom',(40,40),(8,40))
        self.add_arc('bl',(8,40),(4,36),radius_x=4)
        self.add_line('left',(4,36),(4,12))
        self.add_arc('tl',(4,12),(8,8),radius_x=4)
        self.add_contour('shell','top','tr','right','br','bottom','bl','left','tl',closed=True)
        self.add_polyline('flap',(4,12),(14,21),(24,30),(34,21),(44,12))
        self.relate('connect','flap','shell')
        self.add_line('fold-left',(4,36),(14,21))
        self.add_line('fold-right',(44,36),(34,21))
        for f in ('fold-left','fold-right'):
            self.relate('connect',f,'flap');self.relate('connect',f,'shell')

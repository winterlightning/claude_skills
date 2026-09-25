"""Index finger presses the open pad grid. Grid uses 8-unit row/column spacing; simplify curled fingers into palm and omit floating notes. Centerline extremes (6,6)-(42,42). Human reference: full_body_ref.png round-ended continuous limbs; Lucide pointer. No detached head."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='2e9ddede-2e59-4491-8fa8-b1f79514c010'
SOURCE_PATH='pictographic-primitives/music/modern music mix touch_2e9ddede-2e59-4491-8fa8-b1f79514c010.svg'
AUTHOR='gpt-6'

class HandPlayingPadController(Solo48):
    icon_id='hand-playing-pad-controller'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "music"
    aliases=()
    keywords=('mixer', 'pad', 'controller', 'touch', 'hand', 'beat', 'electronic', 'music')

    def build(self):
        self.add_polyline('grid-outline',(22,6),(14,6),(6,6),(6,14),(6,22),(14,22))
        self.add_line('grid-column',(14,6),(14,14))
        self.add_line('grid-column-low',(14,14),(14,22))
        self.add_polyline('grid-row',(6,14),(14,14),(18,14))
        for part in ('grid-column','grid-column-low','grid-row'):
            self.relate('connect',part,'grid-outline')
        self.relate('connect','grid-column','grid-column-low')
        self.relate('connect','grid-column','grid-row')
        self.relate('connect','grid-column-low','grid-row')
        self.add_line('finger-left',(26,34),(26,18))
        self.add_arc('fingertip',(26,18),(34,18),radius_x=4)
        self.add_line('finger-palm-1',(34,18),(34,28))
        self.add_line('finger-palm-2',(34,28),(38,28))
        self.add_arc('palm-round',(38,28),(42,32),radius_x=4)
        self.add_line('wrist-right',(42,32),(42,42))
        self.add_line('wrist-left',(18,42),(10,38))
        self.add_bezier('thumb',(10,38),((6,34),(10,30),(16,31)))
        self.add_line('thumb-web',(16,31),(26,34))
        self.add_contour('hand','wrist-left','thumb','thumb-web','finger-left','fingertip','finger-palm-1','finger-palm-2','palm-round','wrist-right')

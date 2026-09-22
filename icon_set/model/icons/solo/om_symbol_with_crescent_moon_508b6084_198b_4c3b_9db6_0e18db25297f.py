"""Om with a crescent moon, explicitly requested as a SOLO48 symbol.
Square extremes (6,6)-(42,42); upper-left crescent, upper-right dot and
curved accent, lower joined lobes. The source establishes this arrangement.
Lucide moon teaches the joined outer and inner crescent contour, not its grid.
Preserve the complete subject, reduce fine irregularities of the source.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '508b6084-198b-4c3b-9db6-0e18db25297f'
SOURCE_PATH = 'pictographic-primitives/holidays/maha shivaratri om_508b6084-198b-4c3b-9db6-0e18db25297f.svg'
AUTHOR = 'gpt-6-astra'

class Symbol(Solo48):
    icon_id = 'om-symbol-with-crescent-moon'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    aliases = ('Om Symbol with Crescent Moon',)
    keywords = ('om','symbol','crescent','moon','maha shivaratri')

    def build(self):
        self.add_arc('moon-upper',(22,6),(6,12),radius_x=16,radius_y=6,sweep=False)
        self.add_arc('moon-lower',(6,12),(22,18),radius_x=16,radius_y=6,sweep=False)
        self.add_bezier('moon-inner',(22,18),((14,15),(14,9),(22,6)))
        self.add_contour('moon','moon-upper','moon-lower','moon-inner',closed=True)
        self.add_dot('dot',(36,6))
        self.add_bezier('accent',(30,14),((32,18),(38,18),(42,14)))
        self.add_bezier('upper-lobe',(8,30),((18,22),(24,30),(16,34)))
        self.add_bezier('lower-lobe',(16,34),((26,34),(20,46),(8,40)))
        self.add_contour('left-lobes','upper-lobe','lower-lobe')
        self.add_bezier('bridge',(16,34),((28,36),(26,26),(34,26)))
        self.add_arc('right-upper',(34,26),(42,34),radius_x=8)
        self.add_arc('right-lower',(42,34),(34,42),radius_x=8)
        self.add_bezier('right-tip',(34,42),((32,42),(30,40),(30,38)))
        self.add_contour('right-lobe','bridge','right-upper','right-lower','right-tip')
        self.relate('connect','upper-lobe','lower-lobe','bridge')

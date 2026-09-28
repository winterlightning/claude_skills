'Sync arrows: two matched curved turns and open arrowheads, with rotational balance. Lucide rotate-cw informs the construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18f9d573-e7b3-5500-9011-0bd7ffb6dcc0'
SOURCE_PATH = 'pictographic-primitives/interface-essential/button syncing_18f9d573-e7b3-5500-9011-0bd7ffb6dcc0.svg'
AUTHOR = 'gpt-6'

class ButtonSyncing(Solo48):
    icon_id = 'button-syncing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('button', 'syncing', 'interface-essential')

    def build(self) -> None:
        # Two matched smooth turning arcs, mirrored around (24,24).
        for label,flip in (('upper',False),('lower',True)):
            def p(x,y): return (48-x,48-y) if flip else (x,y)
            self.add_bezier(label+'-start',p(8,28),(p(6,26),p(6,25),p(6,24)))
            self.add_arc(label+'-turn',p(6,24),p(24,6),radius_x=18)
            self.add_bezier(label+'-finish',p(24,6),(p(29,6),p(33,8),p(36,12)))
            self.add_contour(label,label+'-start',label+'-turn',label+'-finish')
            self.add_polyline(label+'-head',p(36,6),p(36,12),p(28,12))
            self.relate('connect',label,label+'-head')

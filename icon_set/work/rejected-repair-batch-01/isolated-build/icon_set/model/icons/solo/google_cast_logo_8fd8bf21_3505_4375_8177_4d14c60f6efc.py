"""A rounded screen outline open at its lower left corner, where a small quarter-dot and two nested broadcast arcs fill the gap.

Plan: Open rounded screen; concentric quarter arcs share lower-left centre; radius step 9.
Keyshape: HRECT_L; exact SOLO48 envelope from the contract.
Construction reference: cast: open frame, quarter arcs and origin dot.
Simplification: Quarter wedge becomes a stroke-wide dot.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8fd8bf21-3505-4375-8177-4d14c60f6efc'
SOURCE_PATH = 'pictographic-primitives/logos/google cast logo_8fd8bf21-3505-4375-8177-4d14c60f6efc.svg'
AUTHOR = 'gpt-6'


class GoogleCastLogo(Solo48):
    icon_id = 'google-cast-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('google-cast', 'chromecast', 'cast', 'screen', 'logo', 'brand', 'streaming')

    def build(self):
        self.add_line('left', (4,13),(4,12))
        self.add_arc('tl',(4,12),(8,8),radius_x=4)
        self.add_line('top',(8,8),(40,8))
        self.add_arc('tr',(40,8),(44,12),radius_x=4)
        self.add_line('right',(44,12),(44,36))
        self.add_arc('br',(44,36),(40,40),radius_x=4)
        self.add_line('bottom',(40,40),(31,40))
        self.add_contour('screen','left','tl','top','tr','right','br','bottom')
        for i,r in enumerate((9,18)):
            self.add_arc(f'broadcast-{i}',(4,40-r),(4+r,40),radius_x=r)
        self.add_dot('origin',(4,40))

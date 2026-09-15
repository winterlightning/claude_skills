"""The wordmark HBO in bold rounded capitals, the B and O set closely together.

Plan: Three condensed capital letters; narrow elliptical B allows 9-unit gaps to H and O.
Keyshape: HRECT_L; exact SOLO48 envelope from the contract.
Construction reference: No useful exact wordmark match; shared letter widths and capsule O.
Simplification: Letters narrowed, especially the B bowls, to preserve the complete horizontal HBO wordmark.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5e8442fe-8bb0-4705-af7a-bf422ce50632'
SOURCE_PATH = 'pictographic-primitives/logos/hbo logo_5e8442fe-8bb0-4705-af7a-bf422ce50632.svg'
AUTHOR = 'gpt-6'


class HboLogo(Solo48):
    icon_id = 'hbo-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('hbo', 'tv', 'streaming', 'wordmark', 'logo', 'brand', 'entertainment')

    def build(self):
        for n,x in [('h-left',4),('h-right',12)]:
            self.add_polyline(n,(x,8),(x,24),(x,40))
        self.add_line('h-bar',(4,24),(12,24))
        self.relate('connect','h-left','h-bar')
        self.relate('connect','h-right','h-bar')
        self.add_polyline('b-stem',(21,8),(21,24),(21,40))
        for i,y in enumerate((8,24)):
            self.add_arc(f'b-bowl-{i}',(21,y),(21,y+16),radius_x=6,radius_y=8)
            self.relate('connect','b-stem',f'b-bowl-{i}')
        self.relate('connect','b-bowl-0','b-bowl-1')
        self.add_arc('o-top',(36,12),(44,12),radius_x=4)
        self.add_line('o-right',(44,12),(44,36))
        self.add_arc('o-bottom',(44,36),(36,36),radius_x=4)
        self.add_line('o-left',(36,36),(36,12))
        self.add_contour('o','o-top','o-right','o-bottom','o-left',closed=True)

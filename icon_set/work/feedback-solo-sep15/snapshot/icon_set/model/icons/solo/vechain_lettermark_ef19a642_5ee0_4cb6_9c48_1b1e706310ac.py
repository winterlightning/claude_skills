"""Asymmetric outlined-left V with a rounded lower turn and single ascending right arm. VRECT_L extremes (8,4)-(40,44). Broaden the left ribbon for clearance. Preserve directional asymmetry. No exact Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='ef19a642-5ee0-4cb6-9c48-1b1e706310ac'
SOURCE_PATH='pictographic-primitives/money/virtual coin crypto vechain_ef19a642-5ee0-4cb6-9c48-1b1e706310ac.svg'
AUTHOR='gpt-6'

class VechainLettermark(Solo48):
    icon_id='vechain-lettermark'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="symbols/finance"
    aliases=()
    keywords=('vechain', 'v', 'lettermark', 'crypto', 'currency', 'ribbon')

    def build(self):
        self.add_line('left',(8,4),(20,40))
        self.add_bezier('bottom-left',(20,40),((21,43),(22,44),(24,44)))
        self.add_bezier('bottom-right',(24,44),((26,44),(27,43),(28,40)))
        self.add_line('right-bottom',(28,40),(30,34))
        self.add_line('right-top',(30,34),(40,4))
        self.add_contour('v','left','bottom-left','bottom-right','right-bottom','right-top')
        self.add_polyline('ribbon',(8,4),(18,4),(28,30),(30,34))
        self.relate('connect','v','ribbon')

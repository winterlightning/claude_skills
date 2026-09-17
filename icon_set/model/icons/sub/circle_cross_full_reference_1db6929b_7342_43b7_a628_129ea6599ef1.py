"""Full original composition: circle and inner symbol, with no parts removed.
Circle owns centre (16,16) and radius 14. Inner symbol is centred and retains
its source direction. Earlier extracted variant is preserved separately.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='1db6929b-7342-43b7-a628-129ea6599ef1'
SOURCE_PATH='pictographic-primitives/state/state remove_1db6929b-7342-43b7-a628-129ea6599ef1.svg'
AUTHOR='gpt-6'
class CircleCrossFullReference(Sub32):
    icon_id='circle-cross-full-reference'
    keyshape=Keyshape.CIRCLE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='primitives/mark'
    aliases=()
    keywords=('complete-reference','state','circle')
    def build(self):
        self.add_arc('circle-top',(2,16),(30,16),radius_x=14)
        self.add_arc('circle-bottom',(30,16),(2,16),radius_x=14)
        self.add_contour('circle','circle-top','circle-bottom',closed=True)
        self.add_line('falling',(11,11),(21,21))
        self.add_line('rising',(11,21),(21,11))
        self.relate('connect','falling','rising')

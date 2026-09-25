"""Full original composition: circle and inner symbol, with no parts removed.
Circle owns centre (16,16) and radius 14. Inner symbol is centred and retains
its source direction. Earlier extracted variant is preserved separately.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='c8cdc83b-0683-4b47-8454-a4e5b0461a29'
SOURCE_PATH='pictographic-primitives/state/circle medical cross_c8cdc83b-0683-4b47-8454-a4e5b0461a29.svg'
AUTHOR='gpt-6'
class CirclePlusFullReference(Sub32):
    icon_id='circle-plus-full-reference'
    keyshape=Keyshape.CIRCLE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'state'
    categories = ('state',)
    aliases=()
    keywords=('complete-reference','state','circle')
    def build(self):
        self.add_arc('circle-top',(2,16),(30,16),radius_x=14)
        self.add_arc('circle-bottom',(30,16),(2,16),radius_x=14)
        self.add_contour('circle','circle-top','circle-bottom',closed=True)
        self.add_line('horizontal',(9,16),(23,16))
        self.add_line('vertical',(16,9),(16,23))
        self.relate('connect','horizontal','vertical')

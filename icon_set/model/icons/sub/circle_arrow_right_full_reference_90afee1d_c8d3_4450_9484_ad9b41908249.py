"""Full original composition: circle and inner symbol, with no parts removed.
Circle owns centre (16,16) and radius 14. Inner symbol is centred and retains
its source direction. Earlier extracted variant is preserved separately.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='90afee1d-c8d3-4450-9484-ad9b41908249'
SOURCE_PATH='pictographic-primitives/state/circle arrow right_90afee1d-c8d3-4450-9484-ad9b41908249.svg'
AUTHOR='gpt-6'
class CircleArrowRightFullReference(Sub32):
    icon_id='circle-arrow-right-full-reference'
    keyshape=Keyshape.CIRCLE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'state'
    aliases=()
    keywords=('complete-reference','state','circle')
    def build(self):
        self.add_arc('circle-top',(2,16),(30,16),radius_x=14)
        self.add_arc('circle-bottom',(30,16),(2,16),radius_x=14)
        self.add_contour('circle','circle-top','circle-bottom',closed=True)
        self.add_line('shaft',(9,16),(23,16))
        self.add_polyline('head',(17,10),(23,16),(17,22))
        self.relate('connect','shaft','head')

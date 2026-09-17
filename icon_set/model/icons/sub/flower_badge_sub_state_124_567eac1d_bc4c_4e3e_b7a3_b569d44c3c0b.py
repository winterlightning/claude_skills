"""Flower Badge: A closed flower-shaped outline has six broad rounded lobes arranged around an empty centre. Its upper and lower lobes sit on the vertical axis, with paired lobes spreading left and right.

Construction: Six broad rounded lobes form the original empty flower badge; no central mark added.
Keyshape: CIRCLE; six circular lobes reach the radial SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '567eac1d-bc4c-4e3e-b7a3-b569d44c3c0b'
SOURCE_PATH = 'pictographic-primitives/state/flower badge_567eac1d-bc4c-4e3e-b7a3-b569d44c3c0b.svg'
AUTHOR = 'gpt-6'


class FlowerBadgeSubState124(Sub32):
    icon_id = 'flower-badge-sub-state-124'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('flower', 'badge', 'closed', 'shaped', 'outline', 'six', 'broad', 'rounded')

    def build(self):
        self.add_arc('top',(10,8),(22,8),radius_x=6)
        self.add_arc('upper-right',(22,8),(28,16),radius_x=6)
        self.add_arc('lower-right',(28,16),(22,24),radius_x=6)
        self.add_arc('bottom',(22,24),(10,24),radius_x=6)
        self.add_arc('lower-left',(10,24),(4,16),radius_x=6)
        self.add_arc('upper-left',(4,16),(10,8),radius_x=6)
        self.add_contour('flower','top','upper-right','lower-right','bottom','lower-left','upper-left',closed=True)

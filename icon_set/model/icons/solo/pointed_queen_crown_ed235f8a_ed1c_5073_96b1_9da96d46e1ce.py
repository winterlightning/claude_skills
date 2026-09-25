"""A pointed queen crown with three tips above an elliptical lower rim.
Live centerline extremes: SQUARE (6,6)-(42,42); HRECT_L (4,8)-(44,40);
VRECT_L (8,4)-(40,44). Lucide crown informs construction, source sets subject.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='ed235f8a-ed1c-5073-96b1-9da96d46e1ce'
SOURCE_PATH='pictographic-primitives/rewards/vip crown queen_ed235f8a-ed1c-5073-96b1-9da96d46e1ce.svg'
AUTHOR='gpt-6'
class PointedQueenCrown(Solo48):
    icon_id='pointed-queen-crown'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'rewards'
    aliases=()
    keywords=('reward','celebration','pointed-queen-crown')
    def build(self) -> None:
        self.add_polyline('points',(10,34),(4,16),(14,24),(24,8),(34,24),(44,16),(38,34))
        self.add_arc('rim-front',(38,34),(10,34),radius_x=14,radius_y=6)
        self.add_arc('rim-back',(10,34),(38,34),radius_x=14,radius_y=6)
        self.add_contour('rim','rim-front','rim-back',closed=True)
        self.relate('connect','points','rim')

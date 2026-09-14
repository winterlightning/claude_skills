"""A rounded royal crown with two outer lobes, a central panel and an attached cross.
Live centerline extremes: SQUARE (6,6)-(42,42); HRECT_L (4,8)-(44,40);
VRECT_L (8,4)-(40,44). Lucide crown informs construction, source sets subject.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='4de358a3-f17f-45b3-9bc7-b37ac195220b'
SOURCE_PATH='pictographic-primitives/rewards/vip crown king_4de358a3-f17f-45b3-9bc7-b37ac195220b.svg'
AUTHOR='gpt-6'
class RoyalCrownWithCross(Solo48):
    icon_id='royal-crown-with-cross'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/award'
    aliases=()
    keywords=('reward','celebration','royal-crown-with-cross')
    def build(self) -> None:
        self.add_line('cross-stem',(24,4),(24,16))
        self.add_line('cross-bar',(18,8),(30,8))
        self.relate('connect','cross-stem','cross-bar')
        self.add_arc('outer-left',(24,16),(8,24),radius_x=16,radius_y=8,sweep=False)
        self.add_line('left-lower',(8,24),(12,36))
        self.add_polyline('band',(12,36),(36,36),(36,44),(12,44),closed=True)
        self.add_line('right-lower',(36,36),(40,24))
        self.add_arc('outer-right',(40,24),(24,16),radius_x=16,radius_y=8,sweep=False)
        self.add_contour('dome','outer-left','left-lower')
        self.add_contour('dome-right','right-lower','outer-right')
        self.add_arc('panel-left',(18,28),(24,16),radius_x=6,radius_y=12)
        self.add_arc('panel-right',(24,16),(30,28),radius_x=6,radius_y=12)
        self.add_contour('panel','panel-left','panel-right')
        self.relate('connect','panel','cross-stem')
        self.relate('connect','cross-stem','dome')
        self.relate('connect','cross-stem','dome-right')
        self.relate('connect','panel','dome')
        self.relate('connect','panel','dome-right')
        self.relate('connect','dome','dome-right')
        self.relate('connect','band','dome')
        self.relate('connect','band','dome-right')

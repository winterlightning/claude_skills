"""Dizzy face with spiral eyes.
Plan: HRECT_L uses (4,8)-(44,40) to accommodate large opposing curls.
Design changes: One full turn per eye replaces the denser winding. The outer curls meet the forehead and jaw at shared nodes. The open mouth is a complete radius-3 circle.
References: Original reference supplies opposing spiral directions and open mouth. No local Lucide spiral match found. Human user.svg reviewed; no body is depicted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='aa0c1f8e-f7ca-4bf9-adf6-7f6f74e5b90a'
SOURCE_PATH='pictographic-primitives/_uncategorized_17/face dizzy_aa0c1f8e-f7ca-4bf9-adf6-7f6f74e5b90a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='dizzy-face-with-spiral-eyes-solo'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='people/expressions'
    aliases=()
    keywords=('dizzy','spiral','face')
    def build(self):
        for i,(x,s) in enumerate(((13,1),(35,-1))):
            q=lambda dx,y:(x+s*dx,y)
            self.add_arc(f'eye-{i}-lower',q(0,29),q(-9,20),radius_x=9,sweep=s>0)
            self.add_arc(f'eye-{i}-upper',q(-9,20),q(0,11),radius_x=9,sweep=s>0)
            self.add_arc(f'eye-{i}-inner',q(0,11),q(5,16),radius_x=5,sweep=s>0)
            self.add_arc(f'eye-{i}-end',q(5,16),q(0,21),radius_x=5,sweep=s>0)
            self.add_contour(f'eye-{i}',f'eye-{i}-lower',f'eye-{i}-upper',f'eye-{i}-inner',f'eye-{i}-end')
        self.add_arc('forehead',(13,11),(35,11),radius_x=11,radius_y=3)
        self.add_arc('jaw',(13,29),(35,29),radius_x=11,radius_y=11,sweep=False)
        for eye in ['eye-0','eye-1']:
            self.relate('connect','forehead',eye)
            self.relate('connect','jaw',eye)
        self.add_arc('mouth-top',(21,28),(27,28),radius_x=3)
        self.add_arc('mouth-bottom',(27,28),(21,28),radius_x=3)
        self.add_contour('mouth','mouth-top','mouth-bottom',closed=True)
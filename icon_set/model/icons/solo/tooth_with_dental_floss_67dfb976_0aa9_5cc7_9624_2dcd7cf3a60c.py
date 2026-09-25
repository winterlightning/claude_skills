"""Tooth with Dental Floss.

Plan: One small molar with floss across its middle. Shared molar cusps and root radii; curl ends are deliberately asymmetric. Bounds (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '67dfb976-0aa9-5cc7-9624-2dcd7cf3a60c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/dental floss tooth_67dfb976-0aa9-5cc7-9624-2dcd7cf3a60c.svg'
AUTHOR = 'gpt-6'


class ToothWithDentalFloss(Solo48):
    icon_id = 'tooth-with-dental-floss'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('tooth', 'with', 'dental', 'floss')

    def build(self):
        self.add_arc('crown-l',(12,16),(20,8),radius_x=8)
        self.add_arc('cusp-l',(20,8),(24,10),radius_x=4,radius_y=2,sweep=False)
        self.add_arc('cusp-r',(24,10),(28,8),radius_x=4,radius_y=2,sweep=False)
        self.add_arc('crown-r',(28,8),(36,16),radius_x=8)
        self.add_line('right1',(36,16),(36,24))
        self.add_line('right2',(36,24),(36,36))
        self.add_arc('root-r',(36,36),(28,36),radius_x=4)
        self.add_arc('cleft-r',(28,36),(24,34),radius_x=4,radius_y=2,sweep=False)
        self.add_arc('cleft-l',(24,34),(20,36),radius_x=4,radius_y=2,sweep=False)
        self.add_arc('root-l',(20,36),(12,36),radius_x=4)
        self.add_line('left2',(12,36),(12,24))
        self.add_line('left1',(12,24),(12,16))
        self.add_contour('tooth','crown-l','cusp-l','cusp-r','crown-r','right1','right2','root-r','cleft-r','cleft-l','root-l','left2','left1',closed=True)

        self.add_arc('floss-left',(4,32),(12,24),radius_x=8)
        self.add_line('floss-middle',(12,24),(36,24))
        self.add_arc('floss-right',(36,24),(44,16),radius_x=8,sweep=False)
        self.add_contour('floss','floss-left','floss-middle','floss-right')
        self.relate('connect','floss','tooth')

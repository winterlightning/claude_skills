"""Vibrating Massage Gun.

Plan: Ball head, compact horizontal housing and downward grip form one device. Two vibration strokes flank the ball. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f17b43aa-52f0-4ce6-a7db-95a18f8a62be'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/massage stick electronic_f17b43aa-52f0-4ce6-a7db-95a18f8a62be.svg'
AUTHOR = 'gpt-6'


class VibratingMassageGun(Solo48):
    icon_id = 'vibrating-massage-gun'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('vibrating', 'massage', 'gun')

    def build(self):
        self.add_arc('ball-top',(6,24),(18,24),radius_x=6)
        self.add_arc('ball-bottom',(18,24),(6,24),radius_x=6)
        self.add_contour('ball','ball-top','ball-bottom',closed=True)
        self.add_line('shaft',(18,24),(28,24))
        self.add_polyline('housing',(28,24),(28,16),(42,16),(42,30),(38,30),(38,42),(30,42),(30,30),(28,30),(28,24))
        self.relate('connect','shaft','ball')
        self.relate('connect','shaft','housing')
        self.add_polyline('vibration-top',(6,8),(10,6),(14,8))
        self.add_polyline('vibration-bottom',(6,40),(10,42),(14,40))

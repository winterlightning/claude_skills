"""Charging bolt between mirrored signal waves.
Plan: Wide horizontal composition. Open bolt and one mirrored wave pair preserve wireless charging.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c8b3d9a1-bb0f-4df5-b706-4b00986008d6'
SOURCE_PATH = 'pictographic-primitives/mobile/charging flash wave_c8b3d9a1-bb0f-4df5-b706-4b00986008d6.svg'
AUTHOR = 'gpt-6'

PARENT_RESULT = 'icon_set/work/primitive-make-ray/c8b3d9a1-bb0f-4df5-b706-4b00986008d6/20260923-batch07-c2bf00/result.json'

class Drawing(Solo48):
    icon_id = 'charging-flash-wave'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('charging', 'flash', 'wave')

    def build(self):
        # A coherent open lightning zigzag retains the charging direction.
        # One mirrored wave pair leaves real air around the lightning.
        self.add_polyline('flash',(26,8),(18,24),(30,24),(22,40))
        for side in [-1,1]:
            x=8 if side<0 else 40
            self.add_arc(('left' if side<0 else 'right')+'-wave',(x,10),(x,38),radius_x=4,radius_y=14,sweep=side>0)

PLAN = 'Charging bolt between mirrored signal waves. Wide horizontal composition.'
OMISSIONS = 'Closed bolt reduced to an open zigzag; inner wave pair omitted.'
CONSTRUCTION_REFERENCES = ['No useful local Lucide subject match found.']
PARENT_SOURCE = 'icon_set/model/icons/solo/charging_flash_wave_c8b3d9a1_bb0f_4df5_b706_4b00986008d6.py'

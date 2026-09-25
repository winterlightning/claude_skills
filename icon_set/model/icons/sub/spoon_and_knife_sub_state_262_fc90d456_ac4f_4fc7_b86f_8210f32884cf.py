"""Spoon and knife: retain round spoon bowl and curved knife blade. SQUARE bounds 2..30; source arrangement preserved."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'fc90d456-ac4f-4fc7-b86f-8210f32884cf'
SOURCE_PATH = 'pictographic-primitives/state/circle fork knife_fc90d456-ac4f-4fc7-b86f-8210f32884cf.svg'
AUTHOR = 'gpt-6'


class SpoonAndKnifeSubState262(Sub32):
    icon_id = 'spoon-and-knife-sub-state-262'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('fork', 'knife', 'upright', 'tined', 'stands', 'beside', 'straight', 'handle')

    def build(self):
        self.add_arc('spoon-top',(2,8),(14,8),radius_x=6)
        self.add_arc('spoon-bottom',(14,8),(2,8),radius_x=6)
        self.add_contour('spoon','spoon-top','spoon-bottom',closed=True)
        self.add_line('stem',(8,14),(8,30))
        self.relate('connect','spoon','stem')
        self.add_line('knife-back',(22,2),(22,30))
        self.add_arc('knife-blade',(22,2),(30,16),radius_x=8,radius_y=14)
        self.add_line('knife-base',(30,16),(22,16))
        self.add_contour('blade','knife-blade','knife-base')
        self.relate('connect','knife-back','blade')

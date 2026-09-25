"""Garden Hand Rake.
Plan: Diagonal shaft ends at broad crossbar with four parallel teeth. Extrema (6,6)-(42,42).
Reference: Lucide shovel: diagonal tool axis and shared blade junction.
Reduction: Rounded grip outline reduced to single diagonal handle; four teeth retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4839ccee-590f-4236-a6b4-53a4767ebe4d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/cultivator_4839ccee-590f-4236-a6b4-53a4767ebe4d.svg'
AUTHOR = 'gpt-6'

class Batch28Icon(Solo48):
    icon_id = 'hand-rake-wide-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    aliases = ()
    keywords = ('garden', 'hand', 'rake')

    def build(self):

        self.add_line('shaft',(6,6),(21,21))
        self.add_polyline('bar',(12,30),(18,24),(21,21),(24,18),(30,12))
        self.relate('connect','shaft','bar')
        for i,(x,y) in enumerate(((12,30),(18,24),(24,18),(30,12))):
            self.add_line(f'tine-{i}',(x,y),(x+12,y+12))
            self.relate('connect','bar',f'tine-{i}')

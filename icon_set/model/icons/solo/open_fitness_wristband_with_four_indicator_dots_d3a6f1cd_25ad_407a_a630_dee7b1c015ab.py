"""Smart Fitness Wristband.

Symbol plan: Open fitness cuff with four 2x2 indicator dots. One continuous C-shaped band with rounded end transitions and a broad face. Shared dot pitch 8. No useful exact Lucide match; omit top/bottom panel seams.
Keyshape SQUARE; exact visible bounds (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd3a6f1cd-25ad-407a-a630-dee7b1c015ab'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/devices/wearable smart watch app_d3a6f1cd-25ad-407a-a630-dee7b1c015ab.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'open-fitness-wristband-with-four-indicator-dots'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    aliases = ()
    keywords = ('smart', 'fitness', 'wristband')

    def build(self):
        self.add_arc('outer-top',(6,24),(24,6),radius_x=18)
        self.add_arc('outer-tr',(24,6),(42,16),radius_x=18,radius_y=10)
        self.add_line('end-tr',(42,16),(40,16))
        
        self.add_arc('inner',(40,16),(40,32),radius_x=6,radius_y=8,sweep=False)
        self.add_line('end-br',(40,32),(42,32))
        self.add_arc('outer-br',(42,32),(24,42),radius_x=18,radius_y=10)
        self.add_arc('outer-bottom',(24,42),(6,24),radius_x=18)
        self.add_contour('band','outer-top','outer-tr','end-tr','inner','end-br','outer-br','outer-bottom',closed=True)
        for i,x in enumerate((16,24)):
            for j,y in enumerate((20,28)):self.add_dot(f'indicator-{i}-{j}',(x,y))

'Eight broad teeth are a fourfold rotational pattern with an axial and diagonal tooth per quadrant. Lucide settings inspired concentric hub and repeated perimeter. Retain eight teeth.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'df0f1ced-b7de-421f-b0b9-22b5791aa002'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/h6_df0f1ced-b7de-421f-b0b9-22b5791aa002.svg'
AUTHOR = 'gpt-6'

class Result(Solo48):
    icon_id = 'eight-tooth-gear-batch-057'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/tools'
    aliases = ()
    keywords = ('gear', 'cog', 'settings', 'mechanism', 'wheel', 'machine')

    def build(self):
        quarter=[(20,6),(28,6),(28,11),(30,12),(34,8),(40,14),(36,18),(37,20)]
        points=[]
        for turn in range(4):
            for x,y in quarter:
                x,y=x-24,y-24
                for _ in range(turn):x,y=-y,x
                points.append((24+x,24+y))
        self.add_polyline('teeth',*points,closed=True)
        r=5
        self.add_arc('hub-top',(24-r,24),(24+r,24),radius_x=r)
        self.add_arc('hub-bottom',(24+r,24),(24-r,24),radius_x=r)
        self.add_contour('hub','hub-top','hub-bottom',closed=True)

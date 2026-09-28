"""Side view grasshopper: long abdomen, enlarged angular jumping leg, small foreleg and antenna pair. Lucide bug informs minimal attached appendages; retain natural directional asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '772d4acb-3de3-45c5-8eba-9867d0d56352'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/grasshopper_772d4acb-3de3-45c5-8eba-9867d0d56352.svg'
AUTHOR = 'gpt-6'

class Result(Solo48):
    icon_id = 'side-view-grasshopper-batch-057'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('grasshopper', 'insect', 'antennae', 'legs', 'nature', 'bug')

    def build(self):
        # Open tapered abdomen avoids enclosing tiny pockets beneath the thigh.
        joint=(24,28)
        self.add_line('back',joint,(32,20))
        self.add_arc('head',(32,20),(44,20),radius_x=6)
        self.add_arc('chest',(44,20),(32,28),radius_x=12,radius_y=8)
        self.add_line('belly',(32,28),joint)
        self.add_contour('body','back','head','chest','belly',closed=True)
        self.add_polyline('hindleg',joint,(12,16),(8,28),(4,40))
        self.add_polyline('abdomen',(4,28),(8,28),joint)
        self.add_polyline('foreleg',(32,28),(36,40),(44,40))
        self.add_line('antenna-left',(32,20),(28,8))
        self.add_line('antenna-right',(38,14),(40,8))
        for part in ('hindleg','abdomen','foreleg','antenna-left','antenna-right'):
            self.relate('connect','body',part)
        self.relate('connect','hindleg','abdomen')

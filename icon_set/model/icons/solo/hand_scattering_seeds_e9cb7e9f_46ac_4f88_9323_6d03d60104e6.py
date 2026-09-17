"""Hand Sowing Seeds.
Plan: Leftward hand silhouette with thumb notch and three falling seeds. Extrema (4,8)-(44,40).
Reference: Lucide hand: coherent outer silhouette with thumb notch; human_ref/full_body_ref.png governs minimal anatomy.
Reduction: Two fingers reduced to a single fingertip contour and broad thumb notch; three falling seed marks retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e9cb7e9f-46ac-4f88-9323-6d03d60104e6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/seed hand_e9cb7e9f-46ac-4f88-9323-6d03d60104e6.svg'
AUTHOR = 'gpt-6'

class Batch28Icon(Solo48):
    icon_id = 'hand-scattering-seeds'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/agriculture"
    aliases = ()
    keywords = ('hand', 'sowing', 'seeds')

    def build(self):

        self.add_polyline('hand',(44,10),(36,10),(28,8),(4,18),(8,26),(22,20),(22,28),(36,28),(44,28))
        self.add_line('cuff',(36,10),(36,28));self.relate('connect','cuff','hand')
        self.add_line('seed-0',(4,36),(4,40))
        self.add_line('seed-1',(18,38),(20,40))
        self.add_line('seed-2',(32,38),(31,40))

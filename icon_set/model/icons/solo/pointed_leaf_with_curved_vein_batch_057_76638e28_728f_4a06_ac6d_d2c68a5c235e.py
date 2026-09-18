'Broad pointed leaf with connected curved vein and stem. Lucide leaf informs one organic contour and one vein; deliberate right-leaning tip. Omit secondary veins.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '76638e28-728f-4a06-ac6d-d2c68a5c235e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/green_76638e28-728f-4a06-ac6d-d2c68a5c235e.svg'
AUTHOR = 'gpt-6'

class Result(Solo48):
    icon_id = 'pointed-leaf-with-curved-vein-batch-057'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'nature/plants'
    aliases = ()
    keywords = ('leaf', 'nature', 'plant', 'vein', 'botanical', 'foliage')

    def build(self):
        self.add_arc('left-bottom',(16,36),(8,24),radius_x=8,radius_y=12)
        self.add_arc('left-top',(8,24),(40,4),radius_x=32,radius_y=20)
        self.add_line('edge',(40,4),(40,20))
        self.add_arc('right-bottom',(40,20),(16,36),radius_x=24,radius_y=16)
        self.add_contour('blade','left-bottom','left-top','edge','right-bottom',closed=True)
        self.add_arc('vein',(16,36),(26,22),radius_x=32)
        self.add_line('stem',(16,36),(12,44))
        self.relate('connect','blade','vein')
        self.relate('connect','blade','stem')
        self.relate('connect','vein','stem')

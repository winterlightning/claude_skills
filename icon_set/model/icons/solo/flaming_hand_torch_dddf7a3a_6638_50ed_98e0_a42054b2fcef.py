"""Hand torch with bent teardrop flame meeting the rim and flared cup narrowing to handle. VRECT_XL centerlines 8,4–40,44. Lucide flame informs single tongue; no useful exact local torch match."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dddf7a3a-6638-50ed-98e0-a42054b2fcef'
SOURCE_PATH = 'pictographic-primitives/social/trends torch_dddf7a3a-6638-50ed-98e0-a42054b2fcef.svg'
AUTHOR = 'gpt-6'

class FlamingHandTorch(Solo48):
    icon_id = 'flaming-hand-torch'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "social"
    categories = ("social", "primitives")
    aliases = ()
    keywords = ('torch', 'flame', 'fire', 'handle', 'cup', 'burning')

    def build(self):
        self.add_arc('flame-left',(22,4),(16,15),radius_x=14,sweep=False)
        self.add_arc('flame-base-left',(16,15),(24,22),radius_x=8,radius_y=7,sweep=False)
        self.add_arc('flame-base-right',(24,22),(32,15),radius_x=8,radius_y=7,sweep=False)
        self.add_arc('flame-right',(32,15),(22,4),radius_x=14,sweep=False)
        self.add_contour('flame','flame-left','flame-base-left','flame-base-right','flame-right',closed=True)
        self.add_polyline('cup-left',(8,22),(16,32),(20,32),(20,44))
        self.add_line('handle-bottom',(20,44),(28,44))
        self.add_polyline('cup-right',(28,44),(28,32),(32,32),(40,22))
        self.add_polyline('cup-rim',(40,22),(24,22),(8,22))
        self.relate('connect','cup-left','handle-bottom')
        self.relate('connect','handle-bottom','cup-right')
        self.relate('connect','cup-right','cup-rim')
        self.relate('connect','cup-rim','cup-left')
        self.relate('connect','flame','cup-rim')


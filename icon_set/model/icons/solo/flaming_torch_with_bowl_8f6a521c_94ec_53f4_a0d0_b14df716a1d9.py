"""Broad shallow torch bowl under three flame tips, with long handle. VRECT_XL centerlines 8,4–40,44. Lucide flame informs asymmetric tongues; reduce tapered handle to a single stroke."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8f6a521c-94ec-53f4-a0d0-b14df716a1d9'
SOURCE_PATH = 'pictographic-primitives/social/trends torch_8f6a521c-94ec-53f4-a0d0-b14df716a1d9.svg'
AUTHOR = 'gpt-6'

class FlamingTorchWithBowl(Solo48):
    icon_id = 'flaming-torch-with-bowl'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "social"
    categories = ("social", "primitives")
    aliases = ()
    keywords = ('torch', 'flame', 'fire', 'handle', 'bowl', 'burning')

    def build(self):
        self.add_polyline('flame-left',(8,22),(8,16),(14,10),(18,16))
        self.add_arc('flame-rise',(18,16),(28,4),radius_x=12)
        self.add_arc('flame-fall',(28,4),(32,16),radius_x=12,sweep=False)
        self.add_polyline('flame-right',(32,16),(36,12),(40,17),(40,22))
        self.relate('connect','flame-left','flame-rise')
        self.relate('connect','flame-rise','flame-fall')
        self.relate('connect','flame-fall','flame-right')
        self.add_line('bowl-rim',(8,22),(40,22))
        self.add_arc('bowl',(40,22),(8,22),radius_x=16,radius_y=6)
        self.add_line('handle',(24,28),(24,44))
        self.relate('connect','bowl','bowl-rim')
        self.relate('connect','bowl','handle')
        self.relate('connect','flame-left','bowl-rim')
        self.relate('connect','flame-right','bowl-rim')
        self.relate('connect','flame-left','bowl')
        self.relate('connect','flame-right','bowl')

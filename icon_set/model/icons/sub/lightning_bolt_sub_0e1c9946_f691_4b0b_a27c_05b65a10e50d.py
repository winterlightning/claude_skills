"""Lightning Bolt: A tall outlined lightning bolt follows a sharp zigzag between an upper-right tip and lower-left tip. Two inward notches create the offset middle section, leaving the interior open.

Construction: One six-corner lightning outline, with opposite inward notches and diagonal directional tips.
Keyshape: VRECT_L; extremes follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0e1c9946-f691-4b0b-a27c-05b65a10e50d'
SOURCE_PATH = 'pictographic-primitives/state/lightning_0e1c9946-f691-4b0b-a27c-05b65a10e50d.svg'
AUTHOR = 'gpt-6'


class LightningBoltSub(Sub32):
    icon_id = 'lightning-bolt-sub'
    keyshape = Keyshape.VRECT_L
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "state"
    aliases = ()
    keywords = ('lightning', 'bolt', 'tall', 'outlined', 'follows', 'sharp', 'zigzag', 'between')

    def build(self):
        self.add_polyline("bolt",(22,2),(6,18),(14,18),(10,30),(26,14),(18,14),closed=True)

"""Smile: A broad upward-curving mouth forms a shallow bowl without eyes or a separate face outline. Generate this component alone; exclude Unlocked Padlock Frame.

Construction: One open upward smile curve, with no invented eyes or enclosing face.
Keyshape: HRECT_S; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '747eeb27-6e8b-4476-a9c1-b2824cfdbf79'
SOURCE_PATH = 'pictographic-primitives/state/unlock 1_747eeb27-6e8b-4476-a9c1-b2824cfdbf79.svg'
AUTHOR = 'gpt-6'


class SmileSub(Sub32):
    icon_id = 'smile-sub'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('smile', 'broad', 'upward', 'curving', 'mouth', 'forms', 'shallow', 'bowl')

    def build(self):
        self.add_arc('smile',(2,10),(30,10),radius_x=14,radius_y=12,sweep=False)

"""Telephone handset diagonal.

Construction reference: phone.
Broad cups and bowed grip; no button detail.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = 'a0f4279e-ab4c-40c4-82b8-60c989d1f1d1'
SOURCE_PATH = 'pictographic-primitives/other/phone 1_a0f4279e-ab4c-40c4-82b8-60c989d1f1d1.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'telephone-handset-diagonal-solo-a0f4279e'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ('telephone-handset-diagonal',)
    keywords = ('telephone', 'handset', 'diagonal')

    def build(self):
        # Receiver cups at opposite ends of a bowed grip; deliberate diagonal asymmetry.
        path(self,'receiver',(6,10),[('A',(10,6),4,4,True),('L',(14,6)),('L',(22,14)),('L',(17,19)),('A',(29,31),20,20,False),('L',(34,26)),('L',(42,34)),('L',(42,38)),('A',(38,42),4,4,True),('A',(6,10),32,32,True)],True)

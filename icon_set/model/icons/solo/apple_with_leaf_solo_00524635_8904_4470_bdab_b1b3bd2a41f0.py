"""Apple with leaf.

Construction reference: apple.
The tiny separate leaf is reduced to the short upward stem to preserve open crown spacing.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = '00524635-8904-4470-bdab-b1b3bd2a41f0'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/apple whole_00524635-8904-4470-bdab-b1b3bd2a41f0.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'apple-with-leaf-solo-00524635'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('apple-with-leaf',)
    keywords = ('apple', 'with', 'leaf')

    def build(self):
        # Broad apple, shallow crown/bottom notches, and attached stem.
        path(self,'apple',(24,18),[('A',(16,16),10,6,False),('A',(6,26),10,10,False),('A',(16,42),10,16,False),('L',(24,40)),('L',(32,42)),('A',(42,26),10,16,False),('A',(32,16),10,10,False),('A',(24,18),10,6,False)],True)
        self.add_line('stem',(24,18),(24,6))
        self.relate('connect','apple','stem')

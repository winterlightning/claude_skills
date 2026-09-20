"""Speech bubble left tail.

Construction reference: message-square.
Tail is deliberately left of center. No interior key or medical cross.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = 'eb0b6680-3f5b-40fd-9a39-04012841c110'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/message key_eb0b6680-3f5b-40fd-9a39-04012841c110.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'speech-bubble-left-tail-solo-eb0b6680'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('speech-bubble-left-tail',)
    keywords = ('speech', 'bubble', 'left', 'tail')

    def build(self):
        # Coherent bubble silhouette and downward left tail.
        path(self,'bubble',(8,8),[('L',(40,8)),('A',(44,12),4,4,True),('L',(44,28)),('A',(40,32),4,4,True),('L',(24,32)),('L',(16,40)),('L',(16,32)),('L',(8,32)),('A',(4,28),4,4,True),('L',(4,12)),('A',(8,8),4,4,True)],True)

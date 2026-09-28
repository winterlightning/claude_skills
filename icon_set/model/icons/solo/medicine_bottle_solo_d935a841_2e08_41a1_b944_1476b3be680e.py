"""Medicine bottle.

Construction reference: pill-bottle.
Broad cap and plain straight bottle body.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = 'd935a841-2e08-41a1-b944-1476b3be680e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/prescription bottle cross_d935a841-2e08-41a1-b944-1476b3be680e.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'medicine-bottle-solo-d935a841'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ('medicine-bottle',)
    keywords = ('medicine', 'bottle')

    def build(self):
        # Wide cap, inset straight body, shared shoulder attachment points.
        self.add_polyline('cap',(8,4),(40,4),(40,12),(32,12),(16,12),(8,12),closed=True)
        path(self,'body',(16,12),[('L',(16,16)),('L',(10,20)),('L',(10,40)),('A',(14,44),4,4,False),('L',(34,44)),('A',(38,40),4,4,False),('L',(38,20)),('L',(32,16)),('L',(32,12))])
        self.relate('connect','cap','body')
        self.add_polyline('cross-h',(19,30),(24,30),(29,30))
        self.add_polyline('cross-v',(24,24),(24,30),(24,35))
        self.relate('connect','cross-h','cross-v')

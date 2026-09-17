"""Three Stacked Layers.

Symbol plan: Three mirrored parallel layers; repeated lower V contours use 10-unit vertical pitch. Lucide layers informs diamond plus open edges.
Keyshape: SQUARE; exact visible bounds (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3a01a19c-1ff6-54a1-a219-1e167aa29e07'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/layers stacked_3a01a19c-1ff6-54a1-a219-1e167aa29e07.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'three-diamond-layers-with-open-lower-edges'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/design"
    aliases = ()
    keywords = ('three', 'stacked', 'layers')

    def build(self):
        a=24;half=18
        self.add_polyline('top',(a,6),(a+half,14),(a,22),(a-half,14),closed=True)
        for i in range(2):
            y=24+i*10
            self.add_polyline(f'layer-{i}',(a-half,y),(a,y+8),(a+half,y))

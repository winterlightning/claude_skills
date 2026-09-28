"""Lit Candle on Holder."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '33d4a9fb-1107-5824-af8f-b4090368c880'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/fire/candle_33d4a9fb-1107-5824-af8f-b4090368c880.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'candle-in-shallow-dish'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'fire'
    categories = ('fire', 'primitives')
    aliases = ()
    keywords = ('candle', 'flame', 'holder', 'dish', 'light', 'fire', 'wax')

    def build(self):
        # Plan: Centered pointed flame, wick and pillar on shallow curved dish. Shared axis and symmetric dish. Lucide rounded joins. Bounds (8,4)-(40,44).
        axis=24
        self.add_bezier('fire',(axis,4),((27,8),(29,10),(29,13)),((29,16),(27,18),(axis,18)),((21,18),(19,16),(19,13)),((19,10),(21,8),(axis,4)))
        self.add_contour('flame','fire',closed=True)
        self.add_line('wick',(axis,18),(axis,26))
        self.add_polyline('candle',(16,35),(16,26),(axis,26),(32,26),(32,35))
        self.relate('connect','wick','flame')
        self.relate('connect','wick','candle')
        self.add_line('rim-1',(8,35),(16,35))
        self.add_line('rim-2',(16,35),(32,35))
        self.add_line('rim-3',(32,35),(40,35))
        self.add_bezier('dish',(40,35),((38,41),(36,44),(30,44)),((26,44),(22,44),(18,44)),((12,44),(10,41),(8,35)))
        self.add_contour('holder','rim-1','rim-2','rim-3','dish',closed=True)
        self.relate('connect','candle','holder')

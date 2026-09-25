"""Surgical Scalpel.

Plan: Diagonal surgical blade and rounded handle share neck endpoints. Lucide pill informs handle arc. Bounds (6,6)-(42,42). Deliberate blade tip corner.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c5955135-2594-4186-babf-e5e0951b1a10'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/instrument scalpel_c5955135-2594-4186-babf-e5e0951b1a10.svg'
AUTHOR = 'gpt-6'


class SurgicalScalpel(Solo48):
    icon_id = 'surgical-scalpel'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('surgical', 'scalpel')

    def build(self):
        self.add_line('handle-left',(22,22),(32,6))
        self.add_arc('handle-cap',(32,6),(42,16),radius_x=10)
        self.add_line('handle-right',(42,16),(28,30))
        self.add_line('neck',(28,30),(22,22))
        self.add_contour('handle','handle-left','handle-cap','handle-right','neck',closed=True)
        self.add_line('blade-spine',(22,22),(6,42))
        self.add_arc('blade-edge',(6,42),(28,30),radius_x=22,radius_y=12,sweep=False)
        self.add_contour('blade','blade-spine','blade-edge')
        self.relate('connect','blade','handle')

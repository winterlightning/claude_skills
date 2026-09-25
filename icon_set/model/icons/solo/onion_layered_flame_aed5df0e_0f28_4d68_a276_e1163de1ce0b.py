"""Stylized Fire Flame."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aed5df0e-0f28-4d68-a276-e1163de1ce0b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/fire/onion slice_aed5df0e-0f28-4d68-a276-e1163de1ce0b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'onion-layered-flame'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'fire'
    categories = ('fire', 'primitives')
    aliases = ()
    keywords = ('fire', 'flame', 'onion', 'layered', 'burning', 'heat', 'symbol')

    def build(self):
        # Plan: Symmetric pointed onion flame; nested inner outline preserves layering. Third outline omitted for clearance. Shared axis 24 and mirrored controls. Bounds (8,4)-(40,44).
        a=24
        self.add_bezier('outer',(a,4),((21,14),(8,18),(8,29)),((8,38),(15,44),(a,44)),((33,44),(40,38),(40,29)),((40,18),(27,14),(a,4)))
        self.add_contour('outline','outer',closed=True)
        self.add_bezier('inner',(a,21),((21,26),(18,27),(18,30)),((18,33),(21,35),(a,35)),((27,35),(30,33),(30,30)),((30,27),(27,26),(a,21)))
        self.add_contour('layer','inner',closed=True)

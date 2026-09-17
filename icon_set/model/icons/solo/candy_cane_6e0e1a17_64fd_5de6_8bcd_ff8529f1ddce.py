"""Candy Cane.

Plan: Broad continuous candy cane with round tips, reoriented upright for clean concentric arcs. No stripes in reference. Lucide candy-cane informs hook. Bounds (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6e0e1a17-64fd-5de6-8bcd-ff8529f1ddce'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/christmas sugar cane_6e0e1a17-64fd-5de6-8bcd-ff8529f1ddce.svg'
AUTHOR = 'gpt-6'

class CandyCane(Solo48):
    icon_id = 'candy-cane'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/holidays'
    aliases = ()
    keywords = ('candy', 'cane')

    def build(self):
        self.add_arc('outer-hook',(8,20),(40,20),radius_x=16)
        self.add_arc('hook-tip',(40,20),(32,20),radius_x=4)
        self.add_arc('inner-hook',(32,20),(16,20),radius_x=8,sweep=False)
        self.add_line('inner-stem',(16,20),(16,40))
        self.add_arc('stem-tip',(16,40),(8,40),radius_x=4)
        self.add_line('outer-stem',(8,40),(8,20))
        self.add_contour('cane','outer-hook','hook-tip','inner-hook','inner-stem','stem-tip','outer-stem',closed=True)

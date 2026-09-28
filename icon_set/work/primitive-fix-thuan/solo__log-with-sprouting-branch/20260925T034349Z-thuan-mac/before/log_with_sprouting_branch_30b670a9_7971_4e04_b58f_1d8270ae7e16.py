"""Horizontal log with a cut end and an attached sprouting branch. HRECT extremes (4,8)-(44,40); log owns its paired ends.
Reduction: Removed end-grain rings, bark marks, and the tiny leaf blade; retained the cut-end seam and rising branch stub.
Lucide: leaf
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30b670a9-7971-4e04-b58f-1d8270ae7e16'
SOURCE_PATH = 'pictographic-primitives/nature/tree log_30b670a9-7971-4e04-b58f-1d8270ae7e16.svg'
AUTHOR = 'gpt-6'

class LogWithSproutingBranch(Solo48):
    icon_id = 'log-with-sprouting-branch'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/batch-03"
    aliases = ()
    keywords = ('log', 'wood', 'timber', 'tree', 'rings', 'firewood', 'forestry', 'nature')

    def build(self) -> None:
        self.add_arc('end-left',(14,20),(14,40),radius_x=10,sweep=False)
        self.add_line('bottom',(14,40),(34,40))
        self.add_arc('end-right',(34,40),(34,20),radius_x=10,sweep=False)
        self.add_line('top-right',(34,20),(30,20));self.add_line('top-left',(30,20),(14,20))
        self.add_contour('log','end-left','bottom','end-right','top-right','top-left',closed=True)
        self.add_arc('cut-end',(14,40),(14,20),radius_x=6,radius_y=10,sweep=False)
        for p in ('end-left','bottom','top-left'):self.relate('connect','cut-end',p)
        self.add_polyline('branch',(30,20),(34,8),(42,8))
        for p in ('top-right','top-left'):self.relate('connect','branch-1',p)

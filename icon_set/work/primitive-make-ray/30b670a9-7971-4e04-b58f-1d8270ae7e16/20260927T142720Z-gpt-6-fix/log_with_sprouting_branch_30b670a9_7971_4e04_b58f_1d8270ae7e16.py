"""Horizontal log with a cut end and an attached sprouting branch. HRECT extremes (4,8)-(44,40); log owns its paired ends.
Reduction: Kept the cut-end seam and a rising stem with a simple open leaf; omitted tiny bark marks.
Lucide: leaf
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '30b670a9-7971-4e04-b58f-1d8270ae7e16'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__log-with-sprouting-branch/20260927T142540Z-thuan-mac-1/reference/tree log_30b670a9-7971-4e04-b58f-1d8270ae7e16.svg'
AUTHOR = 'gpt-6'

class LogWithSproutingBranch(Solo48):
    icon_id = 'log-with-sprouting-branch'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    categories = ("nature", "primitives")
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
        self.add_line('sprout-stem',(30,20),(34,10))
        self.add_polyline('sprout-leaf',(34,10),(40,8),(44,10),(40,12))
        self.relate('connect','log','sprout-stem')
        self.relate('connect','sprout-stem','sprout-leaf')

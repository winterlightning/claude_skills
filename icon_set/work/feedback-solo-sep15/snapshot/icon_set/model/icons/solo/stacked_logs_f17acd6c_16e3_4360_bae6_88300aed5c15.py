"""Two horizontal cut logs form a stack. HRECT extremes (4,8)-(44,40); shared 6-unit end radii, staggered lengths.
Reduction: Reduced three logs to two, and omitted end-grain dots and bark marks.
Lucide: No useful wooden-log match; paired circular end construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f17acd6c-16e3-4360-bae6-88300aed5c15'
SOURCE_PATH = 'pictographic-primitives/nature/trees log_f17acd6c-16e3-4360-bae6-88300aed5c15.svg'
AUTHOR = 'gpt-6'

class StackedLogs(Solo48):
    icon_id = 'stacked-logs'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/batch-03"
    aliases = ()
    keywords = ('logs', 'firewood', 'wood', 'timber', 'stack', 'lumber', 'forestry', 'fuel')

    def build(self) -> None:
        for n,(left,right,y) in enumerate(((12,36,14),(4,44,34))):
         r=6;cx=left+r;end=right-r
         self.add_arc(f'end-left-{n}',(cx,y-r),(cx,y+r),radius_x=r,sweep=False)
         self.add_line(f'bottom-{n}',(cx,y+r),(end,y+r))
         self.add_arc(f'end-right-{n}',(end,y+r),(end,y-r),radius_x=r,sweep=False)
         self.add_line(f'top-{n}',(end,y-r),(cx,y-r))
         self.add_contour(f'log-{n}',f'end-left-{n}',f'bottom-{n}',f'end-right-{n}',f'top-{n}',closed=True)
         self.add_arc(f'cut-{n}',(cx,y+r),(cx,y-r),radius_x=r,sweep=False)
         for p in ('end-left','bottom','top'):self.relate('connect',f'cut-{n}',f'{p}-{n}')

"""A square paint can with long and short overflow drips. SQUARE extremes (6,6)-(42,42). Lucide paint-bucket informs coherent paint outlines; source upright can geometry is retained. Enlarge drip widths and simplify the flared rim, preserving both unequal drips."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0cdb0ad7-55f3-4be1-82d1-3b7d166ba704'
SOURCE_PATH = 'pictographic-primitives/symbol/paint_0cdb0ad7-55f3-4be1-82d1-3b7d166ba704.svg'
AUTHOR = 'gpt-6'


class PaintCanDrip(Solo48):
    icon_id = 'paint-can-drip'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('paint', 'can', 'drip', 'decorate', 'color', 'renovation', 'diy', 'bucket')

    def build(self) -> None:
        self.add_polyline('shell-top',(6,15),(6,6),(42,6),(42,22),(42,38))
        self.add_arc('br',(42,38),(38,42),radius_x=4)
        self.add_line('base',(38,42),(12,42))
        self.add_arc('bl',(12,42),(8,38),radius_x=4)
        self.add_polyline('shell-left',(8,38),(8,15),(6,15))
        for a,b in [('shell-top','br'),('br','base'),('base','bl'),('bl','shell-left'),('shell-left','shell-top')]:
            self.relate('connect',a,b)
        self.add_line('paint-left',(8,15),(18,15))
        self.add_line('long-left',(18,15),(18,29))
        self.add_arc('long-bottom',(18,29),(26,29),radius_x=4,sweep=False)
        self.add_line('long-right',(26,29),(26,20))
        self.add_arc('paint-valley',(26,20),(34,20),radius_x=4)
        self.add_line('short-left',(34,20),(34,22))
        self.add_arc('short-bottom',(34,22),(42,22),radius_x=4,sweep=False)
        self.add_contour('paint','paint-left','long-left','long-bottom','long-right','paint-valley','short-left','short-bottom')
        self.relate('connect','paint','shell-top')
        self.relate('connect','paint','shell-left')

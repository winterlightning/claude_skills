"""Two folded capsule handles linked by a central hinge; reoriented upright for legibility."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '64e78c2b-0a71-4f95-92fd-e4df2a5b63ce'
SOURCE_PATH = 'pictographic-primitives/tools/foldable pliers_64e78c2b-0a71-4f95-92fd-e4df2a5b63ce.svg'
AUTHOR = 'gpt-6'

class FoldedMultitool(Solo48):
    icon_id = 'folded-multitool'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    aliases = ()
    keywords = ('multitool', 'pliers', 'folding', 'foldable', 'pocket tool', 'handles', 'compact', 'tool')

    def build(self) -> None:
        # Upright paired handles preserve both closed capsules on the integer grid.
        axis_x = 24
        for n,x in [('left',8),('right',28)]:
            self.add_arc(n+'-top',(x,10),(x+12,10),radius_x=6)
            self.add_line(n+'-outer',(x+12,10),(x+12,38))
            self.add_arc(n+'-bottom',(x+12,38),(x,38),radius_x=6)
            self.add_line(n+'-inner',(x,38),(x,10))
            self.add_contour(n,n+'-top',n+'-outer',n+'-bottom',n+'-inner',closed=True)
        self.add_line('hinge',(axis_x-4,24),(axis_x+4,24))
        self.relate('connect','hinge','left')
        self.relate('connect','hinge','right')

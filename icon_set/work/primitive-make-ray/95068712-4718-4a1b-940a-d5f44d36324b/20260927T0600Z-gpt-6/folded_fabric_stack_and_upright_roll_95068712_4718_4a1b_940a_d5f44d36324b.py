"""Folded Fabric Stack and Upright Roll.

Symbol plan: Two repeated horizontal folded layers and one upright roll; shared stack endpoints. Reduce three layers to two.
SQUARE centerline extremes (6,6)-(42,42); envelope follows the subject's proportions.
Construction reference: No useful exact Lucide match; capsule-like fabric folds and shared layer construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '95068712-4718-4a1b-940a-d5f44d36324b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__folded-fabric-stack-and-upright-roll/20260927T055558Z-thuan-mac-1/reference/material fabric_95068712-4718-4a1b-940a-d5f44d36324b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'folded-fabric-stack-and-upright-roll'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('folded', 'fabric', 'stack', 'and', 'upright', 'roll')

    def build(self) -> None:
        # Three equal folded layers feed into the upright roll on the right.
        self.add_polyline('roll-wall',(30,10),(30,12),(30,22),(30,32),(30,42),(42,42),(42,10))
        self.add_arc('roll-cap',(30,10),(42,10),radius_x=6,radius_y=4,sweep=True)
        self.relate('connect','roll-wall','roll-cap')
        for j,y in enumerate((12,22,32)):
            self.add_line(f'fold-{j}-top',(30,y),(11,y))
            self.add_arc(f'fold-{j}-end',(11,y),(11,y+10),radius_x=5,radius_y=5,sweep=False)
            self.add_line(f'fold-{j}-bottom',(11,y+10),(30,y+10))
            self.add_contour(f'fold-{j}',f'fold-{j}-top',f'fold-{j}-end',f'fold-{j}-bottom')
            self.relate('connect',f'fold-{j}','roll-wall')
            if j:self.relate('connect',f'fold-{j}',f'fold-{j-1}')


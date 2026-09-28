"""Two overlapping busts with equal circular heads and shared baseline. Human user.svg owns round heads and broad shoulders; Lucide users informs overlap. Source oval heads normalized to circular human vocabulary. Head bottoms18 and shoulders26 leave exact4 ink gap.
Keyshape SQUARE; clean centerlines revision. Shared symbol parameters own paired geometry."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2384e2e1-cdf9-4683-9a5b-04f5e95f8a86'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-overlapping-busts-with-oval-heads/20260927T140026Z-thuan-mac-1/reference/spouse_2384e2e1-cdf9-4683-9a5b-04f5e95f8a86.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='two-overlapping-busts-with-oval-heads'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('two', 'overlapping', 'busts', 'with', 'oval', 'heads')
    def build(self):
        # Paired heads share one two-shoulder outline with a central overlap valley.
        for side,x in [('left',14),('right',34)]:
            self.add_arc('head-'+side+'-upper',(x-6,12),(x+6,12),radius_x=6)
            self.add_arc('head-'+side+'-lower',(x+6,12),(x-6,12),radius_x=6)
            self.add_contour('head-'+side,'head-'+side+'-upper','head-'+side+'-lower',closed=True)
        self.add_line('body-left',(6,42),(6,34))
        self.add_bezier('left-outer',(6,34),((6,29),(9,26),(14,26)))
        self.add_bezier('left-inner',(14,26),((19,26),(24,29),(24,34)))
        self.add_bezier('right-inner',(24,34),((24,29),(29,26),(34,26)))
        self.add_bezier('right-outer',(34,26),((39,26),(42,29),(42,34)))
        self.add_line('body-right',(42,34),(42,42))
        self.add_line('body-base',(42,42),(6,42))
        self.add_contour('shared-body','body-left','left-outer','left-inner','right-inner','right-outer','body-right','body-base',closed=True)

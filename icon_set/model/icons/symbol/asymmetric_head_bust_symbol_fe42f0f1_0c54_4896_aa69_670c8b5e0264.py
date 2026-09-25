"""A continuous front-facing head, neck and shoulders silhouette with the source’s asymmetric side contour. Exclude the circle or magnifying glass; complete the bust outline as a standalone symbol.

Plan: One continuous head-neck-shoulder outline; source irregular ear side preserved. Bounds (2,2)-(30,30).
Construction reference: Shared human_ref/user.svg: broad shoulders; source requires continuous neck and asymmetric head."""
from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = 'fe42f0f1-0c54-4896-aa69-670c8b5e0264'
SOURCE_PATH = 'pictographic-primitives/other/person magnifying glass_fe42f0f1-0c54-4896-aa69-670c8b5e0264.svg'
SOURCE_ICON_IDS = ('fe42f0f1-0c54-4896-aa69-670c8b5e0264',)
AUTHOR = 'gpt-6'

class AsymmetricHeadBustSymbol(Symbol32):
    icon_id = 'asymmetric-head-bust-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('asymmetric', 'head', 'bust', 'symbol')

    def build(self) -> None:
        self.add_bezier('left-shoulder',(2,30),((5,28),(8,27),(10,26)))
        self.add_polyline('left-neck',(10,26),(10,22))
        self.add_bezier('head',(10,22),((6,18),(8,14),(7,11)),((5,4),(10,2),(16,2)),((23,2),(27,5),(25,12)),((26,16),(25,19),(22,22)))
        self.add_polyline('right-neck',(22,22),(22,26))
        self.add_bezier('right-shoulder',(22,26),((25,27),(28,29),(30,30)))
        self.add_contour('bust','left-shoulder','left-neck-1','head','right-neck-1','right-shoulder')
        self.contours=[c for c in self.contours if c.contour_id not in ('left-neck','right-neck')]

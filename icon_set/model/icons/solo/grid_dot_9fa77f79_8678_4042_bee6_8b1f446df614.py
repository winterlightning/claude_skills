'grid-dot: independent smooth-curve repair.\n\nConstruction: A regular rounded square; its panel structure uses shared centerlines and four equal corners.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/layout-grid.svg and atomic-debug/layout-grid.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '9fa77f79-8678-4042-bee6-8b1f446df614'
SOURCE_PATH = 'pictographic-primitives/design/grid dot_9fa77f79-8678-4042-bee6-8b1f446df614.svg'
AUTHOR = 'gpt-6'


class GridDot(Solo48):
    icon_id = 'grid-dot'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('grid', 'dot', 'design')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,4,xs=(24,),ys=(24,))
        contacts(self)

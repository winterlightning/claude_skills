"""One pointed leaf with a curved right edge and near-straight left edge, plus one curved interior vein continuing as the lower stem. Preserve the original outline and vein placement.

Plan: One asymmetrical leaf and curved vein continuing through its base as a stem. Bounds (2,2)-(30,30).
Construction reference: Lucide leaf: connected flowing leaf silhouette and vein; source owns its upright leaning orientation."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7268cdee-6014-437c-9511-21426dd1c77e'
SOURCE_PATH = 'pictographic-primitives/state/leaf left_7268cdee-6014-437c-9511-21426dd1c77e.svg'
SOURCE_ICON_IDS = ('7268cdee-6014-437c-9511-21426dd1c77e',)
AUTHOR = 'gpt-6'

class SingleLeafCurvedVeinSub(Sub32):
    icon_id = 'single-leaf-curved-vein-sub'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('single', 'leaf', 'curved', 'vein', 'sub')

    def build(self) -> None:
        self.add_bezier('leaf-upper',(2,2),((9,6),(24,2),(27,14)),((29,20),(27,24),(24,26)))
        self.add_bezier('leaf-lower',(24,26),((8,30),(2,19),(2,2)))
        self.add_contour('leaf','leaf-upper','leaf-lower',closed=True)
        self.add_bezier('vein',(12,13),((19,17),(24,22),(24,26)),((27,27),(29,29),(30,30)))
        self.relate('connect','leaf','vein')

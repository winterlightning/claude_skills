"""Fresh SOLO48 revision of hexagon-design from its claimed original reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '96421daf-8508-4131-bcb0-05c368fcbc6a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hexagon-design/20260927T061852Z-thuan-mac-1/reference/hexagon_96421daf-8508-4131-bcb0-05c368fcbc6a.svg'
AUTHOR = 'gpt-6'

class HexagonDesign(Solo48):
    icon_id = 'hexagon-design'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('hexagon', 'design')
    keyshape = Keyshape.SQUARE

    def build(self) -> None:

        # The claimed original is a plain point-top hexagon with square aspect.
        poly(self,'hexagon',(24,6),(42,16),(42,32),(24,42),(6,32),(6,16),closed=True)

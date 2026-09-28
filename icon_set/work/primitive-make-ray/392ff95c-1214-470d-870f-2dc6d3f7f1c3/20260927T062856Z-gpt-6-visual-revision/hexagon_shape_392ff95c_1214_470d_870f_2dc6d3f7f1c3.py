"""Fresh SOLO48 revision of hexagon-shape from its claimed original reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '392ff95c-1214-470d-870f-2dc6d3f7f1c3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hexagon-shape/20260927T061852Z-thuan-mac-1/reference/hexagon shape_392ff95c-1214-470d-870f-2dc6d3f7f1c3.svg'
AUTHOR = "gpt-6"

class HexagonShape(Solo48):
    icon_id = 'hexagon-shape'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('hexagon', 'shape', 'design')
    keyshape = Keyshape.SQUARE

    def build(self) -> None:

        # The claimed original is a plain point-top hexagon with square aspect.
        poly(self,'hexagon',(24,6),(42,16),(42,32),(24,42),(6,32),(6,16),closed=True)

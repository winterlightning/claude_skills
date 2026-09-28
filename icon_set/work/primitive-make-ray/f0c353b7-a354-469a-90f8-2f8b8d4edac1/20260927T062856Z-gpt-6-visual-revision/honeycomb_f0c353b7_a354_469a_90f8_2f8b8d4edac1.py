"""Fresh SOLO48 revision of honeycomb from its claimed original reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'f0c353b7-a354-469a-90f8-2f8b8d4edac1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__honeycomb/20260927T061852Z-thuan-mac-1/reference/honeycomb_f0c353b7-a354-469a-90f8-2f8b8d4edac1.svg'
AUTHOR = "gpt-6"

class Honeycomb(Solo48):
    icon_id = 'honeycomb'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('honeycomb', 'symbol')
    keyshape = Keyshape.SQUARE

    def build(self) -> None:

        # Three equal cells on one shared hexagonal grid.
        poly(self,'top',(24,6),(33,11),(33,21),(24,26),(15,21),(15,11),closed=True)
        poly(self,'left',(15,21),(24,26),(24,37),(15,42),(6,37),(6,26),closed=True)
        poly(self,'right',(33,21),(42,26),(42,37),(33,42),(24,37),(24,26),closed=True)
        contacts(self)

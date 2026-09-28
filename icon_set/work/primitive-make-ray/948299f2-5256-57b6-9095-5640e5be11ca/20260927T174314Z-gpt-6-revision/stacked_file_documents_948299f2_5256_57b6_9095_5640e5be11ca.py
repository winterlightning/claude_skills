"""Stacked File Documents: overlapping clipped-corner pages.
SQUARE envelope (6,6)-(42,42); common eight-unit stack offset.
Source supplies page arrangement; Lucide files supplies interrupted rear contour.
Omit fine edge slivers to keep the rear page separated at native size.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '948299f2-5256-57b6-9095-5640e5be11ca'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__stacked-file-documents/20260927T173930Z-thuan-mac-1/reference/common file double_948299f2-5256-57b6-9095-5640e5be11ca.svg'
AUTHOR = "gpt-6"
class Icon(Solo48):
    icon_id = 'stacked-file-documents'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "files"
    categories = ("files", "primitives")
    aliases = ['Stacked File Documents']
    keywords = ['stacked', 'file', 'documents']
    def build(self):
        self.add_polyline("front", (6,14), (24,14), (34,24), (34,34), (34,42), (6,42), closed=True)
        self.add_polyline("rear", (14,6), (32,6), (42,16), (42,34), (34,34))
        self.relate("connect", "front", "rear")

"""Stacked Document Files: overlapping clipped-corner pages.
SQUARE envelope (6,6)-(42,42); common eight-unit stack offset.
Source supplies page arrangement; Lucide files supplies interrupted rear contour.
Omit fine edge slivers to keep the rear page separated at native size.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '0c109927-0590-5d6e-9dac-dc846e765d39'
SOURCE_PATH = 'pictographic-primitives/files/common file double_0c109927-0590-5d6e-9dac-dc846e765d39.svg'
AUTHOR = "gpt-6"
class Icon(Solo48):
    icon_id = 'stacked-document-files'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "files"
    categories = ("files", "primitives")
    aliases = ['Stacked Document Files']
    keywords = ['stacked', 'document', 'files']
    def build(self):
        self.add_polyline("front", (14,6), (32,6), (42,16), (42,34), (34,34), (14,34), (14,14), closed=True)
        self.add_polyline("rear", (14,14), (6,14), (6,42), (34,42), (34,34))
        self.relate("connect", "front", "rear")
